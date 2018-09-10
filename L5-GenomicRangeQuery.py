# Lesson: 5 - Prefix Sums
# Excersice: GenomicRangeQuery
# link: https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

# Score : 100%

def solution(S, P, Q):
    leng = len(P)

    result = []
    for i in range(leng):
        subS = S[P[i]:Q[i]+1]
        if 'A' in subS:
            result.append(1)
        elif 'C' in subS:
            result.append(2)
        elif 'G' in subS:
            result.append(3)
        elif 'T' in subS:
            result.append(4)
    
    return result