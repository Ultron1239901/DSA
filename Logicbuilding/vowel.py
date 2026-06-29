# Take a character and check if it’s a vowel or consonant. 

c = input("Enter a character: ").lower()

vowels = {'a','e','i','o','u'}

if c in vowels:
    print("Vowels")

else: 
    print("Consonants")