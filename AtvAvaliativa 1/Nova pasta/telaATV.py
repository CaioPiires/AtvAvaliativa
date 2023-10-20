from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from funcaoCadastrarDados import cadastrar
from funcaoConverterData import converterData

class telaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        carregador = QUiLoader()
        self.tela = carregador.load("telaATV.ui")
        self.componentes()

    def componentes(self):
        self.caixaCategoria = self.tela.findChild(QtWidgets.QComboBox, "caixaCategoria")
        self.caixaDataMov = self.tela.findChild(QtWidgets.QDateEdit, "caixaDataMov")
        self.caixaValor = self.tela.findChild(QtWidgets.QLineEdit, "caixaValor")
        self.caixaEntSaid = self.tela.findChild(QtWidgets.QComboBox, "caixaEntSaid")       
        self.caixaDesc = self.tela.findChild(QtWidgets.QTextEdit, "caixaDesc")
        self.caixaCadastrar = self.tela.findChild(QtWidgets.QPushButton, "caixaCadastrar")
        self.caixaCadastrar.clicked.connect(self.cadastrarDados)

    def cadastrarDados(self):           
        cat = self.caixaCategoria.currentText()
        dtMov = self.caixaDataMov.text()
        val = self.caixaValor.text()
        entSaid = self.caixaEntSaid.currentText()        
        desc = self.caixaDesc.toPlainText()
        cadastrar(desc, val, cat, converterData(dtMov), entSaid)



if __name__ == "__main__":    
    app = QtWidgets.QApplication([])
    interface = telaPrincipal()
    interface.tela.show()
    app.exec()