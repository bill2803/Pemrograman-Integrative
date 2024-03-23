class BMI:
    def __init__(self, weight, height):
        self.weight = weight  # weight in kg
        self.height = height  # height in meters

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False
    
bmi1 = BMI(70, 1.75)
bmi2 = BMI(70, 1.75)
bmi3 = BMI(80, 1.75)

print(bmi1.BMI_Value())  # prints 22.86
print(bmi1 == bmi2)  # prints True
print(bmi1 == bmi3)  # prints False