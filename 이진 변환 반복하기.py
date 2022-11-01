def solution(s):
    answer = []
    count=0
    new_s=''
    times=0
    
    while(len(s)>1):
        new_s=''
        new_num=0
        
        for i in s:
            if i=="0":
                count+=1
            elif i=="1":
                new_s+=i
        new_num= format(len(new_s), 'b')
        s=new_num
        times+=1
    
    answer.append(times)
    answer.append(count)
    
    return answer
