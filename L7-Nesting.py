# Lesson: 7 - Stacks and Queues
# Excersice: Nesting
# link: https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/

# Score : 100%
def solution(S):
    lefts = S.count('(')
    rights = S.count(')')
    if lefts != rights:
        return 0
        
        
    open = 0
    for i in S:
        if i == "(":
            open += 1
        else:
            open -= 1
        
        if open<0:
            return 0
    
    if open == 0 :
        return 1