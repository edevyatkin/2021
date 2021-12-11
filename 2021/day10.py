from collections import deque
from itertools import product

input = open('day10.input', 'r')
data = []
while (line := input.readline().rstrip()):
    data.append([int(ch) for ch in line])

flashes = 0
s = 1
while True: 
    q = deque()
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] += 1
            if data[i][j] > 9:
                q.appendleft((i,j))

    while len(q) > 0:
        pos = q.pop()

        if pos[0] < 0 or pos[0] == len(data):
            continue
        if pos[1] < 0 or pos[1] == len(data[0]):
            continue
        if data[pos[0]][pos[1]] == 0:
            continue

        data[pos[0]][pos[1]] += 1
        if data[pos[0]][pos[1]] <= 9:
            continue

        data[pos[0]][pos[1]] = 0
        if s <= 100:
            flashes += 1
        for c in product([-1,0,1], repeat=2):
            if c == (0,0):
                continue
            q.appendleft((pos[0]+c[0], pos[1]+c[1]))
        
    if all([not any(data[i]) for i in range(len(data))]):
        break

    s += 1

print(flashes)
print(s)