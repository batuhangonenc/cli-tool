import sys, os, shutil

username = input("cli-tool\n\nusername on session:")

raw_lines = open("commands", "r").readlines()

fcontent = "\n"

for line in raw_lines:
	if not( line.startswith("^") ) and (len(line) > 3):
		alias, cmd = line.replace("\n", "").split("&")
		alias = alias.replace(" ", "")
		fcontent += f'alias {alias}="{cmd}"\n'


f = open("/home/{}/.bashrc".format(username), "a")
f.write(fcontent)
f.close()

cp = os.getcwd()
try:
    os.chdir("/home/{}/.cli-tool".format(username))
except:
    os.mkdir("/home/{}/.cli-tool".format(username))

os.chdir(cp)

files = [ 
"git_commit.py",
"git_clone.py",
"git_branch.py",
"git_add.py",
"git_remove.py",
"git_checkout.py",
"git_rao.py"
]

for file in files:
	shutil.move(file, "/home/{}/.cli-tool/{}".format(username, file))

try:
	os.system("rm -rf commands cli-tool.py README.md")

	rmdir = os.getcwd()

	if rmdir.endswith("cli-tool") or rmdir.endswith("CLI-TOOL"):
		os.chdir("..")
		arg="rm -rf cli-tool"
		arg2="rm -rf CLI-TOOL"

		os.system(arg)
		os.system(arg2)

except:
	pass

print("cli-tool installed.")
