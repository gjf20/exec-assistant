from . import light_changer
class Status:

    states = ["Free", "Interrupt-able", "Busy"]

    def __init__(self):
        self.status = 0
        self.changer = light_changer.LightChanger()

    def current(self):
        return self.states[self.status]

    def set_free(self):
        self.status = 0
        self.changer.set_green()

    def set_interruptable(self):
        self.status = 1
        self.changer.set_yellow()

    def set_busy(self):
        self.status = 2
        self.changer.set_red()

    def is_free(self):
        return self.status == 0

    def is_interruptable(self):
        return self.status == 1

    def is_busy(self):
        return self.status == 2