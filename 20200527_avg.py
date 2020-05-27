# 입력으로 들어오는 모든 수의 평균 값을 계산
# 입력으로 들어오는 수의 개수는 정해져 있지 않음

# 숫자 반복으로 입력받아서 total 구하기
target = input("평균을 구하고자 하는 숫자를 입력해주세요.\n입력을 끝내려면 'end'를 입력하세요.\n")
count = 0
total = 0
while target != 'end':
    count += 1
    total += int(target)
    target = input("다음 숫자를 입력해주세요.\n입력을 끝내려면 'end'를 입력해주세요.\n")

# 입력이 종료된 숫자들의 합으로 평균 구하기
if target == 'end':
    avg = total / count
    print("입력하신 숫자들의 평균은 %f입니다." % avg)