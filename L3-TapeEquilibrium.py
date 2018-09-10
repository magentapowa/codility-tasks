# Lesson: 3 - Time Complexity
# Excersice: TapeEquilibrium
# link: https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

# Score : 100%

def solution(A):
    X = A[0]
    Y = sum(A[1:])

    diff = abs(X-Y)
    min = diff
    for i in range(1,len(A)-1):
        X +=A[i]
        Y -=A[i]
        diff = abs(X-Y)
        if diff<min:
            min = diff
    return min