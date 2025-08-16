from PySide6.QtWidgets import QDialog
from view.dialog_agregar_item_factura import (UiDialog)

class DialogAgregarItemFactura(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_agregar_item_factura.clicked.connect(self.agregar_item_factura)
		self.ui.pushButton_cancelar_agregar_item_factura.clicked.connect(self.cancelar_agregar_item_factura)

	def agregar_item_factura(self):
		print("Boton agregar item factura presionado")
		self.accept()

	def cancelar_agregar_item_factura(self):
		print("Boton cancelar agregar item factura presionado")
		self.reject()