def solution(A,B):
    answer = 0

    
    A_sort=sorted(A)
    B_sort=sorted(B, reverse=True)
    
    for i in range(len(A_sort)):
        answer+=A_sort[i]*B_sort[i]
            
            
    return answer
