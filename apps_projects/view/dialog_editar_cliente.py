from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_editar_cliente = None
        self.label_editar_cliente = None
        self.label_nombre_cliente_editar_cliente = None
        self.lineEdit_nombre_cliente_editar_cliente = None
        self.label_ci_rif_editar_cliente = None
        self.horizontalLayout_datos_identidad_editar_cliente = None
        self.comboBox_tipo_documento_editar_cliente = None
        self.lineEdit_numero_documento_identidad_editar_cliente = None
        self.label_numero_phone_editar_cliente = None
        self.horizontalLayout_phone_editar_cliente = None
        self.comboBox_code_editar_cliente = None
        self.lineEdit_numero_phone_editar_cliente = None
        self.label_email_editar_cliente = None
        self.lineEdit_email_editar_cliente = None
        self.label_direction_editar_cliente = None
        self.lineEdit_direction_editar_cliente = None
        self.horizontalLayout_acciones_editar_cliente = None
        self.pushButton_editar_cliente = None
        self.pushButton_cancelar_editar_cliente = None
        self.label_selecciona_cliente_editar_cliente = None
        self.comboBox_editar_cliente = None

    def setup_ui(self, dialog_editar_cliente):
        if not dialog_editar_cliente.objectName():
            dialog_editar_cliente.setObjectName(u"Dialog_editar_cliente")
        dialog_editar_cliente.resize(391, 260)
        self.formLayoutWidget = QWidget(dialog_editar_cliente)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 391, 261))
        self.formLayout_editar_cliente = QFormLayout(self.formLayoutWidget)
        self.formLayout_editar_cliente.setObjectName(u"formLayout_editar_cliente")
        self.formLayout_editar_cliente.setContentsMargins(10, 10, 10, 10)
        self.label_editar_cliente = QLabel(self.formLayoutWidget)
        self.label_editar_cliente.setObjectName(u"label_editar_cliente")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_editar_cliente.setFont(font)

        self.formLayout_editar_cliente.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_editar_cliente)

        self.label_nombre_cliente_editar_cliente = QLabel(self.formLayoutWidget)
        self.label_nombre_cliente_editar_cliente.setObjectName(u"label_nombre_cliente_editar_cliente")

        self.formLayout_editar_cliente.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_nombre_cliente_editar_cliente)

        self.lineEdit_nombre_cliente_editar_cliente = QLineEdit(self.formLayoutWidget)
        self.lineEdit_nombre_cliente_editar_cliente.setObjectName(u"lineEdit_nombre_cliente_editar_cliente")

        self.formLayout_editar_cliente.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_nombre_cliente_editar_cliente)

        self.label_ci_rif_editar_cliente = QLabel(self.formLayoutWidget)
        self.label_ci_rif_editar_cliente.setObjectName(u"label_ci_rif_editar_cliente")

        self.formLayout_editar_cliente.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_ci_rif_editar_cliente)

        self.horizontalLayout_datos_identidad_editar_cliente = QHBoxLayout()
        self.horizontalLayout_datos_identidad_editar_cliente.setObjectName(u"horizontalLayout_datos_identidad_editar_cliente")
        self.comboBox_tipo_documento_editar_cliente = QComboBox(self.formLayoutWidget)
        self.comboBox_tipo_documento_editar_cliente.setObjectName(u"comboBox_tipo_documento_editar_cliente")

        self.horizontalLayout_datos_identidad_editar_cliente.addWidget(self.comboBox_tipo_documento_editar_cliente)

        self.lineEdit_numero_documento_identidad_editar_cliente = QLineEdit(self.formLayoutWidget)
        self.lineEdit_numero_documento_identidad_editar_cliente.setObjectName(u"lineEdit_numero_documento_identidad_editar_cliente")

        self.horizontalLayout_datos_identidad_editar_cliente.addWidget(self.lineEdit_numero_documento_identidad_editar_cliente)


        self.formLayout_editar_cliente.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_datos_identidad_editar_cliente)

        self.label_numero_phone_editar_cliente = QLabel(self.formLayoutWidget)
        self.label_numero_phone_editar_cliente.setObjectName(u"label_numero_phone_editar_cliente")

        self.formLayout_editar_cliente.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_numero_phone_editar_cliente)

        self.horizontalLayout_phone_editar_cliente = QHBoxLayout()
        self.horizontalLayout_phone_editar_cliente.setObjectName(u"horizontalLayout_phone_editar_cliente")
        self.comboBox_code_editar_cliente = QComboBox(self.formLayoutWidget)
        self.comboBox_code_editar_cliente.setObjectName(u"comboBox_code_editar_cliente")

        self.horizontalLayout_phone_editar_cliente.addWidget(self.comboBox_code_editar_cliente)

        self.lineEdit_numero_phone_editar_cliente = QLineEdit(self.formLayoutWidget)
        self.lineEdit_numero_phone_editar_cliente.setObjectName(u"lineEdit_numero_phone_editar_cliente")

        self.horizontalLayout_phone_editar_cliente.addWidget(self.lineEdit_numero_phone_editar_cliente)


        self.formLayout_editar_cliente.setLayout(4, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_phone_editar_cliente)

        self.label_email_editar_cliente = QLabel(self.formLayoutWidget)
        self.label_email_editar_cliente.setObjectName(u"label_email_editar_cliente")

        self.formLayout_editar_cliente.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_email_editar_cliente)

        self.lineEdit_email_editar_cliente = QLineEdit(self.formLayoutWidget)
        self.lineEdit_email_editar_cliente.setObjectName(u"lineEdit_email_editar_cliente")

        self.formLayout_editar_cliente.setWidget(5, QFormLayout.ItemRole.FieldRole, self.lineEdit_email_editar_cliente)

        self.label_direction_editar_cliente = QLabel(self.formLayoutWidget)
        self.label_direction_editar_cliente.setObjectName(u"label_direction_editar_cliente")

        self.formLayout_editar_cliente.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_direction_editar_cliente)

        self.lineEdit_direction_editar_cliente = QLineEdit(self.formLayoutWidget)
        self.lineEdit_direction_editar_cliente.setObjectName(u"lineEdit_direction_editar_cliente")

        self.formLayout_editar_cliente.setWidget(6, QFormLayout.ItemRole.FieldRole, self.lineEdit_direction_editar_cliente)

        self.horizontalLayout_acciones_editar_cliente = QHBoxLayout()
        self.horizontalLayout_acciones_editar_cliente.setSpacing(40)
        self.horizontalLayout_acciones_editar_cliente.setObjectName(u"horizontalLayout_acciones_editar_cliente")
        self.horizontalLayout_acciones_editar_cliente.setContentsMargins(30, 5, 30, 0)
        self.pushButton_editar_cliente = QPushButton(self.formLayoutWidget)
        self.pushButton_editar_cliente.setObjectName(u"pushButton_editar_cliente")

        self.horizontalLayout_acciones_editar_cliente.addWidget(self.pushButton_editar_cliente)

        self.pushButton_cancelar_editar_cliente = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_editar_cliente.setObjectName(u"pushButton_cancelar_editar_cliente")

        self.horizontalLayout_acciones_editar_cliente.addWidget(self.pushButton_cancelar_editar_cliente)


        self.formLayout_editar_cliente.setLayout(7, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_acciones_editar_cliente)

        self.label_selecciona_cliente_editar_cliente = QLabel(self.formLayoutWidget)
        self.label_selecciona_cliente_editar_cliente.setObjectName(u"label_selecciona_cliente_editar_cliente")

        self.formLayout_editar_cliente.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_selecciona_cliente_editar_cliente)

        self.comboBox_editar_cliente = QComboBox(self.formLayoutWidget)
        self.comboBox_editar_cliente.setObjectName(u"comboBox_editar_cliente")

        self.formLayout_editar_cliente.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_editar_cliente)


        self.retranslate_ui(dialog_editar_cliente)

        QMetaObject.connectSlotsByName(dialog_editar_cliente)
    # setupUi

    def retranslate_ui(self, dialog_editar_cliente):
        dialog_editar_cliente.setWindowTitle(QCoreApplication.translate("Dialog_editar_cliente", u"Dialog", None))
        self.label_editar_cliente.setText(QCoreApplication.translate("Dialog_editar_cliente", u"Editar Cliente", None))
        self.label_nombre_cliente_editar_cliente.setText(QCoreApplication.translate("Dialog_editar_cliente", u"Nombre del Cliente:", None))
        self.label_ci_rif_editar_cliente.setText(QCoreApplication.translate("Dialog_editar_cliente", u"Cedula de Identidad o Rif:", None))
        self.label_numero_phone_editar_cliente.setText(QCoreApplication.translate("Dialog_editar_cliente", u"Numero de phone:", None))
        self.label_email_editar_cliente.setText(QCoreApplication.translate("Dialog_editar_cliente", u"Email:", None))
        self.label_direction_editar_cliente.setText(QCoreApplication.translate("Dialog_editar_cliente", u"direction:", None))
        self.pushButton_editar_cliente.setText(QCoreApplication.translate("Dialog_editar_cliente", u"Guardar Cambios", None))
        self.pushButton_cancelar_editar_cliente.setText(QCoreApplication.translate("Dialog_editar_cliente", u"Cancelar", None))
        self.label_selecciona_cliente_editar_cliente.setText(QCoreApplication.translate("Dialog_editar_cliente", u"Selecciona el Cliente:", None))
    # retranslateUi

