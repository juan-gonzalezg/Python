from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QDateEdit, QFormLayout, QHBoxLayout, QLabel, QPushButton, QTableView, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_editar_factura = None
        self.label_editar_factura = None
        self.label_selection_factura_editar_factura = None
        self.comboBox_selection_de_factura_editar_factura = None
        self.label_fecha_editar_factura = None
        self.dateEdit_fecha_editar_factura = None
        self.horizontalLayout_funciones_editar_factura = None
        self.pushButton_agregar_producto_editar_factura = None
        self.pushButton_editar_producto_editar_factura = None
        self.pushButton_eliminar_producto_editar_factura = None
        self.tableView_productos_editar_factura = None
        self.horizontalLayout_funciones_definitivas_editar_factura = None
        self.pushButton_guardar_editar_factura = None
        self.pushButton_cancelar_editar_factura = None
        self.label_productos_materia_prima_adquirir_editar_factura = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(500, 300)
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 501, 301))
        self.formLayout_editar_factura = QFormLayout(self.formLayoutWidget)
        self.formLayout_editar_factura.setObjectName(u"formLayout_editar_factura")
        self.formLayout_editar_factura.setContentsMargins(10, 10, 10, 10)
        self.label_editar_factura = QLabel(self.formLayoutWidget)
        self.label_editar_factura.setObjectName(u"label_editar_factura")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_editar_factura.setFont(font)

        self.formLayout_editar_factura.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_editar_factura)

        self.label_selection_factura_editar_factura = QLabel(self.formLayoutWidget)
        self.label_selection_factura_editar_factura.setObjectName(u"label_selection_factura_editar_factura")

        self.formLayout_editar_factura.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_selection_factura_editar_factura)

        self.comboBox_selection_de_factura_editar_factura = QComboBox(self.formLayoutWidget)
        self.comboBox_selection_de_factura_editar_factura.setObjectName(u"comboBox_selection_de_factura_editar_factura")

        self.formLayout_editar_factura.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_selection_de_factura_editar_factura)

        self.label_fecha_editar_factura = QLabel(self.formLayoutWidget)
        self.label_fecha_editar_factura.setObjectName(u"label_fecha_editar_factura")

        self.formLayout_editar_factura.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_fecha_editar_factura)

        self.dateEdit_fecha_editar_factura = QDateEdit(self.formLayoutWidget)
        self.dateEdit_fecha_editar_factura.setObjectName(u"dateEdit_fecha_editar_factura")

        self.formLayout_editar_factura.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateEdit_fecha_editar_factura)

        self.horizontalLayout_funciones_editar_factura = QHBoxLayout()
        self.horizontalLayout_funciones_editar_factura.setObjectName(u"horizontalLayout_funciones_editar_factura")
        self.pushButton_agregar_producto_editar_factura = QPushButton(self.formLayoutWidget)
        self.pushButton_agregar_producto_editar_factura.setObjectName(u"pushButton_agregar_producto_editar_factura")

        self.horizontalLayout_funciones_editar_factura.addWidget(self.pushButton_agregar_producto_editar_factura)

        self.pushButton_editar_producto_editar_factura = QPushButton(self.formLayoutWidget)
        self.pushButton_editar_producto_editar_factura.setObjectName(u"pushButton_editar_producto_editar_factura")

        self.horizontalLayout_funciones_editar_factura.addWidget(self.pushButton_editar_producto_editar_factura)

        self.pushButton_eliminar_producto_editar_factura = QPushButton(self.formLayoutWidget)
        self.pushButton_eliminar_producto_editar_factura.setObjectName(u"pushButton_eliminar_producto_editar_factura")

        self.horizontalLayout_funciones_editar_factura.addWidget(self.pushButton_eliminar_producto_editar_factura)


        self.formLayout_editar_factura.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_funciones_editar_factura)

        self.tableView_productos_editar_factura = QTableView(self.formLayoutWidget)
        self.tableView_productos_editar_factura.setObjectName(u"tableView_productos_editar_factura")

        self.formLayout_editar_factura.setWidget(4, QFormLayout.ItemRole.FieldRole, self.tableView_productos_editar_factura)

        self.horizontalLayout_funciones_definitivas_editar_factura = QHBoxLayout()
        self.horizontalLayout_funciones_definitivas_editar_factura.setSpacing(40)
        self.horizontalLayout_funciones_definitivas_editar_factura.setObjectName(u"horizontalLayout_funciones_definitivas_editar_factura")
        self.horizontalLayout_funciones_definitivas_editar_factura.setContentsMargins(50, -1, 50, -1)
        self.pushButton_guardar_editar_factura = QPushButton(self.formLayoutWidget)
        self.pushButton_guardar_editar_factura.setObjectName(u"pushButton_guardar_editar_factura")

        self.horizontalLayout_funciones_definitivas_editar_factura.addWidget(self.pushButton_guardar_editar_factura)

        self.pushButton_cancelar_editar_factura = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_editar_factura.setObjectName(u"pushButton_cancelar_editar_factura")

        self.horizontalLayout_funciones_definitivas_editar_factura.addWidget(self.pushButton_cancelar_editar_factura)


        self.formLayout_editar_factura.setLayout(5, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_funciones_definitivas_editar_factura)

        self.label_productos_materia_prima_adquirir_editar_factura = QLabel(self.formLayoutWidget)
        self.label_productos_materia_prima_adquirir_editar_factura.setObjectName(u"label_productos_materia_prima_adquirir_editar_factura")

        self.formLayout_editar_factura.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_productos_materia_prima_adquirir_editar_factura)


        self.retranslate_ui(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_editar_factura.setText(QCoreApplication.translate("Dialog", u"Editar Factura", None))
        self.label_selection_factura_editar_factura.setText(QCoreApplication.translate("Dialog", u"selection la Factura:", None))
        self.label_fecha_editar_factura.setText(QCoreApplication.translate("Dialog", u"Fecha:", None))
        self.pushButton_agregar_producto_editar_factura.setText(QCoreApplication.translate("Dialog", u"Agregar Producto", None))
        self.pushButton_editar_producto_editar_factura.setText(QCoreApplication.translate("Dialog", u"Editar Producto", None))
        self.pushButton_eliminar_producto_editar_factura.setText(QCoreApplication.translate("Dialog", u"Eliminar Producto", None))
        self.pushButton_guardar_editar_factura.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.pushButton_cancelar_editar_factura.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label_productos_materia_prima_adquirir_editar_factura.setText(QCoreApplication.translate("Dialog", u"Productos o Materia\n"
"Prima a Adquirir:", None))
    # retranslateUi

