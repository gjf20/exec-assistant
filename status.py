class Status:

    states = ["Free", "Interrupt-able", "Busy"]

    def __init__(self):
        self.status = 0

    def current(self):
        return self.states[self.status]

    def set_free(self):
        self.status = 0

    def set_interruptable(self):
        self.status = 1

    def set_busy(self):
        self.status = 2

    def is_free(self):
        return self.status == 0

    def is_interruptable(self):
        return self.status == 1

    def is_busy(self):
        return self.status == 2