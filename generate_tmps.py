import subprocess
import sys

folder = sys.argv[1]

cdToFolder = "cd " + folder + " && "
commandLs = cdToFolder + "ls -lhrt "
commandRm  = cdToFolder + "rm -rf *_tmp"
commandCount = commandLs + " |  wc -l"

output = subprocess.getoutput(commandRm)
outputLs = subprocess.getoutput(commandLs)
print("--------AT THE START DIR IS LIKE BELOW--------")
print(output)
outputCount = subprocess.getoutput(commandCount)

print(outputCount)
co = outputLs.split("\n")[1:]

names = []
for name in co:
    fileName = name.split()[8]
    extension = fileName.split(".")[-1]
    if extension == "deb":
        names.append(name.split()[8])

command_maker = lambda x : "dpkg-deb -R " + x + " " + x + "_tmp"
commands = list(map(command_maker, names))

big_cmd = cdToFolder
big_cmd += (" && ".join(commands))



print("--------NOW_WILL_EXTRACT_DEBS--------")
op = subprocess.getoutput(big_cmd)
print("\n".join(big_cmd.split(" && ")))



print("---------------------------------")

print("--------AFTER_EXTRACTING_DEBS--------")
print(commandLs)
output = subprocess.getoutput(commandLs)
print(output)

output = subprocess.getoutput(commandCount)
print(output)