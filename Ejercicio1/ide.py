from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

app = QApplication([])

ventana = QWidget()

ventana.setWindowTitle("PunctumD - Mi Primera App")

ventana.resize(500, 300)

layout = QVBoxLayout()

titulo = QLabel("Bienvenido a PunctumD")

boton = QPushButton("Conectar Mikrotik")

layout.addWidget(titulo)

layout.addWidget(boton)

ventana.setLayout(layout)

ventana.show()

app.exec()