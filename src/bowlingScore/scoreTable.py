
import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QPushButton, QMainWindow, QHBoxLayout, QApplication, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot
from .bowlingGame import BowlingGame
from .bowlingGame import Throws


class ScoreWindow(QMainWindow):

    def __init__(self, bowlingGame):
        QMainWindow.__init__(self)

        self.setWindowTitle('Testing ')

        central = QWidget(self)
        self.setCentralWidget(central)

        mainLayout = QHBoxLayout(central)
        # add a left "margin"
        mainLayout.addStretch(0)

        self.throwButton(mainLayout, bowlingGame)

        # add a "spacing" between the two vertical layouts
        mainLayout.addStretch(1)

        self.scoreTable(mainLayout)

        # add a margin to the right
        mainLayout.addStretch(1)

        self.setFixedSize(1000, 150)

    def throwButton(self, mainLayout, bowlingGame):

        buttonLayout = QVBoxLayout()
        mainLayout.addLayout(buttonLayout)

        # add a top "margin"
        buttonLayout.addStretch(1)

        button1 = QPushButton('Throw the ball!')
        buttonLayout.addWidget(button1, alignment=Qt.AlignHCenter)
        button1.clicked.connect(lambda: self.on_click(bowlingGame))

        # add a bottom "margin"
        buttonLayout.addStretch(1)

    @pyqtSlot()
    def on_click(self, bowlingGame):
        try:
            col, score, result = next(bowlingGame)
            if col > 9:
                sys.exit()
        except StopIteration:
            sys.exit()
        print("col ->", col, "score ->", score, "result ->", result)
        self.tableWidget.setItem(0, col, QTableWidgetItem(result))
        self.tableWidget.setItem(1, col, QTableWidgetItem(str(score)))

        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def scoreTable(self, mainLayout):
        tableLayout = QVBoxLayout()
        mainLayout.addLayout(tableLayout)
        self.tableWidget = QTableWidget(self.centralWidget())
        # add a top "margin" to the right layout
        tableLayout.addStretch(1)

        tableLayout.addWidget(self.tableWidget)
        self.tableWidget.setFixedSize(800, 100)

        self.createTable()

        tableLayout.addStretch(1)

    def createTable(self):

        # Row count
        self.tableWidget.setRowCount(2)

        # Column count
        self.tableWidget.setColumnCount(10)

        labels = ["frame_1", "frame_2", "frame_3", "frame_4", "frame_5", "frame_6", "frame_7", "frame_8", "frame_9", "frame_10"]
        self.tableWidget.setHorizontalHeaderLabels(labels)

        names = ["result:", "Total Score:"]
        self.tableWidget.setVerticalHeaderLabels(names)


class GAME:
    def __init__(self):
        self._game = BowlingGame()
        self._throws = Throws()

        self.run(self.bowlingGame())

    def run(self, bowlingGame):
        app = QApplication(sys.argv)
        ex = ScoreWindow(bowlingGame)
        ex.show()
        sys.exit(app.exec_())

    def bowlingGame(self):
        N, n = 20, 0
        cols = 0
        curr_score = ""
        cont = None
        flag = True
        while n < N:

            if (n % 2) == 0 and n != 0 and flag is True:
                cols += 1

            flag = True
            pins = self._throws.throw(1, 10)
            self._game.roll(pins, n)
            print("index {}  flag {} , cont {} stroke pins {}, throws {}".format(n, flag, cont, pins, self._game.getRolls()))
            if ((n % 2) != 0) and pins == 10:
                N -= 1
                result = "/"
                cont = False
            elif ((n % 2) == 0) and pins == 10:
                result = "X"
                cont = True
            else:
                result = str(pins)
                cont = False

            total = self._game.score()
            if cont is True:
                yield cols, total, str(result)
                cont = False
                flag = False
                cols += 1
                curr_score = ""
            else:
                if len(curr_score) == 0:
                    curr_score = str(result)
                elif len(curr_score) > 1:
                    curr_score = str(result)
                else:
                    curr_score += " " + str(result)

                yield cols, total, curr_score
            n += 1


if __name__ == '__main__':
    # app = QApplication(sys.argv)

    # ex = ScoreWindow()
    # ex.show()
    # sys.exit(app.exec_())

    game = GAME()
