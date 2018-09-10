# Lesson: 4 - Counting Elements
# Excersice: FrogRiverOne
# link: https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

# Score : 54%

def solution(X, A):
    steps = [x  for x in range(1,X+1)]
    
    #check if all steps are in A
    for s in steps:
        if s not in A:
            return -1
    
    # for index,l in enumerate(A):
    #     if l in steps
    #         steps.remove(l)
    #         if steps==[]:
    #             return index
            
    positions = []

    for s in steps:
        positions.append(A.index(s))
    return max(positions)