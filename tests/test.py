import glob
import subprocess
import json
import colorama
from colorama import Fore
from colorama import Style
import sys

colorama.init()

box_folders = glob.glob('boxes/**/')
print("Boxes detected:")
print(box_folders)

test_envs = glob.glob('tests/**/*', recursive=True)
print("Test envs detected:")
print(test_envs)

ALL_TESTS_PASSED = True
for box in box_folders:
    with open(box + "box.json") as json_file:
        json_read = json.load(json_file)
        envs_list = json_read['tested']
        for envs in envs_list:
            proc = subprocess.Popen(["bash", "tests/test.sh", envs, box], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = proc.communicate()
            exit_code = proc.wait()
            if exit_code is not 0:
                ALL_TESTS_PASSED = False
                print("bash", "test.sh", envs, box)
                print(out.decode('utf-8'))
                print("Error code: " + str(exit_code))
            else:
                print(Fore.GREEN + "Box: " + box + "     Env: " + envs)
                print("TESTS PASSED" + Style.RESET_ALL)


if ALL_TESTS_PASSED:
    print('\n' + Fore.GREEN + "ALL TESTS PASSED!" + Style.RESET_ALL)
else:
    print('\n' + Fore.GREEN + "TESTS FAILED!" + Style.RESET_ALL)
    sys.exit(1)

