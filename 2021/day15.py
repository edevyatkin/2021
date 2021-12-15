from heapq import *
import math

input = open('day15.input', 'r')
data = []
while (line := input.readline().rstrip()):
    data.append([int(ch) for ch in line])

repeat = 5
height = len(data)
width = len(data[0])
realh = height*repeat
realw = width*repeat

h = [(0,0,0)]
visited = set()
risks = {}
risks[(0,0)] = 0

def getvalue(i,j):
    ix, jx = i % height, j % width
    extra = i // height + j // width
    num = data[ix][jx] + extra
    return num % 10 + num // 10

while len(h) > 0:
    prisk, i, j = heappop(h) # get pos
    if (i,j) in visited:
        continue
    if (i,j) in risks and risks[(i,j)] != prisk:
        continue
    for diff in [(-1,0),(0,1),(1,0),(0,-1)]:
        di = i + diff[0]
        dj = j + diff[1]
        if di < 0 or di == realh or dj < 0 or dj == realw:
            continue
        if (di,dj) in visited:
            continue
        riskFromPos = getvalue(di,dj)
        riskToPos = risks[(i,j)]
        targetRisk = risks.get((di,dj), math.inf)
        newTargetRisk = min(targetRisk, riskToPos + riskFromPos)
        risks[(di,dj)] = newTargetRisk
        heappush(h, (newTargetRisk, di, dj))
    visited.add((i,j))

print(risks[(realh-1, realw-1)])
