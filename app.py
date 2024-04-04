from flask import Flask, render_template, request, jsonify
from tinydb import TinyDB
from main import inputHandle
from portscanner import RobotWrapper

app = Flask(__name__)
db = TinyDB("db.json")

robot_wrapper = RobotWrapper()


@app.route("/")
def index():
    logs = db.all()
    robot_connected = (
        check_robot_connection()
    )  # Atualize dinamicamente o estado da conexão
    return render_template("index.html", logs=logs, robot_connected=robot_connected)


@app.route("/send-command", methods=["POST"])
def send_command():
    if check_robot_connection():
        command = request.form.get("command")
        if command:
            comand_send = inputHandle(command)
            if comand_send:
                db.insert({"command": command, "status": "sent"})
                return jsonify(success=True)
            else:
                return jsonify(success=False, message="Comando inválido.")
        else:
            return jsonify(
                success=False, message="O campo 'command' está faltando no formulário."
            )
    else:
        return jsonify(success=False, message="O robô está desconectado.")


@app.route("/connect-robot", methods=["GET"])
def connect_robot():
    robot_status = check_robot_connection()
    return jsonify(success=True, robot_connected=robot_status)


def check_robot_connection():
    # Chama is_connected na instância robot_wrapper
    return robot_wrapper.is_connected()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
