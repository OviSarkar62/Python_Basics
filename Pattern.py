# Pattern
"""
n = 5
*
**
***
****
*****
"""
n = int(input())
for i in range(1,n+1):
    print(i*"*")

"""
n = 5
*
***
*****
"""

n = int(input())
for i in range(1,n+1,2):
    print(i*"*")