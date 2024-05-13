# def comb(n, k):
#     ans = 1
#     for i in range(n-k+1,n+1):
#         ans *=i
#     for i in range(1,k+1):
#         ans/=i
#     return ans

# def fact(num):
#     if num == 1 or num == 0:
#         return 1
#     return num * fact(num - 1)

# def comb(n, k):
#     if k>n:
#         return 0
#     fact_n = 1
#     for i in range(1,n+1):
#         fact_n*=i
#     fact_k = 1
#     for i in range(1,k+1):
#         fact_k*=i
#     fact_x = 1
#     for i in range(1,n-k+1):
#         fact_x*=i    
#     return fact_n/(fact_k*fact_x)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def comb(n, k):
    if k > n:
        return 0
    else:
        return factorial(n) // (factorial(k) * factorial(n - k))

print(comb(5,3))
print(comb(10,0))
print(comb(10,2))
print(comb(5,7))