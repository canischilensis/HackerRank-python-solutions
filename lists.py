if __name__ == '__main__':
    N = int(input())
    L = []
    for _ in range(N):
        A = list(input().split())
        cmd = A[0] #cmd is command
        if cmd == "insert":
            L.insert(int(A[1]),int(A[2]))
        elif cmd == "append":
            L.append(int(A[1]))
        elif cmd == "remove":
            L.remove(int(A[1]))
        elif cmd == "print":
            print(L)
        elif cmd == "pop":
            L.pop()
        elif cmd == "reverse":
            L.reverse()
        elif cmd == "sort": 
            L.sort()
