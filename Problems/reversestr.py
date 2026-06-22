def reverseastring(s):
    rstr = ""
    for ch in s:
        rstr = ch + rstr
    return rstr

s = input("Enter a string:")
print(reverseastring(s))