# Reading number of unknowns
n = int(input('Enter number of unknowns: '))

# Making nested lists of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = [[0 for _ in range(n + 1)] for _ in range(n)]

# Making list of n size and initializing 
# to zero for storing solution vector
x = [0 for _ in range(n)]

# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input(f'a[{i}][{j}]='))
        
# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
        
    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]
        
        for k in range(n + 1):
            a[j][k] -= ratio * a[i][k]

    print("----")
    for line in a:
        print(line)
    print("----")

# Back Substitution
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]
    
    for j in range(i + 1, n):
        x[i] -= a[i][j] * x[j]
    
    x[i] /= a[i][i]

# Displaying solution
print('\nRequired solution is: ')
for i in range(1, n + 1):
    print(f'X{i} = {x[i-1]:0.2f}', end='\t')