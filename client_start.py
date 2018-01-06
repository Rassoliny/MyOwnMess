import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QThread, pyqtSlot
from client import User
from handlers import GuiReciever
import subprocess


def authentification():
    login = login_window.LoginPlainTextEdit.toPlainText()
    password = login_window.PasswordPlainTextEdit.toPlainText()
    print(login, password)
    subprocess.Popen('python3.6 ~/MyOwnMess/client_gui.py', shell=True)
    return (login, password)

# Создаем приложение
appl = QtWidgets.QApplication(sys.argv)
# Запускаем форму аутентификаци
login_window = uic.loadUi('login_page.ui')

login_window.pushButton.clicked.connect(authentification)
# Получаем учетные данные пользователя
#login = 
##client = User(name, addr, port)
## получаем список контактов с сервера, которые лежат у нас - не надежные
#client.connect()
#listener = GuiReciever(client.sock, client.request_queue)

login_window.show()
# точка запуска приложения
sys.exit(appl.exec_())
#app.exec_()



