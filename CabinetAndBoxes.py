height = float(input("Enter the height of the cube: "))
width = float(input("Enter the width of the cube: "))
depth = float(input("Enter the depth of the cube: "))

volume = height * width * depth

if volume < 1000:
    label = "Small"
elif volume >= 1000 and volume < 10000:
    label = "Medium"
else:
    label = "Large"

print("The volume of the cube is:", volume)
print("The cube is:", label)
