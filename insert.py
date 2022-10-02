n = int(input())
s = input()
a = [int(x) for x in s.split()]
a += [0]
v = input()
k = [int(x) for x in v.split()]
place = k[1]
num = k[0]
b = ''
for i in range(n,place-1,-1):
    a[i] = a[i-1]
a[place-1] = num
for x in a:
    b+=str(x)
    b+=' '
print(b)
