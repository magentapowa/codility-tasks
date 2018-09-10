# Lesson: 6 - Sorting
# Excersice: NumberOfDiscIntersections
# link: https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/

# Score : 56%

def solution(A):
    count = 0
    
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]+i >= j-A[j]:
                count += 1
                if count>10**7:
                    return -1
    return count