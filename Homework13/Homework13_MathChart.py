n = 16

print('    ', end='')
for i in range(1, n):
    print(' %3d' % (i), end='')
    
for i in range(1, n):
    print('\n %2d:' % (i), end='')
    for j in range(1, n):
        print(' %3d' % (i*j), end='')
        
