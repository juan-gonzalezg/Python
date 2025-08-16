from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QDateEdit, QFormLayout, QHBoxLayout, QLabel, QPushButton, QTableView, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_crear_factura = None
        self.label_cliente_crear_factura = None
        self.label_fecha = None
        self.tableView_productos_materia_prima_crear_factura = None
        self.dateEdit_fecha_crear_factura = None
        self.comboBox_clientes_crear_factura = None
        self.label_crear_factura = None
        self.horizontalLayout_funciones_productos_adquirir_crear_factura = None
        self.pushButton_agregar_producto_crear_factura = None
        self.pushButton_eliminar_producto_crear_factura = None
        self.label_productos_materia_prima_adquirir_crear_factura = None
        self.horizontalLayout_funciones_definitivas_crear_factura = None
        self.pushButton_crear_factura = None
        self.pushButton_cancelar_crear_factura = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(480, 300)
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 481, 301))
        self.formLayout_crear_factura = QFormLayout(self.formLayoutWidget)
        self.formLayout_crear_factura.setObjectName(u"formLayout_crear_factura")
        self.formLayout_crear_factura.setContentsMargins(10, 10, 10, 10)
        self.label_cliente_crear_factura = QLabel(self.formLayoutWidget)
        self.label_cliente_crear_factura.setObjectName(u"label_cliente_crear_factura")

        self.formLayout_crear_factura.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_cliente_crear_factura)

        self.label_fecha = QLabel(self.formLayoutWidget)
        self.label_fecha.setObjectName(u"label_fecha")

        self.formLayout_crear_factura.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_fecha)

        self.tableView_productos_materia_prima_crear_factura = QTableView(self.formLayoutWidget)
        self.tableView_productos_materia_prima_crear_factura.setObjectName(u"tableView_productos_materia_prima_crear_factura")

        self.formLayout_crear_factura.setWidget(4, QFormLayout.ItemRole.FieldRole, self.tableView_productos_materia_prima_crear_factura)

        self.dateEdit_fecha_crear_factura = QDateEdit(self.formLayoutWidget)
        self.dateEdit_fecha_crear_factura.setObjectName(u"dateEdit_fecha_crear_factura")

        self.formLayout_crear_factura.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateEdit_fecha_crear_factura)

        self.comboBox_clientes_crear_factura = QComboBox(self.formLayoutWidget)
        self.comboBox_clientes_crear_factura.setObjectName(u"comboBox_clientes_crear_factura")

        self.formLayout_crear_factura.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_clientes_crear_factura)

        self.label_crear_factura = QLabel(self.formLayoutWidget)
        self.label_crear_factura.setObjectName(u"label_crear_factura")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_crear_factura.setFont(font)
        self.label_crear_factura.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_crear_factura.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_crear_factura)

        self.horizontalLayout_funciones_productos_adquirir_crear_factura = QHBoxLayout()
        self.horizontalLayout_funciones_productos_adquirir_crear_factura.setSpacing(20)
        self.horizontalLayout_funciones_productos_adquirir_crear_factura.setObjectName(u"horizontalLayout_funciones_productos_adquirir_crear_factura")
        self.horizontalLayout_funciones_productos_adquirir_crear_factura.setContentsMargins(30, 5, 30, -1)
        self.pushButton_agregar_producto_crear_factura = QPushButton(self.formLayoutWidget)
        self.pushButton_agregar_producto_crear_factura.setObjectName(u"pushButton_agregar_producto_crear_factura")

        self.horizontalLayout_funciones_productos_adquirir_crear_factura.addWidget(self.pushButton_agregar_producto_crear_factura)

        self.pushButton_eliminar_producto_crear_factura = QPushButton(self.formLayoutWidget)
        self.pushButton_eliminar_producto_crear_factura.setObjectName(u"pushButton_eliminar_producto_crear_factura")

        self.horizontalLayout_funciones_productos_adquirir_crear_factura.addWidget(self.pushButton_eliminar_producto_crear_factura)


        self.formLayout_crear_factura.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_funciones_productos_adquirir_crear_factura)

        self.label_productos_materia_prima_adquirir_crear_factura = QLabel(self.formLayoutWidget)
        self.label_productos_materia_prima_adquirir_crear_factura.setObjectName(u"label_productos_materia_prima_adquirir_crear_factura")

        self.formLayout_crear_factura.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_productos_materia_prima_adquirir_crear_factura)

        self.horizontalLayout_funciones_definitivas_crear_factura = QHBoxLayout()
        self.horizontalLayout_funciones_definitivas_crear_factura.setSpacing(40)
        self.horizontalLayout_funciones_definitivas_crear_factura.setObjectName(u"horizontalLayout_funciones_definitivas_crear_factura")
        self.horizontalLayout_funciones_definitivas_crear_factura.setContentsMargins(60, -1, 60, -1)
        self.pushButton_crear_factura = QPushButton(self.formLayoutWidget)
        self.pushButton_crear_factura.setObjectName(u"pushButton_crear_factura")

        self.horizontalLayout_funciones_definitivas_crear_factura.addWidget(self.pushButton_crear_factura)

        self.pushButton_cancelar_crear_factura = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_crear_factura.setObjectName(u"pushButton_cancelar_crear_factura")

        self.horizontalLayout_funciones_definitivas_crear_factura.addWidget(self.pushButton_cancelar_crear_factura)


        self.formLayout_crear_factura.setLayout(5, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_funciones_definitivas_crear_factura)


        self.retranslate_ui(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_cliente_crear_factura.setText(QCoreApplication.translate("Dialog", u"Cliente:", None))
        self.label_fecha.setText(QCoreApplication.translate("Dialog", u"Fecha:", None))
        self.label_crear_factura.setText(QCoreApplication.translate("Dialog", u"Crear Factura", None))
        self.pushButton_agregar_producto_crear_factura.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
        self.pushButton_eliminar_producto_crear_factura.setText(QCoreApplication.translate("Dialog", u"Eliminar", None))
        self.label_productos_materia_prima_adquirir_crear_factura.setText(QCoreApplication.translate("Dialog", u"Productos o Materia\n"
"Prima a Adquirir:", None))
        self.pushButton_crear_factura.setText(QCoreApplication.translate("Dialog", u"Crear", None))
        self.pushButton_cancelar_crear_factura.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

