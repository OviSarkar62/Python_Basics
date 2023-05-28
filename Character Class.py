# Character Class
import re
pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern, "Os62"):
    print("All letters matched sequentially")
if re.match(pattern, "Ovs62"):
    print("All letters matched sequentially")
else:
    print("All letters didn't match sequentially")