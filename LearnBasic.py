# # lambda function
# lst = [1,2,3,4,5]
# lst_new = list(map(lambda x: x * x, lst))
# print(lst_new)

# try:
#     lst = [1,2,3,4,5]
#     lst_new = list(map(lambda x: x / 0, lst))
#     print(lst_new)
# except ZeroDivisionError:
#     print("khong the chia cho 0")
# else:
#     print("Doan ma khong co loi")
# finally:
#     print("--Hoan tat--")
# print("===============================")

# data = []
# file_name = input("Cung cấp tên một một tệp")
# try:
#     fh = open(file_name, 'r')
# except IOError:
#     print('Không thể mở tệp ', file_name)
# else: #thực hiện khi phần try không có ngoại lệ
#     for new in fh:
#         if new != '\n':
#             addIt = new[:-1].split(',') #Xóa ký tự \n
#             data.append(addIt)
            
#     fh.close()
# finally:
#     print('Chương trình kết thúc')

# print(data)
# print("==================================")

# lst = []
# file = input("Nhap file name: ")
# try:
#     with open(file, "r") as f:
#         data = f.read()
# except IOError:
#     print("không thể mở file", file)
# else:
#     lst = list(map(str, data.split("\n")))
# finally:
#     print("--Chuong trinh hoàn tất--")  
    
# print(lst[:-1])
print("==================================")

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






