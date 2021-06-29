a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

l = [a, b, c]
l = sorted(l)

if (d >= l[0] and e >= l[1]) or (d >= l[1] and e >= l[0]):
    print('YES')
else:
    print('NO')
