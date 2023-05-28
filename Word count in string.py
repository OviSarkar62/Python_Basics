letter = 0
digit = 0
word = 0

text = input("Enter any string: ")

for i in text:
    i = i.lower()
    if(i>='a' and i<='z'):
        letter = letter + 1
    elif(i>= '0' and i<= '9'):
        digit = digit + 1
    elif(i==' '):
        word = word + 1

print(letter)
print(digit)
print(word+1)