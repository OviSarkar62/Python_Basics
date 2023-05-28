import re
pattern1 = r"colour"
text1 = "My favourite colour is always orange"
text2 = re.sub(pattern1,"fruit",text1)
print(text2)

# With Count
pattern2 = r"pen"
text3 = "My favourite pen is always Nataraj pen"
text4 = re.sub(pattern2,"pencil",text3,count=1)
text5 = re.sub(pattern2,"pencil",text3,count=2)
print(text4)
print(text5)