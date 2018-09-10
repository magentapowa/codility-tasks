# Lesson: 5 - Prefix Sums
# Excersice: PassingCars
# link: https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

# Score : 60%

def solution(A):
    lenA = len(A)
    # count = 0
    
    # for i in range(lenA-1):
    #     if A[i]==0:
    #         for j in range(i+1,lenA):
    #             if A[j] == 1:
    #                 count += 1
    
    # return count
    
    zeros = []
    ones = []
    
    for i in range(lenA):
        if A[i] == 0:
            zeros.append(i)
        else:
            ones.append(i)
    
    count = 0
    for i in zeros:
        #count += sum(j > i for j in ones)
        count += sum(1 for j in ones if j > i)  
        if count>1000000000:
            return -1  
    
    return count