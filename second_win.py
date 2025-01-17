#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Студент
#
# Created:     21.10.2024
# Copyright:   (c) Студент 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QPushButton, QLineEdit)
from PyQt5.QtCore import Qt, QTimer, QTime
from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.fio = QLabel("Введите Ф.И.О.:")
        self.fioEdit = QLineEdit()
        self.year = QLabel("Полных лет:")
        self.yearEdit = QLineEdit()
        self.inst1 = QLabel(txt_inst1)
        self.but1 = QPushButton('Начать новый текст')
        self.itog = QLineEdit()
        self.inst2 = QLabel(txt_inst2)
        self.but2 = QPushButton('Начать делать приседания')
        self.inst3 = QLabel(txt_inst3)
        self.but3 = QPushButton('Начать финальный тест')
        self.fin1 = QLineEdit()
        self.fin2 = QLineEdit()
        self.but4 = QPushButton('Отправить результаты')


        self.l_line.addWidget(self.fio, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.fioEdit, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.year, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.yearEdit, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.inst1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.but1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.itog, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.inst2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.but2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.inst3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.but3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.fin1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.fin2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.but4, alignment = Qt.AlignCenter)

        self.r_line.addWidget(self.timer, alignment = Qt.AlignRight)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1500)

    def timer3Event(self):
        global time
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
           self.text_timer.setStyleSheet("color: rgb(0,0,0)")

    def results(self):
        self.index=(4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index<15 and self.index>=11:
                return txt_res2
            elif self.index<11 and self.index>=6:
                return txt_res3
            elif self.index<6 and self.index>=0.5:
                return txt_res4
            elif self.index<0.4:
                return txt_res5
        if self.exp.age >= 13 and self.exp.age <= 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index<16.4 and self.index>=12.5:
                return txt_res2
            elif self.index<12.4 and self.index>=7.5:
                return txt_res3
            elif self.index<7.4 and self.index>=2:
                return txt_res4
            elif self.index<1.9:
                return txt_res5
        if self.exp.age >= 11 and self.exp.age <= 12:
            if self.index >= 18:
                return txt_res1
            elif self.index<17.9 and self.index>=14:
                return txt_res2
            elif self.index<13.9 and self.index>=9:
                return txt_res3
            elif self.index<8.9 and self.index>=3.5:
                return txt_res4
            elif self.index<3.4:
                return txt_res5
        if self.exp.age >= 9 and self.exp.age <= 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index<19.4 and self.index>=15.5:
                return txt_res2
            elif self.index<15.4 and self.index>=10.5:
                return txt_res3
            elif self.index<10.4 and self.index>=5:
                return txt_res4
            elif self.index<4.9:
                return txt_res5
        if self.exp.age >= 7 and self.exp.age <= 8:
            if self.index >= 21:
                return txt_res1
            elif self.index<20.9 and self.index>=17:
                return txt_res2
            elif self.index<16.9 and self.index>=12:
                return txt_res3
            elif self.index<11.9 and self.index>=6.5:
                return txt_res4
            elif self.index<6.4:
                return txt_res5


    def connects(self):
        self.but4.clicked.connect(self.next_click)

        self.but1.clicked.connect(self.timer_test)
        self.but2.clicked.connect(self.timer_sits)
        self.but3.clicked.connect(self.timer_final)


    def next_click(self):
        self.hide()
        self.fw = FinalWin()


