# 입력받은 정수 n 이하까지 피보나치 수열 출력

# 정수 n 입력 받기
limit = int(input("1이상의 자연수를 입력해주세요. : "))

# 피보나치 수열 정렬할 리스트 초기값
fibo = [0,1]

# 정수 n 이하까지 피보나치 수열 정렬
idx = 0
for i in fibo:
    next = fibo[idx]+fibo[idx+1]
    if(next <= limit):
        fibo.append(next)
        idx += 1
print(fibo)
