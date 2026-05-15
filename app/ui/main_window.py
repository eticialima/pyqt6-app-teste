"""
Janela principal da aplicação - Visão (View)
"""
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QSpinBox,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from app.logic.counter import Counter


class MainWindow(QMainWindow):
    """Janela principal da aplicação"""

    def __init__(self):
        """Inicializa a janela principal"""
        super().__init__()

        # Configurar o contador (Model)
        self.counter = Counter()

        # Configurar a janela
        self.setWindowTitle("Aplicação PyQt6 - Contador")
        self.setGeometry(100, 100, 400, 300)

        # Criar widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Criar layout principal (vertical)
        main_layout = QVBoxLayout()

        # Título
        title = QLabel("Contador")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Display do valor atual
        self.display_label = QLabel(str(self.counter.get_value()))
        display_font = QFont()
        display_font.setPointSize(40)
        display_font.setBold(True)
        self.display_label.setFont(display_font)
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.display_label)

        # Layout dos botões (horizontal)
        buttons_layout = QHBoxLayout()

        # Botão decrementar
        btn_decrement = QPushButton("➖ -1")
        btn_decrement.setMinimumHeight(50)
        btn_decrement.clicked.connect(self.on_decrement)
        buttons_layout.addWidget(btn_decrement)

        # Botão reset
        btn_reset = QPushButton("🔄 Reset")
        btn_reset.setMinimumHeight(50)
        btn_reset.clicked.connect(self.on_reset)
        buttons_layout.addWidget(btn_reset)

        # Botão incrementar
        btn_increment = QPushButton("➕ +1")
        btn_increment.setMinimumHeight(50)
        btn_increment.clicked.connect(self.on_increment)
        buttons_layout.addWidget(btn_increment)

        main_layout.addLayout(buttons_layout)

        # Label para histórico
        history_label = QLabel("Histórico:")
        main_layout.addWidget(history_label)

        # Display do histórico
        self.history_label = QLabel(self.format_history())
        self.history_label.setWordWrap(True)
        main_layout.addWidget(self.history_label)

        # Definir layout no widget central
        central_widget.setLayout(main_layout)

    def on_increment(self):
        """Slot chamado quando botão + é clicado"""
        self.counter.increment()
        self.update_display()

    def on_decrement(self):
        """Slot chamado quando botão - é clicado"""
        self.counter.decrement()
        self.update_display()

    def on_reset(self):
        """Slot chamado quando botão reset é clicado"""
        self.counter.reset()
        self.update_display()

    def update_display(self):
        """Atualiza o display com o valor atual"""
        self.display_label.setText(str(self.counter.get_value()))
        self.history_label.setText(self.format_history())

    def format_history(self):
        """Formata o histórico para exibição"""
        history = self.counter.get_history()
        history_str = " → ".join(str(x) for x in history)
        return f"Histórico: {history_str}"
