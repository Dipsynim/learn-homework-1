def count_factorial(n):
    if n ==1:
        return 1
    return n*count_factorial(n-1)
    
print(count_factorial(5))