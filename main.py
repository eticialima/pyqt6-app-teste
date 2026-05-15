"""
Ponto de entrada da aplicação PyQt6
"""
import sys
from PyQt6.QtWidgets import QApplication
from app.ui.main_window import MainWindow


def main():
    """Função principal - inicia a aplicação"""
    # Criar a aplicação
    app = QApplication(sys.argv)

    # Criar e exibir a janela principal
    window = MainWindow()
    window.show()

    # Executar o loop de eventos
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
