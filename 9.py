for i in range(1,500):
    for j in range(1,i):
        for k in range(1,j):
            if k*k + j*j == i*i and i + j + k == 1000:
                print "success %s,%s, %s" % (i,j,k)
        
