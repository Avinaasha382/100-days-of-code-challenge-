import random 

m = random.randint(100,120)



print(m)

s = set()

for _ in range(m):
    s.add((random.randint(1,20),random.randint(1,20)))

print(len(s))

for ele in  s:
    print(ele[0],ele[1])

