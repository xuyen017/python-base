'''
creating a list List trong python = mảng (array)
'''
# List1 = ["banana","apple","orange","strongbery"]
# List2=["xuyen", 5, False, None]
# list3= list()
# print(list3)

'''
Access elements: truy cap den cac gia tri trong list
'''
#my_list = [1,2, '3'  True]
#print(len(my_list))

#print(my_list[3])

#print(my_list.index(2))

# my_list = [1,2, '3', 3,3,'3',  True]
# print(my_list.count(3))
#my_list = [1,2, '3', 3,3,'3',  True]
#for item in my_list:
    #print(item)

# # enumerate funtion
# presidents=["xuyen", 'toan',"hoan",'dat', 'khanh']
# print(presidents)
# for index, president in enumerate(presidents, start=1):
#     print(f" chu tich #{index} : {president}")

# Slicing( cắt list)
# is called slicing and has the format[start: end: step]

#my_list = [1,2, '3', 3,3,'3',  True]

# print(my_list[1:])
# print(my_list[:2])
# print(my_list[-1])
# print(my_list[::2])  #step buoc nhay
# print(my_list[::-1])
'''
3 List operations & useful methods
    3.1 Add to list
'''


my_list = [1,2, '3', 3,3,'3',  True]
##3.1 Add to list
# print (my_list*2)
# print (my_list+[100, 'xuyen'])
# print(my_list.append([100, 'xuyen']))
# print(my_list)
# print(my_list.insert(3,"xuyen2"))
# print(my_list)


## 3.2 remove form List
# print(my_list.pop(1)) #xoa vi tri
# print(my_list)
# print(my_list.remove(3)) # xoa gia tri dau tien
# print(my_list)
# del my_list[3]
# print(my_list)

## 3.3 sorting - xap xep
# my_list2 = [1,2,7,9,3,5]
# my_list2.sort(reverse=True) #xap xep giam dan, tang danh ko co 'reverse=True'
# my_list2.reverse() # dao nguoc list

# my_list2 = [1,2,7,9,3,5]
# print(sorted(my_list2))# tao list moi
# print(list(reversed(my_list2)))
# print(my_list2)

## 3.4 useful operation 
# my_list2 = [1,2,7,9,3,5]

# print(max(my_list2)) 
# print(min(my_list2))
# print(sum(my_list2))


'''
4. List comprehensions : giúp viết code ngắn gọn ( đặc biệt khi đang trong 1 vòng 
lặp đã có và dễ đọc, nhìn code hơn)
'''
# new_list[<action> for <item> in <iterator> if <some condition>]

# word ="hello word"
# print([c for c in word])
# for c in word:
#     print(c)

# even_number = [i for i in range(0,15) if i%2==0]
# print(even_number)

transaction= [100, 200, 250, 500, 100]
tax_rate= 0.08
service_bill= 0.1

def get_price_tax_service(bill):
    return bill*(1 + tax_rate + service_bill)
#print(get_price_tax_service(100))

final_price = [get_price_tax_service(bill) for bill in transaction]
#print(final_price)

########    ADVANCED FUNTIONS

# list() --> cobert string => List
# my_strings ="Hello my girl "
# list_of_chars= list(my_strings)
# print(list_of_chars)

#sum()cong tat ca cac gia tri tung list
# numbers=[3,6,7,8,9]
# print(sum(numbers))

#zip() : looping through two list simltaneously Lap 2 cai lits voi nhau

# Names = ["honda", "BMW","yamaha", "Ducati"]

# Motos = ["cbr1000-rrr", "s1000-rr","R1M","V4s"]

# for index, (nam, moto) in enumerate(zip(Names, Motos)):
#     print(f"{index + 1} : {nam} has {moto}")


# sorted()
# sorted_by_first = sorted(["hi",'hello', 'you', 'phuong anh'])
# print(sorted_by_first)

# sorted_by_second = sorted(["hi",'hello', 'you', 'phuong anh'] , key=lambda el: el[1])
# print(sorted_by_second)

# sorted_by_key = sorted([{'name': 'phuong anh','age':24},
#  {'name': 'xuyen','age':23},
#  {'name': 'NanCy','age': 24}], key=lambda el: el['age'])
# print(sorted_by_key)
'''
5. 2D Array/list = matrix : mảng 2 chiều
'''
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(matrix[0][2]) # ket qua = 3

for row in range(len(matrix)):
    for col in range(len(matrix)):
        print(matrix[row][col]) # in ra matrix
# Transform matrix in List
list_converted = [matrix[row][col]
                  for row in range(len(matrix)) 
                    for col in range(len(matrix))]
print(list_converted)
# combine columns withh zip and *
print([x for x in zip(*matrix)])