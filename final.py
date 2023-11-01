from roboid import *

hamsters = (Hamster(0), Hamster(1))

def trace(robot):
    while True:
        robot.right_led(Hamster.LED_OFF)
        robot.left_led(Hamster.LED_OFF)
        if robot.left_floor() < 50 and robot.right_floor() < 50:
            robot.stop()
            break
        else:
            diff = robot.left_floor() - robot.right_floor()
            if diff < 0:
                robot.right_led(Hamster.LED_CYAN)
            else:
                robot.left_led(Hamster.LED_CYAN)
            robot.wheels(28 + diff * 0.7, 28 - diff * 0.7)

        wait(3)


hamsters[0].wheels(30, 30)
wait(1000)
hamsters[0].stop()

for i in range(1700):
    diff = hamsters[0].left_floor() - hamsters[0].right_floor()
    if diff < 0:
        hamsters[0].right_led(Hamster.LED_CYAN)
    else:
        hamsters[0].left_led(Hamster.LED_CYAN)
    hamsters[0].wheels(32 + diff * 0.6, 32 - diff * 0.6)

    wait(3)
    print(i)

trace(hamsters[0])
hamsters[0].left_led(Hamster.LED_CYAN)
hamsters[0].right_led(Hamster.LED_CYAN)

hamsters[1].wheels(-50, 50)  # 햄스터2 회전
wait(1200)

hamsters[1].stop()
while True:
    hamsters[1].wheels(30, 30)
    wait(15)

    if hamsters[1].left_floor() < 50 and hamsters[1].right_floor() < 50:  # 정지선인 경우
        hamsters[1].stop()
        hamsters[1].wheels(45, 45)
        wait(100)
        hamsters[1].turn_right(1)
        break

trace(hamsters[1])

hamsters[1].buzzer(1500)
wait(50)
hamsters[1].buzzer(0)

hamsters[1].wheels(-100, -100)
wait(50)