import sys
# sys.stdin = open('./input.txt','rt')

n = int(input())

game = []
tot = []

for i in range(n):
    game.append(list(map(int,input().split())))

for i in game:
    if i[0]==i[1]==i[2]:
        tot.append(10000+i[0]*1000)
    elif i[0]==i[1] or i[0]==i[2]:
        tot.append(1000+i[0]*100)
    elif i[1]==i[2]:
        tot.append(1000+i[1]*100)
    else:
        tot.append(max(i)*100)

print(max(tot))

    
