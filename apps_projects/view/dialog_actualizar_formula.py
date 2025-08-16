from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont)
from PySide6.QtWidgets import (QComboBox, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableView, QTextEdit, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_actualizar_formula = None
        self.label_actualizar_formula = None
        self.label_factura = None
        self.comboBox_formula = None
        self.label_cliente = None
        self.lineEdit_nombre_formula = None
        self.label_description_formula = None
        self.textEdit_description = None
        self.horizontalLayout_acciones_tabla_actualizar_formula = None
        self.pushButton_agregar = None
        self.pushButton_eliminar = None
        self.tableView_ingredientes = None
        self.horizontalLayout_acciones_definitivas_actualizar_formula = None
        self.pushButton_guardar = None
        self.pushButton_cancelar = None
        self.label_ingredientes_de_la_formula = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(569, 535)
        dialog.setMinimumSize(QSize(0, 535))
        dialog.setMaximumSize(QSize(16777215, 535))
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 570, 533))
        self.formLayout_actualizar_formula = QFormLayout(self.formLayoutWidget)
        self.formLayout_actualizar_formula.setObjectName(u"formLayout_actualizar_formula")
        self.formLayout_actualizar_formula.setVerticalSpacing(6)
        self.formLayout_actualizar_formula.setContentsMargins(10, 10, 10, 10)
        self.label_actualizar_formula = QLabel(self.formLayoutWidget)
        self.label_actualizar_formula.setObjectName(u"label_actualizar_formula")
        self.label_actualizar_formula.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        self.label_actualizar_formula.setFont(font)
        self.label_actualizar_formula.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_actualizar_formula.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_actualizar_formula)

        self.label_factura = QLabel(self.formLayoutWidget)
        self.label_factura.setObjectName(u"label_factura")

        self.formLayout_actualizar_formula.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_factura)

        self.comboBox_formula = QComboBox(self.formLayoutWidget)
        self.comboBox_formula.setObjectName(u"comboBox_formula")

        self.formLayout_actualizar_formula.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_formula)

        self.label_cliente = QLabel(self.formLayoutWidget)
        self.label_cliente.setObjectName(u"label_cliente")

        self.formLayout_actualizar_formula.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_cliente)

        self.lineEdit_nombre_formula = QLineEdit(self.formLayoutWidget)
        self.lineEdit_nombre_formula.setObjectName(u"lineEdit_nombre_formula")
        self.lineEdit_nombre_formula.setMaximumSize(QSize(400, 16777215))

        self.formLayout_actualizar_formula.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_nombre_formula)

        self.label_description_formula = QLabel(self.formLayoutWidget)
        self.label_description_formula.setObjectName(u"label_description_formula")

        self.formLayout_actualizar_formula.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_description_formula)

        self.textEdit_description = QTextEdit(self.formLayoutWidget)
        self.textEdit_description.setObjectName(u"textEdit_description")
        self.textEdit_description.setMinimumSize(QSize(400, 125))
        self.textEdit_description.setMaximumSize(QSize(400, 125))

        self.formLayout_actualizar_formula.setWidget(3, QFormLayout.ItemRole.FieldRole, self.textEdit_description)

        self.horizontalLayout_acciones_tabla_actualizar_formula = QHBoxLayout()
        self.horizontalLayout_acciones_tabla_actualizar_formula.setSpacing(25)
        self.horizontalLayout_acciones_tabla_actualizar_formula.setObjectName(u"horizontalLayout_acciones_tabla_actualizar_formula")
        self.horizontalLayout_acciones_tabla_actualizar_formula.setContentsMargins(20, 5, 20, -1)
        self.pushButton_agregar = QPushButton(self.formLayoutWidget)
        self.pushButton_agregar.setObjectName(u"pushButton_agregar")
        self.pushButton_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_agregar.setFlat(True)

        self.horizontalLayout_acciones_tabla_actualizar_formula.addWidget(self.pushButton_agregar)

        self.pushButton_eliminar = QPushButton(self.formLayoutWidget)
        self.pushButton_eliminar.setObjectName(u"pushButton_eliminar")
        self.pushButton_eliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_eliminar.setFlat(True)

        self.horizontalLayout_acciones_tabla_actualizar_formula.addWidget(self.pushButton_eliminar)


        self.formLayout_actualizar_formula.setLayout(4, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_acciones_tabla_actualizar_formula)

        self.tableView_ingredientes = QTableView(self.formLayoutWidget)
        self.tableView_ingredientes.setObjectName(u"tableView_ingredientes")
        self.tableView_ingredientes.setMinimumSize(QSize(400, 220))
        self.tableView_ingredientes.setMaximumSize(QSize(400, 220))

        self.formLayout_actualizar_formula.setWidget(5, QFormLayout.ItemRole.FieldRole, self.tableView_ingredientes)

        self.horizontalLayout_acciones_definitivas_actualizar_formula = QHBoxLayout()
        self.horizontalLayout_acciones_definitivas_actualizar_formula.setSpacing(50)
        self.horizontalLayout_acciones_definitivas_actualizar_formula.setObjectName(u"horizontalLayout_acciones_definitivas_actualizar_formula")
        self.horizontalLayout_acciones_definitivas_actualizar_formula.setContentsMargins(30, 10, 30, 0)
        self.pushButton_guardar = QPushButton(self.formLayoutWidget)
        self.pushButton_guardar.setObjectName(u"pushButton_guardar")
        self.pushButton_guardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_guardar.setFlat(True)

        self.horizontalLayout_acciones_definitivas_actualizar_formula.addWidget(self.pushButton_guardar)

        self.pushButton_cancelar = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar.setObjectName(u"pushButton_cancelar")
        self.pushButton_cancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_cancelar.setFlat(True)

        self.horizontalLayout_acciones_definitivas_actualizar_formula.addWidget(self.pushButton_cancelar)


        self.formLayout_actualizar_formula.setLayout(6, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_acciones_definitivas_actualizar_formula)

        self.label_ingredientes_de_la_formula = QLabel(self.formLayoutWidget)
        self.label_ingredientes_de_la_formula.setObjectName(u"label_ingredientes_de_la_formula")

        self.formLayout_actualizar_formula.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_ingredientes_de_la_formula)


        self.retranslate_ui(dialog)

        self.pushButton_agregar.setDefault(False)


        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_actualizar_formula.setText(QCoreApplication.translate("Dialog", u"Actualizar Formula", None))
        self.label_factura.setText(QCoreApplication.translate("Dialog", u"Selecciona la Formula:", None))
        self.label_cliente.setText(QCoreApplication.translate("Dialog", u"Nombre de la Formula:", None))
        self.label_description_formula.setText(QCoreApplication.translate("Dialog", u"Description de la Formula:", None))
        self.pushButton_agregar.setText(QCoreApplication.translate("Dialog", u"Agregar Ingrediente", None))
        self.pushButton_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar Ingrediente", None))
        self.pushButton_guardar.setText(QCoreApplication.translate("Dialog", u"Guardar Actualización", None))
        self.pushButton_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar Actualización", None))
        self.label_ingredientes_de_la_formula.setText(QCoreApplication.translate("Dialog", u"Ingredientes de la Formula:", None))
    # retranslateUi

