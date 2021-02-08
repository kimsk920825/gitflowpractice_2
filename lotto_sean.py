import random

num = int(input("lotto 게임 수를 입력하세요 : "))


def generateLotto():
    print("lotto 자동 번호 입니다.")
    print("----------------------")
    # 입력한 게임 수 만큼 반복
    for x in range(1, num+1):
        lotto = [0, 0, 0, 0, 0, 0]

        lotto[0] = random.randrange(1, 46, 1)

        lotto[1] = lotto[0]
        lotto[2] = lotto[0]
        lotto[3] = lotto[0]
        lotto[4] = lotto[0]
        lotto[5] = lotto[0]
    pass

