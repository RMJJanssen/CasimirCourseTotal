class Multimeter(object):
    def __init__(self,port):
        self.port = port
        
    def set_voltage(self,voltage):
        self.voltage = voltage
        
    def get_voltage(self):
        return self.voltage