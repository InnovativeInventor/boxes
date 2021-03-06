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
print(' '.join(str(i) for i in box_folders),"\n")

test_envs = glob.glob('tests/**/*')
print("Test envs detected:")
print(' '.join(str(i) for i in test_envs),"\n")

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
                print("Error code: " + str(exit_code),"\n")
            else:
                print(Fore.GREEN + "Box: " + box.ljust(17) + "     Env: " + envs)
                print(Fore.GREEN + "TEST PASSED","\n")


print()
if ALL_TESTS_PASSED:
    print(Fore.GREEN + "ALL TESTS PASSED!" + Style.RESET_ALL)
else:
    print(Fore.RED + "TESTS FAILED!" + Style.RESET_ALL)
    sys.exit(1)

