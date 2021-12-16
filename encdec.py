alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(plain_text,shift_amount):

#     cipher_text  = ""
#     for letter in plain_text:
#         position = alphabets.index(letter)
#         new_postion = position + shift_amount
#         new_letter = alphabets[new_postion]
#         cipher_text += new_letter
    
#     print(cipher_text)

# def decrypt(cipher_text,shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabets  .index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabets[new_position] 
#     print(plain_text)
     
         
# if direction == "encode":
#     encrypt(plain_text=text,shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text,shift_amount=shift)

# doing with single function

from logo import logo

print(logo)
 
def caeser(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_amount
            end_text += alphabets[new_position]
        else:
            end_text += char
    print(f"Your {direction}d message is : {end_text}")    

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' for decrypt: \n > ")

    text = input("Enter your message: \n > ").lower()
    shift = int(input("Type the shift number: \n > "))

    shift = shift % 25

    caeser(start_text=text,shift_amount=shift,cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n > ")

    if result == "no":
        should_continue = False
        print("Goodbye...")