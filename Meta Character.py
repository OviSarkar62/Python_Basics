# Dot Character
import re
pattern = r"colo..r"
if re.match(pattern, "colouura"):
    print("Matched")
# ^$ character
pattern2 = r"^colo..r$"
if re.match(pattern2, "colouur"):
    print("Matched2")
if re.match(pattern2, "colouura"):
    print("Matched3")

# - character
pattern3 = r"ice(-)?cream"

if re.match(pattern3,"ice-cream"):
    print("Matched4")
if re.match(pattern3, "icecream"):
    print("Matched5")