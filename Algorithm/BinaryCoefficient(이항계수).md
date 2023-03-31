# BinaryCoefficient(이항계수)
> 재귀, 파스칼 삼각형 


```py
def bi(n, k):
    if k > n:
        return 0
    
    dp = [[-1]* (n+1) for _ in range(n+1)]

    def choose(times, left):
        if times == 0:
            return left == 0
        
        if dp[times][left] != -1:
            return dp[times][left]
        else:
            dp[times][left] = choose(times-1, left) + choose(times-1, left-1)
            return dp[times][left]

    return choose(n, n - k)
```