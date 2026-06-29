# Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.

character = input("Enter a character: ").lower()
atom = ['a','b','c','d','e','f','g','h','i','j','k','j','l','m']
ntoz = ['n','o','p','q','r','s','t','u','v','w','x','y','z']

# if character in atom:
#     print("The character is between a to m")
# elif character in ntoz:
#     print("The character is between n to z")
# else:
#     print("Please enter a valid character")

if 97<=ord(character)<=109:
    print("The character is between a to m")
elif 110<=ord(character)<=122:
    print("The character is between n to z")
else:
    print("Enter a valid letter")
# print(ord(character))