def solution(bandage, health, attacks):

    current_time = 0
    band_time = 0
    answer = 0
    
    curr_health = health
    for attack_time, damage in attacks:
        
        while health > 0:
            
            current_time += 1
            
            if current_time == attack_time: # 공격받는 시간이면
                curr_health -= damage # 데미지를 입는다
                
                if curr_health <= 0: # 체력이 없는 경우 
                    answer = -1
                    break
                else: # 체력이 있는 경우, 연속 성공 초기화
                    band_time = 0
                break
            else: # 공격받는 시간이 아니면
                band_time += 1 # 연속 성공이 증가하고
                curr_health+= bandage[1] # 초당 체력회복
                
                if band_time == bandage[0]: # t초 연속 성공한다면 
                    curr_health += bandage[2] # 추가 체력 회복
                    band_time = 0
                    
                if curr_health > health:
                    curr_health = health
            
    if answer == 0 :
        answer = curr_health
    
    return answer