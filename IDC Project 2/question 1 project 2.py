# Question number one : Ackermann's function

m = float(input('M: '))
n = float(input('N: '))

def ackermann(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

print(ackermann(m,n))


        
    
