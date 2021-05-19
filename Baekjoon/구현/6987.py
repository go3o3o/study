### 월드컵
from itertools import combinations
import sys

input = sys.stdin.readline

def backtracking(k):
    global ans 
    if k == 15:
        if [e for e in team[0].values()] == [0] * 3:
            ans = 1
        return
    if team[game[k][0]]['win'] and team[game[k][1]]['lose']:
        team[game[k][0]]['win'] -= 1
        team[game[k][1]]['lose'] -= 1
        backtracking(k + 1)
        team[game[k][0]]['win'] += 1
        team[game[k][1]]['lose'] += 1

    if team[game[k][0]]['draw'] and team[game[k][1]]['draw']:
        team[game[k][0]]['draw'] -= 1
        team[game[k][1]]['draw'] -= 1
        backtracking(k + 1)
        team[game[k][0]]['draw'] += 1
        team[game[k][1]]['draw'] += 1

    if team[game[k][0]]['lose'] and team[game[k][1]]['win']:
        team[game[k][0]]['lose'] -= 1
        team[game[k][1]]['win'] -= 1
        backtracking(k + 1)
        team[game[k][0]]['lose'] += 1
        team[game[k][1]]['win'] += 1

def make_team(record):
    ret = []
    for i in range(0, 18, 3):
        ret.append({
            'win': record[i],
            'draw': record[i + 1],
            'lose': record[i + 2]
        })
    return ret

for _ in range(4):
    team = make_team(list(map(int, input().split())))
    game = list(combinations(range(6), 2))
    ans = 0
    backtracking(0)
    print(ans, end = ' ')