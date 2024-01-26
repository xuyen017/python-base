'''
Topic  #2: String(Chuỗi ký tự) -a  sepuence of characters
'''
#String: ordered(theo thứ tự), immutable(không thể thay đổi)

#use singe or double quotes( '',"") or 
# my_string ='day la string'
# my_string ="day la string 2"
# Escaping backslash \
# my_string='i\'m am'
# my_string="i tell \"what are you doing\""
# print(my_string, type(my_string))

'''
Access characters and substrings(tiep can cac ky tu nho trong ky tu lon)

'''
my_strings = "Hello World"
# char = my_strings[1]
# print(char)
# # string is immutable -> cannot be changed
# my_strings[1] ="i" # thay 3 = i

# #substring with slicing (lay chuoi)
# sub_string = my_strings[0:5]
# print(sub_string)

'''
concatenate two or more strings
'''
# # concat strinsg with +
# greeting = "my name is"
# channel = " Xuyen"
# sentence = greeting + channel + "Love PA"
# print(sentence)
'''
basic & useful Funtion (ham co ban va huu ich)
'''
# #strip remove character
# print("im alone     ".strip())
# print("Xa em anh nho".strip('X'))
# #split() 
# print('but life is good'.split())
# print('but, life is good'.split(','))
# #replace
# print('but life is good'. replace('but', "also"))

# #check chartacter
# my_strings = 'Need to maake a fire'
# print(my_strings.startswith('Need'))
# print(my_strings.endswith('cold'))
# print(my_strings.index('e'))
# print(my_strings.find('e'))

# #uper - in hoa
# my_strings="still here"
# print(my_strings.upper())
# my_stringr= "TAKE HRER"
# print(my_stringr.lower())
# print(my_stringr.title())
# print(my_stringr.count('E'))

'''
String formatting
'''
#%, .format(), f-Strings

# # %
# name = "TheXuyen"
# my_string = "welcome to %s " % name

# pi = 3.149785
# number = "pi number"
# my_string = "welcome to %.2f + %s " % (pi, number)
# print(my_string)


# # .format()
# age = 23
# height = 167.65
# my_strings = "iam {} years old and height {:.3f}".format(age, height)
# print(my_strings)

#f-strings
age = 23
name= "xuyen"
height = 167.65
my_strings = f"i am {name} years old and height {height:.3f}; {age} years old"
print(my_strings)