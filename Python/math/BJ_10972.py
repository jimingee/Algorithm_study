import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    num = list(map(int, input().split()))
    
    for i in range(N-1, 0, -1):
        if num[i-1] < num[i]:
            for j in range(N-1, 0, -1):
                if num[i-1] < num[j]:
                    num[i-1], num[j] = num[j], num[i-1]
                    num = num[:i]+sorted(num[i:])
                    for i in num :
                        print(i, end=' ')
                    exit()
                    
    print('-1')