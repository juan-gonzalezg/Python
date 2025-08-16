from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QFormLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QSpinBox, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_registrar_salida_inventario = None
        self.label_registrar_salida_inventario = None
        self.label_producto_registrar_salida_inventario = None
        self.label_cantidad_registrar_salida_inventario = None
        self.spinBox_cantidad_registrar_salida_inventario = None
        self.horizontalLayout_acciones_definitivas_registrar_salida_inventario = None
        self.pushButton_registrar_salida_inventario = None
        self.pushButton_cancelar_registrar_salida_inventario = None
        self.comboBox_productos_registrar_salida_inventario = None
        self.horizontalLayout_tipo_producto_registrar_salida_inventario = None
        self.radioButton_materia_prima_registrar_salida_inventario = None
        self.radioButton_producto_terminado_registrar_salida_inventario = None
        self.label_seleccione_registrar_salida_inventario = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(395, 165)
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(3, 4, 391, 161))
        self.formLayout_registrar_salida_inventario = QFormLayout(self.formLayoutWidget)
        self.formLayout_registrar_salida_inventario.setObjectName(u"formLayout_registrar_salida_inventario")
        self.formLayout_registrar_salida_inventario.setContentsMargins(5, 5, 10, 10)
        self.label_registrar_salida_inventario = QLabel(self.formLayoutWidget)
        self.label_registrar_salida_inventario.setObjectName(u"label_registrar_salida_inventario")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_registrar_salida_inventario.setFont(font)

        self.formLayout_registrar_salida_inventario.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_registrar_salida_inventario)

        self.label_producto_registrar_salida_inventario = QLabel(self.formLayoutWidget)
        self.label_producto_registrar_salida_inventario.setObjectName(u"label_producto_registrar_salida_inventario")

        self.formLayout_registrar_salida_inventario.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_producto_registrar_salida_inventario)

        self.label_cantidad_registrar_salida_inventario = QLabel(self.formLayoutWidget)
        self.label_cantidad_registrar_salida_inventario.setObjectName(u"label_cantidad_registrar_salida_inventario")

        self.formLayout_registrar_salida_inventario.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_cantidad_registrar_salida_inventario)

        self.spinBox_cantidad_registrar_salida_inventario = QSpinBox(self.formLayoutWidget)
        self.spinBox_cantidad_registrar_salida_inventario.setObjectName(u"spinBox_cantidad_registrar_salida_inventario")

        self.formLayout_registrar_salida_inventario.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinBox_cantidad_registrar_salida_inventario)

        self.horizontalLayout_acciones_definitivas_registrar_salida_inventario = QHBoxLayout()
        self.horizontalLayout_acciones_definitivas_registrar_salida_inventario.setObjectName(u"horizontalLayout_acciones_definitivas_registrar_salida_inventario")
        self.pushButton_registrar_salida_inventario = QPushButton(self.formLayoutWidget)
        self.pushButton_registrar_salida_inventario.setObjectName(u"pushButton_registrar_salida_inventario")

        self.horizontalLayout_acciones_definitivas_registrar_salida_inventario.addWidget(self.pushButton_registrar_salida_inventario)

        self.pushButton_cancelar_registrar_salida_inventario = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_registrar_salida_inventario.setObjectName(u"pushButton_cancelar_registrar_salida_inventario")

        self.horizontalLayout_acciones_definitivas_registrar_salida_inventario.addWidget(self.pushButton_cancelar_registrar_salida_inventario)


        self.formLayout_registrar_salida_inventario.setLayout(4, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_acciones_definitivas_registrar_salida_inventario)

        self.comboBox_productos_registrar_salida_inventario = QComboBox(self.formLayoutWidget)
        self.comboBox_productos_registrar_salida_inventario.setObjectName(u"comboBox_productos_registrar_salida_inventario")

        self.formLayout_registrar_salida_inventario.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox_productos_registrar_salida_inventario)

        self.horizontalLayout_tipo_producto_registrar_salida_inventario = QHBoxLayout()
        self.horizontalLayout_tipo_producto_registrar_salida_inventario.setObjectName(u"horizontalLayout_tipo_producto_registrar_salida_inventario")
        self.radioButton_materia_prima_registrar_salida_inventario = QRadioButton(self.formLayoutWidget)
        self.radioButton_materia_prima_registrar_salida_inventario.setObjectName(u"radioButton_materia_prima_registrar_salida_inventario")

        self.horizontalLayout_tipo_producto_registrar_salida_inventario.addWidget(self.radioButton_materia_prima_registrar_salida_inventario)

        self.radioButton_producto_terminado_registrar_salida_inventario = QRadioButton(self.formLayoutWidget)
        self.radioButton_producto_terminado_registrar_salida_inventario.setObjectName(u"radioButton_producto_terminado_registrar_salida_inventario")

        self.horizontalLayout_tipo_producto_registrar_salida_inventario.addWidget(self.radioButton_producto_terminado_registrar_salida_inventario)


        self.formLayout_registrar_salida_inventario.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_tipo_producto_registrar_salida_inventario)

        self.label_seleccione_registrar_salida_inventario = QLabel(self.formLayoutWidget)
        self.label_seleccione_registrar_salida_inventario.setObjectName(u"label_seleccione_registrar_salida_inventario")

        self.formLayout_registrar_salida_inventario.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_seleccione_registrar_salida_inventario)


        self.retranslate_ui(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_registrar_salida_inventario.setText(QCoreApplication.translate("Dialog", u"Registrar Salida de Inventario", None))
        self.label_producto_registrar_salida_inventario.setText(QCoreApplication.translate("Dialog", u"Producto:", None))
        self.label_cantidad_registrar_salida_inventario.setText(QCoreApplication.translate("Dialog", u"Cantidad:", None))
        self.pushButton_registrar_salida_inventario.setText(QCoreApplication.translate("Dialog", u"Registrar", None))
        self.pushButton_cancelar_registrar_salida_inventario.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.radioButton_materia_prima_registrar_salida_inventario.setText(QCoreApplication.translate("Dialog", u"Materia Prima", None))
        self.radioButton_producto_terminado_registrar_salida_inventario.setText(QCoreApplication.translate("Dialog", u"Producto Terminado", None))
        self.label_seleccione_registrar_salida_inventario.setText(QCoreApplication.translate("Dialog", u"Seleccione:", None))
    # retranslateUi

