import subprocess

with open("electron_installed.txt", "r") as file:
    if(file.read() != "True"):
        subprocess.Popen("installElectron.cmd")
        
with open("electron_installed.txt", "w") as file:
    file.truncate(0)
    file.write("True")

subprocess.Popen("/Render Engine/Electron/RenderStart.bat")
subprocess.Popen("/Game Engine/EngineStart.bat")