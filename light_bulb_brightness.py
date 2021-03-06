from ABCs import *
from SocketWrapper import SocketWrapper

class LightBulbBrightness(Component, Switchable, Adjustable, Bounded):
    def __init__(self, id, is_on, now):
        super().__init__()
        self.type = 'light_bulb_brightness'
        self.id = id
        self.is_on = is_on
        self.min = 0
        self.max = 100
        self.now = now
        
    def info(self):
        print("[Component]:")
        print("\t id:" + self.id)
        print("\t type:" + self.type)
        print("\t is_on:" + str(self.is_on))
        print("\t min:" + str(self.min))
        print("\t max:" + str(self.max))
        print("\t now:" + str(self.now))
    
    def turnOn(self):
        self.is_on = 1
        SocketWrapper().emmit_update_var(self.id, "is_on", self.is_on)
        
    def turnOff(self):
        self.is_on = 0
        SocketWrapper().emmit_update_var(self.id, "is_on", self.is_on)
        
    def adjust(self, value):
        self.now = value
        SocketWrapper().emmit_update_var(self.id, "now", self.now)

        
    def update_value(self, var_name, var):
        if var_name == 'is_on':
            if var == 1:
                self.turnOn()
            elif var == 0:
                self.turnOff()
        elif var_name == 'now':
            self.adjust(var)
        
            