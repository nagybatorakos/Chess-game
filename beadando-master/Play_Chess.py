import sys
from PyQt5 import QtWidgets, QtGui
from settingwindow import Ui_MainWindow
from ChessWindow import Ui_Gameview
import time
from Base import *
from functools import partial
from PyQt5.QtWidgets import QWidget
#from ff import Widget
from PyQt5.QtGui import QColor
from selectwindow import Ui_Selection
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QMessageBox
import TimerUtil
import datetime
import threading
import ctypes
import copy

class Setting:
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.player_add_button.clicked.connect(self.addPlayer)
        self.h = 0
        self.time = "1"
        self.ui.timebox.currentTextChanged.connect(self.getTime)
        self.ui.playbutton.clicked.connect(self.openChessWindow)

        # self.pic={'00':'WR', '01':'WK', '02':'WB', '03':'WKing', '04':'WQ', '05':'WB' , '06':'WK' , '07':'WR' , '10':'WP' , '11':'WP' , '12':'WP' , '13':'WP' , '14': 'WP', '15': 'WP', '16':'WP' , '17':'WP' , '20':'', '21': '', '22': '', '23': '', '24': '', '25': '', '26': '', '27': '',
        # '30': '', '31': '', '32': '', '33': '', '34': '', '35': '', '36': '', '37': '', '40': '', '41': '', '42': '', '43': '', '44': '', '45': '', '46': '', '47': '', '50': '', '51': '', '52': '', '53':'', '54':'' , '55': '', '56': '', '57': '', '60': '', '61': '', '62': '', '63': '', '64': '', '65': '', '66': '', '67': '', '70': '', '71': '', '72': '', '73': '', '74': '', '75':'' , '76': '', '77': ''}
        self.allW = []
        self.allB = []


        self.MainWindow.show()




    def addPlayer(self):
        self.h+=1
        if self.h>2:
            self.h=1
        if self.h==1:
            name=self.ui.namebox.toPlainText()
            self.ui.player1.setText(name)
            self.ui.namebox.clear()
        if self.h==2:
            name=self.ui.namebox.toPlainText()
            self.ui.player2.setText(name)
            self.ui.namebox.clear()
        print("clicked")


    def getTime(self):
        self.time=self.ui.timebox.currentText()

    # <>[]{}
    def getFormattedTime(self, elapsed_time):
        x = (float(self.time)*60) - elapsed_time
        result = str(datetime.timedelta(seconds=x))[:-3]
        return result

    def openChessWindow(self):
        self.h = 0

        self.pic = {'WR': 'WR.png', 'WK': 'WK.png', 'WKing': 'WKing.png', 'WB': 'WB.png', 'WP': 'WP.png',
                    'WQ': 'WQ.png',
                    'BR': 'BR.png', 'BK': 'BK.png', 'BKing': 'BKing.png', 'BB': 'BB.png', 'BP': 'BP1.png',
                    'BQ': 'BQ.png'}

        self.zold = False
        self.prevLab = None
        self.prevLs = []
        self.prevN = ''
        self.colors = {}
        self.turn = 'W'
        self.outofPlay = []
        self.selected = 'P'
        self.matt = ''
        self.sakkmatt = ''
        self.mattLs = []
        self.inverse = {'W': 'B', 'B': 'W'}



        for i in range(8):
            for j in range(8):
                board[i][j] = ''

        board[0][0] = 'WR'
        board[0][1] = 'WK'
        board[0][2] = 'WB'
        board[0][3] = 'WKing'
        board[0][4] = 'WQ'
        board[0][5] = 'WB'
        board[0][6] = 'WK'
        board[0][7] = 'WR'

        board[1][0] = 'WP'
        board[1][1] = 'WP'
        board[1][2] = 'WP'
        board[1][3] = 'WP'
        board[1][4] = 'WP'
        board[1][5] = 'WP'
        board[1][6] = 'WP'
        board[1][7] = 'WP'

        board[6][0] = 'BP'
        board[6][1] = 'BP'
        board[6][2] = 'BP'
        board[6][3] = 'BP'
        board[6][4] = 'BP'
        board[6][5] = 'BP'
        board[6][6] = 'BP'
        board[6][7] = 'BP'

        board[7][0] = 'BR'
        board[7][1] = 'BK'
        board[7][2] = 'BB'
        board[7][3] = 'BKing'
        board[7][4] = 'BQ'
        board[7][5] = 'BB'
        board[7][6] = 'BK'
        board[7][7] = 'BR'




        self.newWindow=QtWidgets.QMainWindow()
        self.ui2=Ui_Gameview()
        self.ui2.setupUi(self.newWindow)
        # self.ui2.whiteTimer.setText(self.time+':00')
        self.ui2.player_white.setText(self.ui.player1.text())
        self.ui2.player_black.setText(self.ui.player2.text())
        # self.ui2.whiteTimer.setText(self.getFormattedTime(self.play_timer.all_elapsed_time(reset=False)['W']))
        # self.ui2.blackTimer.setText(self.time+':00')
        # self.ui2.blackTimer.setText(self.getFormattedTime(self.play_timer.all_elapsed_time(reset=False)['B']))

        self.poz={'00': self.ui2.label00,'01': self.ui2.label01, '02':self.ui2.label02, '03':self.ui2.label03, '04':self.ui2.label04, '05':self.ui2.label05, '06':self.ui2.label06, '07':self.ui2.label07,
                  '10':self.ui2.label10, '11':self.ui2.label11, '12':self.ui2.label12, '13':self.ui2.label13, '14':self.ui2.label14, '15':self.ui2.label15, '16':self.ui2.label16, '17':self.ui2.label17,
        '20':self.ui2.label20, '21':self.ui2.label21, '22':self.ui2.label22, '23':self.ui2.label23, '24':self.ui2.label24, '25':self.ui2.label25, '26':self.ui2.label26, '27':self.ui2.label27,
        '30':self.ui2.label30, '31':self.ui2.label31, '32':self.ui2.label32, '33':self.ui2.label33, '34':self.ui2.label34, '35':self.ui2.label35, '36':self.ui2.label36, '37':self.ui2.label37,
         '40':self.ui2.label40, '41':self.ui2.label41, '42':self.ui2.label42, '43':self.ui2.label43, '44':self.ui2.label44, '45':self.ui2.label45,'46':self.ui2.label46, '47':self.ui2.label47,
        '50':self.ui2.label50, '51':self.ui2.label51, '52':self.ui2.label52, '53':self.ui2.label53, '54':self.ui2.label54, '55':self.ui2.label55, '56':self.ui2.label56, '57':self.ui2.label57,
        '60':self.ui2.label60, '61':self.ui2.label61, '62':self.ui2.label62, '63':self.ui2.label63, '64':self.ui2.label64, '65':self.ui2.label65, '66':self.ui2.label66, '67':self.ui2.label67,
        '70':self.ui2.label70, '71':self.ui2.label71, '72':self.ui2.label72, '73':self.ui2.label73, '74':self.ui2.label74, '75':self.ui2.label75, '76':self.ui2.label76, '77':self.ui2.label77}

        #self.ui2.gameoverbutton.clicked.connect(self.openWinnerWindow)


###############################################################

        self.ui2.label00.clicked.connect(partial(self.showMoves,'00',self.ui2.label00))
        self.ui2.label01.clicked.connect(partial(self.showMoves,'01',self.ui2.label01))
        self.ui2.label02.clicked.connect(partial(self.showMoves,'02',self.ui2.label02))
        self.ui2.label03.clicked.connect(partial(self.showMoves,'03',self.ui2.label03))
        self.ui2.label04.clicked.connect(partial(self.showMoves,'04',self.ui2.label04))
        self.ui2.label05.clicked.connect(partial(self.showMoves,'05',self.ui2.label05))
        self.ui2.label06.clicked.connect(partial(self.showMoves,'06',self.ui2.label06))
        self.ui2.label07.clicked.connect(partial(self.showMoves,'07',self.ui2.label07))
        self.ui2.label10.clicked.connect(partial(self.showMoves,'10',self.ui2.label10))
        self.ui2.label11.clicked.connect(partial(self.showMoves,'11',self.ui2.label11))
        self.ui2.label12.clicked.connect(partial(self.showMoves,'12',self.ui2.label12))
        self.ui2.label13.clicked.connect(partial(self.showMoves,'13',self.ui2.label13))
        self.ui2.label14.clicked.connect(partial(self.showMoves,'14',self.ui2.label14))
        self.ui2.label15.clicked.connect(partial(self.showMoves,'15',self.ui2.label15))
        self.ui2.label16.clicked.connect(partial(self.showMoves,'16',self.ui2.label16))
        self.ui2.label17.clicked.connect(partial(self.showMoves,'17',self.ui2.label17))
        self.ui2.label20.clicked.connect(partial(self.showMoves,'20',self.ui2.label20))
        self.ui2.label21.clicked.connect(partial(self.showMoves,'21',self.ui2.label21))
        self.ui2.label22.clicked.connect(partial(self.showMoves,'22',self.ui2.label22))
        self.ui2.label23.clicked.connect(partial(self.showMoves,'23',self.ui2.label23))
        self.ui2.label24.clicked.connect(partial(self.showMoves,'24',self.ui2.label24))
        self.ui2.label25.clicked.connect(partial(self.showMoves,'25',self.ui2.label25))
        self.ui2.label26.clicked.connect(partial(self.showMoves,'26',self.ui2.label26))
        self.ui2.label27.clicked.connect(partial(self.showMoves,'27',self.ui2.label27))
        self.ui2.label30.clicked.connect(partial(self.showMoves,'30',self.ui2.label30))
        self.ui2.label31.clicked.connect(partial(self.showMoves,'31',self.ui2.label31))
        self.ui2.label32.clicked.connect(partial(self.showMoves,'32',self.ui2.label32))
        self.ui2.label33.clicked.connect(partial(self.showMoves,'33',self.ui2.label33))
        self.ui2.label34.clicked.connect(partial(self.showMoves,'34',self.ui2.label34))
        self.ui2.label35.clicked.connect(partial(self.showMoves,'35',self.ui2.label35))
        self.ui2.label36.clicked.connect(partial(self.showMoves,'36',self.ui2.label36))
        self.ui2.label37.clicked.connect(partial(self.showMoves,'37',self.ui2.label37))
        self.ui2.label40.clicked.connect(partial(self.showMoves,'40',self.ui2.label40))
        self.ui2.label41.clicked.connect(partial(self.showMoves,'41',self.ui2.label41))
        self.ui2.label42.clicked.connect(partial(self.showMoves,'42',self.ui2.label42))
        self.ui2.label43.clicked.connect(partial(self.showMoves,'43',self.ui2.label43))
        self.ui2.label44.clicked.connect(partial(self.showMoves,'44',self.ui2.label44))
        self.ui2.label45.clicked.connect(partial(self.showMoves,'45',self.ui2.label45))
        self.ui2.label46.clicked.connect(partial(self.showMoves,'46',self.ui2.label46))
        self.ui2.label47.clicked.connect(partial(self.showMoves,'47',self.ui2.label47))
        self.ui2.label50.clicked.connect(partial(self.showMoves,'50',self.ui2.label50))
        self.ui2.label51.clicked.connect(partial(self.showMoves,'51',self.ui2.label51))
        self.ui2.label52.clicked.connect(partial(self.showMoves,'52',self.ui2.label52))
        self.ui2.label53.clicked.connect(partial(self.showMoves,'53',self.ui2.label53))
        self.ui2.label54.clicked.connect(partial(self.showMoves,'54',self.ui2.label54))
        self.ui2.label55.clicked.connect(partial(self.showMoves,'55',self.ui2.label55))
        self.ui2.label56.clicked.connect(partial(self.showMoves,'56',self.ui2.label56))
        self.ui2.label57.clicked.connect(partial(self.showMoves,'57',self.ui2.label57))
        self.ui2.label60.clicked.connect(partial(self.showMoves,'60',self.ui2.label60))
        self.ui2.label61.clicked.connect(partial(self.showMoves,'61',self.ui2.label61))
        self.ui2.label62.clicked.connect(partial(self.showMoves,'62',self.ui2.label62))
        self.ui2.label63.clicked.connect(partial(self.showMoves,'63',self.ui2.label63))
        self.ui2.label64.clicked.connect(partial(self.showMoves,'64',self.ui2.label64))
        self.ui2.label65.clicked.connect(partial(self.showMoves,'65',self.ui2.label65))
        self.ui2.label66.clicked.connect(partial(self.showMoves,'66',self.ui2.label66))
        self.ui2.label67.clicked.connect(partial(self.showMoves,'67',self.ui2.label67))
        self.ui2.label70.clicked.connect(partial(self.showMoves,'70',self.ui2.label70))
        self.ui2.label71.clicked.connect(partial(self.showMoves,'71',self.ui2.label71))
        self.ui2.label72.clicked.connect(partial(self.showMoves,'72',self.ui2.label72))
        self.ui2.label73.clicked.connect(partial(self.showMoves,'73',self.ui2.label73))
        self.ui2.label74.clicked.connect(partial(self.showMoves,'74',self.ui2.label74))
        self.ui2.label75.clicked.connect(partial(self.showMoves,'75',self.ui2.label75))
        self.ui2.label76.clicked.connect(partial(self.showMoves,'76',self.ui2.label76))
        self.ui2.label77.clicked.connect(partial(self.showMoves,'77',self.ui2.label77))

        self.play_timer = TimerUtil.timer_()
        self.play_timer.switch_to('B')
        self.play_timer.switch_to(self.turn)
###############################################################



        self.newWindow.show()

        threading._start_new_thread(self.timer, ())


    # <>{}[]

    def timer(self):
        tmp = True
        while tmp:
            self.ui2.whiteTimer.setText(self.getFormattedTime(self.play_timer.all_elapsed_time(reset=False)['W']))
            self.ui2.blackTimer.setText(self.getFormattedTime(self.play_timer.all_elapsed_time(reset=False)['B']))

            if self.play_timer.all_elapsed_time(reset=False)['W'] >= float(self.time)*60:
                tmp = False
                self.ui2.whiteTimer.setText("00:00:00")
                resp = ctypes.windll.user32.MessageBoxW(0, self.ui.player2.text() + " has won!", "GAME OVER", 1)
                if resp:
                    self.newWindow.close()
                    # self.MainWindow.close()



            if self.play_timer.all_elapsed_time(reset=False)['B'] >= float(self.time) * 60:
                tmp = False
                self.ui2.blackTimer.setText("00:00:00")
                resp = ctypes.windll.user32.MessageBoxW(0, self.ui.player1.text() + " has won!", "GAME OVER", 1)
                if resp:
                    self.newWindow.close()
                    # self.MainWindow.close()


            time.sleep(0.1)





    def showMoves(self, n, label):
        x=int(n[0])
        y=int(n[1])
        ls= []
        ls0=self.canMove(x,y)
        k=King(self.inverse[self.turn]+'King')
        print(self.searchall())

        print("TESZT: ", self.play_timer.all_elapsed_time(reset=False))
        self.ui2.whiteTimer.setText(self.getFormattedTime(self.play_timer.all_elapsed_time(reset=False)['W']))
        self.ui2.blackTimer.setText(self.getFormattedTime(self.play_timer.all_elapsed_time(reset=False)['B']))


        if getname(x, y) != '' and len(ls0) > 0 and k.getPosition() in ls0:
            ls0.remove(k.getPosition())

        if self.matt != self.turn:
            ls = ls0

        if self.matt == self.turn and ls0 != [] and getname(x, y) != '':
            if getname(x, y)[1:] == 'King':
                if getname(x, y)[0] == 'W':
                    for i in ls0:
                        if i not in self.allB:
                            ls.append(i)

                elif getname(x, y)[0] == 'B':
                    for i in ls0:
                        if i not in self.allW:
                            ls.append(i)
            else:
                for i in ls0:
                    if i in self.mattLs:
                        ls.append(i)

        if self.zold == False:
            if getname(x, y) != '' and getname(x, y)[0] == self.turn:
                if ls != []:
                    self.zold = True
                    for i in range(len(ls)):
                        which = self.poz[ls[i]]
                        self.colors[ls[i]] = which.palette().button().color()
                        # self.colors.append(which.palette().button().color())
                        which.setStyleSheet(
                            'background-color:' + which.palette().button().color().name() + ';' + 'border: 7px inset green;')

                    self.prevLab = label
                    self.prevLs = ls
                    self.prevName = getname(x, y)
                    self.prevN = n

        elif self.zold and n in self.prevLs:

            if self.prevN != '':
                i = int(self.prevN[0])
                j = int(self.prevN[1])
                label.setPixmap(QtGui.QPixmap(self.pic[self.prevName]))
                self.prevLab.clear()

                if getname(x, y) != '' and getname(x, y)[1] != 'P':
                    self.outofPlay.append(getname(x, y))

                board[i][j] = ''
                board[x][y] = self.prevName
                print(self.searchall())
                print(self.searchChain(x, y))

                for i in range(len(self.prevLs)):
                    which = self.poz[self.prevLs[i]]
                    which.setStyleSheet('background-color:' + self.colors[self.prevLs[i]].name() + ';')

                if (x == 0 or x == 7) and self.prevName[1] == 'P':
                    print(self.openSelection(x, y, label))

                self.zold = False
                self.turn = self.inverse[self.turn]

                self.play_timer.switch_to(self.turn)


        elif self.zold and n not in self.prevLs:
            self.zold = False
            for i in range(len(self.prevLs)):
                which = self.poz[self.prevLs[i]]
                which.setStyleSheet('background-color:' + self.colors[self.prevLs[i]].name() + ';')


    def openSelection(self, x, y, label):
        self.anotherWindow = QtWidgets.QMainWindow()
        self.ui3 = Ui_Selection()
        self.ui3.setupUi(self.anotherWindow)
        # msg = QMessageBox()
        # msg.setWindowTitle("")
        # msg.setText("You can replace yor pawn with one of these pieces.")
        # msg.setIcon(QMessageBox.Information)
        # msg.setStandardButtons(QMessageBox.Ok)
        self.ui3.selectbutton.clicked.connect(partial(self.replace, x, y, label))
        self.ui3.selectbutton.clicked.connect(self.anotherWindow.close)

        has_item = False
        for i in self.outofPlay:
            item = QListWidgetItem()

            if i[0] != self.turn:
                continue
            if i[1] == 'Q':
                item.setText('Queen ♛')
                has_item = True
            if i[1] == 'R':
                item.setText('Rook ♜')
                has_item = True
            if i[1] == 'K':
                item.setText('Knight ♞')
                has_item = True
            if i[1] == 'B':
                item.setText('Bishop ♝')
                has_item = True
            self.ui3.listWidget.addItem(item)
            self.ui3.listWidget.setCurrentItem(item)

        if has_item:
            self.anotherWindow.show()



    def replace(self, x, y, label):
        curr = self.ui3.listWidget.currentItem()
        self.selected = self.inverse[self.turn] + curr.text()[0]
        label.setPixmap(QtGui.QPixmap(self.pic[self.selected]))
        board[x][y] = self.selected

        self.outofPlay.remove(self.selected)
        print("self.outofPlay: ", self.outofPlay)


    def searchChain(self, x, y):
        k = King(self.inverse[self.turn] + 'King')
        n = k.getPosition()
        i = int(n[0])
        j = int(n[1])
        ls = self.canMove(x, y)
        self.mattLs = []
        if n not in ls:
            self.matt = ''
        elif n in ls:
            msg = QMessageBox()
            msg.setWindowTitle("")

            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)

            self.matt = self.inverse[self.turn]
            ls.remove(k.getPosition())
            if x == i:
                if y > j:
                    for b in range(j, y):
                        if str(x) + str(b) in ls:
                            self.mattLs.append(str(x) + str(b))
                elif j > y:
                    for b in range(y, j, -1):
                        if str(x) + str(b) in ls:
                            self.mattLs.append(str(x) + str(b))
            elif y == j:
                if x > i:
                    for b in range(x, i, -1):
                        if str(b) + str(i) in ls:
                            self.mattLs.append(str(b) + str(j))
                if i > x:
                    for b in range(x, i):
                        if str(b) + str(i) in ls:
                            self.mattLs.append(str(b) + str(j))
            elif x > i:
                if y > j:
                    h = x - 1
                    for b in range(y - 1, j, -1):
                        if str(h) + str(b) in ls:
                            self.mattLs.append(str(h) + str(b))
                        h -= 1
                if j > y:
                    h = x - 1
                    for b in range(y + 1, j):
                        if str(h) + str(b) in ls:
                            self.mattLs.append(str(h) + str(b))
                        h -= 1
            elif i > x:
                if y > j:
                    h = x + 1
                    for b in range(y - 1, j, -1):
                        if str(h) + str(b) in ls:
                            self.mattLs.append(str(h) + str(b))
                        h += 1
                if j > y:
                    h = x + 1
                    for b in range(y + 1, j):
                        if str(h) + str(b) in ls:
                            self.mattLs.append(str(h) + str(b))
                        h += 1

            if k.getPosition() in self.mattLs:
                self.mattLs.remove(k.getPosition())
            if str(x) + str(y) not in self.mattLs:
                self.mattLs.append(str(x) + str(y))

            print(self.mattLs,self.searchall(),self.allB,self.allW)

            c = 0
            for u in self.mattLs:
                if self.matt == 'W':
                    for h in self.allW:
                        if u == h:
                            c += 1
                elif self.matt == 'B':
                    for h in self.allB:
                        if u == h:
                            c += 1
            if c == 0 and self.canMove(i, j) == []:
                self.sakkmatt = True

            if self.sakkmatt != True:
                msg.setText("Check!")

            else:
                if self.turn == 'W':
                    msg.setText('Checkmate! ' + self.ui.player1.text() + ' wins!')
                else:
                    msg.setText('Checkmate! ' + self.ui.player2.text() + ' wins!')
                self.newWindow.close()
            msg.exec()


    def searchall(self):
        self.allW = []
        self.allB = []
        wk=King('WKing')
        w=int(wk.getPosition()[0])
        k1=int(wk.getPosition()[1])

        bk=King('BKing')
        b=int(bk.getPosition()[0])
        k2=int(bk.getPosition()[1])

        for i in range(board_shape[0]):
            for j in range(board_shape[1]):
                if getname(i, j) != '' and getname(i, j)[0] == 'W' and getname(i,j)!='WKing':
                    for k in self.canMove(i, j):
                        if k not in self.allW:
                            self.allW.append(k)
                if getname(i, j) != '' and getname(i, j)[0] == 'B' and getname(i,j)!='BKing':
                    for k in self.canMove(i, j):
                        if k not in self.allB:
                            self.allB.append(k)
        # for i in self.canMove(w,k1):
        #     if i in self.allB:
        #         self.allW.remove(i)
        # for j in self.canMove(b,k2):
        #     if j in self.allW:
        #         self.allB.remove(j)


    def canMove(self,x, y):
        name = getname(x, y)
        if name != '':
            if name[1] == 'R':
                name = Rook(name)
                return name.canMove(x, y)
            elif name[1:] == 'King':
                piece = King(name)
                ls=[]
                if name[0]=='W':
                    for i in piece.canMove(x,y):
                        if i not in self.allB:
                            ls.append(i)
                elif name[0]=='B':
                    for i in piece.canMove(x,y):
                        if i not in self.allW:
                            ls.append(i)
                return ls
            elif name[1] == 'B':
                name = Bishop(name)
                return name.canMove(x, y)
            elif name[1] == 'Q':
                name = Queen(name)
                return name.canMove(x, y)
            elif name[1:] == 'K':
                name = Knight(name)
                return name.canMove(x, y)
            elif name[1] == 'P':
                name = Pawn(name)
                return name.canMove(x, y)

    # def mattAppend()


app = QtWidgets.QApplication(sys.argv)
cntrl = Setting()
sys.exit(app.exec_())
