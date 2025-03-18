a, b = map(int, input().split())

def cond(a, b):
    cnt = 0  # 전체 누적 카운트를 위한 변수는 for문 바깥에 선언
    for i in range(a, b+1):
        if i < 2:
            continue
        
        # 소수 판별
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if not is_prime:
            continue  # 소수가 아니면 다음 숫자로 넘어감
        
        # 자리수 합 계산 (내장 함수 sum()을 사용)
        digit_sum = sum(int(d) for d in str(i))
        if digit_sum % 2 == 0:
            cnt += 1
    return cnt

print(cond(a, b))
