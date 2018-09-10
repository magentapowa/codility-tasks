# Lesson: 5 - Prefix Sums
# Excersice: CountDiv
# link: https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

# Score : 62%

def solution(A, B, K):
    count = 0
    step = 1 
    i = A
    while i<=B:
        if i%K == 0:
            step = K
            count += 1
        i += step
    return count