# Lesson: 2 - Arrays
# Excersice: CyclicRotations
# link: https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

# Score : 100%

def solution(A, K):
    if len(A) == 0 or K==0:
        return A
    for i in range(K):
        A = [A[-1]] + A[:-1]
    return A