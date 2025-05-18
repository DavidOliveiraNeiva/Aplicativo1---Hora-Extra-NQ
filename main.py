#main.py
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from interface_ui import Ui_telaAplicativo
from services import carregar_tabela_banco_de_dados, criar_tabela, carregar_supervisores

#ui 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface_ui = Ui_telaAplicativo()
        self.interface_ui.setupUi(self)

        self.interface_ui.btn_VisualizarMes.clicked.connect(self.carregar_dados)
        self.interface_ui.comboFiltro.currentIndexChanged.connect(self.filtrar_por_supervisor)

    def filtrar_por_supervisor(self):

        nome_Tabela = self.interface_ui.comboVisualizarMes.currentText()
        supervisores = self.interface_ui.comboFiltro.currentText()
        carregar_tabela_banco_de_dados(nome_Tabela, supervisores, self.interface_ui.tabelaBancoDados)

    def carregar_dados(self):
        self.interface_ui.label_3.hide()
        self.interface_ui.label_4.show()

        self.interface_ui.comboFiltro.blockSignals(True)  # <- Bloqueia sinal
        self.interface_ui.comboFiltro.clear()
        nome_Tabela = self.interface_ui.comboVisualizarMes.currentText()
        self.interface_ui.comboFiltro.addItems(carregar_supervisores(nome_Tabela))
        self.interface_ui.comboFiltro.blockSignals(False)  # <- Libera sinal

        supervisores = self.interface_ui.comboFiltro.currentText()
        carregar_tabela_banco_de_dados(nome_Tabela, supervisores, self.interface_ui.tabelaBancoDados)


if __name__ == "__main__":
    criar_tabela()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
