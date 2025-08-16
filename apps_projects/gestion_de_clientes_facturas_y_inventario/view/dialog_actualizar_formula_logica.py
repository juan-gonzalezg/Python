from PySide6.QtWidgets import QDialog
from view.dialog_actualizar_formula import UiDialog

class DialogActualizarFormula(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_agregar.clicked.connect(self.agregar_actualizacion)
		self.ui.pushButton_eliminar.clicked.connect(self.eliminar_actualizacion)
		self.ui.pushButton_guardar.clicked.connect(self.guardar_actualizacion)
		self.ui.pushButton_cancelar.clicked.connect(self.cancelar_actualizacion)

	def agregar_actualizacion(self):
		print("Bonton agregar presionado")

	def eliminar_actualizacion(self):
		print("Bonton eliminar presionado")

	def guardar_actualizacion(self):
		print("Bonton guardar presionado")
		self.accept()

	def cancelar_actualizacion(self):
		print("Bonton cancelar presionado")
		self.reject()