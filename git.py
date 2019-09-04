
import os

reponame = rawinput("Enter the reponame")

os.system("git init")
os.system("git add .")

commit = print("git commit -m 'first commit'")
os.system(commit)

remoteseturl = print("git remote set-url origin https://github.com/TolentinoDev/{}.git").format(reponame)
os.system(remoteseturl)
os.system("git push -u origin master")

