import calculater

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculater.area(width, length)
perimeter = calculater.perimeter(width, length)


print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")