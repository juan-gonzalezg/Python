from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QDateEdit, QFormLayout, QHBoxLayout, QLabel, QPushButton, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_ajustar_periodo_grafica = None
        self.label_ajustar_periodo_grafica = None
        self.label_desde_ajustar_periodo_grafica = None
        self.dateEdit_desde__ajustar_periodo_grafica = None
        self.label_hasta_ajustar_periodo_grafica = None
        self.dateEdit_hasta__ajustar_periodo_grafica = None
        self.horizontalLayout_funciones_ajustar_periodo_grafica = None
        self.pushButton_ajustar_periodo_grafica = None
        self.pushButton_cancelar_ajustar_periodo_grafica = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(178, 141)
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 181, 141))
        self.formLayout_ajustar_periodo_grafica = QFormLayout(self.formLayoutWidget)
        self.formLayout_ajustar_periodo_grafica.setObjectName(u"formLayout_ajustar_periodo_grafica")
        self.formLayout_ajustar_periodo_grafica.setContentsMargins(10, 10, 10, 10)
        self.label_ajustar_periodo_grafica = QLabel(self.formLayoutWidget)
        self.label_ajustar_periodo_grafica.setObjectName(u"label_ajustar_periodo_grafica")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_ajustar_periodo_grafica.setFont(font)

        self.formLayout_ajustar_periodo_grafica.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_ajustar_periodo_grafica)

        self.label_desde_ajustar_periodo_grafica = QLabel(self.formLayoutWidget)
        self.label_desde_ajustar_periodo_grafica.setObjectName(u"label_desde_ajustar_periodo_grafica")

        self.formLayout_ajustar_periodo_grafica.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_desde_ajustar_periodo_grafica)

        self.dateEdit_desde__ajustar_periodo_grafica = QDateEdit(self.formLayoutWidget)
        self.dateEdit_desde__ajustar_periodo_grafica.setObjectName(u"dateEdit_desde__ajustar_periodo_grafica")

        self.formLayout_ajustar_periodo_grafica.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateEdit_desde__ajustar_periodo_grafica)

        self.label_hasta_ajustar_periodo_grafica = QLabel(self.formLayoutWidget)
        self.label_hasta_ajustar_periodo_grafica.setObjectName(u"label_hasta_ajustar_periodo_grafica")

        self.formLayout_ajustar_periodo_grafica.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_hasta_ajustar_periodo_grafica)

        self.dateEdit_hasta__ajustar_periodo_grafica = QDateEdit(self.formLayoutWidget)
        self.dateEdit_hasta__ajustar_periodo_grafica.setObjectName(u"dateEdit_hasta__ajustar_periodo_grafica")

        self.formLayout_ajustar_periodo_grafica.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateEdit_hasta__ajustar_periodo_grafica)

        self.horizontalLayout_funciones_ajustar_periodo_grafica = QHBoxLayout()
        self.horizontalLayout_funciones_ajustar_periodo_grafica.setObjectName(u"horizontalLayout_funciones_ajustar_periodo_grafica")
        self.horizontalLayout_funciones_ajustar_periodo_grafica.setContentsMargins(-1, 10, -1, -1)
        self.pushButton_ajustar_periodo_grafica = QPushButton(self.formLayoutWidget)
        self.pushButton_ajustar_periodo_grafica.setObjectName(u"pushButton_ajustar_periodo_grafica")

        self.horizontalLayout_funciones_ajustar_periodo_grafica.addWidget(self.pushButton_ajustar_periodo_grafica)

        self.pushButton_cancelar_ajustar_periodo_grafica = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_ajustar_periodo_grafica.setObjectName(u"pushButton_cancelar_ajustar_periodo_grafica")

        self.horizontalLayout_funciones_ajustar_periodo_grafica.addWidget(self.pushButton_cancelar_ajustar_periodo_grafica)


        self.formLayout_ajustar_periodo_grafica.setLayout(3, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_funciones_ajustar_periodo_grafica)


        self.retranslate_ui(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_ajustar_periodo_grafica.setText(QCoreApplication.translate("Dialog", u"Ajustar Periodo", None))
        self.label_desde_ajustar_periodo_grafica.setText(QCoreApplication.translate("Dialog", u"Desde:", None))
        self.label_hasta_ajustar_periodo_grafica.setText(QCoreApplication.translate("Dialog", u"Hasta:", None))
        self.pushButton_ajustar_periodo_grafica.setText(QCoreApplication.translate("Dialog", u"Ajustar", None))
        self.pushButton_cancelar_ajustar_periodo_grafica.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

