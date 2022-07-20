tests = [[[1,2,3],[3,1,2],[2,3,1]], [[1,1,1],[1,2,3],[1,2,3]]]

for test in tests:

    t = len(test[0])
    for i in range(t):
        for j in range(t):
            print(test[i][j], end='')
        print('')
    print('')