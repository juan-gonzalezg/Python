from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QDateEdit, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QSpinBox, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_registrar_entrada_inventario = None
        self.label_registrar_entrada_inventario = None
        self.label_nombre_registrar_entrada_inventario = None
        self.lineEdit_nombre_producto_registrar_entrada_inventario = None
        self.label_cantidad_registrar_entrada_inventario = None
        self.spinBox_cantidad_producto_registrar_entrada_inventario = None
        self.label_fecha_registrar_entrada_inventario = None
        self.dateEdit_fecha_registrar_entrada_inventario = None
        self.horizontalLayout_acciones_definitivas_registrar_entrada_inventario = None
        self.pushButton_registrar_entrada_inventario = None
        self.pushButton_cancelar_registrar_entrada_inventario = None
        self.horizontalLayout_tipo_inventario_registrar_entrada_inventario = None
        self.radioButton_materia_prima_registrar_entrada_inventario = None
        self.radioButton_producto_terminado_registrar_entrada_inventario = None
        self.label_seleccione_registrar_entrada_inventario = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(393, 191)
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(3, 0, 391, 191))
        self.formLayout_registrar_entrada_inventario = QFormLayout(self.formLayoutWidget)
        self.formLayout_registrar_entrada_inventario.setObjectName(u"formLayout_registrar_entrada_inventario")
        self.formLayout_registrar_entrada_inventario.setContentsMargins(10, 10, 10, 10)
        self.label_registrar_entrada_inventario = QLabel(self.formLayoutWidget)
        self.label_registrar_entrada_inventario.setObjectName(u"label_registrar_entrada_inventario")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_registrar_entrada_inventario.setFont(font)

        self.formLayout_registrar_entrada_inventario.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_registrar_entrada_inventario)

        self.label_nombre_registrar_entrada_inventario = QLabel(self.formLayoutWidget)
        self.label_nombre_registrar_entrada_inventario.setObjectName(u"label_nombre_registrar_entrada_inventario")

        self.formLayout_registrar_entrada_inventario.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_nombre_registrar_entrada_inventario)

        self.lineEdit_nombre_producto_registrar_entrada_inventario = QLineEdit(self.formLayoutWidget)
        self.lineEdit_nombre_producto_registrar_entrada_inventario.setObjectName(u"lineEdit_nombre_producto_registrar_entrada_inventario")

        self.formLayout_registrar_entrada_inventario.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_nombre_producto_registrar_entrada_inventario)

        self.label_cantidad_registrar_entrada_inventario = QLabel(self.formLayoutWidget)
        self.label_cantidad_registrar_entrada_inventario.setObjectName(u"label_cantidad_registrar_entrada_inventario")

        self.formLayout_registrar_entrada_inventario.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_cantidad_registrar_entrada_inventario)

        self.spinBox_cantidad_producto_registrar_entrada_inventario = QSpinBox(self.formLayoutWidget)
        self.spinBox_cantidad_producto_registrar_entrada_inventario.setObjectName(u"spinBox_cantidad_producto_registrar_entrada_inventario")

        self.formLayout_registrar_entrada_inventario.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinBox_cantidad_producto_registrar_entrada_inventario)

        self.label_fecha_registrar_entrada_inventario = QLabel(self.formLayoutWidget)
        self.label_fecha_registrar_entrada_inventario.setObjectName(u"label_fecha_registrar_entrada_inventario")

        self.formLayout_registrar_entrada_inventario.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_fecha_registrar_entrada_inventario)

        self.dateEdit_fecha_registrar_entrada_inventario = QDateEdit(self.formLayoutWidget)
        self.dateEdit_fecha_registrar_entrada_inventario.setObjectName(u"dateEdit_fecha_registrar_entrada_inventario")

        self.formLayout_registrar_entrada_inventario.setWidget(4, QFormLayout.ItemRole.FieldRole, self.dateEdit_fecha_registrar_entrada_inventario)

        self.horizontalLayout_acciones_definitivas_registrar_entrada_inventario = QHBoxLayout()
        self.horizontalLayout_acciones_definitivas_registrar_entrada_inventario.setObjectName(u"horizontalLayout_acciones_definitivas_registrar_entrada_inventario")
        self.pushButton_registrar_entrada_inventario = QPushButton(self.formLayoutWidget)
        self.pushButton_registrar_entrada_inventario.setObjectName(u"pushButton_registrar_entrada_inventario")

        self.horizontalLayout_acciones_definitivas_registrar_entrada_inventario.addWidget(self.pushButton_registrar_entrada_inventario)

        self.pushButton_cancelar_registrar_entrada_inventario = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_registrar_entrada_inventario.setObjectName(u"pushButton_cancelar_registrar_entrada_inventario")

        self.horizontalLayout_acciones_definitivas_registrar_entrada_inventario.addWidget(self.pushButton_cancelar_registrar_entrada_inventario)


        self.formLayout_registrar_entrada_inventario.setLayout(5, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_acciones_definitivas_registrar_entrada_inventario)

        self.horizontalLayout_tipo_inventario_registrar_entrada_inventario = QHBoxLayout()
        self.horizontalLayout_tipo_inventario_registrar_entrada_inventario.setObjectName(u"horizontalLayout_tipo_inventario_registrar_entrada_inventario")
        self.radioButton_materia_prima_registrar_entrada_inventario = QRadioButton(self.formLayoutWidget)
        self.radioButton_materia_prima_registrar_entrada_inventario.setObjectName(u"radioButton_materia_prima_registrar_entrada_inventario")

        self.horizontalLayout_tipo_inventario_registrar_entrada_inventario.addWidget(self.radioButton_materia_prima_registrar_entrada_inventario)

        self.radioButton_producto_terminado_registrar_entrada_inventario = QRadioButton(self.formLayoutWidget)
        self.radioButton_producto_terminado_registrar_entrada_inventario.setObjectName(u"radioButton_producto_terminado_registrar_entrada_inventario")

        self.horizontalLayout_tipo_inventario_registrar_entrada_inventario.addWidget(self.radioButton_producto_terminado_registrar_entrada_inventario)


        self.formLayout_registrar_entrada_inventario.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_tipo_inventario_registrar_entrada_inventario)

        self.label_seleccione_registrar_entrada_inventario = QLabel(self.formLayoutWidget)
        self.label_seleccione_registrar_entrada_inventario.setObjectName(u"label_seleccione_registrar_entrada_inventario")

        self.formLayout_registrar_entrada_inventario.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_seleccione_registrar_entrada_inventario)


        self.retranslate_ui(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_registrar_entrada_inventario.setText(QCoreApplication.translate("Dialog", u"Registrar entrada de Inventario", None))
        self.label_nombre_registrar_entrada_inventario.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.label_cantidad_registrar_entrada_inventario.setText(QCoreApplication.translate("Dialog", u"Cantidad:", None))
        self.label_fecha_registrar_entrada_inventario.setText(QCoreApplication.translate("Dialog", u"Fecha:", None))
        self.pushButton_registrar_entrada_inventario.setText(QCoreApplication.translate("Dialog", u"Registrar", None))
        self.pushButton_cancelar_registrar_entrada_inventario.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.radioButton_materia_prima_registrar_entrada_inventario.setText(QCoreApplication.translate("Dialog", u"Materia Prima", None))
        self.radioButton_producto_terminado_registrar_entrada_inventario.setText(QCoreApplication.translate("Dialog", u"Producto Terminado", None))
        self.label_seleccione_registrar_entrada_inventario.setText(QCoreApplication.translate("Dialog", u"Seleccione:", None))
    # retranslateUi

