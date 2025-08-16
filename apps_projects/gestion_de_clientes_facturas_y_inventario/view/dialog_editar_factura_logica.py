from PySide6.QtWidgets import QDialog
from view.dialog_editar_factura import UiDialog
from view.dialog_editar_item_factura_logica import DialogEditarItemFactura
from view.dialog_agregar_item_factura_logica import DialogAgregarItemFactura
from view.dialog_eliminar_generico_logica import DialogEliminar

class DialogEditarFactura(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = UiDialog()
		self.ui.setup_ui(self)

		self.ui.pushButton_agregar_producto_editar_factura.clicked.connect(self.agregar_producto)
		self.ui.pushButton_editar_producto_editar_factura.clicked.connect(self.editar_producto)
		self.ui.pushButton_eliminar_producto_editar_factura.clicked.connect(self.eliminar_producto)
		self.ui.pushButton_guardar_editar_factura.clicked.connect(self.guardar_editar_factura)
		self.ui.pushButton_cancelar_editar_factura.clicked.connect(self.cancelar_editar_factura)
		
	def agregar_producto(self):
		print("button agregar producto presionado")
		dialog = DialogAgregarItemFactura(self)
		if dialog.exec() == QDialog.accepted:
			print("Producto agregado")
	
	def editar_producto(self):
		print("button editar producto presionado")
		dialog = DialogEditarItemFactura(self)
		if dialog.exec() == QDialog.accepted:
			print("Producto editado")
			
	def eliminar_producto(self):
		print("button eliminar producto presionado")
		dialog = DialogEliminar(self)
		if dialog.exec() == QDialog.accepted:
			print("Producto eliminado")
	
	def guardar_editar_factura(self):
		print("button guardar editar factura presionado")
		self.accept()
		
	def cancelar_editar_factura(self):
		print("button cancelar editar factura presionado")
		self.reject()