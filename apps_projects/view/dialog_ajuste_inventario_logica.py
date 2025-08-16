from PySide6.QtWidgets import QDialog
from view.dialog_ajuste_inventario import UiDialog

class DialogAjusteInventario(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_ajustar_item_stock.clicked.connect(self.ajustar_item_stock)
		self.ui.pushButton_cancelar_ajustar_item_stock.clicked.connect(self.cancelar_ajustar_item_stock)

	def ajustar_item_stock(self):
		print("Boton ajustar item stock presionado")
		self.accept()

	def cancelar_ajustar_item_stock(self):
		print("Boton cancelar presionado")
		self.reject()