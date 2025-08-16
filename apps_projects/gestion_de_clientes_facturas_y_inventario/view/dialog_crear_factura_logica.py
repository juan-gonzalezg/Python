from PySide6.QtWidgets import QDialog
from view.dialog_crear_factura import UiDialog

class DialogCrearFactura(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_agregar_producto_crear_factura.clicked.connect(self.add_product)
		self.ui.pushButton_eliminar_producto_crear_factura.clicked.connect(self.remove_product)
		self.ui.pushButton_crear_factura.clicked.connect(self.create_invoice)
		self.ui.pushButton_cancelar_crear_factura.clicked.connect(self.cancel_creation_invoice)

	def add_product(self):
		print("Adding product...")

	def remove_product(self):
		print("Removing product...")

	def create_invoice(self):
		print("Creating invoice...")
		self.close()

	def cancel_creation_invoice(self):
		print("Cancelling invoice creation...")
		self.close()
