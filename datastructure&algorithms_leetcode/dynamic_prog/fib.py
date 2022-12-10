memo = {}

def fib(n):
    if n in memo: 
        return memo[n]
    if n<= 2: 
        f = 1
    else: 
        f = fib(n-1) + fib(n-2)
        memo[n] = f
    return f

print(fib(80))

# dynamic bottom-up
fi  ={}
def fibs(n):
    for k in range(1, n+1):
        if k <= 2: 
            f = 1
        else: 
            f = fi[k-1] + fi[k-2]            
        fi[k] = f
    return fi[n]

print(fibs(80))

def s(n):
    one, two = 1, 1
    for _ in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one

print(s(80))    
        
        
    