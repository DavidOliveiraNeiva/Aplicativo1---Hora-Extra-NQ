#interface_ui.py
from PySide2.QtWidgets import (
    QSizePolicy, QDialog, 
    QMessageBox, QWidget, 
    QAction, QFrame, 
    QGroupBox, QLabel, 
    QComboBox, QPushButton, 
    QMenu, QMenuBar, 
    QStatusBar, QTableView,
    QPlainTextEdit, QProgressBar,
    QLineEdit, 
    )
from PySide2.QtCore import (
    QRect, QSize,
    QTimer, QMetaObject,
    QCoreApplication, Qt
    )

from services import (
    inserir_registro, exportar_tabela_para_xlsx, 
    obter_ids_por_mes, obter_dados_por_id,
    excluir_Registro
    )

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# 
class Ui_telaAplicativo(object):
    def setupUi(self, telaAplicativo):
        if not telaAplicativo.objectName():
            telaAplicativo.setObjectName(u"telaAplicativo")
        telaAplicativo.resize(1125, 625)
        telaAplicativo.setAutoFillBackground(False)
        telaAplicativo.setStyleSheet(u"")
        
        # Ações do menu comboselecionarmes
        self.actionImportar_Dados = QAction(telaAplicativo)
        self.actionImportar_Dados.setObjectName(u"actionImportar_Dados")
        self.actionExportar_Excel = QAction(telaAplicativo)
        self.actionExportar_Excel.setObjectName(u"actionExportar_Excel")
        self.actionExcluir_Operador = QAction(telaAplicativo)
        self.actionExcluir_Operador.setObjectName(u"actionExcluir_Operador")

        # Configurações do widget principal
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

        # Menu 
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
        self.label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n""\n""")

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
        self.label_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n""\n""")
        self.label_3 = QLabel(self.frameFundoVisualizar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 170, 1061, 381))
        self.label_3.setStyleSheet(u"font: 50pt \"MS Shell Dlg 2\";\n""\n""")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frameFundoVisualizar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(590, 10, 511, 131))
        self.label_4.setStyleSheet(u"font: 24pt \"MS Shell Dlg 2\";\n""\n""")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.hide()
        telaAplicativo.setCentralWidget(self.centralwidget)

        # Menu
        self.barraMenu = QMenuBar(telaAplicativo)
        self.barraMenu.setObjectName(u"barraMenu")
        self.barraMenu.setGeometry(QRect(0, 0, 1125, 26))

        self.menuArquivo = QMenu(self.barraMenu)
        self.menuArquivo.setObjectName(u"menuArquivo")
        self.menuSobre = QMenu(self.barraMenu)
        self.actionSobreApp = QAction("Sobre o Aplicativo", telaAplicativo)
        self.menuSobre.addAction(self.actionSobreApp)

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
        self.actionSobreApp.triggered.connect(self.mostrar_mensagem_sobre)
        
        # Conectar as ações para abrir a tela branca
        self.actionImportar_Dados.triggered.connect(self.abrir_tela_importar)
        self.actionExportar_Excel.triggered.connect(self.abrir_tela_exportar)
        self.actionExcluir_Operador.triggered.connect(self.abrir_tela_excluir)

    # SetupUi
    def mostrar_mensagem_sobre(self):
        QMessageBox.information(None, "Sobre", "Aplicativo para controle de horas extras - NQ\nVersão 1.0\nCriado por David Oliveira Neiva")
    
    def abrir_tela_importar(self):
        
        telaImportar = QDialog()
        telaImportar.setWindowTitle("Tela Importar")
        telaImportar.resize(356, 624)
        telaImportar.setMinimumSize(QSize(356, 624))
        telaImportar.setMaximumSize(QSize(356, 624))
        
        frameFundoImportar = QFrame(telaImportar)
        frameFundoImportar.setGeometry(QRect(0, 0, 361, 631))
        frameFundoImportar.setStyleSheet("""
            QFrame {
                background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:0, y2:1,
                stop:0 rgba(0, 170, 0, 255), stop:1 rgba(0, 255, 0, 255));
            }
            QGroupBox {
                background-color: rgb(238, 238, 238);
                border-radius: 10px;
            }
            QLabel {
                background-color: rgb(238, 238, 238);
            }
            QPushButton {
                background-color: #2c3e50;
                color: white;
                border: 1px solid #1abc9c;
                border-radius: 8px;
                padding: 8px 16px;
                font: 11pt "Segoe UI";
            }
            QPushButton:hover {
                background-color: #34495e;
                border: 1px solid #16a085;
            }
            QPushButton:pressed {
                background-color: #1abc9c;
                border: 1px solid #16a085;
            }
        """)

        grupoImportar = QGroupBox(frameFundoImportar)
        grupoImportar.setGeometry(QRect(10, 20, 331, 131))

        comboEscolherMes = QComboBox(grupoImportar)
        comboEscolherMes.setGeometry(QRect(20, 50, 161, 31))
        comboEscolherMes.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        comboEscolherMes.setStyleSheet("background-color: rgb(255, 255, 255);")
        comboEscolherMes.addItems(meses)
        comboEscolherMes.setCurrentText("Janeiro")

        label = QLabel("Selecione o mês :", grupoImportar)
        label.setGeometry(QRect(20, 20, 161, 21))
        label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")

        btn_Salvar = QPushButton("Salvar Lista", grupoImportar)
        btn_Salvar.setGeometry(QRect(190, 20, 131, 91))

        plainTextEdit = QPlainTextEdit(frameFundoImportar)
        plainTextEdit.setGeometry(QRect(10, 160, 331, 451))
        plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        plainTextEdit.setPlainText("Operador, Supervisor")
        
        def salvar_lista():
            texto = plainTextEdit.toPlainText()
            mes = comboEscolherMes.currentText()

            inserir_registro(mes, texto, parent_widget=self)
            plainTextEdit.setPlainText("Operador, Supervisor")

        btn_Salvar.clicked.connect(salvar_lista)

        telaImportar.exec_()


    def abrir_tela_exportar(self):
        telaExportar = QDialog()
        telaExportar.setWindowTitle("Tela exportar")
        telaExportar.resize(350, 250)
        telaExportar.setMinimumSize(QSize(350, 251))
        telaExportar.setMaximumSize(QSize(350, 251))

        frameExportar = QFrame(telaExportar)
        frameExportar.setObjectName("frameExportar")
        frameExportar.setGeometry(QRect(0, 0, 351, 251))
        frameExportar.setStyleSheet("background-color: rgb(238, 238, 238);")
        frameExportar.setFrameShape(QFrame.StyledPanel)
        frameExportar.setFrameShadow(QFrame.Raised)

        progressBar = QProgressBar(frameExportar)
        progressBar.setObjectName("progressBar")
        progressBar.setGeometry(QRect(20, 200, 321, 23))
        progressBar.setValue(0)

        btn_Exportar = QPushButton(frameExportar)
        btn_Exportar.setObjectName("btn_Exportar")
        btn_Exportar.setGeometry(QRect(60, 10, 201, 91))
        btn_Exportar.setStyleSheet("""
            QPushButton {
                background-color: #2c3e50;
                color: white;
                border: 1px solid #1abc9c;
                border-radius: 8px;
                padding: 8px 16px;
                font: 11pt "Segoe UI";
            }
            QPushButton:hover {
                background-color: #34495e;
                border: 1px solid #16a085;
            }
            QPushButton:pressed {
                background-color: #1abc9c;
                border: 1px solid #16a085;
            }
        """)
        btn_Exportar.setText("Exportar Para Excel")

        label_2 = QLabel(frameExportar)
        label_2.setObjectName("label_2")
        label_2.setGeometry(QRect(80, 120, 161, 21))
        label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        label_2.setText("Selecione o mês :")

        comboSelecionarMes = QComboBox(frameExportar)
        comboSelecionarMes.setObjectName("comboSelecionarMes")
        comboSelecionarMes.setGeometry(QRect(80, 150, 161, 31))
        comboSelecionarMes.setStyleSheet("background-color: rgb(255, 255, 255);")
        comboSelecionarMes.setEditable(False)

        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        comboSelecionarMes.addItems(meses)
        comboSelecionarMes.setCurrentText("Janeiro")

        def exportar_para_excel():
            mes = comboSelecionarMes.currentText()

            # Simula progresso
            progressBar.setValue(10)

            def atualizar_progresso(valor):
                progressBar.setValue(valor)

            def finalizar_exportacao():
                exportar_tabela_para_xlsx(mes, telaExportar)
                progressBar.setValue(100)

            QTimer.singleShot(300, lambda: atualizar_progresso(40))
            QTimer.singleShot(600, lambda: atualizar_progresso(70))
            QTimer.singleShot(900, finalizar_exportacao)

        btn_Exportar.clicked.connect(exportar_para_excel)

        telaExportar.exec_()
       

    def abrir_tela_excluir(self):
        telaExcluir = QDialog()
        telaExcluir.setWindowTitle("Tela Excluir")
        telaExcluir.resize(356, 348)
        telaExcluir.setMinimumSize(QSize(356, 348))
        telaExcluir.setMaximumSize(QSize(356, 348))

        frameFundoExcluir = QFrame(telaExcluir)
        frameFundoExcluir.setGeometry(QRect(0, 0, 361, 361))
        frameFundoExcluir.setStyleSheet("""
            QFrame {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,
                                                stop:0 rgba(170, 0, 0, 255),
                                                stop:1 rgba(255, 0, 0, 255));
            }
            QGroupBox {
                background-color: rgb(238, 238, 238);
                border-radius: 10px;
            }
            QLabel {
                background-color: rgb(238, 238, 238);
            }
            QPushButton {
                background-color: #2c3e50;
                color: white;
                border: 1px solid #1abc9c;
                border-radius: 8px;
                padding: 8px 16px;
                font: 11pt "Segoe UI";
            }
            QPushButton:hover {
                background-color: #34495e;
                border: 1px solid #16a085;
            }
            QPushButton:pressed {
                background-color: #1abc9c;
                border: 1px solid #16a085;
            }
        """)

        grupoExcluir = QGroupBox(frameFundoExcluir)
        grupoExcluir.setGeometry(QRect(10, 20, 331, 191))

        comboSelecionarMes = QComboBox(grupoExcluir)
        comboSelecionarMes.setGeometry(QRect(20, 50, 161, 31))
        comboSelecionarMes.setStyleSheet("background-color: rgb(255, 255, 255);")
        comboSelecionarMes.addItems(meses)

        label_2 = QLabel("Selecione o mês :", grupoExcluir)
        label_2.setGeometry(QRect(20, 20, 161, 21))
        label_2.setStyleSheet('font: 12pt "MS Shell Dlg 2";')

        btn_Excluir = QPushButton("Excluir", grupoExcluir)
        btn_Excluir.setGeometry(QRect(190, 20, 131, 161))

        comboSelecionarId = QComboBox(grupoExcluir)
        comboSelecionarId.setGeometry(QRect(20, 150, 161, 31))
        comboSelecionarId.setStyleSheet("background-color: rgb(255, 255, 255);")


        label_3 = QLabel("Selecione o ID :", grupoExcluir)
        label_3.setGeometry(QRect(20, 110, 161, 21))
        label_3.setStyleSheet('font: 12pt "MS Shell Dlg 2";')

        grupoInformacaoExcluir = QGroupBox(frameFundoExcluir)
        grupoInformacaoExcluir.setGeometry(QRect(10, 220, 331, 121))

        label_4 = QLabel("Informações", grupoInformacaoExcluir)
        label_4.setGeometry(QRect(10, 10, 161, 21))
        label_4.setStyleSheet('font: 12pt "MS Shell Dlg 2";')

        label_5 = QLabel("Operador:", grupoInformacaoExcluir)
        label_5.setGeometry(QRect(30, 50, 71, 21))
        label_5.setStyleSheet('font: 8pt "MS Shell Dlg 2";')

        label_6 = QLabel("Supervisor:", grupoInformacaoExcluir)
        label_6.setGeometry(QRect(30, 80, 71, 21))
        label_6.setStyleSheet('font: 8pt "MS Shell Dlg 2";')
        
        # Declare 'lineEdit' and 'lineEdit_2' here, or use self if in a class
        lineEdit = QLineEdit(grupoInformacaoExcluir)
        lineEdit.setGeometry(QRect(100, 50, 221, 22))
        lineEdit.setEnabled(False)
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        lineEdit_2 = QLineEdit(grupoInformacaoExcluir)
        lineEdit_2.setGeometry(QRect(100, 80, 221, 22))
        lineEdit_2.setEnabled(False)
        lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")

        def atualizar_ids():
            # Obter o mês selecionado
            mes_atual = comboSelecionarMes.currentText()

            # Obter os IDs relacionados ao mês
            ids = obter_ids_por_mes(mes_atual)

            # Limpar a lista de IDs
            comboSelecionarId.clear()

            # Adicionar os IDs ao combobox
            comboSelecionarId.addItems(ids)

            # Se houver IDs, seleciona o primeiro e atualiza as informações
            if ids:
                comboSelecionarId.setCurrentIndex(0)
                atualizar_informacoes()

        def atualizar_informacoes():
            # Obter o mês e o ID selecionados
            mes = comboSelecionarMes.currentText()
            id_selecionado = comboSelecionarId.currentText()
            # Obter os dados usando a função obter_dados_por_id
            dados = obter_dados_por_id(mes, id_selecionado)
            operador = dados.get('nome', 'N/A')  # Definir valor padrão 'N/A' caso a chave não exista
            supervisor = dados.get('supervisor', 'N/A')  # Mesma coisa para o supervisor
            lineEdit.setText(operador)
            lineEdit_2.setText(supervisor)


        # Chamando a função para carregar os IDs ao abrir a tela
        mes_inicial = comboSelecionarMes.currentText()
        ids = obter_ids_por_mes(mes_inicial)
        comboSelecionarId.clear()
        comboSelecionarId.addItems(ids)

        if ids:
            comboSelecionarId.setCurrentIndex(0)
            atualizar_informacoes()

        comboSelecionarId.currentTextChanged.connect(atualizar_informacoes)
        comboSelecionarMes.currentTextChanged.connect(atualizar_ids)


        def excluir_lista():
            mes = comboSelecionarMes.currentText()
            id_ = comboSelecionarId.currentText()

            if not id_:
                QMessageBox.warning(telaExcluir, "Erro", "Nenhum ID selecionado para excluir.")
                return

            resposta = QMessageBox.question(
                telaExcluir,
                "Confirmar Exclusão",
                f"Tem certeza que deseja excluir o ID {id_} do mês {mes}?",
                QMessageBox.Yes | QMessageBox.No
            )

            if resposta == QMessageBox.Yes:
                excluir_Registro(mes, id_)
                QMessageBox.information(telaExcluir, "Sucesso", "Registro excluído com sucesso.")
                

        btn_Excluir.clicked.connect(excluir_lista)

        telaExcluir.exec_()

    def retranslateUi(self, telaAplicativo):
        telaAplicativo.setWindowTitle(QCoreApplication.translate("telaAplicativo", u"App Hora Extra - NQ", None))
        self.actionImportar_Dados.setText(QCoreApplication.translate("telaAplicativo", u"Importar Dados", None))
        self.actionExportar_Excel.setText(QCoreApplication.translate("telaAplicativo", u"Exportar Excel", None))
        self.actionExcluir_Operador.setText(QCoreApplication.translate("telaAplicativo", u"Excluir Operador", None))
        self.grupoVisualizarDados.setTitle("")
        self.comboVisualizarMes.setItemText(0, QCoreApplication.translate("telaAplicativo", u"Janeiro", None))
        self.comboVisualizarMes.setItemText(1, QCoreApplication.translate("telaAplicativo", u"Fevereiro", None))
        self.comboVisualizarMes.setItemText(2, QCoreApplication.translate("telaAplicativo", u"Marco", None))
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
        self.label_3.setText(QCoreApplication.translate("telaAplicativo", u"Nova Quest - Equipe Reneg", None))
        self.label_4.setText(QCoreApplication.translate("telaAplicativo", u"NovaQuest - Equipe Reneg", None))
        self.menuArquivo.setTitle(QCoreApplication.translate("telaAplicativo", u"Arquivo", None))
        self.menuSobre.setTitle(QCoreApplication.translate("telaAplicativo", u"Sobre", None))