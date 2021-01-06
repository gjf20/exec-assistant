import subprocess
from colorutils import Color


class LightChanger:

    exec_path = "C:/Users/grego/workspace/exec-assistant/C#/MSI-Mystic-Light-Controller/SetLEDsGreen/Deployment/netcoreapp3.1/SetLEDsGreen.exe"
    RED = Color((255, 0, 0))
    GREEN = Color((0, 255, 0))
    YELLOW = Color((255, 255, 0))

    def set_green(self):
        return self.set_color(self.GREEN)

    def set_red(self):
        return self.set_color(self.RED)

    def set_yellow(self):
        return self.set_color(self.YELLOW)

    def set_color(self, color):
        color_args = " " + str(color.red) + " " + str(color.green) + " " + str(color.blue)
        command = self.exec_path + color_args
        return subprocess.call(args=command)
