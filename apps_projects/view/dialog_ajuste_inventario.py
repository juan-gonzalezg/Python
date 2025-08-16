from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QFormLayout, QHBoxLayout, QLabel, QPushButton, QSpinBox, QTextEdit, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_ajustar_item_stock = None
        self.label_cantidad_ajustar_item_stock = None
        self.spinBox_cantidad_ajustar_item_stock = None
        self.label_justification_ajustar_item_stock = None
        self.textEdit_justification_ajustar_item_stock = None
        self.label_ajustar_item_stock = None
        self.comboBox_item_ajustar_item_stock = None
        self.label_seleccione_item_ajustar_item_stock = None
        self.horizontalLayout_funciones_ajustar_item_stock = None
        self.pushButton_ajustar_item_stock = None
        self.pushButton_cancelar_ajustar_item_stock = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(439, 235)
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(-2, 4, 441, 231))
        self.formLayout_ajustar_item_stock = QFormLayout(self.formLayoutWidget)
        self.formLayout_ajustar_item_stock.setObjectName(u"formLayout_ajustar_item_stock")
        self.formLayout_ajustar_item_stock.setContentsMargins(10, 0, 10, 10)
        self.label_cantidad_ajustar_item_stock = QLabel(self.formLayoutWidget)
        self.label_cantidad_ajustar_item_stock.setObjectName(u"label_cantidad_ajustar_item_stock")

        self.formLayout_ajustar_item_stock.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_cantidad_ajustar_item_stock)

        self.spinBox_cantidad_ajustar_item_stock = QSpinBox(self.formLayoutWidget)
        self.spinBox_cantidad_ajustar_item_stock.setObjectName(u"spinBox_cantidad_ajustar_item_stock")

        self.formLayout_ajustar_item_stock.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinBox_cantidad_ajustar_item_stock)

        self.label_justification_ajustar_item_stock = QLabel(self.formLayoutWidget)
        self.label_justification_ajustar_item_stock.setObjectName(u"label_justification_ajustar_item_stock")

        self.formLayout_ajustar_item_stock.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_justification_ajustar_item_stock)

        self.textEdit_justification_ajustar_item_stock = QTextEdit(self.formLayoutWidget)
        self.textEdit_justification_ajustar_item_stock.setObjectName(u"textEdit_justification_ajustar_item_stock")

        self.formLayout_ajustar_item_stock.setWidget(4, QFormLayout.ItemRole.FieldRole, self.textEdit_justification_ajustar_item_stock)

        self.label_ajustar_item_stock = QLabel(self.formLayoutWidget)
        self.label_ajustar_item_stock.setObjectName(u"label_ajustar_item_stock")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_ajustar_item_stock.setFont(font)

        self.formLayout_ajustar_item_stock.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.label_ajustar_item_stock)

        self.comboBox_item_ajustar_item_stock = QComboBox(self.formLayoutWidget)
        self.comboBox_item_ajustar_item_stock.setObjectName(u"comboBox_item_ajustar_item_stock")

        self.formLayout_ajustar_item_stock.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox_item_ajustar_item_stock)

        self.label_seleccione_item_ajustar_item_stock = QLabel(self.formLayoutWidget)
        self.label_seleccione_item_ajustar_item_stock.setObjectName(u"label_seleccione_item_ajustar_item_stock")

        self.formLayout_ajustar_item_stock.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_seleccione_item_ajustar_item_stock)

        self.horizontalLayout_funciones_ajustar_item_stock = QHBoxLayout()
        self.horizontalLayout_funciones_ajustar_item_stock.setSpacing(50)
        self.horizontalLayout_funciones_ajustar_item_stock.setObjectName(u"horizontalLayout_funciones_ajustar_item_stock")
        self.horizontalLayout_funciones_ajustar_item_stock.setContentsMargins(40, -1, 40, -1)
        self.pushButton_ajustar_item_stock = QPushButton(self.formLayoutWidget)
        self.pushButton_ajustar_item_stock.setObjectName(u"pushButton_ajustar_item_stock")

        self.horizontalLayout_funciones_ajustar_item_stock.addWidget(self.pushButton_ajustar_item_stock)

        self.pushButton_cancelar_ajustar_item_stock = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_ajustar_item_stock.setObjectName(u"pushButton_cancelar_ajustar_item_stock")

        self.horizontalLayout_funciones_ajustar_item_stock.addWidget(self.pushButton_cancelar_ajustar_item_stock)


        self.formLayout_ajustar_item_stock.setLayout(5, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_funciones_ajustar_item_stock)


        self.retranslate_ui(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_cantidad_ajustar_item_stock.setText(QCoreApplication.translate("Dialog", u"Cantidad:", None))
        self.label_justification_ajustar_item_stock.setText(QCoreApplication.translate("Dialog", u"Justificación (opcional):", None))
        self.label_ajustar_item_stock.setText(QCoreApplication.translate("Dialog", u"Ajustar Item del Inventario", None))
        self.label_seleccione_item_ajustar_item_stock.setText(QCoreApplication.translate("Dialog", u"Seleccione un Item:", None))
        self.pushButton_ajustar_item_stock.setText(QCoreApplication.translate("Dialog", u"Ajustar", None))
        self.pushButton_cancelar_ajustar_item_stock.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

