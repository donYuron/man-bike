import random
f1 = open("man.txt", 'w')
f2 = open("bike.txt", 'w')
n = 100
m = 150
s = ''
for i in range(n):
    s = s + ' ' + str(random.randint(0, 20)) + ',' + \
        str(random.randint(0, 20))
print(s, file=f1)
f1.close()
s = ''
for i in range(m):
    s = s + ' ' + str(random.randint(0, 20)) + ',' + \
        str(random.randint(0, 20))
print(s, file=f2)
f2.close()


