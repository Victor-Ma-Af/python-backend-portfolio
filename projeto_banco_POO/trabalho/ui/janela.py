
from senha.gerador import geraSenha
from senha.forca import verificaForca, formata_resultado
from senha.constantes import total_senhas
import sys

def build_gui():
    try:
        from PySide6.QtCore import Qt
        from PySide6.QtWidgets import (
            QApplication, QLabel, QLineEdit, QPushButton,
            QVBoxLayout, QWidget,
        )
    except ImportError:
        print("PySide6 não está instalado. Instale com: pip install PySide6")
        return False


    class PasswordGeneratorWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Gerador de Senhas")
            self.setMinimumSize(700, 260)
            self._build_ui()

        def _build_ui(self):
            title = QLabel("Gerador de Senhas e Verificador de Força")
            title.setAlignment(Qt.AlignCenter)
            title.setStyleSheet("font-weight: bold; font-size: 16px;")

            self.stats_label = QLabel(f"Quantidade total de senhas possíveis: {total_senhas:,}")
            self.stats_label.setWordWrap(True)

            self.generated_password = QLineEdit()
            self.generated_password.setReadOnly(True)
            self.generated_password.setPlaceholderText("Clique em Gerar Senha")

            self.strength_label = QLabel("Força da senha gerada: -")

            self.custom_password = QLineEdit()
            self.custom_password.setPlaceholderText("Digite uma senha para verificar")

            self.custom_strength_label = QLabel("Força da senha digitada: -")

            generate_button = QPushButton("Gerar Senha")
            generate_button.clicked.connect(self.on_generate_password)

            check_button = QPushButton("Verificar Força")
            check_button.clicked.connect(self.on_check_custom_password)

            generated_layout = QVBoxLayout()
            generated_layout.addWidget(QLabel("Senha gerada:"))
            generated_layout.addWidget(self.generated_password)
            generated_layout.addWidget(self.strength_label)
            generated_layout.addWidget(generate_button)

            custom_layout = QVBoxLayout()
            custom_layout.addWidget(QLabel("Senha personalizada:"))
            custom_layout.addWidget(self.custom_password)
            custom_layout.addWidget(check_button)
            custom_layout.addWidget(self.custom_strength_label)

            main_layout = QVBoxLayout()
            main_layout.addWidget(title)
            main_layout.addWidget(self.stats_label)
            main_layout.addLayout(generated_layout)
            main_layout.addSpacing(12)
            main_layout.addLayout(custom_layout)
            self.setLayout(main_layout)

        def on_generate_password(self):
            senha = geraSenha()
            self.generated_password.setText(senha)
            self.strength_label.setText(f"Força da senha gerada: {formata_resultado(verificaForca(senha))}")

        def on_check_custom_password(self):
            senha = self.custom_password.text().strip()
            if not senha:
                self.custom_strength_label.setText("Força da senha digitada: informe uma senha")
                return
            self.custom_strength_label.setText(
                f"Força da senha digitada: {formata_resultado(verificaForca(senha))}"
            )

    app = QApplication(sys.argv)
    window = PasswordGeneratorWindow()
    window.show()
    app.exec()
    return True
