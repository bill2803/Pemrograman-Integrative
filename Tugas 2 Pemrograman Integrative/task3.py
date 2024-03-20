class BMI_Calculator:
    def __init__(self, weight, height):
        self.weight = weight  # weight in kg
        self.height = height  # height in cm
        
    @property
    def Weight(self):
        return self.weight
    
    @property
    def Height(self):
        return self.height
    
    def BMI_Value(self):
        bmi = self.weight / (self.height/100)**2
        return bmi


person = BMI_Calculator(71, 170)  # weight: 71 kg, height: 170 cm

# Access the properties
print("Weight:", person.Weight,"Kg")
print("Height:", person.Height, "Cm")  

# Calculate and print the BMI value
print("BMI:", person.BMI_Value())
