def reversesentence(s):
    sarr = s.split()
    reversestr = []
    for word in sarr:
	    rstr = ""
	    for ch in word:
	        rstr = ch + rstr
	    reversestr.append(rstr)
    normalstring = "".join(reversestr)
    print("Input string:",s)
    print("Reversed string:",reversestr)
	
sentence = input("Enter a sentence:")
reversesentence(sentence) 