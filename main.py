from Robot import Robot

roboti = Robot()


def inputHandle(comand):
    splitComand = comand.split(" ")
    action = splitComand[0]
    args = splitComand[1:]

    movements = {
        "x": lambda: roboti.moveX(float(args[1])),
        "y": lambda: roboti.moveY(float(args[1])),
        "z": lambda: roboti.moveZ(float(args[1])),
        "r": lambda: roboti.moveR(float(args[1])),
    }

    comands = {
        "home": lambda: roboti.moveHome(),
        "ligar": lambda: roboti.actuatorOn(),
        "desligar": lambda: roboti.actuatorOff(),
        "mover": lambda: (
            movements[args[0]]()
            if args[0] in movements
            else print("Sentido invalido desconhecido.")
        ),
        "atual": lambda: roboti.current(),
        "setHome": lambda: roboti.setHome(),
    }

    # Executar o comando
    if action in comands:
        print(action)
        if action == "mover" and len(args) > 1:
            comands[action]()
            return True
        else:
            comands[action]()
    else:
        print("Comando desconhecido.")
        return False
