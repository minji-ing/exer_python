# 단어 통계 정보 산출
import os
# random과 datetime 모듈을 import
import random
import datetime

# log directory 없으면 생성
if not os.path.isdir("log"):
    os.mkdir("log")

# log directory 있지만 log\count_log.txt 파일 없으면 파일 생성
if not os.path.isfile("log\\count_log.txt"):
    f = open("log\\count_log.txt","w", encoding = "utf-8")
    f.close()

# log/count_log.txt 을 append mode로 파일을 오픈
with open("log\\count_log.txt", "a", encoding="utf-8") as f:
    # range(1,11) 함수를 사용하여 for loop 돌면서
    for i in range(1, 11):
        # 현재 시간(timestamp)을 string으로 변환하여 stamp에 저장
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        stamp = str(timestamp)
        # 랜덤한 값에 100000 곱해서 value에 저장
        value = random.randint(1,10) * 100000
        # stamp와 value를 파일에 write()
        data = "현재 시각 : %s, random : %d \n" % (stamp, value)
        f.write(data)


