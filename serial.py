"""Python serial number generator."""

class SerialGenerator:
    def __init__(self, start=0):
        self.start = 0
        self.next = start
    def generate(self):
        serial = self.next
        self.next += 1
        return serial

    def reset(self):
        self.next = self.start
    
serial = SerialGenerator(start=100)

print(serial.generate())  # Output: 100
print(serial.generate())  # Output: 101
print(serial.generate())  # Output: 102

