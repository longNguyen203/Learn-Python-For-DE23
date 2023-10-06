import math

def SQRT(x):
    if x < 0:
        return "Error"
    else:
        return math.sqrt(x)

print(SQRT(5))