# Lesson: 6 - Sorting
# Excersice: Triangle
# link: https://app.codility.com/programmers/lessons/6-sorting/triangle/

# Score : 75%

def solution(A):
    lenA = len(A)
    for i in range(lenA-2):
        for j in range(i+1,lenA-1):
            for k in range(j+1,lenA):
                if A[i]+A[j]>A[k] and A[i]+A[k]>A[j] and A[j]+A[k]>A[i]:
                    return 1
                
    return 0