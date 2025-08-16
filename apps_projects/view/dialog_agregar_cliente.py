from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_agregar_cliente = None
        self.label_agregar_editar_agregar_cliente = None
        self.label_nombre_cliente_agregar_cliente = None
        self.lineEdit_nombre_cliente_agregar_cliente = None
        self.label_ci_rif_agregar_cliente = None
        self.horizontalLayout_datos_identidad_agregar_cliente = None
        self.comboBox_tipo_documento_agregar_cliente = None
        self.lineEdit_numero_documento_identidad_agregar_cliente = None
        self.label_numero_phone_agregar_cliente = None
        self.horizontalLayout_phone_agregar_cliente = None
        self.comboBox_code_agregar_cliente = None
        self.lineEdit_numero_phone_agregar_cliente = None
        self.label_email_agregar_cliente = None
        self.lineEdit_email_agregar_cliente = None
        self.label_direction_agregar_cliente = None
        self.lineEdit_direction_agregar_cliente = None
        self.horizontalLayout_acciones_agregar_cliente = None
        self.pushButton_agregar_cliente = None
        self.pushButton_cancelar_agregar_cliente = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(391, 222)
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 391, 231))
        self.formLayout_agregar_cliente = QFormLayout(self.formLayoutWidget)
        self.formLayout_agregar_cliente.setObjectName(u"formLayout_agregar_cliente")
        self.formLayout_agregar_cliente.setContentsMargins(10, 10, 10, 10)
        self.label_agregar_editar_agregar_cliente = QLabel(self.formLayoutWidget)
        self.label_agregar_editar_agregar_cliente.setObjectName(u"label_agregar_editar_agregar_cliente")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_agregar_editar_agregar_cliente.setFont(font)

        self.formLayout_agregar_cliente.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_agregar_editar_agregar_cliente)

        self.label_nombre_cliente_agregar_cliente = QLabel(self.formLayoutWidget)
        self.label_nombre_cliente_agregar_cliente.setObjectName(u"label_nombre_cliente_agregar_cliente")

        self.formLayout_agregar_cliente.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_nombre_cliente_agregar_cliente)

        self.lineEdit_nombre_cliente_agregar_cliente = QLineEdit(self.formLayoutWidget)
        self.lineEdit_nombre_cliente_agregar_cliente.setObjectName(u"lineEdit_nombre_cliente_agregar_cliente")

        self.formLayout_agregar_cliente.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_nombre_cliente_agregar_cliente)

        self.label_ci_rif_agregar_cliente = QLabel(self.formLayoutWidget)
        self.label_ci_rif_agregar_cliente.setObjectName(u"label_ci_rif_agregar_cliente")

        self.formLayout_agregar_cliente.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_ci_rif_agregar_cliente)

        self.horizontalLayout_datos_identidad_agregar_cliente = QHBoxLayout()
        self.horizontalLayout_datos_identidad_agregar_cliente.setObjectName(u"horizontalLayout_datos_identidad_agregar_cliente")
        self.comboBox_tipo_documento_agregar_cliente = QComboBox(self.formLayoutWidget)
        self.comboBox_tipo_documento_agregar_cliente.setObjectName(u"comboBox_tipo_documento_agregar_cliente")

        self.horizontalLayout_datos_identidad_agregar_cliente.addWidget(self.comboBox_tipo_documento_agregar_cliente)

        self.lineEdit_numero_documento_identidad_agregar_cliente = QLineEdit(self.formLayoutWidget)
        self.lineEdit_numero_documento_identidad_agregar_cliente.setObjectName(u"lineEdit_numero_documento_identidad_agregar_cliente")

        self.horizontalLayout_datos_identidad_agregar_cliente.addWidget(self.lineEdit_numero_documento_identidad_agregar_cliente)


        self.formLayout_agregar_cliente.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_datos_identidad_agregar_cliente)

        self.label_numero_phone_agregar_cliente = QLabel(self.formLayoutWidget)
        self.label_numero_phone_agregar_cliente.setObjectName(u"label_numero_phone_agregar_cliente")

        self.formLayout_agregar_cliente.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_numero_phone_agregar_cliente)

        self.horizontalLayout_phone_agregar_cliente = QHBoxLayout()
        self.horizontalLayout_phone_agregar_cliente.setObjectName(u"horizontalLayout_phone_agregar_cliente")
        self.comboBox_code_agregar_cliente = QComboBox(self.formLayoutWidget)
        self.comboBox_code_agregar_cliente.setObjectName(u"comboBox_code_agregar_cliente")

        self.horizontalLayout_phone_agregar_cliente.addWidget(self.comboBox_code_agregar_cliente)

        self.lineEdit_numero_phone_agregar_cliente = QLineEdit(self.formLayoutWidget)
        self.lineEdit_numero_phone_agregar_cliente.setObjectName(u"lineEdit_numero_phone_agregar_cliente")

        self.horizontalLayout_phone_agregar_cliente.addWidget(self.lineEdit_numero_phone_agregar_cliente)


        self.formLayout_agregar_cliente.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_phone_agregar_cliente)

        self.label_email_agregar_cliente = QLabel(self.formLayoutWidget)
        self.label_email_agregar_cliente.setObjectName(u"label_email_agregar_cliente")

        self.formLayout_agregar_cliente.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_email_agregar_cliente)

        self.lineEdit_email_agregar_cliente = QLineEdit(self.formLayoutWidget)
        self.lineEdit_email_agregar_cliente.setObjectName(u"lineEdit_email_agregar_cliente")

        self.formLayout_agregar_cliente.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineEdit_email_agregar_cliente)

        self.label_direction_agregar_cliente = QLabel(self.formLayoutWidget)
        self.label_direction_agregar_cliente.setObjectName(u"label_direction_agregar_cliente")

        self.formLayout_agregar_cliente.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_direction_agregar_cliente)

        self.lineEdit_direction_agregar_cliente = QLineEdit(self.formLayoutWidget)
        self.lineEdit_direction_agregar_cliente.setObjectName(u"lineEdit_direction_agregar_cliente")

        self.formLayout_agregar_cliente.setWidget(5, QFormLayout.ItemRole.FieldRole, self.lineEdit_direction_agregar_cliente)

        self.horizontalLayout_acciones_agregar_cliente = QHBoxLayout()
        self.horizontalLayout_acciones_agregar_cliente.setSpacing(40)
        self.horizontalLayout_acciones_agregar_cliente.setObjectName(u"horizontalLayout_acciones_agregar_cliente")
        self.horizontalLayout_acciones_agregar_cliente.setContentsMargins(30, 5, 30, 0)
        self.pushButton_agregar_cliente = QPushButton(self.formLayoutWidget)
        self.pushButton_agregar_cliente.setObjectName(u"pushButton_agregar_cliente")

        self.horizontalLayout_acciones_agregar_cliente.addWidget(self.pushButton_agregar_cliente)

        self.pushButton_cancelar_agregar_cliente = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_agregar_cliente.setObjectName(u"pushButton_cancelar_agregar_cliente")

        self.horizontalLayout_acciones_agregar_cliente.addWidget(self.pushButton_cancelar_agregar_cliente)


        self.formLayout_agregar_cliente.setLayout(6, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_acciones_agregar_cliente)


        self.retranslate_ui(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_agregar_editar_agregar_cliente.setText(QCoreApplication.translate("Dialog", u"Agregar Cliente", None))
        self.label_nombre_cliente_agregar_cliente.setText(QCoreApplication.translate("Dialog", u"Nombre del Cliente:", None))
        self.label_ci_rif_agregar_cliente.setText(QCoreApplication.translate("Dialog", u"Cedula de Identidad o Rif:", None))
        self.label_numero_phone_agregar_cliente.setText(QCoreApplication.translate("Dialog", u"Numero de phone:", None))
        self.label_email_agregar_cliente.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.label_direction_agregar_cliente.setText(QCoreApplication.translate("Dialog", u"Direction:", None))
        self.pushButton_agregar_cliente.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
        self.pushButton_cancelar_agregar_cliente.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

