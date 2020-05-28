# i_have_a_dream 파일을 읽어서 
# 전체 글자 수, 전체 단어 수, 전체 라인 수 출력

# i_have_a_dream 파일 open
with open("i_have_a_dream.txt", "r") as my_file:
    # open한 파일 띄어쓰기 기준으로 잘라 전체 단어 contents 리스트에 넣기
    contents = my_file.read().split()
    # contents 리스트의 단어들의 글자 수를 셀 변수 선언
    words = 0
    idx = 0
    # contents 리스트의 인덱스 기준으로 반복하여 words에 글자수 더하기
    while idx < len(contents):
        words += len(contents[idx])
        idx += 1
    # 한 번 read한 파일 다시 read하기 위해 처음으로 위치 돌리기
    my_file.seek(0)
    # 파일 한 줄씩 읽어서 content_line 리스트에 저장
    content_line = my_file.readlines()

    print("파일의 전체 글자 수는 %d 개이다." % words)
    print("파일의 전체 단어 수는 %d 개이다." % len(contents))
    print("파일의 전체 라인 수는 %d 개이다." % len(content_line))
