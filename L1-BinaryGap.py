# Lesson: 1 - Iterations
# Excersice: BinaryGap
# link: https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

# Score : 100%

def solution(N):
    a = format(N,'b')
    b = a.split("1")
    b = b[1:-1]
    if len(b) == 0:
        return 0
    return len(max(b, key=len))