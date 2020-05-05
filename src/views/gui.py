import socket

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QPen
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
import sys
import os

sys.path.append(os.path.dirname(__file__) + "/..")
from QGraphViz.QGraphViz import QGraphViz
from QGraphViz.DotParser import Graph
from QGraphViz.Engines import Dot

from PyQt5.QtGui import QFont

window = None


def Calendar(x, y):
    item = QCalendarWidget()
    item.move(x, y)
    item.adjustSize()
    return item


def Graphics(self, x, y):
    item = QGraphViz(window,
                     auto_freeze=True,
                     hilight_Nodes=True,
                     )
    item.setStyleSheet("background-color:white;")
    item.new(Dot(Graph("Main_Graph"), font=QFont("Arial", 12), margins=[40, 40]))
    item.move(x, y)
    item.resize(1150, 500)
    self.widgets.append(item)
    return item


def Label(self, name, x, y):
    item = QLabel(name, window)
    item.move(x, y)
    item.adjustSize()
    self.widgets.append(item)
    return item


def Button(self, name, x, y, icon=None):
    item = QPushButton(name, window)
    item.move(x, y)
    item.adjustSize()
    self.widgets.append(item)
    if icon is not None:
        item.setIcon(QIcon(QPixmap('../../res/icons/' + icon)))
    return item


def CheckBox(self, name, x, y):
    item = QCheckBox(name, window)
    item.move(x, y)
    item.adjustSize()
    self.widgets.append(item)
    return item


def Table(self, x, y):
    item = QTableWidget(window)
    item.move(x, y)
    item.adjustSize()
    self.widgets.append(item)
    return item


def LineEdit(self, name, x, y):
    item = QLineEdit(name, window)
    item.move(x, y)
    item.adjustSize()
    self.widgets.append(item)
    return item


def TextBox(self, x, y):
    item = QPlainTextEdit(window)
    item.move(x, y)
    item.adjustSize()
    self.widgets.append(item)
    return item


def ComboBox(self, x, y):
    item = QComboBox(window)
    item.move(x, y)
    item.adjustSize()
    self.widgets.append(item)
    return item


class PICK_UI(QWidget):

    def __init__(self):
        super().__init__()
        global window
        window = self
        self.title = 'PICK'
        self.left = 100
        self.top = 100
        self.width = 1280
        self.height = 720
        self.widgets = []

        self.lbl_coord = Label(self, '', 5, 690)
        self.lbl_coord.resize(200, 40)
        self.setMouseTracking(True)

        self.team_ui = TeamView()
        self.event_ui = EventView()
        self.directory_ui = DirectoryView()
        self.vector_ui = VectorView()
        self.log_file_ui = LogFileView()
        self.filter_ui = FilterView()
        self.graph_ui = GraphView()
        self.vector_table_ui = TableView()
        self.relationships_ui = RelationshipsView()

        self.ui = View()

        self.init_ui()

    def mouseMoveEvent(self, event):
        self.lbl_coord.setText('x:%d  y:%d' % (event.x(), event.y()))

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.load(self.team_ui)
        self.show()

    def load(self, ui):
        if self.ui == ui:
            return
        self.ui.clear()
        for w in ui.widgets:
            w.show()
        self.ui = ui


class View:
    def __init__(self):
        self.widgets = []

    def clear(self):
        for w in self.widgets:
            w.hide()


class TeamView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Team Configuration<\\h1>', 50, 50)
        self.chk_lead = CheckBox(self, 'Lead', 400, 200)
        self.lbl_lead_ip = Label(self, 'Lead IP Address:', 400, 300)
        self.lin_lead_ip_value = LineEdit(self, '', 600, 300)
        self.lbl_no_connections = Label(self, 'Established connections: ', 400, 400)
        self.lbl_val_no_connections = Label(self, '', 600, 400)
        self.lbl_ip = Label(self, 'IP Address:', 400, 500)
        self.lbl_ip_value = Label(self, socket.gethostbyname(socket.gethostname()), 600, 500)
        self.btn_continue = Button(self, 'Continue', 1000, 600)
        self.btn_continue.setVisible(False)
        self.btn_connect = Button(self, 'Connect', 1000, 600)

        self.clear()


class EventView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Event Configuration<\\h1>', 50, 50)
        self.lbl_name = Label(self, 'Event Name: ', 300, 150)
        self.lin_name = LineEdit(self, '', 400, 150)
        self.lbl_description = Label(self, 'Event Description: ', 300, 200)
        self.txt_description = TextBox(self, 400, 200)
        self.lbl_start_time = Label(self, 'Start Time: ', 300, 400)
        self.lin_start_date = LineEdit(self, '', 400, 400)
        self.btn_cal_start_date = Button(self, '', 470, 399, 'calendar.png')
        self.btn_cal_start_date.resize(22, 22)
        self.cal_start_date = Calendar(600, 400)
        self.cal_start_date.hide()
        self.cal_start_date.setWindowTitle('Start Date')
        self.lin_start_time = LineEdit(self, '', 510, 400)
        self.lbl_end_time = Label(self, 'End Time: ', 300, 450)
        self.lin_end_date = LineEdit(self, '', 400, 450)
        self.btn_cal_end_date = Button(self, '', 470, 449, 'calendar.png')
        self.btn_cal_end_date.resize(22, 22)
        self.cal_end_date = Calendar(600, 400)
        self.cal_end_date.hide()
        self.cal_start_date.setWindowTitle('End Date')
        self.lin_end_time = LineEdit(self, '', 510, 450)
        self.btn_back = Button(self, 'Back', 200, 600)
        self.btn_save = Button(self, 'Continue', 1000, 600)
        self.lin_name.resize(300, 20)
        self.txt_description.resize(500, 160)
        self.lin_start_date.setPlaceholderText('MM/DD/YYYY')
        self.lin_start_date.resize(70, 20)
        self.lin_start_time.setPlaceholderText('HH:MM:SS')
        self.lin_start_time.resize(60, 20)
        self.lin_end_date.setPlaceholderText('MM/DD/YYYY')
        self.lin_end_date.resize(70, 20)
        self.lin_end_time.setPlaceholderText('HH:MM:SS')
        self.lin_end_time.resize(60, 20)

        self.clear()


class DirectoryView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Directory Configuration<\\h1>', 50, 50)
        self.lbl_root_dir = Label(self, 'Root Directory: ', 350, 250)
        self.lin_root_dir = LineEdit(self, '', 450, 250)
        self.btn_browse = Button(self, 'Browse', 800, 250)
        self.lbl_red_dir = Label(self, 'Red Directory: ', 350, 300)
        self.lin_red_dir = Label(self, '', 450, 300)
        self.lbl_blue_dir = Label(self, 'Blue Directory: ', 350, 350)
        self.lin_blue_dir = Label(self, '', 450, 350)
        self.lbl_white_dir = Label(self, 'White Directory: ', 350, 400)
        self.lin_white_dir = Label(self, '', 450, 400)
        self.lbl_splunk = Label(self, '<h3>Splunk</h3>', 350, 500)
        self.lbl_user = Label(self, 'Username: ', 350, 550)
        self.lin_user = LineEdit(self, '', 410, 550)
        self.lbl_password = Label(self, 'Password: ', 600, 550)
        self.lin_password = LineEdit(self, '', 660, 550)
        self.lin_password.setEchoMode(QLineEdit.Password)
        self.btn_ingestion = Button(self, 'Start Ingestion', 1000, 600)
        self.lin_root_dir.resize(340, 20)

        self.clear()


class VectorView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Vectors<\\h1>', 50, 50)
        self.tbl_vector = Table(self, 150, 100)
        self.btn_add = Button(self, 'Add Vector', 50, 100)
        self.btn_delete = Button(self, 'Delete Vector', 50, 150)
        self.btn_save = Button(self, 'Continue', 1000, 630)
        self.tbl_vector.setRowCount(1)
        self.tbl_vector.setColumnCount(2)
        self.tbl_vector.setMinimumSize(1050, 500)
        self.tbl_vector.setColumnWidth(0, 200)
        self.tbl_vector.setColumnWidth(1, 800)
        self.tbl_vector.setHorizontalHeaderLabels(['Vector Name', 'Vector Description'])

        self.clear()


class LogFileView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Log Entries<\\h1>', 50, 50)
        self.tbl_logs = Table(self, 50, 150)
        self.btn_continue = Button(self, 'Continue', 1125, 660)
        self.tbl_logs.setRowCount(2)
        self.tbl_logs.setColumnCount(5)
        self.tbl_logs.setHorizontalHeaderLabels(
            ['Name', 'Timestamp', 'Description', 'Creator', 'Source'])
        self.tbl_logs.setMinimumSize(1150, 500)
        self.tbl_logs.setColumnWidth(0, 135)
        self.tbl_logs.setColumnWidth(1, 150)
        self.tbl_logs.setColumnWidth(2, 400)
        self.tbl_logs.setColumnWidth(3, 65)
        self.tbl_logs.setColumnWidth(4, 380)

        self.clear()


class FilterView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Filter Configuration<\\h1>', 50, 50)
        self.lbl_search = Label(self, 'Keyword Search: ', 100, 200)
        self.lin_search = LineEdit(self, '', 200, 200)
        self.lbl_creator = Label(self, 'Creator', 300, 300)
        self.chk_filter_red = CheckBox(self, 'Red', 300, 300)
        self.chk_filter_blue = CheckBox(self, 'Blue', 300, 350)
        self.chk_filter_white = CheckBox(self, 'White', 300, 400)
        self.lin_start = LineEdit(self, 'Start Timestamp', 200, 200)
        self.lin_end = LineEdit(self, 'End Timestamp', 200, 200)

        self.clear()


class GraphView(View):
    def __init__(self):
        super().__init__()
        self.blackpen = QPen(Qt.black)
        self.lbl_title = Label(self, '<h1>Graph<\\h1>', 50, 50)
        self.graph = Graphics(self, 50, 150)
        self.cmb_vectors = ComboBox(self, 50, 100)
        self.cmb_vectors.resize(150, 20)
        self.btn_table = Button(self, "Table", 50, 660)
        self.btn_relationships = Button(self, "Relationships", 150, 660)
        self.btn_save = Button(self, 'Save', 1125, 660)

        self.clear()


class TableView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Vector Table<\\h1>', 50, 50)
        self.tbl_logs = Table(self, 50, 150)
        self.btn_graph = Button(self, "Graph", 50, 660)
        self.btn_relationships = Button(self, "Relationships", 150, 660)
        self.cmb_vectors = ComboBox(self, 50, 100)
        self.cmb_vectors.resize(150, 20)
        # self.tbl_logs.setRowCount(2)
        self.tbl_logs.setColumnCount(10)
        self.tbl_logs.setHorizontalHeaderLabels(
            ['Significant', 'Visible', 'ID', 'Name', 'Timestamp', 'Description', 'Creator', 'Event Type', 'Icon',
             'Source'])
        self.tbl_logs.setMinimumSize(1150, 500)

        self.clear()


class RelationshipsView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Relationship Configuration<\\h1>', 50, 50),
        self.tbl_relationships = Table(self, 50, 150)
        self.cmb_vectors = ComboBox(self, 50, 100)
        self.cmb_vectors.resize(150, 20)
        self.tbl_relationships.setRowCount(1)
        self.tbl_relationships.setColumnCount(2)
        self.tbl_relationships.setHorizontalHeaderLabels(
            ['Parent', 'Child'])
        self.tbl_relationships.setMinimumSize(1150, 500)
        self.btn_table = Button(self, "Table", 50, 660)
        self.btn_graph = Button(self, "Graph", 150, 660)
        self.btn_add = Button(self, 'Add Row', 1125, 660)

        self.clear()
