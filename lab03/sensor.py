p = float(input())
k = int(input())
er_count = 0
bolwe_count = 0
suma = 0
vern = 0
max_temp = -100000000000
for i in range(k):
    c = input()
    if c == 'error':
        er_count += 1
    else:
        temp = float(c)
        vern += 1
        suma += temp
        if temp > p:
            bolwe_count += 1
        if temp > max_temp:
            max_temp = temp
if vern > 0:
    a = suma / vern
else:
    a = 0.0
print(k)
print(er_count)
print(bolwe_count)
print(f"{max_temp:.1f}")
print(f"{a:.1f}")
        
        
