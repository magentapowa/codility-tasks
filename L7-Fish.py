# Lesson: 7 - Stacks and Queues
# Excersice: Fish
# link: https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

# Score : 75%

def solution(A, B):
    
    i = 0
    while i < len(A)-1:
        if B[i] == 1 and B[i+1] == 0:
            if A[i] > A[i+1]:
                A.pop(i+1)
                B.pop(i+1)
            else:
                A.pop(i)
                B.pop(i)
                i = 0
        else:
            i += 1
    
    return len(A)