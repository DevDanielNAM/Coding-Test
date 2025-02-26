from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    cur_weight = 0
    while len(truck_weights) > 0:
        time+=1
        cur_weight = cur_weight - bridge.popleft()
        
        if cur_weight + truck_weights[0] <= weight:
            cur_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else: 
            bridge.append(0)
        
    time += bridge_length
    
    return time