import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QTableWidget, QPushButton
from bowlingScore import BowlingGame
from bowlingScore import Throws
from PyQt5.QtCore import pyqtSlot


# Main Window
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Bowling - Score'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.throwButton()

        self._game = BowlingGame()
        self._throws = Throws()

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)


        # Show window
        self.show()

    def throwButton(self):

        self.button = QPushButton("throw the ball!", self)
        self.button.move(100, 100)
        self.button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print('button click')

    # Create table
    def createTable(self):
        self.tableWidget = QTableWidget()
        # Row count
        self.tableWidget.setRowCount(3)

        # Column count
        self.tableWidget.setColumnCount(10)

        labels = ["frame_1", "frame_2", "frame_3", "frame_4", "frame_5", "frame_6", "frame_7", "frame_8", "frame_9",    "frame_10"]
        self.tableWidget.setHorizontalHeaderLabels(labels)
        names = ["result:", "Frame Score:", "Running Total"]
        self.tableWidget.setVerticalHeaderLabels(names)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())