from PySide6.QtWidgets import QDialog
from view.dialog_eliminar_generico import UiDialog

class DialogEliminar(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_eliminar.clicked.connect(self.eliminar_generico)
		self.ui.pushButton_cancelar_eliminar.clicked.connect(self.cancelar_eliminar_generico)

	def eliminar_generico(self):
		print("Boton eliminar generico presionado")
		self.accept()

	def cancelar_eliminar_generico(self):
		print("Boton cancelar presionado")
		self.reject()