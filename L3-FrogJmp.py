# Lesson: 3 - Time Complexity
# Excersice: FrogJmp
# link: https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

# Score : 100%
import math
def solution(X, Y, D):
    if X==Y:
        return 0
    return math.ceil((Y-X)/D)