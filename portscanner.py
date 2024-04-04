import pydobot
from serial.tools import list_ports


class RobotWrapper:
    def __init__(self):
        self.port = self.scan_ports()
        self.robot = pydobot.Dobot(port=self.port)

    def scan_ports(self) -> str:
        ports = list_ports.comports()
        for port in ports:
            print(f"Trying port {port.device}")
            try:
                robot = pydobot.Dobot(port=port.device)
                robot.close()
                print(f"Found robot at {port.device}")
                return port.device
            except:
                print(f"No robot found at {port.device}")
        raise Exception("No robot found")

    def is_connected(self) -> bool:
        try:
            # Tenta obter a posição atual do robô como um teste de conexão.
            # Você pode substituir esta chamada por qualquer outra operação de leitura segura.
            pos = pydobot.Dobot(port=self.port).pose()
            print(f"Robot connected, current position: {pos}")
            return True
        except:
            print("Robot not connected or communication failed.")
            return False


robot = RobotWrapper()
