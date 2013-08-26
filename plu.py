
def plu():
    z=raw_input("\nenter a word: ")































    if z[-1]=='y':
        z=z[0:-1]+'ies'



    










        
    elif z[-1]=='f':
        z=z[0:-1]+'ves'
    
    
    elif z[-1]=='h' or z[-1]=='x' or z[-1]=='s':
        z=z+'es'

  
    else:
        z=z+'s'
    print "plural of this word is",z
    x=raw_input("\nDo you want to try again?(y/n): ")
    if x=='y':
        plu()
plu()
