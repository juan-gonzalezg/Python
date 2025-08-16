from PySide6.QtWidgets import QDialog
from view.dialog_agregar_cliente import UiDialog

class DialogAgregarCliente(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_agregar_cliente.clicked.connect(self.agregar_cliente)
		self.ui.pushButton_cancelar_agregar_cliente.clicked.connect(self.cancelar_agregar_cliente)

	def agregar_cliente(self):
		print("Boton agregar cliente presionado")
		self.accept()

	def cancelar_agregar_cliente(self):
		print("Bonton cancelar presionado")
		self.reject()