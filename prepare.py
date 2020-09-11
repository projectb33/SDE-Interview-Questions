import os

if not os.path.exists("docs"):
    os.system("mkdir docs")

for filename in os.listdir("."):
    if os.path.isdir(filename) and filename != "docs" and filename != ".git":
        os.system("cp -r ./{} ./docs".format(filename))


with open('./index.md', 'w') as IndexF:
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            IndexF.write("* [{}](./{})\n".format(filename.title(), filename))

os.system("cp ./index.md ./docs")
