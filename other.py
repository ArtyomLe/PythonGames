def f(t):
    if(t > 0):
        return t * t + 44
    else:
        return t * t + 53

k = -16
m = 16
d = k
n = f(k)
for a in range(k, m + 1):
    if(f(a) <= n):
        d = a    #
        print(d)
        n = f(a) #
        print(n)
print(d)