# Lesson: 7 - Stacks and Queues
# Excersice: Brackets
# link: https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/

# Score : 75%

def solution(S):
    lenS = len(S)
    while True:
        S = S.replace('()','')
        S = S.replace('[]','')
        S = S.replace('{}','')
        if lenS == len(S):
            break
        lenS = len(S)
    
    if len(S) == 0:
        return 1
    
    lefts1 = S.count('(')
    lefts2 = S.count('[')
    lefts3 = S.count('{')
    rights1 = S.count(')')
    rights2 = S.count(']')
    rights3 = S.count('}')
    if lefts1 != rights1 or lefts2 != rights2 or lefts3 != rights3:
        return 0
    
    latestOpen = ''
    open1 = 0
    open2 = 0
    open3 = 0
    for i in S:
        if i == "(":
            latestOpen = i
            open1 += 1
        elif i ==')':
            if latestOpen != '(': return 0
            open1 -= 1
        elif i == "[":
            latestOpen = i
            open2 += 1
        elif i ==']':
            if latestOpen != '[': return 0
            open2 -= 1
        elif i == "{":
            latestOpen = i
            open3 += 1
        elif i =='}':
            if latestOpen != '{': return 0
            open3 -= 1
        
        if open1<0 or open2<0 or open3<0:
            return 0
        

    if open1==0 and open2==0 and open3==0:
        return 1