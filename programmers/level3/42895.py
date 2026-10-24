# N으로 표현

def solution(N, number):
    # N으로 만들 수 있는 숫자를 저장할 set
    check = [set() for _ in range(9)]
    
    for i in range(1, 9) :
        # N을 이어 붙여서 만든 숫자 추가
        check[i].add(int(str(N)*i))
        
        # 사칙연산 조합
        for j in range(1, i) :
            for num1 in check[j] :
                for num2 in check[i-j] :
                    check[i].add(num1 + num2)
                    check[i].add(num1 - num2)
                    check[i].add(num1 * num2)
                    if num2 != 0 :
                        check[i].add(num1//num2)
                        
        if number in check[i] :
            return i
    return -1