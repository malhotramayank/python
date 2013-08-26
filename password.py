# PASSWORD PROGRAM


def pas(pwd):
    ##pwd=raw_input("Enter a password")
    if pwd=="cluster":
        print"password right"
    else:
        print"Access denied"
        pas(raw_input())
pwd=raw_input("Enter a password")
pas(pwd)     

    
