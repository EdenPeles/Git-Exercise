class Analog_To_Digital_Converter:

    def __init__(self):
        self.analog_value = 0

    def set_analog_value(self, value):
        if value < 0:
            self.analog_value = 0
        elif value > 5:
            self.analog_value = 5
        else:
            self.analog_value = value

    def to_digital(self):
        d_value = int((self.analog_value / 5) * 1023)
        b_value = format(d_value, '010b')
        return b_value


converter = Analog_To_Digital_Converter()
converter.set_analog_value(2.5)
digital_value = converter.to_digital()
print("Analog value:", converter.analog_value)
print("Digital value:", digital_value)


