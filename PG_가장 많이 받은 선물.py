
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

                if give_info[idx][idx2] > give_info[idx2][idx]:
                    answer_list[name] += 1
                elif give_info[idx][idx2] < give_info[idx2][idx]:
                    answer_list[name2] += 1
                else:
                    name_score = sum(give_info[idx]) - sum(receive_info[idx])
                    name2_score = sum(give_info[idx2]) - sum(receive_info[idx2])
                    
                    if name_score > name2_score:
                        answer_list[name] += 1 
                    elif name_score < name2_score:
                        answer_list[name2] += 1
                    
            else: # 없다면

                name_score = sum(give_info[idx]) - sum(receive_info[idx])
                name2_score = sum(give_info[idx2]) - sum(receive_info[idx2])

                if name_score > name2_score:
                    answer_list[name] += 1 
                elif name_score < name2_score:
                    answer_list[name2] += 1

    if answer_list:
        answer = max(answer_list.values()) // 2
    else:
        answer = 0
    
    return answer