from PySide6.QtWidgets import QDialog
from view.dialog_ajustar_periodo import UiDialog

class DialogAjustarPeriodo(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_ajustar_periodo_grafica.clicked.connect(self.ajustar_periodo)
		self.ui.pushButton_cancelar_ajustar_periodo_grafica.clicked.connect(self.cancelar_ajustar_periodo)

	def ajustar_periodo(self):
		print("Boton ajustar periodo presionado")
		self.accept()

	def cancelar_ajustar_periodo(self):
		print("Boton cancelar presionado")
		self.reject()