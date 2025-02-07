import sys

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLayout, QLabel, QWidget, QGridLayout, QLineEdit,\
     QPushButton

from datetime import datetime


class AgeCalculater(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculater")
        layout=QGridLayout()

        self.name=QLabel("NAME")
        self.name_edit=QLineEdit()

        name_label=QLabel("date opf brith dd//mm/year")
        self.date_of_brith_edit =QLineEdit()

        calculate_button=QPushButton("calculate age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label=QLabel("")

        layout.addWidget(self.name,0,0)
        layout.addWidget(self.name_edit,0,1)
        layout.addWidget(name_label,1,0)
        layout.addWidget(self.date_of_brith_edit,1,1)
        layout.addWidget(calculate_button,2,0,1,2)
        layout.addWidget(self.output_label,3,0,1,2)

        self.setLayout(layout)
    def calculate_age(self):
        concurrent_year=datetime.now().year
        date_of_brith=self.date_of_brith_edit.text()
        year_of_brith=datetime.strptime(date_of_brith,"%d/%m/%Y").year
        age=concurrent_year-year_of_brith
        self.output_label.setText(f"{self.name_edit.text()} is {age} year old")

app=QApplication(sys.argv)
age=AgeCalculater()
age.show()
sys.exit(app.exec())