from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont)
from PySide6.QtWidgets import (QComboBox, QDateEdit, QFrame, QGridLayout, QGroupBox, QHBoxLayout, QLCDNumber, QLabel, QLineEdit, QListWidget, QPushButton, QRadioButton, QScrollArea, QTabWidget, QTableView, QToolButton, QVBoxLayout, QWidget)

class UiMainWindow(object):
    def __init__(self):
        self.central_widget = None
        self.main = None
        self.tab_home = None
        self.frame_pedidos_pendientes_inicio = None
        self.label_pedidos_pendientes_inicio = None
        self.lcdNumber_inicio = None
        self.listWidget_alertas_criticas_inicio = None
        self.listWidget_tareas_pendientes_inicio = None
        self.widget_grafica_inicio = None
        self.label_tareas_pendientes_inicio = None
        self.label_alertas_criticas_inicio = None
        self.label_resumen_ventas_inicio = None
        self.pushButton_crear_tarea_inicio = None
        self.tab_stock = None
        self.frame_materia_prima = None
        self.horizontalLayoutWidget = None
        self.horizontalLayout_materia_prima = None
        self.lineEdit_buscador_materia_prima = None
        self.pushButton_filtrar_materia_prima = None
        self.toolButton_filtrado_avanzado_materia_prima = None
        self.tableView_materia_prima = None
        self.label_materia_prima = None
        self.frame_productos_terminados = None
        self.horizontalLayoutWidget_2 = None
        self.horizontalLayout_productos_terminados = None
        self.lineEdit_buscador_productos_terminados = None
        self.pushButton_filtrar_productos_terminados = None
        self.label_productos_terminados = None
        self.tableView_productos_terminados = None
        self.frame_funciones_action_speed_inventario = None
        self.pushButton_ajustar_stock_inventario = None
        self.pushButton_registrar_entrada_inventario = None
        self.label_funciones_action_speed_inventario = None
        self.pushButton_registrar_salida_inventario = None
        self.tab_recipe = None
        self.frame_funciones_action_speed_formulas = None
        self.pushButton_actualizar_formula = None
        self.label_funciones_action_speed_formula = None
        self.pushButton_eliminar_formula = None
        self.pushButton_agregar_formula = None
        self.frame_formula = None
        self.label_formula_recetas = None
        self.horizontalLayoutWidget_4 = None
        self.horizontalLayout_buscador_formula = None
        self.lineEdit_buscador_formulas = None
        self.pushButton_filtrar_formulas = None
        self.toolButton_filtrado_avanzado_formulas = None
        self.scrollArea_formula = None
        self.scrollAreaWidgetContents_formulas = None
        self.gridLayout_2 = None
        self.tab_traceability = None
        self.frame_filtrado_trazabilidad = None
        self.label_trazabilidad = None
        self.lineEdit_trazabilidad = None
        self.pushButton_filtrar_trazabilidad = None
        self.radioButton_mostrar_productos_terminados_trazabilidad = None
        self.radioButton_periodo_tiempo_trazabilidad = None
        self.groupBox_periodo_tiempo_trazabilidad = None
        self.dateEdit_de_periodo_tiempo_trazabilidad = None
        self.dateEdit_a_periodo_tiempo_trazabilidad = None
        self.label_de_periodo_tiempo_trazabilidad = None
        self.label_a_periodo_tiempo_trazabilidad = None
        self.pushButton_filtrar_periodo_tiempo_trazabilidad = None
        self.radioButton_estado_lote_trazabilidad = None
        self.groupBox_estado_lote_trazabilidad = None
        self.comboBox_estado_lote_trazabilidad = None
        self.pushButton_filtrar_estado_lote_trazabilidad = None
        self.pushButton_generar_informe_trazabilidad = None
        self.label_trazabilidad_2 = None
        self.tableView_trazabilidad = None
        self.tab_statistics = None
        self.tabWidget_statistics = None
        self.tab_sales_statistics = None
        self.tableView_clientes_importantes_sales_statistics = None
        self.frame_grafico_ventas_por_periodo_sales_statistics = None
        self.frame_grafico_ventas_productos_sales_statistics = None
        self.label_tabla_clientes_mas_importantes_sales_statistics = None
        self.pushButton_ajustar_periodo_productos_sales_statistics = None
        self.label_grafico_ventas_por_productos_sales_statistics = None
        self.pushButton_filtrar_clientes_sales_statistics = None
        self.lineEdit_buscador_clientes_sales_statistics = None
        self.pushButton_ajustar_periodo_periodo_sales_statistics = None
        self.label_grafico_ventas_por_periodo_sales_statistics = None
        self.tab_stock_statistics = None
        self.frame_grafico_consumo_materia_prima_stock_statistics = None
        self.frame_grafico_pronostico_stock_stock_statistics = None
        self.tableView_productos_bajo_movimiento_stock_statistics = None
        self.label_tabla_productos_bajo_movimiento_stock_statistics = None
        self.pushButton_ajustar_periodo_pronostico_stock_statistics = None
        self.label_grafico_pronostico_stock_stock_statistics = None
        self.pushButton_ajustar_periodo_consumo_stock_statistics = None
        self.label_grafico_consumo_materia_prima_stock_statistics = None
        self.lineEdit_buscador_productos_stock_statistics = None
        self.pushButton_filtrar_productos_stock_statistics = None
        self.tab_production_statistics = None
        self.tableView_costo_production_por_lotes_production_statistics = None
        self.frame_grafico_lotes_producidos_production_statistics = None
        self.frame_grafico_rendimiento_production_production_statistics = None
        self.label_tabla_costo_production_por_lote_production_statistics = None
        self.label_grafico_lotes_producido_production_statistics = None
        self.pushButton_ajustar_periodo_lotes_production_statistics = None
        self.label_grafico_rendimiento_production_production_statistics = None
        self.pushButton_ajustar_periodo_rendimiento_production_statistics = None
        self.lineEdit_buscador_production_lotes_production_statistics = None
        self.pushButton_filtrar_production_por_lotes_production_statistics = None
        self.tab_invoicing = None
        self.frame_funciones_action_speed_invoicing = None
        self.pushButton_crear_nueva_factura_invoicing = None
        self.pushButton_editar_factura_invoicing = None
        self.pushButton_eliminar_factura_invoicing = None
        self.pushButton_generar_pdf_imprimir_invoicing = None
        self.label_funciones_invoicing = None
        self.tableView_invoicing = None
        self.tab_customers = None
        self.frame_clientes = None
        self.pushButton_agregar_cliente = None
        self.pushButton_editar_cliente = None
        self.pushButton_eliminar_cliente = None
        self.label_funciones_action_speed_clientes = None
        self.tableView_clientes = None
        self.frame_menu = None
        self.verticalLayoutWidget = None
        self.verticalLayout_menu = None
        self.pushButton_home = None
        self.pushButton_stock = None
        self.pushButton_recipe = None
        self.pushButton_traceability = None
        self.pushButton_statistics = None
        self.verticalLayout_statistics_menu = None
        self.pushButton_statistics_sales = None
        self.pushButton_statistics_production = None
        self.pushButton_statistics_stock = None
        self.pushButton_invoicing = None
        self.pushButton_customers = None

    def setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(1320, 669)
        main_window.setMaximumSize(QSize(1320, 688))
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.main = QTabWidget(self.central_widget)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(210, 20, 1111, 651))
        self.main.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.main.setMouseTracking(False)
        self.main.setTabletTracking(False)
        self.tab_home = QWidget()
        self.tab_home.setObjectName(u"tab_home")
        self.frame_pedidos_pendientes_inicio = QFrame(self.tab_home)
        self.frame_pedidos_pendientes_inicio.setObjectName(u"frame_pedidos_pendientes_inicio")
        self.frame_pedidos_pendientes_inicio.setGeometry(QRect(690, 20, 211, 111))
        self.frame_pedidos_pendientes_inicio.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pedidos_pendientes_inicio.setFrameShadow(QFrame.Shadow.Raised)
        self.label_pedidos_pendientes_inicio = QLabel(self.frame_pedidos_pendientes_inicio)
        self.label_pedidos_pendientes_inicio.setObjectName(u"label_pedidos_pendientes_inicio")
        self.label_pedidos_pendientes_inicio.setGeometry(QRect(10, 0, 201, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_pedidos_pendientes_inicio.setFont(font)
        self.lcdNumber_inicio = QLCDNumber(self.frame_pedidos_pendientes_inicio)
        self.lcdNumber_inicio.setObjectName(u"lcdNumber_inicio")
        self.lcdNumber_inicio.setGeometry(QRect(60, 40, 101, 61))
        self.lcdNumber_inicio.setDigitCount(3)
        self.listWidget_alertas_criticas_inicio = QListWidget(self.tab_home)
        self.listWidget_alertas_criticas_inicio.setObjectName(u"listWidget_alertas_criticas_inicio")
        self.listWidget_alertas_criticas_inicio.setGeometry(QRect(10, 50, 301, 561))
        self.listWidget_tareas_pendientes_inicio = QListWidget(self.tab_home)
        self.listWidget_tareas_pendientes_inicio.setObjectName(u"listWidget_tareas_pendientes_inicio")
        self.listWidget_tareas_pendientes_inicio.setGeometry(QRect(350, 50, 301, 561))
        self.widget_grafica_inicio = QWidget(self.tab_home)
        self.widget_grafica_inicio.setObjectName(u"widget_grafica_inicio")
        self.widget_grafica_inicio.setGeometry(QRect(690, 200, 391, 341))
        self.label_tareas_pendientes_inicio = QLabel(self.tab_home)
        self.label_tareas_pendientes_inicio.setObjectName(u"label_tareas_pendientes_inicio")
        self.label_tareas_pendientes_inicio.setGeometry(QRect(360, 10, 181, 41))
        self.label_tareas_pendientes_inicio.setFont(font)
        self.label_alertas_criticas_inicio = QLabel(self.tab_home)
        self.label_alertas_criticas_inicio.setObjectName(u"label_alertas_criticas_inicio")
        self.label_alertas_criticas_inicio.setGeometry(QRect(20, 10, 161, 41))
        self.label_alertas_criticas_inicio.setFont(font)
        self.label_resumen_ventas_inicio = QLabel(self.tab_home)
        self.label_resumen_ventas_inicio.setObjectName(u"label_resumen_ventas_inicio")
        self.label_resumen_ventas_inicio.setGeometry(QRect(700, 160, 201, 31))
        self.label_resumen_ventas_inicio.setFont(font)
        self.pushButton_crear_tarea_inicio = QPushButton(self.tab_home)
        self.pushButton_crear_tarea_inicio.setObjectName(u"pushButton_crear_tarea_inicio")
        self.pushButton_crear_tarea_inicio.setGeometry(QRect(570, 20, 75, 24))
        self.main.addTab(self.tab_home, "")
        self.tab_stock = QWidget()
        self.tab_stock.setObjectName(u"tab_stock")
        self.frame_materia_prima = QFrame(self.tab_stock)
        self.frame_materia_prima.setObjectName(u"frame_materia_prima")
        self.frame_materia_prima.setGeometry(QRect(9, 79, 701, 541))
        self.frame_materia_prima.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_materia_prima.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame_materia_prima)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(230, 0, 451, 41))
        self.horizontalLayout_materia_prima = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_materia_prima.setObjectName(u"horizontalLayout_materia_prima")
        self.horizontalLayout_materia_prima.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_buscador_materia_prima = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_buscador_materia_prima.setObjectName(u"lineEdit_buscador_materia_prima")

        self.horizontalLayout_materia_prima.addWidget(self.lineEdit_buscador_materia_prima)

        self.pushButton_filtrar_materia_prima = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_filtrar_materia_prima.setObjectName(u"pushButton_filtrar_materia_prima")

        self.horizontalLayout_materia_prima.addWidget(self.pushButton_filtrar_materia_prima)

        self.toolButton_filtrado_avanzado_materia_prima = QToolButton(self.horizontalLayoutWidget)
        self.toolButton_filtrado_avanzado_materia_prima.setObjectName(u"toolButton_filtrado_avanzado_materia_prima")

        self.horizontalLayout_materia_prima.addWidget(self.toolButton_filtrado_avanzado_materia_prima)

        self.tableView_materia_prima = QTableView(self.frame_materia_prima)
        self.tableView_materia_prima.setObjectName(u"tableView_materia_prima")
        self.tableView_materia_prima.setGeometry(QRect(10, 40, 681, 491))
        self.label_materia_prima = QLabel(self.frame_materia_prima)
        self.label_materia_prima.setObjectName(u"label_materia_prima")
        self.label_materia_prima.setGeometry(QRect(8, 10, 181, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_materia_prima.setFont(font1)
        self.frame_productos_terminados = QFrame(self.tab_stock)
        self.frame_productos_terminados.setObjectName(u"frame_productos_terminados")
        self.frame_productos_terminados.setGeometry(QRect(750, 80, 351, 541))
        self.frame_productos_terminados.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_productos_terminados.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_2 = QWidget(self.frame_productos_terminados)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 40, 331, 41))
        self.horizontalLayout_productos_terminados = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_productos_terminados.setObjectName(u"horizontalLayout_productos_terminados")
        self.horizontalLayout_productos_terminados.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_buscador_productos_terminados = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_buscador_productos_terminados.setObjectName(u"lineEdit_buscador_productos_terminados")

        self.horizontalLayout_productos_terminados.addWidget(self.lineEdit_buscador_productos_terminados)

        self.pushButton_filtrar_productos_terminados = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_filtrar_productos_terminados.setObjectName(u"pushButton_filtrar_productos_terminados")

        self.horizontalLayout_productos_terminados.addWidget(self.pushButton_filtrar_productos_terminados)

        self.label_productos_terminados = QLabel(self.frame_productos_terminados)
        self.label_productos_terminados.setObjectName(u"label_productos_terminados")
        self.label_productos_terminados.setGeometry(QRect(8, 10, 221, 31))
        self.label_productos_terminados.setFont(font1)
        self.tableView_productos_terminados = QTableView(self.frame_productos_terminados)
        self.tableView_productos_terminados.setObjectName(u"tableView_productos_terminados")
        self.tableView_productos_terminados.setGeometry(QRect(10, 80, 331, 451))
        self.frame_funciones_action_speed_inventario = QFrame(self.tab_stock)
        self.frame_funciones_action_speed_inventario.setObjectName(u"frame_funciones_action_speed_inventario")
        self.frame_funciones_action_speed_inventario.setGeometry(QRect(310, 10, 531, 61))
        self.frame_funciones_action_speed_inventario.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_funciones_action_speed_inventario.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_ajustar_stock_inventario = QPushButton(self.frame_funciones_action_speed_inventario)
        self.pushButton_ajustar_stock_inventario.setObjectName(u"pushButton_ajustar_stock_inventario")
        self.pushButton_ajustar_stock_inventario.setGeometry(QRect(390, 10, 121, 41))
        self.pushButton_registrar_entrada_inventario = QPushButton(self.frame_funciones_action_speed_inventario)
        self.pushButton_registrar_entrada_inventario.setObjectName(u"pushButton_registrar_entrada_inventario")
        self.pushButton_registrar_entrada_inventario.setGeometry(QRect(120, 10, 121, 41))
        self.label_funciones_action_speed_inventario = QLabel(self.frame_funciones_action_speed_inventario)
        self.label_funciones_action_speed_inventario.setObjectName(u"label_funciones_action_speed_inventario")
        self.label_funciones_action_speed_inventario.setGeometry(QRect(20, 20, 91, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_funciones_action_speed_inventario.setFont(font2)
        self.pushButton_registrar_salida_inventario = QPushButton(self.frame_funciones_action_speed_inventario)
        self.pushButton_registrar_salida_inventario.setObjectName(u"pushButton_registrar_salida_inventario")
        self.pushButton_registrar_salida_inventario.setGeometry(QRect(260, 10, 111, 41))
        self.main.addTab(self.tab_stock, "")
        self.tab_recipe = QWidget()
        self.tab_recipe.setObjectName(u"tab_recipe")
        self.frame_funciones_action_speed_formulas = QFrame(self.tab_recipe)
        self.frame_funciones_action_speed_formulas.setObjectName(u"frame_funciones_action_speed_formulas")
        self.frame_funciones_action_speed_formulas.setGeometry(QRect(260, 9, 651, 51))
        self.frame_funciones_action_speed_formulas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_funciones_action_speed_formulas.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_actualizar_formula = QPushButton(self.frame_funciones_action_speed_formulas)
        self.pushButton_actualizar_formula.setObjectName(u"pushButton_actualizar_formula")
        self.pushButton_actualizar_formula.setGeometry(QRect(480, 5, 161, 41))
        self.label_funciones_action_speed_formula = QLabel(self.frame_funciones_action_speed_formulas)
        self.label_funciones_action_speed_formula.setObjectName(u"label_funciones_action_speed_formula")
        self.label_funciones_action_speed_formula.setGeometry(QRect(20, 0, 101, 49))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_funciones_action_speed_formula.setFont(font3)
        self.pushButton_eliminar_formula = QPushButton(self.frame_funciones_action_speed_formulas)
        self.pushButton_eliminar_formula.setObjectName(u"pushButton_eliminar_formula")
        self.pushButton_eliminar_formula.setGeometry(QRect(310, 5, 151, 41))
        self.pushButton_agregar_formula = QPushButton(self.frame_funciones_action_speed_formulas)
        self.pushButton_agregar_formula.setObjectName(u"pushButton_agregar_formula")
        self.pushButton_agregar_formula.setGeometry(QRect(140, 5, 151, 41))
        self.frame_formula = QFrame(self.tab_recipe)
        self.frame_formula.setObjectName(u"frame_formula")
        self.frame_formula.setGeometry(QRect(10, 70, 1091, 551))
        self.frame_formula.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_formula.setFrameShadow(QFrame.Shadow.Raised)
        self.label_formula_recetas = QLabel(self.frame_formula)
        self.label_formula_recetas.setObjectName(u"label_formula_recetas")
        self.label_formula_recetas.setGeometry(QRect(20, 0, 181, 41))
        self.label_formula_recetas.setFont(font)
        self.horizontalLayoutWidget_4 = QWidget(self.frame_formula)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(370, 0, 701, 41))
        self.horizontalLayout_buscador_formula = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_buscador_formula.setObjectName(u"horizontalLayout_buscador_formula")
        self.horizontalLayout_buscador_formula.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_buscador_formulas = QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_buscador_formulas.setObjectName(u"lineEdit_buscador_formulas")

        self.horizontalLayout_buscador_formula.addWidget(self.lineEdit_buscador_formulas)

        self.pushButton_filtrar_formulas = QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_filtrar_formulas.setObjectName(u"pushButton_filtrar_formulas")

        self.horizontalLayout_buscador_formula.addWidget(self.pushButton_filtrar_formulas)

        self.toolButton_filtrado_avanzado_formulas = QToolButton(self.horizontalLayoutWidget_4)
        self.toolButton_filtrado_avanzado_formulas.setObjectName(u"toolButton_filtrado_avanzado_formulas")

        self.horizontalLayout_buscador_formula.addWidget(self.toolButton_filtrado_avanzado_formulas)

        self.scrollArea_formula = QScrollArea(self.frame_formula)
        self.scrollArea_formula.setObjectName(u"scrollArea_formula")
        self.scrollArea_formula.setGeometry(QRect(-1, 39, 1091, 511))
        self.scrollArea_formula.setWidgetResizable(True)
        self.scrollArea_formula.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.scrollAreaWidgetContents_formulas = QWidget()
        self.scrollAreaWidgetContents_formulas.setObjectName(u"scrollAreaWidgetContents_formulas")
        self.scrollAreaWidgetContents_formulas.setGeometry(QRect(0, 0, 1089, 509))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_formulas)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.scrollArea_formula.setWidget(self.scrollAreaWidgetContents_formulas)
        self.main.addTab(self.tab_recipe, "")
        self.tab_traceability = QWidget()
        self.tab_traceability.setObjectName(u"tab_traceability")
        self.frame_filtrado_trazabilidad = QFrame(self.tab_traceability)
        self.frame_filtrado_trazabilidad.setObjectName(u"frame_filtrado_trazabilidad")
        self.frame_filtrado_trazabilidad.setGeometry(QRect(10, 60, 241, 421))
        self.frame_filtrado_trazabilidad.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_filtrado_trazabilidad.setFrameShadow(QFrame.Shadow.Raised)
        self.label_trazabilidad = QLabel(self.frame_filtrado_trazabilidad)
        self.label_trazabilidad.setObjectName(u"label_trazabilidad")
        self.label_trazabilidad.setGeometry(QRect(20, 10, 111, 31))
        self.label_trazabilidad.setFont(font2)
        self.lineEdit_trazabilidad = QLineEdit(self.frame_filtrado_trazabilidad)
        self.lineEdit_trazabilidad.setObjectName(u"lineEdit_trazabilidad")
        self.lineEdit_trazabilidad.setGeometry(QRect(10, 50, 151, 21))
        self.pushButton_filtrar_trazabilidad = QPushButton(self.frame_filtrado_trazabilidad)
        self.pushButton_filtrar_trazabilidad.setObjectName(u"pushButton_filtrar_trazabilidad")
        self.pushButton_filtrar_trazabilidad.setGeometry(QRect(170, 50, 61, 24))
        self.radioButton_mostrar_productos_terminados_trazabilidad = QRadioButton(self.frame_filtrado_trazabilidad)
        self.radioButton_mostrar_productos_terminados_trazabilidad.setObjectName(u"radioButton_mostrar_productos_terminados_trazabilidad")
        self.radioButton_mostrar_productos_terminados_trazabilidad.setGeometry(QRect(10, 90, 201, 20))
        font4 = QFont()
        font4.setBold(False)
        self.radioButton_mostrar_productos_terminados_trazabilidad.setFont(font4)
        self.radioButton_periodo_tiempo_trazabilidad = QRadioButton(self.frame_filtrado_trazabilidad)
        self.radioButton_periodo_tiempo_trazabilidad.setObjectName(u"radioButton_periodo_tiempo_trazabilidad")
        self.radioButton_periodo_tiempo_trazabilidad.setGeometry(QRect(10, 120, 131, 20))
        self.groupBox_periodo_tiempo_trazabilidad = QGroupBox(self.frame_filtrado_trazabilidad)
        self.groupBox_periodo_tiempo_trazabilidad.setObjectName(u"groupBox_periodo_tiempo_trazabilidad")
        self.groupBox_periodo_tiempo_trazabilidad.setGeometry(QRect(40, 140, 191, 111))
        self.dateEdit_de_periodo_tiempo_trazabilidad = QDateEdit(self.groupBox_periodo_tiempo_trazabilidad)
        self.dateEdit_de_periodo_tiempo_trazabilidad.setObjectName(u"dateEdit_de_periodo_tiempo_trazabilidad")
        self.dateEdit_de_periodo_tiempo_trazabilidad.setGeometry(QRect(40, 20, 116, 23))
        self.dateEdit_a_periodo_tiempo_trazabilidad = QDateEdit(self.groupBox_periodo_tiempo_trazabilidad)
        self.dateEdit_a_periodo_tiempo_trazabilidad.setObjectName(u"dateEdit_a_periodo_tiempo_trazabilidad")
        self.dateEdit_a_periodo_tiempo_trazabilidad.setGeometry(QRect(40, 50, 116, 23))
        self.label_de_periodo_tiempo_trazabilidad = QLabel(self.groupBox_periodo_tiempo_trazabilidad)
        self.label_de_periodo_tiempo_trazabilidad.setObjectName(u"label_de_periodo_tiempo_trazabilidad")
        self.label_de_periodo_tiempo_trazabilidad.setGeometry(QRect(10, 20, 21, 20))
        self.label_a_periodo_tiempo_trazabilidad = QLabel(self.groupBox_periodo_tiempo_trazabilidad)
        self.label_a_periodo_tiempo_trazabilidad.setObjectName(u"label_a_periodo_tiempo_trazabilidad")
        self.label_a_periodo_tiempo_trazabilidad.setGeometry(QRect(10, 50, 21, 20))
        self.pushButton_filtrar_periodo_tiempo_trazabilidad = QPushButton(self.groupBox_periodo_tiempo_trazabilidad)
        self.pushButton_filtrar_periodo_tiempo_trazabilidad.setObjectName(u"pushButton_filtrar_periodo_tiempo_trazabilidad")
        self.pushButton_filtrar_periodo_tiempo_trazabilidad.setGeometry(QRect(50, 80, 75, 24))
        self.radioButton_estado_lote_trazabilidad = QRadioButton(self.frame_filtrado_trazabilidad)
        self.radioButton_estado_lote_trazabilidad.setObjectName(u"radioButton_estado_lote_trazabilidad")
        self.radioButton_estado_lote_trazabilidad.setGeometry(QRect(10, 260, 101, 20))
        self.groupBox_estado_lote_trazabilidad = QGroupBox(self.frame_filtrado_trazabilidad)
        self.groupBox_estado_lote_trazabilidad.setObjectName(u"groupBox_estado_lote_trazabilidad")
        self.groupBox_estado_lote_trazabilidad.setGeometry(QRect(40, 280, 191, 81))
        self.comboBox_estado_lote_trazabilidad = QComboBox(self.groupBox_estado_lote_trazabilidad)
        self.comboBox_estado_lote_trazabilidad.setObjectName(u"comboBox_estado_lote_trazabilidad")
        self.comboBox_estado_lote_trazabilidad.setGeometry(QRect(10, 20, 171, 24))
        self.pushButton_filtrar_estado_lote_trazabilidad = QPushButton(self.groupBox_estado_lote_trazabilidad)
        self.pushButton_filtrar_estado_lote_trazabilidad.setObjectName(u"pushButton_filtrar_estado_lote_trazabilidad")
        self.pushButton_filtrar_estado_lote_trazabilidad.setGeometry(QRect(60, 50, 75, 24))
        self.pushButton_generar_informe_trazabilidad = QPushButton(self.frame_filtrado_trazabilidad)
        self.pushButton_generar_informe_trazabilidad.setObjectName(u"pushButton_generar_informe_trazabilidad")
        self.pushButton_generar_informe_trazabilidad.setGeometry(QRect(60, 380, 121, 24))
        self.label_trazabilidad_2 = QLabel(self.tab_traceability)
        self.label_trazabilidad_2.setObjectName(u"label_trazabilidad_2")
        self.label_trazabilidad_2.setGeometry(QRect(18, 0, 131, 51))
        self.label_trazabilidad_2.setFont(font)
        self.tableView_trazabilidad = QTableView(self.tab_traceability)
        self.tableView_trazabilidad.setObjectName(u"tableView_trazabilidad")
        self.tableView_trazabilidad.setGeometry(QRect(260, 10, 841, 601))
        self.main.addTab(self.tab_traceability, "")
        self.tab_statistics = QWidget()
        self.tab_statistics.setObjectName(u"tab_statistics")
        self.tabWidget_statistics = QTabWidget(self.tab_statistics)
        self.tabWidget_statistics.setObjectName(u"tabWidget_estadísticas")
        self.tabWidget_statistics.setGeometry(QRect(0, 30, 1111, 591))
        self.tab_sales_statistics = QWidget()
        self.tab_sales_statistics.setObjectName(u"tab_sales_statistics")
        self.tableView_clientes_importantes_sales_statistics = QTableView(self.tab_sales_statistics)
        self.tableView_clientes_importantes_sales_statistics.setObjectName(u"tableView_clientes_importantes_sales_statistics")
        self.tableView_clientes_importantes_sales_statistics.setGeometry(QRect(425, 41, 671, 511))
        self.frame_grafico_ventas_por_periodo_sales_statistics = QFrame(self.tab_sales_statistics)
        self.frame_grafico_ventas_por_periodo_sales_statistics.setObjectName(u"frame_grafico_ventas_por_periodo_sales_statistics")
        self.frame_grafico_ventas_por_periodo_sales_statistics.setGeometry(QRect(10, 40, 380, 210))
        self.frame_grafico_ventas_por_periodo_sales_statistics.setMinimumSize(QSize(380, 210))
        self.frame_grafico_ventas_por_periodo_sales_statistics.setMaximumSize(QSize(380, 210))
        self.frame_grafico_ventas_por_periodo_sales_statistics.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grafico_ventas_por_periodo_sales_statistics.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_grafico_ventas_productos_sales_statistics = QFrame(self.tab_sales_statistics)
        self.frame_grafico_ventas_productos_sales_statistics.setObjectName(u"frame_grafico_ventas_productos_sales_statistics")
        self.frame_grafico_ventas_productos_sales_statistics.setGeometry(QRect(10, 341, 380, 210))
        self.frame_grafico_ventas_productos_sales_statistics.setMinimumSize(QSize(380, 210))
        self.frame_grafico_ventas_productos_sales_statistics.setMaximumSize(QSize(380, 210))
        self.frame_grafico_ventas_productos_sales_statistics.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grafico_ventas_productos_sales_statistics.setFrameShadow(QFrame.Shadow.Raised)
        self.label_tabla_clientes_mas_importantes_sales_statistics = QLabel(self.tab_sales_statistics)
        self.label_tabla_clientes_mas_importantes_sales_statistics.setObjectName(u"label_tabla_clientes_mas_importantes_sales_statistics")
        self.label_tabla_clientes_mas_importantes_sales_statistics.setGeometry(QRect(430, 0, 242, 41))
        self.label_tabla_clientes_mas_importantes_sales_statistics.setFont(font2)
        self.pushButton_ajustar_periodo_productos_sales_statistics = QPushButton(self.tab_sales_statistics)
        self.pushButton_ajustar_periodo_productos_sales_statistics.setObjectName(u"pushButton_ajustar_periodo_productos_sales_statistics")
        self.pushButton_ajustar_periodo_productos_sales_statistics.setGeometry(QRect(290, 310, 91, 24))
        self.label_grafico_ventas_por_productos_sales_statistics = QLabel(self.tab_sales_statistics)
        self.label_grafico_ventas_por_productos_sales_statistics.setObjectName(u"label_grafico_ventas_por_productos_sales_statistics")
        self.label_grafico_ventas_por_productos_sales_statistics.setGeometry(QRect(20, 300, 251, 41))
        self.label_grafico_ventas_por_productos_sales_statistics.setFont(font2)
        self.pushButton_filtrar_clientes_sales_statistics = QPushButton(self.tab_sales_statistics)
        self.pushButton_filtrar_clientes_sales_statistics.setObjectName(u"pushButton_filtrar_clientes_sales_statistics")
        self.pushButton_filtrar_clientes_sales_statistics.setGeometry(QRect(1010, 10, 75, 24))
        self.lineEdit_buscador_clientes_sales_statistics = QLineEdit(self.tab_sales_statistics)
        self.lineEdit_buscador_clientes_sales_statistics.setObjectName(u"lineEdit_buscador_clientes_sales_statistics")
        self.lineEdit_buscador_clientes_sales_statistics.setGeometry(QRect(720, 10, 261, 21))
        self.pushButton_ajustar_periodo_periodo_sales_statistics = QPushButton(self.tab_sales_statistics)
        self.pushButton_ajustar_periodo_periodo_sales_statistics.setObjectName(u"pushButton_ajustar_periodo_periodo_sales_statistics")
        self.pushButton_ajustar_periodo_periodo_sales_statistics.setGeometry(QRect(293, 10, 91, 24))
        self.label_grafico_ventas_por_periodo_sales_statistics = QLabel(self.tab_sales_statistics)
        self.label_grafico_ventas_por_periodo_sales_statistics.setObjectName(u"label_grafico_ventas_por_periodo_sales_statistics")
        self.label_grafico_ventas_por_periodo_sales_statistics.setGeometry(QRect(20, 0, 231, 41))
        self.label_grafico_ventas_por_periodo_sales_statistics.setFont(font2)
        self.tabWidget_statistics.addTab(self.tab_sales_statistics, "")
        self.tab_stock_statistics = QWidget()
        self.tab_stock_statistics.setObjectName(u"tab_stock_statistics")
        self.frame_grafico_consumo_materia_prima_stock_statistics = QFrame(self.tab_stock_statistics)
        self.frame_grafico_consumo_materia_prima_stock_statistics.setObjectName(u"frame_grafico_consumo_materia_prima_stock_statistics")
        self.frame_grafico_consumo_materia_prima_stock_statistics.setGeometry(QRect(10, 50, 380, 210))
        self.frame_grafico_consumo_materia_prima_stock_statistics.setMinimumSize(QSize(380, 210))
        self.frame_grafico_consumo_materia_prima_stock_statistics.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grafico_consumo_materia_prima_stock_statistics.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_grafico_pronostico_stock_stock_statistics = QFrame(self.tab_stock_statistics)
        self.frame_grafico_pronostico_stock_stock_statistics.setObjectName(u"frame_grafico_pronostico_stock_stock_statistics")
        self.frame_grafico_pronostico_stock_stock_statistics.setGeometry(QRect(10, 340, 380, 210))
        self.frame_grafico_pronostico_stock_stock_statistics.setMinimumSize(QSize(380, 210))
        self.frame_grafico_pronostico_stock_stock_statistics.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grafico_pronostico_stock_stock_statistics.setFrameShadow(QFrame.Shadow.Raised)
        self.tableView_productos_bajo_movimiento_stock_statistics = QTableView(self.tab_stock_statistics)
        self.tableView_productos_bajo_movimiento_stock_statistics.setObjectName(u"tableView_productos_bajo_movimiento_stock_statistics")
        self.tableView_productos_bajo_movimiento_stock_statistics.setGeometry(QRect(425, 41, 671, 511))
        self.label_tabla_productos_bajo_movimiento_stock_statistics = QLabel(self.tab_stock_statistics)
        self.label_tabla_productos_bajo_movimiento_stock_statistics.setObjectName(u"label_tabla_productos_bajo_movimiento_stock_statistics")
        self.label_tabla_productos_bajo_movimiento_stock_statistics.setGeometry(QRect(430, 0, 311, 41))
        self.label_tabla_productos_bajo_movimiento_stock_statistics.setFont(font2)
        self.pushButton_ajustar_periodo_pronostico_stock_statistics = QPushButton(self.tab_stock_statistics)
        self.pushButton_ajustar_periodo_pronostico_stock_statistics.setObjectName(u"pushButton_ajustar_periodo_pronostico_stock_statistics")
        self.pushButton_ajustar_periodo_pronostico_stock_statistics.setGeometry(QRect(286, 310, 101, 24))
        self.label_grafico_pronostico_stock_stock_statistics = QLabel(self.tab_stock_statistics)
        self.label_grafico_pronostico_stock_stock_statistics.setObjectName(u"label_grafico_pronostico_stock_stock_statistics")
        self.label_grafico_pronostico_stock_stock_statistics.setGeometry(QRect(20, 300, 241, 41))
        self.label_grafico_pronostico_stock_stock_statistics.setFont(font2)
        self.pushButton_ajustar_periodo_consumo_stock_statistics = QPushButton(self.tab_stock_statistics)
        self.pushButton_ajustar_periodo_consumo_stock_statistics.setObjectName(u"pushButton_ajustar_periodo_consumo_stock_statistics")
        self.pushButton_ajustar_periodo_consumo_stock_statistics.setGeometry(QRect(300, 20, 91, 24))
        self.label_grafico_consumo_materia_prima_stock_statistics = QLabel(self.tab_stock_statistics)
        self.label_grafico_consumo_materia_prima_stock_statistics.setObjectName(u"label_grafico_consumo_materia_prima_stock_statistics")
        self.label_grafico_consumo_materia_prima_stock_statistics.setGeometry(QRect(10, 10, 291, 41))
        self.label_grafico_consumo_materia_prima_stock_statistics.setFont(font2)
        self.lineEdit_buscador_productos_stock_statistics = QLineEdit(self.tab_stock_statistics)
        self.lineEdit_buscador_productos_stock_statistics.setObjectName(u"lineEdit_buscador_productos_stock_statistics")
        self.lineEdit_buscador_productos_stock_statistics.setGeometry(QRect(750, 10, 251, 21))
        self.pushButton_filtrar_productos_stock_statistics = QPushButton(self.tab_stock_statistics)
        self.pushButton_filtrar_productos_stock_statistics.setObjectName(u"pushButton_filtrar_productos_stock_statistics")
        self.pushButton_filtrar_productos_stock_statistics.setGeometry(QRect(1014, 10, 71, 24))
        self.tabWidget_statistics.addTab(self.tab_stock_statistics, "")
        self.tab_production_statistics = QWidget()
        self.tab_production_statistics.setObjectName(u"tab_production_statistics")
        self.tableView_costo_production_por_lotes_production_statistics = QTableView(self.tab_production_statistics)
        self.tableView_costo_production_por_lotes_production_statistics.setObjectName(u"tableView_costo_production_por_lotes_production_statistics")
        self.tableView_costo_production_por_lotes_production_statistics.setGeometry(QRect(425, 41, 671, 511))
        self.frame_grafico_lotes_producidos_production_statistics = QFrame(self.tab_production_statistics)
        self.frame_grafico_lotes_producidos_production_statistics.setObjectName(u"frame_grafico_lotes_producidos_production_statistics")
        self.frame_grafico_lotes_producidos_production_statistics.setGeometry(QRect(10, 50, 380, 210))
        self.frame_grafico_lotes_producidos_production_statistics.setMinimumSize(QSize(380, 210))
        self.frame_grafico_lotes_producidos_production_statistics.setMaximumSize(QSize(380, 210))
        self.frame_grafico_lotes_producidos_production_statistics.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grafico_lotes_producidos_production_statistics.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_grafico_rendimiento_production_production_statistics = QFrame(self.tab_production_statistics)
        self.frame_grafico_rendimiento_production_production_statistics.setObjectName(u"frame_grafico_rendimiento_production__production_statistics")
        self.frame_grafico_rendimiento_production_production_statistics.setGeometry(QRect(10, 340, 380, 210))
        self.frame_grafico_rendimiento_production_production_statistics.setMinimumSize(QSize(380, 210))
        self.frame_grafico_rendimiento_production_production_statistics.setMaximumSize(QSize(380, 210))
        self.frame_grafico_rendimiento_production_production_statistics.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grafico_rendimiento_production_production_statistics.setFrameShadow(QFrame.Shadow.Raised)
        self.label_tabla_costo_production_por_lote_production_statistics = QLabel(self.tab_production_statistics)
        self.label_tabla_costo_production_por_lote_production_statistics.setObjectName(u"label_tabla_costo_production_por_lote_production_statistics")
        self.label_tabla_costo_production_por_lote_production_statistics.setGeometry(QRect(430, 0, 297, 41))
        self.label_tabla_costo_production_por_lote_production_statistics.setFont(font2)
        self.label_grafico_lotes_producido_production_statistics = QLabel(self.tab_production_statistics)
        self.label_grafico_lotes_producido_production_statistics.setObjectName(u"label_grafico_lotes_producido_production_statistics")
        self.label_grafico_lotes_producido_production_statistics.setGeometry(QRect(20, 0, 211, 49))
        self.label_grafico_lotes_producido_production_statistics.setFont(font2)
        self.pushButton_ajustar_periodo_lotes_production_statistics = QPushButton(self.tab_production_statistics)
        self.pushButton_ajustar_periodo_lotes_production_statistics.setObjectName(u"pushButton_ajustar_periodo_lotes_production_statistics")
        self.pushButton_ajustar_periodo_lotes_production_statistics.setGeometry(QRect(300, 10, 91, 24))
        self.label_grafico_rendimiento_production_production_statistics = QLabel(self.tab_production_statistics)
        self.label_grafico_rendimiento_production_production_statistics.setObjectName(u"label_grafico_rendimiento_production_production_statistics")
        self.label_grafico_rendimiento_production_production_statistics.setGeometry(QRect(10, 290, 291, 49))
        self.label_grafico_rendimiento_production_production_statistics.setFont(font2)
        self.pushButton_ajustar_periodo_rendimiento_production_statistics = QPushButton(self.tab_production_statistics)
        self.pushButton_ajustar_periodo_rendimiento_production_statistics.setObjectName(u"pushButton_ajustar_periodo_rendimiento_production_statistics")
        self.pushButton_ajustar_periodo_rendimiento_production_statistics.setGeometry(QRect(308, 300, 91, 24))
        self.lineEdit_buscador_production_lotes_production_statistics = QLineEdit(self.tab_production_statistics)
        self.lineEdit_buscador_production_lotes_production_statistics.setObjectName(u"lineEdit_buscador_production_lotes_production_statistics")
        self.lineEdit_buscador_production_lotes_production_statistics.setGeometry(QRect(760, 10, 238, 21))
        self.pushButton_filtrar_production_por_lotes_production_statistics = QPushButton(self.tab_production_statistics)
        self.pushButton_filtrar_production_por_lotes_production_statistics.setObjectName(u"pushButton_filtrar_production_por_lotes_production_statistics")
        self.pushButton_filtrar_production_por_lotes_production_statistics.setGeometry(QRect(1010, 10, 81, 24))
        self.tabWidget_statistics.addTab(self.tab_production_statistics, "")
        self.main.addTab(self.tab_statistics, "")
        self.tab_invoicing = QWidget()
        self.tab_invoicing.setObjectName(u"tab_invoicing")
        self.frame_funciones_action_speed_invoicing = QFrame(self.tab_invoicing)
        self.frame_funciones_action_speed_invoicing.setObjectName(u"frame_funciones_action_speed_facturación")
        self.frame_funciones_action_speed_invoicing.setGeometry(QRect(180, 10, 731, 51))
        self.frame_funciones_action_speed_invoicing.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_funciones_action_speed_invoicing.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_crear_nueva_factura_invoicing = QPushButton(self.frame_funciones_action_speed_invoicing)
        self.pushButton_crear_nueva_factura_invoicing.setObjectName(u"pushButton_crear_nueva_factura_facturación")
        self.pushButton_crear_nueva_factura_invoicing.setGeometry(QRect(140, 10, 131, 31))
        self.pushButton_editar_factura_invoicing = QPushButton(self.frame_funciones_action_speed_invoicing)
        self.pushButton_editar_factura_invoicing.setObjectName(u"pushButton_editar_factura_facturación")
        self.pushButton_editar_factura_invoicing.setGeometry(QRect(290, 10, 121, 31))
        self.pushButton_eliminar_factura_invoicing = QPushButton(self.frame_funciones_action_speed_invoicing)
        self.pushButton_eliminar_factura_invoicing.setObjectName(u"pushButton_eliminar_factura")
        self.pushButton_eliminar_factura_invoicing.setGeometry(QRect(430, 10, 121, 31))
        self.pushButton_generar_pdf_imprimir_invoicing = QPushButton(self.frame_funciones_action_speed_invoicing)
        self.pushButton_generar_pdf_imprimir_invoicing.setObjectName(u"pushButton_generar_pdf_imprimir_facturación")
        self.pushButton_generar_pdf_imprimir_invoicing.setGeometry(QRect(570, 10, 141, 31))
        self.label_funciones_invoicing = QLabel(self.frame_funciones_action_speed_invoicing)
        self.label_funciones_invoicing.setObjectName(u"label_funciones_facturación")
        self.label_funciones_invoicing.setGeometry(QRect(10, 10, 121, 31))
        self.label_funciones_invoicing.setFont(font)
        self.tableView_invoicing = QTableView(self.tab_invoicing)
        self.tableView_invoicing.setObjectName(u"tableView_facturación")
        self.tableView_invoicing.setGeometry(QRect(10, 70, 1081, 541))
        self.main.addTab(self.tab_invoicing, "")
        self.tab_customers = QWidget()
        self.tab_customers.setObjectName(u"tab_customers")
        self.frame_clientes = QFrame(self.tab_customers)
        self.frame_clientes.setObjectName(u"frame_clientes")
        self.frame_clientes.setGeometry(QRect(300, 10, 501, 51))
        self.frame_clientes.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_clientes.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_agregar_cliente = QPushButton(self.frame_clientes)
        self.pushButton_agregar_cliente.setObjectName(u"pushButton_agregar_cliente")
        self.pushButton_agregar_cliente.setGeometry(QRect(130, 10, 101, 31))
        self.pushButton_editar_cliente = QPushButton(self.frame_clientes)
        self.pushButton_editar_cliente.setObjectName(u"pushButton_editar_cliente")
        self.pushButton_editar_cliente.setGeometry(QRect(250, 10, 101, 31))
        self.pushButton_eliminar_cliente = QPushButton(self.frame_clientes)
        self.pushButton_eliminar_cliente.setObjectName(u"pushButton_eliminar_cliente")
        self.pushButton_eliminar_cliente.setGeometry(QRect(370, 10, 111, 31))
        self.label_funciones_action_speed_clientes = QLabel(self.frame_clientes)
        self.label_funciones_action_speed_clientes.setObjectName(u"label_funciones_action_speed_clientes")
        self.label_funciones_action_speed_clientes.setGeometry(QRect(10, 10, 111, 31))
        self.label_funciones_action_speed_clientes.setFont(font)
        self.tableView_clientes = QTableView(self.tab_customers)
        self.tableView_clientes.setObjectName(u"tableView_clientes")
        self.tableView_clientes.setGeometry(QRect(10, 70, 1081, 541))
        self.main.addTab(self.tab_customers, "")
        self.frame_menu = QFrame(self.central_widget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setGeometry(QRect(-1, -1, 211, 671))
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget = QWidget(self.frame_menu)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 200, 191, 371))
        self.verticalLayout_menu = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_menu.setSpacing(0)
        self.verticalLayout_menu.setObjectName(u"verticalLayout_menu")
        self.verticalLayout_menu.setContentsMargins(0, 0, 0, 0)
        self.pushButton_home = QPushButton(self.verticalLayoutWidget)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setFont(font)

        self.verticalLayout_menu.addWidget(self.pushButton_home)

        self.pushButton_stock = QPushButton(self.verticalLayoutWidget)
        self.pushButton_stock.setObjectName(u"pushButton_stock")
        self.pushButton_stock.setFont(font)

        self.verticalLayout_menu.addWidget(self.pushButton_stock)

        self.pushButton_recipe = QPushButton(self.verticalLayoutWidget)
        self.pushButton_recipe.setObjectName(u"pushButton_recipe")
        self.pushButton_recipe.setFont(font)

        self.verticalLayout_menu.addWidget(self.pushButton_recipe)

        self.pushButton_traceability = QPushButton(self.verticalLayoutWidget)
        self.pushButton_traceability.setObjectName(u"pushButton_traceability")
        self.pushButton_traceability.setFont(font)

        self.verticalLayout_menu.addWidget(self.pushButton_traceability)

        self.pushButton_statistics = QPushButton(self.verticalLayoutWidget)
        self.pushButton_statistics.setObjectName(u"pushButton_statistics")
        self.pushButton_statistics.setFont(font)

        self.verticalLayout_menu.addWidget(self.pushButton_statistics)

        self.verticalLayout_statistics_menu = QVBoxLayout()
        self.verticalLayout_statistics_menu.setSpacing(0)
        self.verticalLayout_statistics_menu.setObjectName(u"verticalLayout_statistics_menu")
        self.verticalLayout_statistics_menu.setContentsMargins(40, -1, -1, -1)
        self.pushButton_statistics_sales = QPushButton(self.verticalLayoutWidget)
        self.pushButton_statistics_sales.setObjectName(u"pushButton_statistics_sales")
        self.pushButton_statistics_sales.setFont(font)

        self.verticalLayout_statistics_menu.addWidget(self.pushButton_statistics_sales)

        self.pushButton_statistics_production = QPushButton(self.verticalLayoutWidget)
        self.pushButton_statistics_production.setObjectName(u"pushButton_statistics_production")
        self.pushButton_statistics_production.setFont(font)

        self.verticalLayout_statistics_menu.addWidget(self.pushButton_statistics_production)

        self.pushButton_statistics_stock = QPushButton(self.verticalLayoutWidget)
        self.pushButton_statistics_stock.setObjectName(u"pushButton_statistics_stock")
        self.pushButton_statistics_stock.setFont(font)

        self.verticalLayout_statistics_menu.addWidget(self.pushButton_statistics_stock)


        self.verticalLayout_menu.addLayout(self.verticalLayout_statistics_menu)

        self.pushButton_invoicing = QPushButton(self.verticalLayoutWidget)
        self.pushButton_invoicing.setObjectName(u"pushButton_invoicing")
        self.pushButton_invoicing.setFont(font)

        self.verticalLayout_menu.addWidget(self.pushButton_invoicing)

        self.pushButton_customers = QPushButton(self.verticalLayoutWidget)
        self.pushButton_customers.setObjectName(u"pushButton_customers")
        self.pushButton_customers.setFont(font)

        self.verticalLayout_menu.addWidget(self.pushButton_customers)

        main_window.setCentralWidget(self.central_widget)

        self.retranslate_ui(main_window)

        self.main.setCurrentIndex(0)
        self.tabWidget_statistics.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_pedidos_pendientes_inicio.setText(QCoreApplication.translate("MainWindow", u"Pedidos Pendientes", None))
        self.label_tareas_pendientes_inicio.setText(QCoreApplication.translate("MainWindow", u"Tareas Pendientes", None))
        self.label_alertas_criticas_inicio.setText(QCoreApplication.translate("MainWindow", u"Alertas Críticas", None))
        self.label_resumen_ventas_inicio.setText(QCoreApplication.translate("MainWindow", u"Resumen de Ventas", None))
        self.pushButton_crear_tarea_inicio.setText(QCoreApplication.translate("MainWindow", u"Crear Tarea", None))
        self.main.setTabText(self.main.indexOf(self.tab_home), QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.pushButton_filtrar_materia_prima.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolButton_filtrado_avanzado_materia_prima.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_materia_prima.setText(QCoreApplication.translate("MainWindow", u"Materia Prima", None))
        self.pushButton_filtrar_productos_terminados.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_productos_terminados.setText(QCoreApplication.translate("MainWindow", u"Productos Terminados", None))
        self.pushButton_ajustar_stock_inventario.setText(QCoreApplication.translate("MainWindow", u"Ajustar Inventario", None))
        self.pushButton_registrar_entrada_inventario.setText(QCoreApplication.translate("MainWindow", u"Registrar Entrada", None))
        self.label_funciones_action_speed_inventario.setText(QCoreApplication.translate("MainWindow", u"Funciones: ", None))
        self.pushButton_registrar_salida_inventario.setText(QCoreApplication.translate("MainWindow", u"Registrar Salida", None))
        self.main.setTabText(self.main.indexOf(self.tab_stock), QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.pushButton_actualizar_formula.setText(QCoreApplication.translate("MainWindow", u"Actualizar Fórmula/Receta", None))
        self.label_funciones_action_speed_formula.setText(QCoreApplication.translate("MainWindow", u"Funciones:", None))
        self.pushButton_eliminar_formula.setText(QCoreApplication.translate("MainWindow", u"Eliminar Fórmula/Receta", None))
        self.pushButton_agregar_formula.setText(QCoreApplication.translate("MainWindow", u"Agregar Fórmula/Receta", None))
        self.label_formula_recetas.setText(QCoreApplication.translate("MainWindow", u"Fórmulas/Recetas", None))
        self.pushButton_filtrar_formulas.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolButton_filtrado_avanzado_formulas.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.main.setTabText(self.main.indexOf(self.tab_recipe), QCoreApplication.translate("MainWindow", u"Formula", None))
        self.label_trazabilidad.setText(QCoreApplication.translate("MainWindow", u"Filtros:", None))
        self.lineEdit_trazabilidad.setText("")
        self.pushButton_filtrar_trazabilidad.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.radioButton_mostrar_productos_terminados_trazabilidad.setText(QCoreApplication.translate("MainWindow", u"Mostrar Productos Terminados", None))
        self.radioButton_periodo_tiempo_trazabilidad.setText(QCoreApplication.translate("MainWindow", u"Periodo de Tiempo", None))
        self.groupBox_periodo_tiempo_trazabilidad.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_de_periodo_tiempo_trazabilidad.setText(QCoreApplication.translate("MainWindow", u"De:", None))
        self.label_a_periodo_tiempo_trazabilidad.setText(QCoreApplication.translate("MainWindow", u"a:", None))
        self.pushButton_filtrar_periodo_tiempo_trazabilidad.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.radioButton_estado_lote_trazabilidad.setText(QCoreApplication.translate("MainWindow", u"Estado del Lote", None))
        self.groupBox_estado_lote_trazabilidad.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_filtrar_estado_lote_trazabilidad.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.pushButton_generar_informe_trazabilidad.setText(QCoreApplication.translate("MainWindow", u"Generar Informe", None))
        self.label_trazabilidad_2.setText(QCoreApplication.translate("MainWindow", u"Trazabilidad", None))
        self.main.setTabText(self.main.indexOf(self.tab_traceability), QCoreApplication.translate("MainWindow", u"Trazabilidad", None))
        self.label_tabla_clientes_mas_importantes_sales_statistics.setText(QCoreApplication.translate("MainWindow", u"Tabla de Clientes m\u00e1s Importantes", None))
        self.pushButton_ajustar_periodo_productos_sales_statistics.setText(QCoreApplication.translate("MainWindow", u"Ajustar Periodo", None))
        self.label_grafico_ventas_por_productos_sales_statistics.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Ventas por Productos", None))
        self.pushButton_filtrar_clientes_sales_statistics.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.pushButton_ajustar_periodo_periodo_sales_statistics.setText(QCoreApplication.translate("MainWindow", u"Ajustar Periodo", None))
        self.label_grafico_ventas_por_periodo_sales_statistics.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Ventas por Periodo", None))
        self.tabWidget_statistics.setTabText(self.tabWidget_statistics.indexOf(self.tab_sales_statistics), QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.label_tabla_productos_bajo_movimiento_stock_statistics.setText(QCoreApplication.translate("MainWindow", u"Tabla de Productos de Bajo Movimiento", None))
        self.pushButton_ajustar_periodo_pronostico_stock_statistics.setText(QCoreApplication.translate("MainWindow", u"Ajustar Periodo", None))
        self.label_grafico_pronostico_stock_stock_statistics.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Pronóstico de Stock", None))
        self.pushButton_ajustar_periodo_consumo_stock_statistics.setText(QCoreApplication.translate("MainWindow", u"Ajustar Periodo", None))
        self.label_grafico_consumo_materia_prima_stock_statistics.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Consumo de Materia Prima", None))
        self.pushButton_filtrar_productos_stock_statistics.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.tabWidget_statistics.setTabText(self.tabWidget_statistics.indexOf(self.tab_stock_statistics), QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.label_tabla_costo_production_por_lote_production_statistics.setText(QCoreApplication.translate("MainWindow", u"Tabla de Costos de Producción por Lote", None))
        self.label_grafico_lotes_producido_production_statistics.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Lotes Producidos", None))
        self.pushButton_ajustar_periodo_lotes_production_statistics.setText(QCoreApplication.translate("MainWindow", u"Ajustar Periodo", None))
        self.label_grafico_rendimiento_production_production_statistics.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Rendimiento de Producción", None))
        self.pushButton_ajustar_periodo_rendimiento_production_statistics.setText(QCoreApplication.translate("MainWindow", u"Ajustar Periodo", None))
        self.pushButton_filtrar_production_por_lotes_production_statistics.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.tabWidget_statistics.setTabText(self.tabWidget_statistics.indexOf(self.tab_production_statistics), QCoreApplication.translate("MainWindow", u"Producción", None))
        self.main.setTabText(self.main.indexOf(self.tab_statistics), QCoreApplication.translate("MainWindow", u"Estadísticas", None))
        self.pushButton_crear_nueva_factura_invoicing.setText(QCoreApplication.translate("MainWindow", u"Crear Nueva Factura", None))
        self.pushButton_editar_factura_invoicing.setText(QCoreApplication.translate("MainWindow", u"Editar Factura", None))
        self.pushButton_eliminar_factura_invoicing.setText(QCoreApplication.translate("MainWindow", u"Eliminar Factura", None))
        self.pushButton_generar_pdf_imprimir_invoicing.setText(QCoreApplication.translate("MainWindow", u"Generar PDF/Imprimir", None))
        self.label_funciones_invoicing.setText(QCoreApplication.translate("MainWindow", u"Funciones:", None))
        self.main.setTabText(self.main.indexOf(self.tab_invoicing), QCoreApplication.translate("MainWindow", u"Facturación", None))
        self.pushButton_agregar_cliente.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Cliente", None))
        self.pushButton_editar_cliente.setText(QCoreApplication.translate("MainWindow", u"Editar Cliente", None))
        self.pushButton_eliminar_cliente.setText(QCoreApplication.translate("MainWindow", u"Eliminar Cliente", None))
        self.label_funciones_action_speed_clientes.setText(QCoreApplication.translate("MainWindow", u"Funciones:", None))
        self.main.setTabText(self.main.indexOf(self.tab_customers), QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.pushButton_home.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.pushButton_stock.setText(QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.pushButton_recipe.setText(QCoreApplication.translate("MainWindow", u"Fórmula", None))
        self.pushButton_traceability.setText(QCoreApplication.translate("MainWindow", u"Trazabilidad", None))
        self.pushButton_statistics.setText(QCoreApplication.translate("MainWindow", u"Estadísticas", None))
        self.pushButton_statistics_sales.setText(QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.pushButton_statistics_production.setText(QCoreApplication.translate("MainWindow", u"Producción", None))
        self.pushButton_statistics_stock.setText(QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.pushButton_invoicing.setText(QCoreApplication.translate("MainWindow", u"Facturación", None))
        self.pushButton_customers.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
    # retranslateUi

