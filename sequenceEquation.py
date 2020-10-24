n = int(input().strip())
p = list(map(int,input().strip().split(' ')))
pos = 0
for x in range(1,n+1):
    for i in range(n):
        if p[i] == x:
            pos = i+1
            for j in range(n):
                if p[j] == pos:
                    print(j+1)
