from PySide6.QtWidgets import QDialog
from view.dialog_tareas_pendientes import UiDialog

class DialogTareasPendientes(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_crear_tarea.clicked.connect(self.crear_tareas_pendientes)
		self.ui.pushButton_cancelar_crear_tarea.clicked.connect(self.cancelar_crear_tareas_pendientes)

	def crear_tareas_pendientes(self):
		print("Boton crear tareas pendientes presionado")
		self.accept()

	def cancelar_crear_tareas_pendientes(self):
		print("Boton cancelar creacion de tareas pendientes presionado")
		self.reject()