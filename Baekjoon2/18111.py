### 마인크래프트
import sys
from collections import Counter

def make_land(height):
    sec = 0
    for key in land:
        if key < height:
            sec += (height - key) * land[key]
        elif key > height:
            sec += (key - height) * 2 * land[key]
    return sec

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

_sum, length = sum(land), n*m 
land = dict(Counter(land))
height, min_sec = 0, sys.maxsize

for h in range(257):
    if length * h <= _sum + b:
        sec = make_land(h)
    if sec <= min_sec:
        min_sec = sec 
        height = h

print(min_sec, height)