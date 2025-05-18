# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_inicial.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_telaAplicativo(object):
    def setupUi(self, telaAplicativo):
        if not telaAplicativo.objectName():
            telaAplicativo.setObjectName(u"telaAplicativo")
        telaAplicativo.resize(1125, 625)
        telaAplicativo.setAutoFillBackground(False)
        telaAplicativo.setStyleSheet(u"")
        self.actionImportar_Dados = QAction(telaAplicativo)
        self.actionImportar_Dados.setObjectName(u"actionImportar_Dados")
        self.actionExportar_Excel = QAction(telaAplicativo)
        self.actionExportar_Excel.setObjectName(u"actionExportar_Excel")
        self.actionExcluir_Operador = QAction(telaAplicativo)
        self.actionExcluir_Operador.setObjectName(u"actionExcluir_Operador")
        self.centralwidget = QWidget(telaAplicativo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.frameFundoVisualizar = QFrame(self.centralwidget)
        self.frameFundoVisualizar.setObjectName(u"frameFundoVisualizar")
        self.frameFundoVisualizar.setGeometry(QRect(0, 0, 1131, 591))
        self.frameFundoVisualizar.setStyleSheet(u"QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(85, 0, 255, 255));\n"
"}\n"
"QGroupBox {\n"
"background-color: rgb(238, 238, 238);\n"
"border-radius: 10px;\n"
"}\n"
"/*---*/\n"
"QLabel {\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2c3e50;\n"
"    color: white;\n"
"    border: 1px solid #1abc9c;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font: 11pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #34495e;\n"
"    border: 1px solid #16a085;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1abc9c;\n"
"    border: 1px solid #16a085;\n"
"}")
        self.frameFundoVisualizar.setFrameShape(QFrame.StyledPanel)
        self.frameFundoVisualizar.setFrameShadow(QFrame.Raised)
        self.tabelaBancoDados = QTableView(self.frameFundoVisualizar)
        self.tabelaBancoDados.setObjectName(u"tabelaBancoDados")
        self.tabelaBancoDados.setGeometry(QRect(10, 150, 1111, 421))
        self.tabelaBancoDados.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.grupoVisualizarDados = QGroupBox(self.frameFundoVisualizar)
        self.grupoVisualizarDados.setObjectName(u"grupoVisualizarDados")
        self.grupoVisualizarDados.setGeometry(QRect(10, 10, 571, 131))
        self.grupoVisualizarDados.setStyleSheet(u"")
        self.comboVisualizarMes = QComboBox(self.grupoVisualizarDados)
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.addItem("")
        self.comboVisualizarMes.setObjectName(u"comboVisualizarMes")
        self.comboVisualizarMes.setGeometry(QRect(20, 50, 161, 31))
        self.comboVisualizarMes.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboVisualizarMes.setEditable(False)
        self.label = QLabel(self.grupoVisualizarDados)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 161, 21))
        self.label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.btn_VisualizarMes = QPushButton(self.grupoVisualizarDados)
        self.btn_VisualizarMes.setObjectName(u"btn_VisualizarMes")
        self.btn_VisualizarMes.setGeometry(QRect(430, 20, 131, 91))
        self.comboFiltro = QComboBox(self.grupoVisualizarDados)
        self.comboFiltro.addItem("")
        self.comboFiltro.setObjectName(u"comboFiltro")
        self.comboFiltro.setGeometry(QRect(200, 50, 211, 31))
        self.comboFiltro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboFiltro.setEditable(False)
        self.label_2 = QLabel(self.grupoVisualizarDados)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 20, 221, 21))
        self.label_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.telainicial = QLabel(self.frameFundoVisualizar)
        self.telainicial.setObjectName(u"telainicial")
        self.telainicial.setGeometry(QRect(30, 170, 1061, 381))
        self.telainicial.setStyleSheet(u"font: 50pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.telainicial.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frameFundoVisualizar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(590, 10, 511, 131))
        self.label_4.setStyleSheet(u"font: 24pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        telaAplicativo.setCentralWidget(self.centralwidget)
        self.barraMenu = QMenuBar(telaAplicativo)
        self.barraMenu.setObjectName(u"barraMenu")
        self.barraMenu.setGeometry(QRect(0, 0, 1125, 26))
        self.menuArquivo = QMenu(self.barraMenu)
        self.menuArquivo.setObjectName(u"menuArquivo")
        self.menuSobre = QMenu(self.barraMenu)
        self.menuSobre.setObjectName(u"menuSobre")
        telaAplicativo.setMenuBar(self.barraMenu)
        self.statusbar = QStatusBar(telaAplicativo)
        self.statusbar.setObjectName(u"statusbar")
        telaAplicativo.setStatusBar(self.statusbar)

        self.barraMenu.addAction(self.menuArquivo.menuAction())
        self.barraMenu.addAction(self.menuSobre.menuAction())
        self.menuArquivo.addAction(self.actionImportar_Dados)
        self.menuArquivo.addAction(self.actionExportar_Excel)
        self.menuArquivo.addAction(self.actionExcluir_Operador)

        self.retranslateUi(telaAplicativo)

        QMetaObject.connectSlotsByName(telaAplicativo)
    # setupUi

    def retranslateUi(self, telaAplicativo):
        telaAplicativo.setWindowTitle(QCoreApplication.translate("telaAplicativo", u"App Hora Extra - NQ", None))
        self.actionImportar_Dados.setText(QCoreApplication.translate("telaAplicativo", u"Importar Dados", None))
        self.actionExportar_Excel.setText(QCoreApplication.translate("telaAplicativo", u"Exportar Excel", None))
        self.actionExcluir_Operador.setText(QCoreApplication.translate("telaAplicativo", u"Excluir Operador", None))
        self.grupoVisualizarDados.setTitle("")
        self.comboVisualizarMes.setItemText(0, QCoreApplication.translate("telaAplicativo", u"Janeiro", None))
        self.comboVisualizarMes.setItemText(1, QCoreApplication.translate("telaAplicativo", u"Fevereiro", None))
        self.comboVisualizarMes.setItemText(2, QCoreApplication.translate("telaAplicativo", u"Mar\u00e7o", None))
        self.comboVisualizarMes.setItemText(3, QCoreApplication.translate("telaAplicativo", u"Abril", None))
        self.comboVisualizarMes.setItemText(4, QCoreApplication.translate("telaAplicativo", u"Maio", None))
        self.comboVisualizarMes.setItemText(5, QCoreApplication.translate("telaAplicativo", u"Junho", None))
        self.comboVisualizarMes.setItemText(6, QCoreApplication.translate("telaAplicativo", u"Julho", None))
        self.comboVisualizarMes.setItemText(7, QCoreApplication.translate("telaAplicativo", u"Agosto", None))
        self.comboVisualizarMes.setItemText(8, QCoreApplication.translate("telaAplicativo", u"Setembro", None))
        self.comboVisualizarMes.setItemText(9, QCoreApplication.translate("telaAplicativo", u"Outubro", None))
        self.comboVisualizarMes.setItemText(10, QCoreApplication.translate("telaAplicativo", u"Novembro", None))
        self.comboVisualizarMes.setItemText(11, QCoreApplication.translate("telaAplicativo", u"Dezembro", None))

        self.comboVisualizarMes.setCurrentText(QCoreApplication.translate("telaAplicativo", u"Janeiro", None))
        self.label.setText(QCoreApplication.translate("telaAplicativo", u"Selecione o m\u00eas :", None))
        self.btn_VisualizarMes.setText(QCoreApplication.translate("telaAplicativo", u"Carregar", None))
        self.comboFiltro.setItemText(0, QCoreApplication.translate("telaAplicativo", u"Todos", None))

        self.comboFiltro.setCurrentText(QCoreApplication.translate("telaAplicativo", u"Todos", None))
        self.label_2.setText(QCoreApplication.translate("telaAplicativo", u"Selecione o Supervisor :", None))
        self.telainicial.setText(QCoreApplication.translate("telaAplicativo", u"Nova Quest - Equipe Reneg", None))
        self.label_4.setText(QCoreApplication.translate("telaAplicativo", u"NovaQuest - Equipe Reneg", None))
        self.menuArquivo.setTitle(QCoreApplication.translate("telaAplicativo", u"Arquivo", None))
        self.menuSobre.setTitle(QCoreApplication.translate("telaAplicativo", u"Sobre", None))
    # retranslateUi

