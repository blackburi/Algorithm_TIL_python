# 섬 연결하기

def solution(n, costs):
    answer = 0
    # cost 기준으로 정렬
    costs.sort(key = lambda x : x[2])
    connect = set()
    connect.add(costs[0][0])
    
    # 모든 도시가 연결될 때까지 진행
    while len(connect) != n :
        for cost in costs :
            # 두 node가 이미 연결된 경우
            if cost[0] in connect and cost[1] in connect :
                continue
            # 두 node 중 1개만 연결된 경우
            if cost[0] in connect or cost[1] in connect :
                connect.add(cost[0])
                connect.add(cost[1])
                answer += cost[2]
                break # break가 꼭 들어가야 함 -> 현재 연결된 다리 중 최적을 나타내지만, 전체의 최적이 아니기 때문에

    return answer