import sys
input = sys.stdin.readline

dp = [0] * 1001

dp[0] = 1
dp[1] = 1

T = int(input())

for i in range(2, T+1):
    dp[i] = (dp[i-1] +  2*dp[i-2]) % 10007

print(dp[T])