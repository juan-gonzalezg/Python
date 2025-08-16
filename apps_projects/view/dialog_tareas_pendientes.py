from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFormLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_crear_tarea = None
        self.label_ingrese_proxima_tarea_crear_tarea = None
        self.lineEdit_tarea__crear_tarea = None
        self.horizontalLayout_acciones_definitivas_crear_tarea = None
        self.pushButton_crear_tarea = None
        self.pushButton_cancelar_crear_tarea = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(318, 128)
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(-1, -1, 321, 147))
        self.formLayout_crear_tarea = QFormLayout(self.formLayoutWidget)
        self.formLayout_crear_tarea.setObjectName(u"formLayout_crear_tarea")
        self.formLayout_crear_tarea.setContentsMargins(10, 20, 10, 20)
        self.label_ingrese_proxima_tarea_crear_tarea = QLabel(self.formLayoutWidget)
        self.label_ingrese_proxima_tarea_crear_tarea.setObjectName(u"label_ingrese_proxima_tarea_crear_tarea")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_ingrese_proxima_tarea_crear_tarea.setFont(font)

        self.formLayout_crear_tarea.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_ingrese_proxima_tarea_crear_tarea)

        self.lineEdit_tarea__crear_tarea = QLineEdit(self.formLayoutWidget)
        self.lineEdit_tarea__crear_tarea.setObjectName(u"lineEdit_tarea__crear_tarea")

        self.formLayout_crear_tarea.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_tarea__crear_tarea)

        self.horizontalLayout_acciones_definitivas_crear_tarea = QHBoxLayout()
        self.horizontalLayout_acciones_definitivas_crear_tarea.setObjectName(u"horizontalLayout_acciones_definitivas_crear_tarea")
        self.pushButton_crear_tarea = QPushButton(self.formLayoutWidget)
        self.pushButton_crear_tarea.setObjectName(u"pushButton_crear_crear_tarea")

        self.horizontalLayout_acciones_definitivas_crear_tarea.addWidget(self.pushButton_crear_tarea)

        self.pushButton_cancelar_crear_tarea = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_crear_tarea.setObjectName(u"pushButton_cancelar_crear_tarea")

        self.horizontalLayout_acciones_definitivas_crear_tarea.addWidget(self.pushButton_cancelar_crear_tarea)


        self.formLayout_crear_tarea.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_acciones_definitivas_crear_tarea)


        self.retranslate_ui(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_ingrese_proxima_tarea_crear_tarea.setText(QCoreApplication.translate("Dialog", u"Ingrese la proxima tarea:", None))
        self.pushButton_crear_tarea.setText(QCoreApplication.translate("Dialog", u"Crear", None))
        self.pushButton_cancelar_crear_tarea.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

