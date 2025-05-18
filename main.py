#main.py
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from interface_ui import Ui_telaAplicativo
from services import carregar_tabelaBancoDados, criar_tabela, carregar_supervisores

#ui
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface_ui = Ui_telaAplicativo()
        self.interface_ui.setupUi(self)

        self.interface_ui.btn_VisualizarMes.clicked.connect(self.carregar_dados)
        self.interface_ui.comboFiltro.currentIndexChanged.connect(self.filtrar_por_supervisor)

    def filtrar_por_supervisor(self):
        supervisor = self.interface_ui.comboFiltro.currentText()
        nome_mes = self.interface_ui.comboVisualizarMes.currentText()

        conn = conectar()
        cursor = conn.cursor()

        if supervisor == "Todos":
            query = f"SELECT * FROM {nome_mes}"
            parametros = ()
        else:
            query = f"SELECT * FROM {nome_mes} WHERE supervisor = ?"
            parametros = (supervisor,)

        cursor.execute(query, parametros)
        registros = cursor.fetchall()
        colunas = [desc[0] for desc in cursor.description]

        cursor.close()
        conn.close()

        self.atualizar_tabela(registros, colunas)


    def carregar_dados(self):
        #nome_Supervisor = "david"
        self.interface_ui.label_3.hide()
        self.interface_ui.label_4.show()
        
        self.interface_ui.comboFiltro.clear()
        nome_Tabela = self.interface_ui.comboVisualizarMes.currentText()
        supervisores = carregar_supervisores(nome_Tabela)
        self.interface_ui.comboFiltro.addItems(supervisores)
        carregar_tabelaBancoDados(nome_Tabela, self.interface_ui.tabelaBancoDados)


if __name__ == "__main__":
    criar_tabela()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
