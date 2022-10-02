n = int(input())
s = input()
a = [int(x) for x in s.split()]
b = ''
for i in range(1,n):
    j = i-1
    k = a[i]
    while(j >= 0 and a[j] > k):
        a[j+1] = a[j]
        j-=1
    a[j+1] = k
for x in a:
    b += str(x)
    b += ' ' 
print(b)
