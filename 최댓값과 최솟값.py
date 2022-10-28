def solution(s):
    answer = ''
    arr=[]
    s_split=s.split(" ")
    
    for i in s_split:
        arr.append(int(i))
    

    answer+=str(min(arr))+" "+str(max(arr))
    
    return answer
