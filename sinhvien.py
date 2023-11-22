import math
import random

def tinh_tong(a, b):
    return a + b

def tinh_tich(a, b):
    return a * b

def tinh_mu(a, b):
    return a ** b

def tinh_can_bac_hai(a):
    return math.sqrt(a)

def tinh_tan(a):
    return math.tan(a)

def giai_ptb2(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return "Phương trình có hai nghiệm phân biệt:", x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return "Phương trình có nghiệm kép:", x
    else:
        return "Phương trình vô nghiệm."

def sinh_so_nguyen():
    a = random.randint(1, 100)
    b = random.randint(1, 5)
    c = random.randint(1, 50)
    return a, b, c
