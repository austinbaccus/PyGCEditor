from PyQt5.QtWidgets import QHeaderView, QTableWidget

class QtTableWidgetFactory():
    def __init__(self):
        pass
    
    def construct(self, label = ["Empty"], columns = 1) -> QTableWidget:
        tableWidget: QTableWidget = QTableWidget()
        tableWidget.setColumnCount(columns)
        tableWidget.setHorizontalHeaderLabels(label)
        tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        tableWidget.verticalHeader().setVisible(False)
        return tableWidget

    