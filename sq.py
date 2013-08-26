def sq(a):
    a=a/1.0
    x=a/2
    while True:
        y= (x+a/x)/2
        if abs(y-x) < 0.001:
            
            break
        else:
            x=y
    print y    
