# Lesson: 3 - Time Complexity
# Excersice: PermMissingElem
# link: https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

# Score : 100%

def solution(A):
    A.sort()
    if A:
        if len(A) != A[-1]-A[0]+1:
            for i in range(len(A)):
                if A[i]+1 != A[i+1]:
                    return A[0]+i+1
        else:   
            if A[0]-1==0:
                return A[-1]+1
            else: 
                return A[0]-1
    else:
        return 1