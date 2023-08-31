import subprocess

with open("electron_installed.txt", "r") as file:
    if(file.read() != "True"):
        subprocess.Popen("installElectron.cmd")
        
with open("electron_installed.txt", "w") as file:
    file.truncate(0)
    file.write("True")