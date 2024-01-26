import string
import random


Letters = string.ascii_letters
Numbers = string.digits
Punctuation = string.punctuation
def get_password_length():
    password_length = input("how long do you want your password:")
    return int(password_length)

def password_generatorc( password_length):
   
    printable= f'{Letters}{Numbers}{Punctuation}'
    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=  password_length)
    random_password=''.join(random_password)
    print(random_password)
    #print(printable)

def main():
    password_length = get_password_length()
    password = password_generatorc(password_length)

if __name__ == "__main__":
    main()