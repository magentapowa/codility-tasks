# Lesson: 5 - Prefix Sums
# Excersice: MinAvgTwoSlice
# link: https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

# Score : 50%

def solution(A):
    lenA = len(A)
    avg = []
    pos = []
    
    for i in range(lenA-1):
        for j in range(i+1,lenA):
            sub = A[i:j+1]
            avg.append(sum(sub)/len(sub))
            pos.append(i)
            

    return pos[avg.index(min(avg))]