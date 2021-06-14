### 파일 합치기
import sys
tc = int(input())

MAX = sys.maxsize

def solution(N, A):
    sums = [0]
    for i in A:
        sums.append(sums[-1] + i)

    dp = [[], [0] * N, [sums[i + 1] - sums[i] for i in range(N - 1)]]
    knuth_old = [1] * (N - 1)

    for d in range(3, N + 1):
        min_sum, knuth_new = [], [] 

        for i in range(N - d + 1):
            tmp_sum, tmp_knuth = MAX, knuth_old[i]

            for k in range(knuth_old[i], knuth_old[i + 1] + 2):
                if tmp_sum >= (new_sum := dp[k][i] + dp[d - k][k + i] + sums[d + i] - sums[i]):
                    tmp_sum, tmp_knuth = new_sum, k
            min_sum.append(tmp_sum)
            knuth_new.append(tmp_knuth)

        dp.append(min_sum)
        knuth_old = knuth_new

    return dp[-1][-1]

tc = int(input())
for _ in range(tc):
    N = int(input())
    A = list(map(int, input().split()))
    print(solution(N, A))