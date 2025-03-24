def main():
    import random

    flag = 0

    while 1:
        if flag:
            break

        computer = random.sample(range(1, 10), 3)

        print("숫자 야구 게임을 시작합니다.")

        while 1:
            print("숫자를 입력해주세요: ", end="")
            player = list(map(int, input()))

            if len(player) != 3:
                raise (ValueError)

            for i in range(3):
                if player[i] < 1 or player[i] > 9:
                    raise (ValueError)

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
                q = int(input())
                if q == 1:
                    flag = 0
                elif q == 2:
                    flag = 1
                print("게임 종료")
                break


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
