'''
Topic 8 - Dictionary:  một tập hợp các cặp key-value không có thứ tự, có thể thay đổi và lập chỉ mục (truy cập phần tử theo chỉ mục). 
Dictionary được khởi tạo với các dấu ngoặc nhọn {} và chúng có các khóa và giá trị (key-value). 
Mỗi cặp key-value được xem như là một item. Key mà đã truyền cho item đó phải là duy nhất, 
trong khi đó value có thể là bất kỳ kiểu giá trị nào. 

Key phải là một kiểu dữ liệu không thay đổi (immutable) như chuỗi, số hoặc tuple.
'''
#create a new dictionary: A dictionary is a collection which is unordered, changeable and indexed.
# a dictionary consists of a collection of key-value pairs.
my_dict ={"name": "thexuyen", "content": "Love", "city": 'thp hcm', "age": '12'}
#print(my_dict)

my_dict2=dict(name="sss", conten= "aaa",city='hn')
#print(my_dict2)
# # Access iteams
# content_in_my_dict = my_dict["content"]
# print(content_in_my_dict)
# print(my_dict2["age"]) #keys errros

#check for keys  
# # use if .. else
# if "age" in my_dict:
#     print(my_dict["name"])
# else:
#     print("no key found")
# # use try except
# try:
#     print(my_dict2["age"])
# except KeyError:
#     print("no key found")

# Add and change items (key values) pairs
# # add a new key
# my_dict["email"]= "thexuyen@gmail.com"
## overwrite the values on existing key
# my_dict["age"]=19
# print(my_dict)

#Delete items
# delete a key-values pair
#del my_dict["city"]
# print("poped value :" + my_dict.pop("age"))
# print(my_dict)
# my_dict.popitem() # delete the last inserted key-values pair

#Looping through Dictionary
# loop over keys
for key in my_dict:
    print(key, my_dict[key])
#loop over values
for value in my_dict.values():
    print(value)
#loop over keys and values\
for key, value in my_dict.items():
    print(key, value)




