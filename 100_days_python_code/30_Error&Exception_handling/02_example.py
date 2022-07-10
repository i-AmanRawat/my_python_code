height= float(input("Height: "))    #(in meters)
if (height>3):raise ValueError("Human Height should not be over 3 meters.")
weight= int(input("Weight: "))      #(in kg)

#but what if the user has entered some unexpected kong level of height ? then we can raise error
bmi= weight/height**2
print(f"Your BMI is {bmi}")
