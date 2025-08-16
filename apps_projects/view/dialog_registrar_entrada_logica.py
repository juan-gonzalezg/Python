from PySide6.QtWidgets import QDialog
from view.dialog_registrar_entrada import UiDialog

class DialogRegistrarEntrada(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_registrar_entrada_inventario.clicked.connect(self.registrar_entrada)
		self.ui.pushButton_cancelar_registrar_entrada_inventario.clicked.connect(self.cancelar_registrar_entrada)

	def registrar_entrada(self):
		print("Boton registrar entrada presionado")
		self.accept()

	def cancelar_registrar_entrada(self):
		print("Boton cancelar presionado")
		self.reject()