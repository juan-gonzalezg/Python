from PySide6.QtWidgets import QDialog
from view.dialog_editar_cliente import UiDialog

class DialogEditarCliente(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_editar_cliente.clicked.connect(self.editar_cliente)
		self.ui.pushButton_cancelar_editar_cliente.clicked.connect(self.cancelar_editar_cliente)

	def editar_cliente(self):
		print("Boton editar cliente presionado")
		self.accept()

	def cancelar_editar_cliente(self):
		print("Bonton cancelar presionado")
		self.reject()