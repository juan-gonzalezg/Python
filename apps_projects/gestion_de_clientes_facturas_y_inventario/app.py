import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from view.view import UiMainWindow
from view.dialog_actualizar_formula_logica import DialogActualizarFormula
from view.dialog_agregar_cliente_logica import DialogAgregarCliente
from view.dialog_editar_cliente_logica import DialogEditarCliente
from view.dialog_agregar_formula_logica import DialogAgregarFormula
from view.dialog_ajustar_periodo_logica import DialogAjustarPeriodo
from view.dialog_ajuste_inventario_logica import DialogAjusteInventario
from view.dialog_crear_factura_logica import DialogCrearFactura
from view.dialog_eliminar_generico_logica import DialogEliminar
from view.dialog_editar_factura_logica import DialogEditarFactura
from view.dialog_registrar_entrada_logica import DialogRegistrarEntrada
from view.dialog_registrar_salida_logica import DialogRegistrarSalida
from view.dialog_tareas_pendientes_logica import DialogTareasPendientes

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = UiMainWindow()
		self.ui.setup_ui(self)

		self.ui.pushButton_home.clicked.connect(lambda: self.change_tab_by_name("tab_home"))
		self.ui.pushButton_stock.clicked.connect(lambda: self.change_tab_by_name("tab_stock"))
		self.ui.pushButton_recipe.clicked.connect(lambda: self.change_tab_by_name("tab_recipe"))
		self.ui.pushButton_traceability.clicked.connect(lambda: self.change_tab_by_name("tab_traceability"))
		self.ui.pushButton_statistics.clicked.connect(lambda: self.change_tab_by_name("tab_statistics"))
		self.ui.pushButton_invoicing.clicked.connect(lambda: self.change_tab_by_name("tab_invoicing"))
		self.ui.pushButton_customers.clicked.connect(lambda: self.change_tab_by_name("tab_customers"))

		self.ui.pushButton_crear_tarea_inicio.clicked.connect(self.show_create_task_dialog)

		self.ui.pushButton_registrar_entrada_inventario.clicked.connect(self.show_register_entry_inventory_dialog)
		self.ui.pushButton_registrar_salida_inventario.clicked.connect(self.show_register_exit_inventory_dialog)
		self.ui.pushButton_ajustar_stock_inventario.clicked.connect(self.show_adjust_stock_dialog)
		#self.ui.toolButton_filtrado_avanzado_materia_prima.clicked.connect()

		self.ui.pushButton_agregar_formula.clicked.connect(self.show_add_formula_dialog)
		self.ui.pushButton_eliminar_formula.clicked.connect(self.show_eliminate_dialog)
		self.ui.pushButton_actualizar_formula.clicked.connect(self.show_update_formula_dialog)
		#self.ui.toolButton_filtrado_avanzado_formulas.clicked.connect()

		#self.ui.pushButton_generar_informe_trazabilidad.clicked.connect()

		self.ui.pushButton_statistics_sales.clicked.connect(lambda: self.show_statistics_and_subtab("tab_sales_statistics"))
		self.ui.pushButton_statistics_production.clicked.connect(lambda: self.show_statistics_and_subtab("tab_production_statistics"))
		self.ui.pushButton_statistics_stock.clicked.connect(lambda: self.show_statistics_and_subtab("tab_stock_statistics"))

		self.ui.pushButton_ajustar_periodo_productos_sales_statistics.clicked.connect(self.show_adjust_period_dialog)
		self.ui.pushButton_ajustar_periodo_periodo_sales_statistics.clicked.connect(self.show_adjust_period_dialog)
		self.ui.pushButton_ajustar_periodo_lotes_production_statistics.clicked.connect(self.show_adjust_period_dialog)
		self.ui.pushButton_ajustar_periodo_rendimiento_production_statistics.clicked.connect(self.show_adjust_period_dialog)
		self.ui.pushButton_ajustar_periodo_pronostico_stock_statistics.clicked.connect(self.show_adjust_period_dialog)
		self.ui.pushButton_ajustar_periodo_consumo_stock_statistics.clicked.connect(self.show_adjust_period_dialog)

		self.ui.pushButton_crear_nueva_factura_invoicing.clicked.connect(self.show_create_invoice_dialog)
		self.ui.pushButton_eliminar_factura_invoicing.clicked.connect(self.show_eliminate_dialog)
		self.ui.pushButton_editar_factura_invoicing.clicked.connect(self.show_edit_invoice_dialog)
		#self.ui.pushButton_generar_pdf_imprimir_invoicing.clicked.connect()

		self.ui.pushButton_agregar_cliente.clicked.connect(self.show_add_customer_dialog)
		self.ui.pushButton_eliminar_cliente.clicked.connect(self.show_eliminate_dialog)
		self.ui.pushButton_editar_cliente.clicked.connect(self.show_edit_customer_dialog)

		self.ui.main.setCurrentIndex(0)

	def change_tab_by_name(self, tab_name):
		for i in range(self.ui.main.count()):
			if self.ui.main.widget(i).objectName() == tab_name:
				self.ui.main.setCurrentIndex(i)

	def change_statistics_tab_by_name(self, tab_name):
		for i in range(self.ui.tabWidget_statistics.count()):
			if self.ui.tabWidget_statistics.widget(i).objectName() == tab_name:
				self.ui.tabWidget_statistics.setCurrentIndex(i)

	def show_statistics_and_subtab(self, sub_tab_name):
		self.change_tab_by_name("tab_statistics")
		self.change_statistics_tab_by_name(sub_tab_name)

	def show_eliminate_dialog(self):
		dialog = DialogEliminar(self)
		if dialog.exec() == QDialog.accepted:
			print("Eliminado")
		else:
			print("Elimination cancelada")

	def show_create_task_dialog(self):
		dialog = DialogTareasPendientes(self)
		if dialog.exec() == QDialog.accepted:
			print("Tarea creada")
		else:
			print("Creation de tarea cancelada")

	def show_register_entry_inventory_dialog(self):
		dialog = DialogRegistrarEntrada(self)
		if dialog.exec() == QDialog.accepted:
			print("Entrada registrada")
		else:
			print("Registro de entrada cancelado")

	def show_register_exit_inventory_dialog(self):
		dialog = DialogRegistrarSalida(self)
		if dialog.exec() == QDialog.accepted:
			print("Salida registrada")
		else:
			print("Registro de salida cancelado")

	def show_adjust_stock_dialog(self):
		dialog = DialogAjusteInventario(self)
		if dialog.exec() == QDialog.accepted:
			print("Stock ajustado")
		else:
			print("Ajuste de stock cancelado")

	def show_add_formula_dialog(self):
		dialog = DialogAgregarFormula(self)
		if dialog.exec() == QDialog.accepted:
			print("Formula agregada")
		else:
			print("Add de formula cancelada")

	def show_update_formula_dialog(self):
		dialog = DialogActualizarFormula(self)
		if dialog.exec() == QDialog.accepted:
			print("Formula actualizada")
		else:
			print("Update de formula cancelada")

	def show_adjust_period_dialog(self):
		dialog = DialogAjustarPeriodo(self)
		if dialog.exec() == QDialog.accepted:
			print("Periodo ajustado")
		else:
			print("Ajuste de periodo cancelado")

	def show_create_invoice_dialog(self):
		dialog = DialogCrearFactura(self)
		if dialog.exec() == QDialog.accepted:
			print("Factura creada")
		else:
			print("Creation de factura cancelada")

	def show_add_customer_dialog(self):
		dialog = DialogAgregarCliente(self)
		if dialog.exec() == QDialog.accepted:
			print("Cliente agregado")
		else:
			print("Add de cliente cancelada")

	def show_edit_invoice_dialog(self):
		dialog = DialogEditarFactura(self)
		if dialog.exec() == QDialog.accepted:
			print("Factura editada")
		else:
			print("Edition de factura cancelada")

	def show_edit_customer_dialog(self):
		dialog = DialogEditarCliente(self)
		if dialog.exec() == QDialog.accepted:
			print("Cliente editado")
		else:
			print("Edition de cliente cancelada")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())