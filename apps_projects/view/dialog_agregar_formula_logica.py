from PySide6.QtWidgets import QDialog
from view.dialog_agregar_formula import UiDialog

class DialogAgregarFormula(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_agregar_ingrediente_agregar_formula.clicked.connect(self.agregar_ingrediente)
		self.ui.pushButton_eliminar_ingrediente_agregar_formula.clicked.connect(self.eliminar_ingrediente)
		self.ui.pushButton_agregar_formula.clicked.connect(self.agregar_formula)
		self.ui.pushButton_cancelar_agregar_formula.clicked.connect(self.cancelar_agregar_formula)

	def agregar_ingrediente(self):
		print("Boton agregar ingrediente presionado")

	def eliminar_ingrediente(self):
		print("Boton eliminar ingrediente presionado")

	def agregar_formula(self):
		print("Boton agregar formula presionado")
		self.accept()

	def cancelar_agregar_formula(self):
		print("Boton cancelar presionado")
		self.reject()