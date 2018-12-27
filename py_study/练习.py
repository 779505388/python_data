for i in range(1, 10):
    for j in range(i, i+1):
        print('{}*{}={:2}'.format(j, i, i*j), end='')
    print('')
