# Lesson: 6 - Sorting
# Excersice: Distinct
# link: https://app.codility.com/programmers/lessons/6-sorting/distinct/

# Score : 100%

def solution(A):
    A.sort()
    un = [A[0]] if len(A)>0 else []
    
    for i in A: 
        if i != un[-1]: 
            un.append(i)
    
    return len(un)