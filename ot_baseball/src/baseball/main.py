def main():
    import random

    flag = False

    while not flag:
        computer = random.sample(range(1, 10), 3)
        print("숫자 야구 게임을 시작합니다.")

        while 1:
            print("숫자를 입력해주세요: ", end="")

            player = list(map(int, input()))

            if len(player) != 3 or any(num <= 0 for num in player):
                raise ValueError

            strike = 0
            ball = 0

            for i in range(3):
                for j in range(3):
                    if computer[i] == player[j]:
                        if i == j:
                            strike += 1
                        else:
                            ball += 1

            if strike == 0:
                if ball == 0:
                    print("낫싱")
                else:
                    print(f"{ball}볼")
            else:
                if ball == 0:
                    print(f"{strike}스트라이크")
                else:
                    print(f"{ball}볼 {strike}스트라이크")

            if player == computer:
                print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
                print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")

                q = input()
                if q == "1":
                    flag = False
                elif q == "2":
                    flag = True
                else:
                    raise ValueError

                break


if __name__ == "__main__":
    main()
