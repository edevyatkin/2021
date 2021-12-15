from heapq import *
from itertools import product
import math

input = open('day15.input', 'r')
data = []
while (line := input.readline().rstrip()):
    data.append([int(ch) for ch in line])

height = len(data)
width = len(data[0])
h = [(0,0,0)]
visited = set()
risks = {}
risks[(0,0)] = 0

while len(h) > 0:
    prisk, i, j = heappop(h) # get pos
    if (i, j) in visited:
        continue
    if (i,j) in risks and risks[(i,j)] != prisk:
        continue
    for diff in product([-1,0,1], repeat=2):
        if abs(diff[0]) == abs(diff[1]):
            continue
        di = i + diff[0]
        dj = j + diff[1]
        if di < 0 or di == height or dj < 0 or dj == width:
            continue
        if (di, dj) in visited:
            continue
        riskFromPos = data[di][dj]
        riskToPos = risks[(i,j)]
        targetRisk = risks.get((di,dj), math.inf)
        newTargetRisk = min(targetRisk, riskToPos + riskFromPos)
        risks[(di,dj)] = newTargetRisk
        heappush(h, (newTargetRisk, di, dj))
    visited.add((i,j))
    
print(risks[(height-1, width-1)])


