generate_tmps.py scripts extract debs from specified folder which is present in current folder.

./generate_tmps.py Folder_that_contains_debfiles


You can use this for other purposes too, replace dpkg-deb command with your shell command.

Be carefull about below commands, I am deleting files which ends with _tmp. 

commandRm  = cdToFolder + "rm -rf *_tmp"
commandCount = commandLs + " |  wc -l"

output = subprocess.getoutput(commandRm)
