import subprocess


class LightChanger:


#have a path to the C3 executable
 #   have a function that takes a color(can get RGB values from it) and passes that to the exec as args
 #   overridde the color change fucntion to take raw RGB values

   # havee a set yellow
   # have a set green
   # have a set red fucntion for clarity

    exec_path = "C:/Users/grego/workspace/exec-assistant/C#/MSI-Mystic-Light-Controller/SetLEDsGreen/Deployment/netcoreapp3.1/SetLEDsGreen.exe"

   #def __init__(self):
   #     self.command = exec_""

    def set_yellow(self):
        command = self.exec_path + " 255 255 0"
        return subprocess.call(args=command)