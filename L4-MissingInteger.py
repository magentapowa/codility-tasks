# Lesson: 4 - Counting Elements
# Excersice: MissingInteger
# link: https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

# Score : 66%

def solution(A):
   # A = [ x for x in A if x>0]
    
    for i in range(1,100001):
        if i not in A:
            return i
    #    else:
    #       A = [x for x in A if x>i]