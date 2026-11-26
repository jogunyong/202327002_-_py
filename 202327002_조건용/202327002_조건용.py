def gugu(num):
    for i in range(1, 10):
        print(num, "X", i, "=", num * i)

num = int(input("몇단을 입력할까요? "))
gugu(num)

import turtle

# 화면 설정
screen = turtle.Screen()
screen.setup(800, 800)
screen.tracer(1)  # 실시간 그리기 활성화

turtle.hideturtle()
turtle.speed(0)  # 그림 그리는 속도 최대로 설정


def go(x, y, heading=0):
    try:
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(heading)
        turtle.pendown()
    except turtle.Terminator:
        pass  # 실행 도중 창을 닫아도 에러 메시지가 뜨지 않도록 처리


# 보노보노 그리기 (얼굴 + 다리)
def bonobono(cx=0, cy=40):
    # 1. 다리 (얼굴보다 먼저 그려서 몸통 아래쪽으로 자연스럽게 연결)
    turtle.color("#3b6e9c", "#6ea8d8")
    turtle.pensize(3)
    for dx in (-68, 68):
        go(cx + dx, cy - 178)
        turtle.begin_fill()
        turtle.circle(36)
        turtle.end_fill()

    # 2. 얼굴 (위쪽은 살짝 좁고 아래 볼이 통통한 달걀형 실루엣)
    go(cx, cy - 145)
    turtle.color("#3b6e9c", "#6ea8d8")
    turtle.pensize(3)
    turtle.begin_fill()
    turtle.circle(165, 65)
    turtle.circle(135, 230)
    turtle.circle(165, 65)
    turtle.end_fill()

    # 3. 눈
    turtle.color("black")
    for dx in (-88, 88):
        go(cx + dx, cy + 32)
        turtle.dot(16)

    # 4. 입 (볼주머니 아래 살짝 보이는 분홍빛 입)
    go(cx - 14, cy - 88, -60)
    turtle.color("#3b6e9c", "#e88b9c")
    turtle.pensize(2)
    turtle.begin_fill()
    turtle.circle(16, 120)
    turtle.left(120)
    turtle.forward(28)
    turtle.end_fill()

    # 5. 흰 볼주머니
    turtle.color("#4a6b82", "white")
    turtle.pensize(2)
    for dx in (-26, 26):
        go(cx + dx, cy - 88)
        turtle.begin_fill()
        turtle.circle(31)
        turtle.end_fill()

    # 6. 코 (둥근 역삼각형)
    go(cx - 22, cy - 22, 0)
    turtle.color("black", "black")
    turtle.pensize(6)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(44)
        turtle.right(120)
    turtle.end_fill()

    # 7. 수염
    turtle.pensize(2)
    turtle.color("black")
    for side in (-1, 1):
        base_heading = 0 if side == 1 else 180
        for dy, angle in ((12, 12), (0, 0), (-12, -12)):
            go(cx + side * 48, cy - 58 + dy, base_heading + (side * angle))
            turtle.forward(55)
    turtle.pensize(1)


# 화면 중앙에 보노보노 그리기
bonobono(0, 40)

# 화면 클릭 시 창 닫기
screen.exitonclick()