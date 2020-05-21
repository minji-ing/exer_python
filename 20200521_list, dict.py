# 주어진 데이터를 리스트와 딕셔너리를 사용하여 작성

# 각 로우를 딕셔너리로 표현
key = {}
val1 = {}
val2 = {}
val3 = {}
val4 = {}
key['key'] = 'id','name','email','hp_num'
val1['val1'] = '1','2','3','4'
val2['val2'] = 'hong kildong','lee soonsin','jang youngsil','king sejong'
val3['val3'] = 'hong@mail.com','lee@mail.com','jang@mail.com','king@mail.com'
val4['val4'] = '010-2343-9870','010-3333-5555','010-7777-1234','010-4567-0987'

# 4개의 딕셔너리를 포함한 리스트를 만든다
list = [key, val1, val2, val3, val4]

# 각 딕셔너리의 key와 value 출력
i = 0
while i < len(list):
    dict1 = list[i].keys()
    for val in list[i][dict1]:
        print(val)
    i += 1

