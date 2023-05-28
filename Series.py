"""""""""
# 1 + 2 + 3 + 4 + n
s = 0
n= int(input())
for i in range(1,n+1,1):
    s = s + i
print(s)
"""""""""
"""""""""
# 2 + 4 + 6 + n
s2 = 0
n2= int(input())
for i in range(2,n2+1,2):
    s2 = s2 + i
print(s2)
"""""""""
"""""""""
# 2*2 + 4*4 + 6*6 + n*n
s3 = 0
n3= int(input())
for i in range(2, n3+1, 2):
    s3 = s3 + i*i
print(s3)
"""""""""
# 1 * 2 * 3 * 4 * n
s4 = 1
n4 = int(input())
for i in range(1,n4+1,1):
    s4 = s4 * i
print(s4)