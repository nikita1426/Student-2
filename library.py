n = int(input())
s = input()
a = [int(x) for x in s.split()]
arr = []
for i in range(1,n):
    arr = a
    j = i-1
    k = a[i]
    while(j >= 0 and a[j] > k):
        a[j+1] = a[j]
        j-=1
    a[j+1] = k
    if k != a[i]:
        b = ''
        for x in a:
            b+=str(x)
            b+=' '
        print(b)
