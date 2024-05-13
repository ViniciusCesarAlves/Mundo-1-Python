num = str(input('Digite um numero entre 0 e 9999: ')).split()
n = int(num)
u = n - n[-1]
d = n - n[-2:]
c = n - n[-3:]
m = n - n[-4:]
print(u, d, c, m)