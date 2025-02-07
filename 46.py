from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QToolBar, \
    QHBoxLayout, QStatusBar, QLabel
from PyQt6.QtGui import QAction
import sys
import sqlite3

from matplotlib.backend_bases import cursors
from streamlit import button, connection


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")


        file_menu_item=self.menuBar().addMenu("&File")
        help_menu_item=self.menuBar().addMenu("&Help")
        edit_menu_item=self.menuBar().addMenu("edit")

        file_menu_action=QAction("add student",self)
        file_menu_action.triggered.connect(self.insert)
        file_menu_item.addAction(file_menu_action)

        help_menu_action=QAction("About",self)
        help_menu_item.addAction(help_menu_action)

        edit=QAction("search",self)
        edit_menu_item.addAction(edit)
        edit_menu_item.triggered.connect(self.search)


        self.tabel=QTableWidget()
        self.tabel.setColumnCount(4)
        self.tabel.setHorizontalHeaderLabels(["id","name","course","mobile"])
        self.tabel.verticalHeader().setVisible(False)
        self.setCentralWidget(self.tabel)


        # create toolbar and toolbar elements
        toolbar=QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(file_menu_action)
        toolbar.addAction(edit)

        # create status bar and add status bar elements
        self.statusbar=QStatusBar()
        self.setStatusBar(self.statusbar)

        self.tabel.cellClicked.connect(self.cell_clicked)


    def cell_clicked(self):
        edit_button=QPushButton("edit records")
        edit_button.clicked.connect(self.edit)

        delite_button=QPushButton("delete records")
        delite_button.clicked.connect(self.delete)

        children=self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)
        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delite_button)

    def edit(self):
        dialog=EditDialog()
        dialog.exec()

    def delete(self):
        dialog=DeleteDialog()
        dialog.exec()



    def load_data(self):
        connection=sqlite3.connect("database.db")
        cursor=connection.cursor()
        cursor.execute("select * from students")
        result=cursor.fetchall()
        self.tabel.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tabel.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tabel.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        connection.close()



    def insert(self):
        dialog=InsertDialog()
        dialog.exec()

    def search(self):
        dialog=SearchDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # add student name widget
        layout=QVBoxLayout()
        self.student_name=QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)


        #add courses name widget
        course=["Biology","Math","Astronomy","Pyhsics"]
        self.course_name=QComboBox()
        self.course_name.addItems(course)
        layout.addWidget(self.course_name)

        # add mobile number in widget
        self.mobile=QLineEdit()
        self.mobile.setPlaceholderText("Mobile Number")
        layout.addWidget(self.mobile)

        # add a submit button55
        button1= QPushButton("Register")
        button1.clicked.connect(self.add_student)
        layout.addWidget(button1)


        self.setLayout(layout)

    def add_student(self):
        name=self.student_name.text()
        course=self.course_name.itemText(self.course_name.currentIndex())
        mobile=self.mobile.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("insert into students (name,course,mobile) values(?,?,?)",(name,course,mobile))
        connection.commit()
        cursor.close()
        connection.close()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout=QVBoxLayout()
        self.student_name=QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        button=QPushButton("Search")
        button.clicked.connect(self.search)
        layout.addWidget(button)

        self.setLayout(layout)

    def search(self):
        name=self.student_name.text()
        connection1=sqlite3.connect("database.db")
        cursor=connection1.cursor()
        result=cursor.execute("select * from students where name = ?",(name,))
        row=list(result)
        print(row)
        items=main.tabel.findItems(name,Qt.MatchFlag.MatchFixedString)
        for  item in items:
            print(item)
            main.tabel.item(item.row(),1).setSelected(True)

        cursor.close()
        connection1.close()


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # add student name widget
        layout=QVBoxLayout()

        #get student name from selected row
        index=main.tabel.currentRow()
        student_name=main.tabel.item(index,1).text()

        #get id row selected row
        self.student_id=main.tabel.item(index,0).text()


        self.student_name=QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)


        #add courses name widget
        course_name=main.tabel.item(index,2).text()
        course=["Biology","Math","Astronomy","Pyhsics"]
        self.course_name=QComboBox()
        self.course_name.addItems(course)
        self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)

        # add mobile number in widget
        mobile=main.tabel.item(index,3).text()
        self.mobile=QLineEdit(mobile)
        self.mobile.setPlaceholderText("Mobile Number")
        layout.addWidget(self.mobile)

        # add a submit button55
        button1= QPushButton("update")
        button1.clicked.connect(self.update)
        layout.addWidget(button1)


        self.setLayout(layout)

    def update(self):
        connection1=sqlite3.connect("database.db")
        cursor=connection1.cursor()
        cursor.execute("UPDATE students SET name= ?, course= ?, mobile= ? where id=?",
                        (self.student_name.text(),self.course_name.itemText(self.course_name.currentIndex()),
                         self.mobile.text(),self.student_id))

        connection1.commit()
        cursor.close()
        connection1.close()
        main.load_data()

class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("delete data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout=QHBoxLayout()
        index=main.tabel.currentRow()
        student=main.tabel.item(index,1).text()
        self.student_name=QLineEdit(student)
        self.student=QLabel('student name')

        button=QPushButton("ok")
        button.clicked.connect(self.ok)

        layout.addWidget(self.student)
        layout.addWidget(self.student_name)


        layout.addWidget(button)

        self.setLayout(layout)

    def ok(self):
        index=main.tabel.currentRow()
        student_id=main.tabel.item(index,0).text()

        connection1 = sqlite3.connect("database.db")
        cursor = connection1.cursor()
        cursor.execute("delete from students where id = ?",(student_id, ))

        connection1.commit()
        cursor.close()
        connection1.close()
        main.load_data()


app=QApplication(sys.argv)
main=MainWindow()
main.load_data()
main.show()
sys.exit(app.exec())