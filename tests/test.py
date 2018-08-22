import glob
import subprocess
import json

box_folders = glob.glob('boxes/**/')
print("Boxes detected:")
print(box_folders)

test_envs = glob.glob('tests/**/*', recursive=True)
print("Test envs detected:")
print(test_envs)

for box in box_folders:
    with open(box + "box.json") as json_file:
        json_read = json.load(json_file)
        envs_list = json_read['tested']
        for envs in envs_list:
            print("bash", "test.sh", envs, box)
            proc = subprocess.Popen(["bash", "tests/test.sh", envs, box], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = proc.communicate()
            exit_code = proc.wait()
            print(out)
            print("Error code: " + str(exit_code))
