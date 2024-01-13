'''
if 선물 더 많이 주면 담달에 하나 받음
else면 선물지수 비교 후 작은 사람에게 하나 받음 

선물지수 : 준 선물 수 - 받은 선물 수 (음수 가능)

'''

def whos_more(idx,idx2,give_info,receive_info):
    if give_info[idx][idx2] > give_info[idx2][idx]:
        return idx
    
    elif give_info[idx][idx2] < give_info[idx2][idx]:
        return idx2
    
    else:
        name_score = sum(give_info[idx]) - sum(receive_info[idx])
        name2_score = sum(give_info[idx2]) - sum(receive_info[idx2])

        if name_score > name2_score:
            return idx
        elif name_score < name2_score:
            return idx2
        else:
            return -1 # 선물 지수가 같은 경우
        
    
    
def get_gift_score(idx,idx2,give_info,receive_info):
    
    name_score = sum(give_info[idx]) - sum(receive_info[idx])
    name2_score = sum(give_info[idx2]) - sum(receive_info[idx2])

    if name_score > name2_score:
        return idx
    elif name_score < name2_score:
        return idx2
    
    return -1 # 선물 지수가 같은 경우

def solution(friends, gifts):
    from collections import defaultdict
    
    name_to_num = {}
    num_to_name = {}
    
    for idx, name in enumerate(friends):
        name_to_num[name] = idx
        num_to_name[idx] = name
        
    N = len(friends)
    
    give_info = [[0] * N for _ in range(N)]
    receive_info = [[0] * N for _ in range(N)]
    
    for gift in gifts:
        give_name, receive_name = gift.split()
        
        give_info[name_to_num[give_name]][name_to_num[receive_name]] += 1
        receive_info[name_to_num[receive_name]][name_to_num[give_name]] += 1
        
    answer_list = defaultdict(int)
    
    for idx, name in enumerate(friends):
        for idx2, name2 in enumerate(friends):
            if idx == idx2: continue

            if give_info[idx][idx2] or give_info[idx2][idx]: # 주고 받은 기록이 있다면
                
                result = whos_more(idx,idx2,give_info,receive_info)

                if result < 0: continue
                
                answer_list[num_to_name[result]] += 1
                  
            else: # 없다면
                result = get_gift_score(idx,idx2,give_info,receive_info)

                if result < 0: continue 
                
                answer_list[num_to_name[result]] += 1

                
    if answer_list:
        print(answer_list)
        answer = max(answer_list.values()) // 2
    else:
        answer = 0
    
    return answer