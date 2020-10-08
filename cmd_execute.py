from subprocess import Popen,PIPE
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

cms = ["python --version", "timeout 10"]
data = os.popen("python --version")
data2 = os.popen("pause")

print("Current directory is: {}".format(dir_path))
# print(cwd)
# print(data.read())
# print(data2.read())
print("End....")