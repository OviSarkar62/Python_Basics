import re
pattern = r"colour"
text = "My favourite colour is always black & red"
match = re.search(pattern,text)

if match:
    print(match.start())
    print(match.end())
    print(match.span())