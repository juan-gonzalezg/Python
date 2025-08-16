from PySide6.QtWidgets import QDialog
from view.dialog_editar_item_factura import UiDialog

class DialogEditarItemFactura(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_editar_item_factura.clicked.connect(self.editar_item_factura)
		self.ui.pushButton_cancelar_editar_item_factura.clicked.connect(self.cancelar_editar_item_factura)

	def editar_item_factura(self):
		print("Boton editar item factura presionado")
		self.accept()

	def cancelar_editar_item_factura(self):
		print("Boton cancelar presionado")
		self.reject()