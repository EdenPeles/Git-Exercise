class Analog_To_Digital_Converter:

    def __init__(self,max,maxnum):
        self.analog_value = 0
        self.max = max
        self.maxnum = maxnum

    def set_analog_value(self, value):
        if value < 0:
            self.analog_value = 0
        elif value > self.max:
            self.analog_value = self.max
        else:
            self.analog_value = value

    def to_digital(self):
        d_value = int((self.analog_value / self.max) * 1023)
        b_value = format(d_value, '0'+str(self.maxnum)+'b')
        print('0'+str(self.maxnum)+'b')
        print(self.max)
        print(self.maxnum)
        return b_value


converter = Analog_To_Digital_Converter(10,10)
converter.set_analog_value(5)
digital_value = converter.to_digital()
print("Analog value:", converter.analog_value)
print("Digital value:", digital_value)

