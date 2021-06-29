N, K, M = input().split(' ')
N = int(N)
K = int(K)
M = int(M)

details = 0 

while N >= K and M <= K:
    details += (N // K) * (K // M)
    N = (N % K) + (N // K)*(K % M)
    
print(details)
