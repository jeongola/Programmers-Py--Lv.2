def solution(brown, yellow):

    sum_ = brown + yellow
    answer = []

    for a in range(3, sum_):
        b = int(sum_ / a)

        if( ((b * a) == sum_) & (b >= a) & ( ((a-2) * (b-2)) == yellow)):                
            answer = [b, a]
            break


    return answer
