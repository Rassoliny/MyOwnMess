from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QThread, pyqtSlot
import subprocess
import sys
import my_own_messenger.login_page as login_page



def main():
    # Связываем кнопку и функцию аутентификации
    ui.pushButton.clicked.connect(authentification)
    login_window.show()
    # точка запуска приложения
    sys.exit(appl.exec_())
    #app.exec_()


def authentification():
    login = ui.LoginPlainTextEdit.toPlainText()
    password = ui.PasswordPlainTextEdit.toPlainText()
    print(login, password)
    subprocess.Popen('python3.6 -m my_own_client localhost 7777 {}'.format(login), shell=True)
    exit(0)
    return (login, password)



if __name__ == "__main__":
    # Создаем приложение
    appl = QtWidgets.QApplication(sys.argv)
    # Запускаем форму аутентификаци
    login_window = QtWidgets.QMainWindow()
    ui = login_page.Ui_MainWindow()
    ui.setupUi(login_window)
    main()