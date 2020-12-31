f = open("man.txt", mode="rt")
people = f.read().strip.split()
f1 = open("bike.txt", mode="rt")
bicycle = f.read().strip.split()
way = 0
for i in people:
    k = i.split(',')
    ind = 0
    n = -1
    for j in bicycle:
        b = j.split(',')
        if abs(int(k[0]) - int(b[0])) + abs(int(k[1]) - int(b[1])) < n or n == -1:
            n = abs(int(k[0]) - int(b[0])) + abs(int(k[1]) - int(b[1]))
        ind += 1
    way += n
print(way)
        