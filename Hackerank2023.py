# L2: Control Flow - Branching 1
year = int(input("Nhap nam: "))
if year <= 0: 
    print("false")
else:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("true")
    else:
        print("false")
        
