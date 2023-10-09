"""lambda function"""
lst = [1,2,3,4,5]
lst_new = list(map(lambda x: x * x, lst))
print(lst_new)

try:
    lst = [1,2,3,4,5]
    lst_new = list(map(lambda x: x / 0, lst))
    print(lst_new)
except ZeroDivisionError:
    print("khong the chia cho 0")
else:
    print("Doan ma khong co loi")
finally:
    print("--Hoan tat--")
print("===============================")

data = []
file_name = input("Cung cấp tên một một tệp")
try:
    fh = open(file_name, 'r')
except IOError:
    print('Không thể mở tệp ', file_name)
else: #thực hiện khi phần try không có ngoại lệ
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') #Xóa ký tự \n
            data.append(addIt)
            
    fh.close()
finally:
    print('Chương trình kết thúc')

print(data)
print("==================================")

lst = []
file = input("Nhap file name: ")
try:
    with open(file, "r") as f:
        data = f.read()
except IOError:
    print("không thể mở file", file)
else:
    lst = list(map(str, data.split("\n")))
finally:
    print("--Chuong trinh hoàn tất--")  
    
print(lst[:-1])
print("==================================")

"""Ngoại lệ Exception"""
def get_ratios(L1, L2):
    """ Giả sử: L1 and L2 là các lists có độ dài bằng nhau
    Returns: một list chứa L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) #NaN = Not a Number
        except:
            raise ValueError("lỗi không xác định")
    return ratios

L1 = [2,4,6,8]
L2 = [1,2,0,4]
print(get_ratios(L1, L2))

lst = [-1,-2,-3,-4,-5]
"""map() function"""
def ABS(x):
    return abs(x)
result = list(map(ABS, lst))
print(result)

"""filter() function"""
def is_even(x):
    return x % 2 == 0
result2 = list(filter(is_even, lst))
print(result2)

"""Xóa giá trị trùng lặp(Duplicates)"""
mylist = [1,4,7,2,4,7]
mylist = list(dict.fromkeys(mylist))
print(mylist)

"""Dictionary Python"""

"""clear()"""
dict = {
    "name": "Long",
    "age" : 20,
    "address": "Phu Xuyen",
    "weight" : 55.2
}
print(dict.clear())
print(dict)

"""List Python"""
lst = ["name", "Long", 20, 55.4, 20]
lst.append("age")
for i in lst:
    print(i)
    
"""Tuples Python"""
myTuple = (10, 20, 10, "Long")
myTuple[1] = 30 # không thể thay đổi phần tử của một tuple
print(myTuple.index("Long"))
for i in range(len(myTuple)):
    print(myTuple[i])

"""Set Python"""
mySet = {1,2,5,"Long"} # không cho trùng lặp
mySet.update(mySet)
for i in range(len(mySet)):
    print(mySet[i]) # set không có thứ tự nên không thể duyệt


