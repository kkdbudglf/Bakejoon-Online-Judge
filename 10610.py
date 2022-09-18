n = int(input())  # 정수 입력 받기
str_n = str(n)  # 입력 받은 정수 문자형으로 변환하여 저장
save = []  # 리스트 생성

end = False  # while 문 돌기 위한 변수

# - 입력 받은 정수 내림차순 정렬 -

while not end:
    for i in str_n:
        save.append(int(i))
    save.sort(reverse=True)

    # - 일의 자리가 0인지 확인 -
    if save[len(save)-1] != 0:
        print(-1)
        end = True

    # - 입력된 정수들을 다 더한 후 3의 배수일 때 -
    elif sum(save) % 3 == 0:
        for j in save:
            print(j, end="")
            end = True

    # - 입력된 정수들을 다 더한 후 3의 배수가 아닐 때 -
    else:
        print(-1)
        end = True
