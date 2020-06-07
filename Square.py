side = int(input("Give side value:"))

perimeter = 4*side

print("Perimeter of Square is {:.2f}".format(perimeter))


print("**********************************************")


def area_of_square(side):
    area = side ** 2
    print("Area of square(using function) is {:.2f}".format(area))
area_of_square(side)