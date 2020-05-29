# 겹치는 수가 없는 로또 만들기

import random

# 서로 다른 6개의 정수를 저장할 배열 선언
num_arr = []

# 배열에 정수가 포함되는 지 확인하는 함수
def chk(num_arr, num):
    chk_result = True
    for i in num_arr:
        if(i == num):
            chk_result = False
    return chk_result

# 1~45 사이 임의의 정수를 만든 후
# 얻은 정수가 배열에 포함된 수인지 확인하고 포함되지 않은 정수만 배열에 저장
seq = 1
while seq <= 6:
    num = random.randint(1,45)
    if seq == 1:
        num_arr.append(num)
    else:
        if chk(num_arr, num) == True:
            num_arr.append(num)
    seq += 1

# 6개가 저장된 배열을 증가순으로 정렬
num_arr.sort()

# 정렬된 배열 출력
print(num_arr)
    