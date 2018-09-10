# Lesson: 6 - Sorting
# Excersice: MaxProductOfThree
# link: https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/

# Score : 44%

def solution(A):
    lenA = len(A)
    maxP = -1000000000
    for i in range(lenA-2):
        for j in range(i+1,lenA-1):
            for k in range(j+1, lenA):
                prod = A[i]*A[j]*A[k]
                if prod > maxP:
                    maxP = prod
    
    return maxP