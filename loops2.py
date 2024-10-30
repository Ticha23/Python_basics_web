#function
import math
from datetime import date


def calc_area(base, height):
    area =0.5 * base * height
    print(area)

def calc_area_circle(radius):
    area = 22/7 * radius * radius
    area =round(area, 2)
    print("Area of the circle is", area, "cm^2")
def print_todays_date():
    today = date.today()
    print(today.strftime("%A, %B %d, %Y"))

def add(*args):
    total = 0
    for num in args:
        total += num
    print("Total is" , total),

def sayHi(name, age=21 ):
    print("Hello", name, "I am ", age, "years old")

sayHi("Martin")
sayHi("Baby", 25)


calc_area(15,10)
calc_area(56,15)

triangles = [[15,6], [45,12], [7,25], [40,6], [28,19]]

for t in triangles:
    calc_area(t[0],t[1])

calc_area_circle(5)
calc_area_circle(84)
print_todays_date()
add(5,6)
add(8,9,50)
add(90,76,54,34,78)
