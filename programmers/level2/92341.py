# 주차ㅇ 요금 계산

from collections import defaultdict
from math import ceil

def to_minutes(time) :
    h, m = map(int, time.split(":"))
    return 60*h+m

def solution(fees, records):
    base, base_fee, unit_time, unit_fee = fees
    dict_records = {}
    dict_fee = defaultdict(int)
    
    for record in records :
        t, num, IO = record.split(" ")
        
        t_min = to_minutes(t)
        
        if IO == "IN" :
            dict_records[num] = t_min
        elif IO == "OUT" :
            dict_fee[num] += t_min - dict_records.pop(num)
    
    for car, in_time in dict_records.items() :
        dict_fee[car] += to_minutes("23:59") - in_time
        
    answer = []
        
    for car_num in sorted(dict_fee.keys()) :
        total_time = dict_fee[car_num]
        if total_time > base :
            fee = base_fee + ceil((total_time - base)/unit_time)*unit_fee
            
            answer.append(fee)
        else :
            answer.append(base_fee)
    
    return answer