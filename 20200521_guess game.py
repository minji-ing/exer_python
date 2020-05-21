# Guess Game

# 1~100 사이의 값을 랜덤하게 추출
import random
target = random.randint(1,100)

# 사용자로부터 숫자를 입력 받는다.
inputNum = int(input("1부터 100 사이의 숫자 중 하나를 입력해주세요.\n"))

# 랜덤하게 추출한 숫자와 입력 받는 숫자가 같을 때까지 count하여 loop
count = 0
while count >= 0:
    if target != inputNum:
        if target < inputNum:
            print("숫자가 너무 큽니다. random : %s \n" % target)
        else:
            print("숫자가 너무 작습니다. random : %s \n" % target)
        count += 1
        target = random.randint(1,100)
        continue
    else:
        print(str(count)+"번")
        break
            
