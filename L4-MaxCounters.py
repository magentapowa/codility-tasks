# Lesson: 4 - Counting Elements
# Excersice: MaxCounters
# link: https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

# Score : 77%

def solution(N, A):
    #result
    R = [0 for x in range(N)]
    UP = [x for x in A if x > N]
    if len(UP) == len(A):
        return R
    
    flag = False
    for i in A:
        if i > N:
            if flag:
                continue
            flag = True
            maxR = max(R)
            R = [maxR for x in R]
        else:
            flag = False
            R[i-1]+=1
    
    return R