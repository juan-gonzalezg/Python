from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFormLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableView, QTextEdit, QWidget)

class UiDialog(object):
    def __init__(self):
        self.formLayoutWidget = None
        self.formLayout_agregar_formula = None
        self.label_agregar_formula = None
        self.label_nombre_formula_agregar_formula = None
        self.lineEdit_nombre_agregar_formula = None
        self.label_description_formula_agregar_formula = None
        self.textEdit_description_agregar_formula = None
        self.horizontalLayout_funciones_ingredientes_agregar_formula = None
        self.pushButton_agregar_ingrediente_agregar_formula = None
        self.pushButton_eliminar_ingrediente_agregar_formula = None
        self.label_ingredientes_formula_agregar_formula = None
        self.tableView_ingredientes_agregar_formula = None
        self.label_instrucciones_agregar_formula = None
        self.textEdit_instrucciones_agregar_formula = None
        self.horizontalLayout_funciones_definitivas__agregar_formula = None
        self.pushButton_agregar_formula = None
        self.pushButton_cancelar_agregar_formula = None

    def setup_ui(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"Dialog")
        dialog.resize(565, 620)
        dialog.setMinimumSize(QSize(565, 620))
        dialog.setMaximumSize(QSize(16777215, 620))
        self.formLayoutWidget = QWidget(dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(-3, 0, 571, 621))
        self.formLayout_agregar_formula = QFormLayout(self.formLayoutWidget)
        self.formLayout_agregar_formula.setObjectName(u"formLayout_agregar_formula")
        self.formLayout_agregar_formula.setContentsMargins(10, 0, 10, 10)
        self.label_agregar_formula = QLabel(self.formLayoutWidget)
        self.label_agregar_formula.setObjectName(u"label_agregar_formula")
        self.label_agregar_formula.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_agregar_formula.setFont(font)

        self.formLayout_agregar_formula.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_agregar_formula)

        self.label_nombre_formula_agregar_formula = QLabel(self.formLayoutWidget)
        self.label_nombre_formula_agregar_formula.setObjectName(u"label_nombre_formula_agregar_formula")

        self.formLayout_agregar_formula.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_nombre_formula_agregar_formula)

        self.lineEdit_nombre_agregar_formula = QLineEdit(self.formLayoutWidget)
        self.lineEdit_nombre_agregar_formula.setObjectName(u"lineEdit_nombre_agregar_formula")
        self.lineEdit_nombre_agregar_formula.setMaximumSize(QSize(400, 16777215))

        self.formLayout_agregar_formula.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_nombre_agregar_formula)

        self.label_description_formula_agregar_formula = QLabel(self.formLayoutWidget)
        self.label_description_formula_agregar_formula.setObjectName(u"label_description_formula_agregar_formula")

        self.formLayout_agregar_formula.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_description_formula_agregar_formula)

        self.textEdit_description_agregar_formula = QTextEdit(self.formLayoutWidget)
        self.textEdit_description_agregar_formula.setObjectName(u"textEdit_description_agregar_formula")
        self.textEdit_description_agregar_formula.setMinimumSize(QSize(400, 125))
        self.textEdit_description_agregar_formula.setMaximumSize(QSize(400, 125))

        self.formLayout_agregar_formula.setWidget(2, QFormLayout.ItemRole.FieldRole, self.textEdit_description_agregar_formula)

        self.horizontalLayout_funciones_ingredientes_agregar_formula = QHBoxLayout()
        self.horizontalLayout_funciones_ingredientes_agregar_formula.setSpacing(40)
        self.horizontalLayout_funciones_ingredientes_agregar_formula.setObjectName(u"horizontalLayout_funciones_ingredientes_agregar_formula")
        self.horizontalLayout_funciones_ingredientes_agregar_formula.setContentsMargins(30, 5, 30, -1)
        self.pushButton_agregar_ingrediente_agregar_formula = QPushButton(self.formLayoutWidget)
        self.pushButton_agregar_ingrediente_agregar_formula.setObjectName(u"pushButton_agregar_ingrediente_agregar_formula")

        self.horizontalLayout_funciones_ingredientes_agregar_formula.addWidget(self.pushButton_agregar_ingrediente_agregar_formula)

        self.pushButton_eliminar_ingrediente_agregar_formula = QPushButton(self.formLayoutWidget)
        self.pushButton_eliminar_ingrediente_agregar_formula.setObjectName(u"pushButton_eliminar_ingrediente_agregar_formula")

        self.horizontalLayout_funciones_ingredientes_agregar_formula.addWidget(self.pushButton_eliminar_ingrediente_agregar_formula)


        self.formLayout_agregar_formula.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_funciones_ingredientes_agregar_formula)

        self.label_ingredientes_formula_agregar_formula = QLabel(self.formLayoutWidget)
        self.label_ingredientes_formula_agregar_formula.setObjectName(u"label_ingredientes_formula_agregar_formula")

        self.formLayout_agregar_formula.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_ingredientes_formula_agregar_formula)

        self.tableView_ingredientes_agregar_formula = QTableView(self.formLayoutWidget)
        self.tableView_ingredientes_agregar_formula.setObjectName(u"tableView_ingredientes_agregar_formula")
        self.tableView_ingredientes_agregar_formula.setMinimumSize(QSize(400, 220))
        self.tableView_ingredientes_agregar_formula.setMaximumSize(QSize(400, 220))

        self.formLayout_agregar_formula.setWidget(4, QFormLayout.ItemRole.FieldRole, self.tableView_ingredientes_agregar_formula)

        self.label_instrucciones_agregar_formula = QLabel(self.formLayoutWidget)
        self.label_instrucciones_agregar_formula.setObjectName(u"label_instrucciones_agregar_formula")

        self.formLayout_agregar_formula.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_instrucciones_agregar_formula)

        self.textEdit_instrucciones_agregar_formula = QTextEdit(self.formLayoutWidget)
        self.textEdit_instrucciones_agregar_formula.setObjectName(u"textEdit_instrucciones_agregar_formula")
        self.textEdit_instrucciones_agregar_formula.setMinimumSize(QSize(400, 125))
        self.textEdit_instrucciones_agregar_formula.setMaximumSize(QSize(400, 125))

        self.formLayout_agregar_formula.setWidget(5, QFormLayout.ItemRole.FieldRole, self.textEdit_instrucciones_agregar_formula)

        self.horizontalLayout_funciones_definitivas__agregar_formula = QHBoxLayout()
        self.horizontalLayout_funciones_definitivas__agregar_formula.setSpacing(60)
        self.horizontalLayout_funciones_definitivas__agregar_formula.setObjectName(u"horizontalLayout_funciones_definitivas__agregar_formula")
        self.horizontalLayout_funciones_definitivas__agregar_formula.setContentsMargins(70, 5, 70, -1)
        self.pushButton_agregar_formula = QPushButton(self.formLayoutWidget)
        self.pushButton_agregar_formula.setObjectName(u"pushButton_agregar_formula")

        self.horizontalLayout_funciones_definitivas__agregar_formula.addWidget(self.pushButton_agregar_formula)

        self.pushButton_cancelar_agregar_formula = QPushButton(self.formLayoutWidget)
        self.pushButton_cancelar_agregar_formula.setObjectName(u"pushButton_cancelar_agregar_formula")

        self.horizontalLayout_funciones_definitivas__agregar_formula.addWidget(self.pushButton_cancelar_agregar_formula)


        self.formLayout_agregar_formula.setLayout(6, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_funciones_definitivas__agregar_formula)


        self.retranslate_ui(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_agregar_formula.setText(QCoreApplication.translate("Dialog", u"Agregar Fórmula", None))
        self.label_nombre_formula_agregar_formula.setText(QCoreApplication.translate("Dialog", u"Nombre de la Formula:", None))
        self.label_description_formula_agregar_formula.setText(QCoreApplication.translate("Dialog", u"Descripción de la formula:", None))
        self.pushButton_agregar_ingrediente_agregar_formula.setText(QCoreApplication.translate("Dialog", u"Agregar Ingrediente", None))
        self.pushButton_eliminar_ingrediente_agregar_formula.setText(QCoreApplication.translate("Dialog", u"Eliminar Ingrediente", None))
        self.label_ingredientes_formula_agregar_formula.setText(QCoreApplication.translate("Dialog", u"Ingredientes de la formula:", None))
        self.label_instrucciones_agregar_formula.setText(QCoreApplication.translate("Dialog", u"Instrucciones (opcional):", None))
        self.pushButton_agregar_formula.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
        self.pushButton_cancelar_agregar_formula.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

