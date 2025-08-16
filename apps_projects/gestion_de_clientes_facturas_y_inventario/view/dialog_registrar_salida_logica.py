from PySide6.QtWidgets import QDialog
from view.dialog_registrar_salida import UiDialog

class DialogRegistrarSalida(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_registrar_salida_inventario.clicked.connect(self.registrar_salida)
		self.ui.pushButton_cancelar_registrar_salida_inventario.clicked.connect(self.cancelar_registrar_salida)

	def registrar_salida(self):
		print("Boton registrar salida presionado")
		self.accept()

	def cancelar_registrar_salida(self):
		print("Boton cancelar presionado")
		self.reject()