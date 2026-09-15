
def printfunction(x):
    y = ""
    for i in range(x+1):
        if i != 0:
            y = y+str(i)
    print(y)

def printfunction1(x):
    for i in range(1,n+1):
        print(i,end="")

def printfunction2(x):
    for i in range(n):
        print(i+1, end="")


if __name__ == '__main__':
    n = 3
    printfunction(n)