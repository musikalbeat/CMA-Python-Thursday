class Phone:
    def __init__(self, length, width, color, brand):
        self.length = length
        self.width = width
        self.color = color
        self.brand = brand

    def dial(self, number):
        print("Dialing the number:", number, "...")

    def calcArea(self):
        return self.length * self.width

    def brandName(self):
        return self.brand

applePhone = Phone(30, 20, "silver", "Apple")

print(applePhone.color)
print(applePhone.brandName())
print(applePhone.dial("123-456-7890"))