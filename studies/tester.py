def solution(N):
    # write your code in Python 3.6
    if (N < 10):
        return 0
    i = 0

    while N >= 10:
        N = N // 10
        i += 1
    temp = 1

    for j in range(0, i):
        temp *= 10

    return temp

print(solution(7000))