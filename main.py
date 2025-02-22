import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.load_data()

    def load_data(self):
        try:
            conn = sqlite3.connect('coffee.sqlite')
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM coffee")
            data = cursor.fetchall()

            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(7)

            headers = [
                'ID', 'Название', 'Степень обжарки',
                'Тип', 'Описание вкуса', 'Цена', 'Объем упаковки'
            ]
            self.tableWidget.setHorizontalHeaderLabels(headers)

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget.setItem(row_idx, col_idx, item)

            conn.close()

        except sqlite3.Error as e:
            QMessageBox.critical(
                self, 'Ошибка',
                f'Ошибка при работе с базой данных:\n{e}'
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
