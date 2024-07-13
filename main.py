#Hexa project


#function to print the first row hexagonal figure
def sa(a, b):
    m=b-1
    for i in range(b):
        print(' ___', end="    ")
    print('')
    for i in range(b):
        print("/   \\", end="")
        if 0<m:
            print("___",end="")
            m=m-1

    print()
    for i in range(b):
        print('\___/', end="   ")

#function to print the existing hexagonal structure
def samp(c,d):
    for i in range(c-1):
        m=c-1
        for i in range(c):
            print('', end="    ")
        print('')
        for i in range(c):
            print("/   \\", end="")
            if 0<m:
                print("___",end="")
                m=m-1

        print()
        for i in range(c):
            print('\___/', end="   ")
#assigning values to the rows and columns
x=int(input("ENTER THE NO OF ROW:"))
y=int(input("ENTER THE NO OF COLOUMN:"))
#function calls
sa(1,x)
samp(x,y)