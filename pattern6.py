for r in range(5):
    for c in range(r+1):
        if c<1 :
            print((5-r)*' ',r,end = '')
        else:
            print('',r,end = '')
    print()
       
