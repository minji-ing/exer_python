# 태어난 년도를 입력 받아 나이를 계산하고, 고등학생인지 대학생인지 확인

# 현재 년도 계산
from datetime import datetime as dt
today = dt.today().year

# 태어난 년도를 입력하라고 메시지를 보내고 사용자 입력을 받음
birth = input("태어난 연도를 입력하세요.\n")

# 나이 계산
age = today - int(birth) + 1

# 학생 확인
if 17 <= age < 20:
    print("고등학생입니다.\n")
elif 20 <= age < 27:
    print("대학생입니다.\n")
else:
    print("학생이 아닙니다.\n")