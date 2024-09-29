import sys
def rS(): return sys.stdin.readline().rstrip()

def main():
    ans = 0;
    for i in range(12):
        S = sys.stdin.readline().rstrip()

        if len(S) == i+1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
