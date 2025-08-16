from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QFormLayout, QHBoxLayout, QLabel, QPushButton, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_eliminar = None
        self.label_eliminar = None
        self.label_seleccione_eliminar = None
        self.comboBox_opciones_eliminar = None
        self.horizontalLayout_funciones_definitivas__eliminar = None
        self.pushButton_eliminar = None
        self.pushButton_cancelar_eliminar = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(380, 109)
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 381, 111))
        self.formLayout_eliminar = QFormLayout(self.formLayoutWidget)
        self.formLayout_eliminar.setObjectName(u"formLayout_eliminar")
        self.formLayout_eliminar.setContentsMargins(10, 10, 10, 10)
        self.label_eliminar = QLabel(self.formLayoutWidget)
        self.label_eliminar.setObjectName(u"label_eliminar")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_eliminar.setFont(font)

        self.formLayout_eliminar.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_eliminar)

        self.label_seleccione_eliminar = QLabel(self.formLayoutWidget)
        self.label_seleccione_eliminar.setObjectName(u"label_seleccione_eliminar")

        self.formLayout_eliminar.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_seleccione_eliminar)

        self.comboBox_opciones_eliminar = QComboBox(self.formLayoutWidget)
        self.comboBox_opciones_eliminar.setObjectName(u"comboBox_opciones_eliminar")

        self.formLayout_eliminar.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_opciones_eliminar)

        self.horizontalLayout_funciones_definitivas__eliminar = QHBoxLayout()
        self.horizontalLayout_funciones_definitivas__eliminar.setSpacing(30)
        self.horizontalLayout_funciones_definitivas__eliminar.setObjectName(u"horizontalLayout_funciones_definitivas__eliminar")
        self.horizontalLayout_funciones_definitivas__eliminar.setContentsMargins(40, 5, 40, -1)
        self.pushButton_eliminar = QPushButton(self.formLayoutWidget)
        self.pushButton_eliminar.setObjectName(u"pushButton_eliminar")

        self.horizontalLayout_funciones_definitivas__eliminar.addWidget(self.pushButton_eliminar)

        self.pushButton_cancelar_eliminar = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_eliminar.setObjectName(u"pushButton_cancelar_eliminar")

        self.horizontalLayout_funciones_definitivas__eliminar.addWidget(self.pushButton_cancelar_eliminar)


        self.formLayout_eliminar.setLayout(2, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_funciones_definitivas__eliminar)


        self.retranslate_ui(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar", None))
        self.label_seleccione_eliminar.setText(QCoreApplication.translate("Dialog", u"Seleccione:", None))
        self.pushButton_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar", None))
        self.pushButton_cancelar_eliminar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

