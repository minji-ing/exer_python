def make(array, commands):
    answer = []

    for i in commands:
        com = i
        cut = []
        for j in range(com[0],com[1]+1):
            cut.append(array[j-1])
        cut.sort()
        answer.append(cut[com[2]-1])
    print(answer)

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

make(array, commands)