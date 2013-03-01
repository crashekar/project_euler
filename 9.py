for i in range(1,99):
    for j in range(1,99):
        for k in range(1,99):
            if i*i + j*j == k*k and i + j + k == 1000:
                print "success %s,%s, %s" % (i,j,k)
        
