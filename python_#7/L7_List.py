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
my_list2 = [1,2,7,9,3,5]

print(max(my_list2)) 
print(min(my_list2))
print(sum(my_list2))
