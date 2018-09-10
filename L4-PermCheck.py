# Lesson: 4 - Counting Elements
# Excersice: PermCheck
# link: https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

# Score : 75%

def solution(A):
    A.sort()
    
    if len(A) == max(A)-min(A)+1:
        if A[0]==1:
            distinct = list(set(A))
            if len(distinct) == len(A):
                return 1
            else: 
                return 0
        else:
            return 0
    
    for i in range(1,len(A)+1):
        if i not in A:
            return 0
    