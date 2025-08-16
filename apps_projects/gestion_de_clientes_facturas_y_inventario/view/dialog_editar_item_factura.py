from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QFormLayout, QHBoxLayout, QLabel, QPushButton, QSpinBox, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_editar_item_factura = None
        self.label_editar_item_factura = None
        self.label_item_editar_item_factura = None
        self.comboBox_items_editar_item_factura = None
        self.label_cantidad_items_editar_item_factura = None
        self.spinBox_cantidad_item_editar_item_factura = None
        self.horizontalLayout_accione_editar_item_factura = None
        self.pushButton_editar_item_factura = None
        self.pushButton_cancelar_editar_item_factura = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(400, 140)
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 401, 142))
        self.formLayout_editar_item_factura = QFormLayout(self.formLayoutWidget)
        self.formLayout_editar_item_factura.setObjectName(u"formLayout_editar_item_factura")
        self.formLayout_editar_item_factura.setContentsMargins(10, 15, 10, 10)
        self.label_editar_item_factura = QLabel(self.formLayoutWidget)
        self.label_editar_item_factura.setObjectName(u"label_editar_item_factura")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_editar_item_factura.setFont(font)

        self.formLayout_editar_item_factura.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_editar_item_factura)

        self.label_item_editar_item_factura = QLabel(self.formLayoutWidget)
        self.label_item_editar_item_factura.setObjectName(u"label_item_editar_item_factura")

        self.formLayout_editar_item_factura.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_item_editar_item_factura)

        self.comboBox_items_editar_item_factura = QComboBox(self.formLayoutWidget)
        self.comboBox_items_editar_item_factura.setObjectName(u"comboBox_items_editar_item_factura")

        self.formLayout_editar_item_factura.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_items_editar_item_factura)

        self.label_cantidad_items_editar_item_factura = QLabel(self.formLayoutWidget)
        self.label_cantidad_items_editar_item_factura.setObjectName(u"label_cantidad_items_editar_item_factura")

        self.formLayout_editar_item_factura.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_cantidad_items_editar_item_factura)

        self.spinBox_cantidad_item_editar_item_factura = QSpinBox(self.formLayoutWidget)
        self.spinBox_cantidad_item_editar_item_factura.setObjectName(u"spinBox_cantidad_item_editar_item_factura")

        self.formLayout_editar_item_factura.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinBox_cantidad_item_editar_item_factura)

        self.horizontalLayout_accione_editar_item_factura = QHBoxLayout()
        self.horizontalLayout_accione_editar_item_factura.setSpacing(40)
        self.horizontalLayout_accione_editar_item_factura.setObjectName(u"horizontalLayout_accione_editar_item_factura")
        self.horizontalLayout_accione_editar_item_factura.setContentsMargins(30, 5, 30, 0)
        self.pushButton_editar_item_factura = QPushButton(self.formLayoutWidget)
        self.pushButton_editar_item_factura.setObjectName(u"pushButton_editar_item_factura")

        self.horizontalLayout_accione_editar_item_factura.addWidget(self.pushButton_editar_item_factura)

        self.pushButton_cancelar_editar_item_factura = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_editar_item_factura.setObjectName(u"pushButton_cancelar_editar_item_factura")

        self.horizontalLayout_accione_editar_item_factura.addWidget(self.pushButton_cancelar_editar_item_factura)


        self.formLayout_editar_item_factura.setLayout(3, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_accione_editar_item_factura)


        self.retranslate_ui(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_editar_item_factura.setText(QCoreApplication.translate("Dialog", u"Editar Item de a la Factura", None))
        self.label_item_editar_item_factura.setText(QCoreApplication.translate("Dialog", u"Item a Editar:", None))
        self.label_cantidad_items_editar_item_factura.setText(QCoreApplication.translate("Dialog", u"Cantidad de Items:", None))
        self.pushButton_editar_item_factura.setText(QCoreApplication.translate("Dialog", u"Editar", None))
        self.pushButton_cancelar_editar_item_factura.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

