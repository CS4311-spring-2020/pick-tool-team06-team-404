import sys
import socket
from src import AdversarialAssessment as aa
from src import Vector, LogEntry
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from src.splunk import SplunkTest
import datetime
import os
import csv


def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%m/%d/%Y')
        return True
    except ValueError:
        return False


def validate_time(time_text):
    try:
        datetime.datetime.strptime(time_text, '%H:%M:%S')
        return True
    except ValueError:
        return False


def FileDialog():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    options |= QFileDialog.DontUseCustomDirectoryIcons
    dialog = QFileDialog()
    dialog.setOptions(options)

    dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)

    # ARE WE TALKING ABOUT FILES OR FOLDERS

    dialog.setFileMode(QFileDialog.DirectoryOnly)
    # OPENING OR SAVING
    dialog.setAcceptMode(QFileDialog.AcceptOpen)

    # SET THE STARTING DIRECTORY
    dialog.setDirectory(str(os.getcwd()))

    if dialog.exec_() == QDialog.Accepted:
        path = dialog.selectedFiles()[0]  # returns a list
        return path
    else:
        return ''


# Check box  	chk
# Combo box     cmb
# Button	    btn
# Form       	frm
# Group box	    grp
# Label	        lbl
# Line edit	    lin
# List box	    lst
# Radio button	rdb
# Picture box	pic
# Tab control	tab
# Text box	    txt
# Timer	        tmr
# Table	        tbl

# enums
CheckBox = 1
Button = 2
Label = 3
LineEdit = 4
RadioButton = 5
TextBox = 6
Table = 7
ComboBox = 8


def clear_widgets(widgets):
    for w in widgets:
        widgets[w].hide()


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.aa = aa.AdversarialAssessment()
        self.menu_buttons = []
        self.title = 'PICK'
        self.left = 100
        self.top = 100
        self.width = 1280
        self.height = 720
        self.create_widgets()

        clear_widgets(self.team_widgets)
        clear_widgets(self.event_widgets)
        clear_widgets(self.directory_widgets)
        clear_widgets(self.vector_widgets)
        clear_widgets(self.log_file_widgets)
        clear_widgets(self.filter_widgets)
        clear_widgets(self.log_entry_widgets)
        clear_widgets(self.export_widgets)
        clear_widgets(self.change_widgets)
        clear_widgets(self.vector_db_widgets)
        clear_widgets(self.icon_widgets)
        clear_widgets(self.graph_builder_widgets)
        clear_widgets(self.vector_table_widgets)
        clear_widgets(self.vector_graph_widgets)
        clear_widgets(self.relationships_widgets)

        self.current_widgets = {}

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.set_menu_buttons()
        self.team_ui_clicked()
        self.show()

    def set_menu_buttons(self):
        buttons = {
            'Exit': self.close,
            'Team': self.team_ui_clicked,
            'Event': self.event_ui_clicked,
            'Directory': self.directory_ui_clicked,
            'Vector': self.vector_ui_clicked,
            'Log File': self.log_file_ui_clicked,
            'Filter': self.filter_ui_clicked,
            'Log Entry': self.log_entry_ui_clicked,
            'Export': self.export_ui_clicked,
            'Change': self.change_ui_clicked,
            'Vector DB': self.vector_db_ui_clicked,
            'Icon': self.icon_ui_clicked,
            'Graph Builder': self.graph_builder_ui_clicked,
            'Vector Table': self.table_ui_clicked,
            'Vector Graph': self.graph_ui_clicked,
            'Relationships': self.relationship_ui_clicked}

        i = 0
        for k in buttons:
            btn = QPushButton(k, self)
            btn.move(i * 80, 0)
            btn.adjustSize()
            btn.clicked.connect(buttons[k])
            btn.show()
            self.menu_buttons.append(btn)
            i += 1

    def add(self, qclass, name, x, y):
        item = None
        if qclass == Label:
            item = QLabel(name, self)
        elif qclass == Button:
            item = QPushButton(name, self)
        elif qclass == CheckBox:
            item = QCheckBox(name, self)
        elif qclass == LineEdit:
            item = QLineEdit(name, self)
        elif qclass == Table:
            item = QTableWidget(self)
        elif qclass == ComboBox:
            item = QComboBox(self)
        elif qclass == TextBox:
            item = QPlainTextEdit(self)
        item.move(x, y)
        item.adjustSize()
        return item

    def load(self, widgets):
        if self.current_widgets == widgets:
            return
        self.clear()
        for w in widgets:
            widgets[w].show()
        self.current_widgets = widgets
        self.show()

    def clear(self):
        for w in self.current_widgets:
            self.current_widgets[w].hide()

    def create_widgets(self):
        self.team_widgets = {
            'lbl_title': self.add(Label, '<h1>Team Configuration<\\h1>', 50, 50),
            'chk_lead': self.add(CheckBox, 'Lead', 400, 200),
            'lbl_lead_ip': self.add(Label, 'Lead IP Address:', 400, 300),
            'lin_lead_ip_value': self.add(LineEdit, '', 600, 300),
            'lbl_no_connections': self.add(Label, 'Established connections: ', 400, 400),
            'lbl_val_no_connections': self.add(Label, '', 600, 400),  # 4
            'lbl_ip': self.add(Label, 'IP Address:', 400, 500),
            'lbl_ip_value': self.add(Label, socket.gethostbyname(socket.gethostname()), 600, 500),
            'btn_continue': self.add(Button, 'Continue', 1000, 600),
            'btn_connect': self.add(Button, 'Connect', 1000, 600)}
        self.team_widgets['btn_continue'].setVisible(False)
        self.team_widgets['chk_lead'].clicked.connect(self.team_chk_lead_clicked)
        self.team_widgets['btn_connect'].clicked.connect(self.team_btn_connect_clicked)
        self.team_widgets['btn_continue'].clicked.connect(self.team_btn_continue_clicked)

        self.event_widgets = {
            'lbl_title': self.add(Label, '<h1>Event Configuration<\\h1>', 50, 50),
            'lbl_name': self.add(Label, 'Event Name: ', 300, 200),
            'lin_name': self.add(LineEdit, '', 400, 200),
            'lbl_description': self.add(Label, 'Event Description: ', 300, 250),
            'txt_description': self.add(TextBox, '', 400, 250),
            'lbl_start_time': self.add(Label, 'Start Time: ', 300, 450),
            'lin_start_date': self.add(LineEdit, '', 400, 450),
            'lin_start_time': self.add(LineEdit, '', 480, 450),
            'lbl_end_time': self.add(Label, 'End Time: ', 300, 500),
            'lin_end_date': self.add(LineEdit, '', 400, 500),
            'lin_end_time': self.add(LineEdit, '', 480, 500),
            'btn_save': self.add(Button, 'Save', 1000, 600)}
        self.event_widgets['lin_name'].resize(300, 20)
        self.event_widgets['txt_description'].resize(500, 160)
        self.event_widgets['lin_start_date'].setPlaceholderText('MM/DD/YYYY')
        self.event_widgets['lin_start_date'].resize(70, 20)
        self.event_widgets['lin_start_time'].setPlaceholderText('HH:MM:SS')
        self.event_widgets['lin_start_time'].resize(60, 20)
        self.event_widgets['lin_end_date'].setPlaceholderText('MM/DD/YYYY')
        self.event_widgets['lin_end_date'].resize(70, 20)
        self.event_widgets['lin_end_time'].setPlaceholderText('HH:MM:SS')
        self.event_widgets['lin_end_time'].resize(60, 20)
        self.event_widgets['btn_save'].clicked.connect(self.event_btn_save_clicked)

        self.directory_widgets = {
            'lbl_title': self.add(Label, '<h1>Directory Configuration<\\h1>', 50, 50),
            'lbl_root_dir': self.add(Label, 'Root Directory: ', 350, 250),
            'lin_root_dir': self.add(LineEdit, '', 450, 250),
            'btn_browse': self.add(Button, 'Browse', 800, 250),
            'lbl_red_dir': self.add(Label, 'Red Directory: ', 350, 300),
            'lin_red_dir': self.add(Label, '', 450, 300),
            'lbl_blue_dir': self.add(Label, 'Blue Directory: ', 350, 350),
            'lin_blue_dir': self.add(Label, '', 450, 350),
            'lbl_white_dir': self.add(Label, 'White Directory: ', 350, 400),
            'lin_white_dir': self.add(Label, '', 450, 400),
            'btn_ingestion': self.add(Button, 'Start Ingestion', 1000, 600)}
        self.directory_widgets['lin_root_dir'].resize(340, 20)
        self.directory_widgets['lin_root_dir'].textChanged.connect(self.directory_directory_changed)
        self.directory_widgets['btn_browse'].clicked.connect(self.directory_browse_clicked)
        self.directory_widgets['btn_ingestion'].clicked.connect(self.directory_ingest_clicked)

        self.vector_widgets = {
            'lbl_title': self.add(Label, '<h1>Vector Configuration<\\h1>', 50, 50),
            'tbl_vector': self.add(Table, None, 100, 200),
            'btn_add': self.add(Button, 'Add Vector', 400, 600),
            'btn_delete': self.add(Button, 'Delete Vector', 600, 600),
            'btn_save': self.add(Button, 'Save Changes', 800, 600)}
        self.vector_widgets['tbl_vector'].setRowCount(1)
        self.vector_widgets['tbl_vector'].setColumnCount(2)
        self.vector_widgets['tbl_vector'].setMinimumSize(1050, 360)
        self.vector_widgets['tbl_vector'].setColumnWidth(0, 200)
        self.vector_widgets['tbl_vector'].setColumnWidth(1, 800)
        self.vector_widgets['tbl_vector'].setHorizontalHeaderLabels(['Vector Name', 'Vector Description'])
        self.vector_widgets['btn_add'].clicked.connect(self.vector_add_clicked)
        self.vector_widgets['btn_delete'].clicked.connect(self.vector_delete_clicked)
        self.vector_widgets['btn_save'].clicked.connect(self.vector_save_clicked)

        self.log_file_widgets = {
            'lbl_title': self.add(Label, '<h1>Log File Configuration<\\h1>', 50, 50),
            'tbl_log_file': self.add(Table, None, 100, 100),
            'tbl_file_action_report': self.add(Table, None, 100, 300),
            'btn_validate': self.add(Button, "Validate", 100, 300),
            'btn_cancel': self.add(Button, "Cancel", 100, 300)}
        self.log_file_widgets['tbl_log_file'].setHorizontalHeaderLabels(
            ['File Name', 'Source', 'Cleansing Status', 'Validation', 'Ingestion Status', 'View EA Report'])
        self.log_file_widgets['tbl_log_file'].setRowCount(34)
        self.log_file_widgets['tbl_log_file'].setColumnCount(6)
        self.log_file_widgets['tbl_file_action_report'].setRowCount(34)
        self.log_file_widgets['tbl_file_action_report'].setColumnCount(3)
        self.log_file_widgets['tbl_file_action_report'].setHorizontalHeaderLabels(
            ['File Name', 'Line Number', 'Error Message'])

        self.filter_widgets = {
            'lbl_title': self.add(Label, '<h1>Filter Configuration<\\h1>', 50, 50),
            'lbl_search': self.add(Label, 'Keyword Search: ', 100, 200),
            'lin_search': self.add(LineEdit, '', 200, 200),
            'lbl_creator': self.add(Label, 'Creator', 300, 300),
            'chk_filter_red': self.add(CheckBox, 'Red', 300, 300),
            'chk_filter_blue': self.add(CheckBox, 'Blue', 300, 350),
            'chk_filter_white': self.add(CheckBox, 'White', 300, 400),
            'lin_start': self.add(LineEdit, 'Start Timestamp', 200, 200),
            'lin_end': self.add(LineEdit, 'End Timestamp', 200, 200)}

        self.log_entry_widgets = {
            'lbl_title': self.add(Label, '<h1>Log Entry<\\h1>', 50, 50),
            'tbl_log_entry': self.add(Table, None, 100, 100)}
        self.log_entry_widgets['tbl_log_entry'].setRowCount(34)
        self.log_entry_widgets['tbl_log_entry'].setColumnCount(5)
        self.log_entry_widgets['tbl_log_entry'].setHorizontalHeaderLabels(
            ['', 'List Number', 'Log Entry Timestamp', 'Log Entry Event', 'Vector'])

        self.export_widgets = {
            'lbl_title': self.add(Label, '<h1>Export<\\h1>', 50, 50),
            'cmb_export': self.add(ComboBox, None, 200, 200),
            'btn_export': self.add(Button, 'Export', 300, 300)}
        self.export_widgets['cmb_export'].addItem('PDF')
        self.export_widgets['cmb_export'].addItem('GIF')
        self.export_widgets['cmb_export'].addItem('ABC')

        self.change_widgets = {
            'lbl_title': self.add(Label, '<h1>Change List<\\h1>', 50, 50),
            'btn_undo': self.add(Button, 'Undo', 100, 100),
            'btn_commit': self.add(Button, 'Commit', 100, 200)}

        self.vector_db_widgets = {
            'lbl_title': self.add(Label, '<h1>Vector Data Base<\\h1>', 50, 50),
            'lbl_connection': self.add(Label, 'Connection status to lead: ', 200, 200),
            'lbl_connection_val': self.add(Label, '4', 200, 200),  # 4 is hardcoded
            'lbl_pulled_table': self.add(Label, 'PULLED vector DB table (Analyst)', 200, 200),
            'tbl_pulled': self.add(Table, None, 300, 300),
            'btn_pull': self.add(Button, 'Pull', 500, 500),
            'lbl_pushed_table': self.add(Label, 'PUSHED vector DB table (Analyst)', 200, 400),
            'tbl_pushed': self.add(Table, None, 300, 300),
            'btn_push': self.add(Button, 'Push', 500, 500)}
        self.vector_db_widgets['tbl_pulled'].setRowCount(34)
        self.vector_db_widgets['tbl_pulled'].setColumnCount(1)
        self.vector_db_widgets['tbl_pushed'].setRowCount(34)
        self.vector_db_widgets['tbl_pushed'].setColumnCount(1)

        self.icon_widgets = {
            'lbl_title': self.add(Label, '<h1>Icon Configuration<\\h1>', 50, 50),
            'tbl_icon': self.add(Table, None, 100, 200),
            'btn_add_icon': self.add(Button, 'Add Icon', 100, 100),
            'btn_delete_icon': self.add(Button, 'Delete Icon', 100, 100),
            'btn_edit_icon': self.add(Button, 'Edit Icon', 100, 100)}
        self.icon_widgets['tbl_icon'].setRowCount(34)
        self.icon_widgets['tbl_icon'].setColumnCount(4)
        self.icon_widgets['tbl_icon'].setHorizontalHeaderLabels(['Select', 'Icon Name', 'Icon Source', 'Image Preview'])

        self.graph_builder_widgets = {
            'lbl_title': self.add(Label, '<h1Graph Builder<\\h1>', 50, 50),
            'cmb_graph_builder': self.add(ComboBox, None, 200, 200),
            'lbl_description': self.add(Label, 'Description: ', 200, 200),
            'lin_description': self.add(LineEdit, None, 200, 200),
            'btn_add_node': self.add(Button, 'Add Node', 200, 200),
            'btn_delete_node': self.add(Button, 'Delete Node', 200, 200),
            'btn_edit_node': self.add(Button, 'Edit Node', 200, 200),
            'btn_add_relationship': self.add(Button, 'Add Relationship', 200, 200),
            'btn_delete_relationship': self.add(Button, 'Delete Relationship', 200, 200),
            'btn_edit_relationship': self.add(Button, 'Edit Relationship', 200, 200)}
        self.graph_builder_widgets['cmb_graph_builder'].addItem('example vector 1')
        self.graph_builder_widgets['cmb_graph_builder'].addItem('example vector 2')

        self.vector_table_widgets = {
            'lbl_title': self.add(Label, '<h1>Vector Table<\\h1>', 50, 50),
            'tbl_logs': self.add(Table, None, 50, 100)}
        self.vector_table_widgets['tbl_logs'].setRowCount(2)
        self.vector_table_widgets['tbl_logs'].setColumnCount(10)
        self.vector_table_widgets['tbl_logs'].setHorizontalHeaderLabels(
            ['Visibile', 'Node ID', 'Node Name', 'Node Timestamp', 'Node Description',
             'Reference', 'Log Creator', 'Event Type', 'Icon Type', 'Source'])
        self.vector_table_widgets['tbl_logs'].setMinimumSize(1150, 560)

        self.vector_graph_widgets = {
            'lbl_title': self.add(Label, '<h1>Vector Graph<\\h1>', 50, 50),
            'lbl_timeline_orientation': self.add(Label, 'Timeline Orientation', 200, 200),
            'cmb_timeline_orientation': self.add(ComboBox, None, 200, 200),
            'lbl_interval_units': self.add(Label, 'Interval Units', 300, 300),
            'cmb_interval_units': self.add(ComboBox, None, 300, 300),
            'lbl_timeline': self.add(Label, 'A TIMELINE IS SUPPOSED TO GO HERE', 200, 200),
            'btn_zoom_in': self.add(Button, 'Zoom In', 300, 300),
            'btn_zoom_out': self.add(Button, 'Zoom Out', 300, 300)}
        self.vector_graph_widgets['cmb_timeline_orientation'].addItem('example orientation')
        self.vector_graph_widgets['cmb_interval_units'].addItem('example interval unit')

        self.relationships_widgets = {
            'lbl_title': self.add(Label, '<h1>Relationship Configuration<\\h1>', 50, 50),
            'tbl_relationship': self.add(Table, None, 200, 200)}
        self.relationships_widgets['tbl_relationship'].setRowCount(34)
        self.relationships_widgets['tbl_relationship'].setColumnCount(7)

    def team_chk_lead_clicked(self):
        x = False if self.team_widgets['chk_lead'].isChecked() else True
        self.team_widgets['lin_lead_ip_value'].setEnabled(x)
        self.team_widgets['btn_continue'].setVisible(not x)
        self.team_widgets['btn_connect'].setVisible(x)

    def team_btn_connect_clicked(self):
        x = 0

    def team_btn_continue_clicked(self):
        self.load(self.event_widgets)

    def team_ui_clicked(self):
        self.load(self.team_widgets)

    def event_ui_clicked(self):
        self.load(self.event_widgets)

    def event_btn_save_clicked(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setStyleSheet("QLabel{min-width: 200px;}")
        x = self.event_widgets
        if x['lin_name'].text() == '':
            msg.setText("Event name can't be empty")
            msg.exec_()
            return
        if not validate_date(x['lin_start_date'].text()):
            msg.setText("Wrong 'Start date' format")
            msg.exec_()
            return
        if not validate_time(x['lin_start_time'].text()):
            msg.setText("Wrong 'Start time' format")
            msg.exec_()
        if not validate_date(x['lin_end_date'].text()):
            msg.setText("Wrong 'End date' format")
            msg.exec_()
            return
        if not validate_time(x['lin_end_time'].text()):
            msg.setText("Wrong 'End time' format")
            msg.exec_()
            return
        self.aa.name = x['lin_name'].text()
        print('hir')
        self.aa.description = x['txt_description'].toPlainText()
        print('hir')
        self.aa.time_start = x['lin_start_date'].text() + '-' + x['lin_start_time'].text()
        print('hir')
        self.aa.time_end = x['lin_end_date'].text() + '-' + x['lin_end_time'].text()
        print('hir')

        self.load(self.directory_widgets)

    def directory_ui_clicked(self):
        self.load(self.directory_widgets)

    def directory_browse_clicked(self):
        self.directory_widgets['lin_root_dir'].setText(FileDialog())

    def directory_directory_changed(self):
        x = self.directory_widgets['lin_root_dir'].text()
        self.directory_widgets['lin_red_dir'].setText(x + '/red')
        self.directory_widgets['lin_white_dir'].setText(x + '/white')
        self.directory_widgets['lin_blue_dir'].setText(x + '/blue')
        self.directory_widgets['lin_red_dir'].resize(400, 20)
        self.directory_widgets['lin_white_dir'].resize(400, 20)
        self.directory_widgets['lin_blue_dir'].resize(400, 20)
        isdir = os.path.isdir(self.directory_widgets['lin_root_dir'].text() + '/red')

    def directory_ingest_clicked(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setStyleSheet("QLabel{min-width: 200px;}")
        dir = self.directory_widgets['lin_root_dir'].text()
        if not os.path.isdir(dir):
            msg.setText("Root directory not found")
            msg.exec_()
            return
        if not os.path.isdir(dir + '/red'):
            msg.setText("Red directory not found")
            msg.exec_()
            return
        if not os.path.isdir(dir + '/blue'):
            msg.setText("Blue directory not found")
            msg.exec_()
            return
        if not os.path.isdir(dir + '/white'):
            msg.setText("White directory not found")
            msg.exec_()
            return

        self.aa.root_dir = dir
        self.read_files(dir)

        print("BEGIN")
        testing = SplunkTest.Splunkimport()
        testing.upload_logfiles(self.directory_widgets['lin_root_dir'].text())
        testing.transform_log_entry()
        print("END")
        self.load(self.vector_widgets)

    def read_files(self, dir):
        a = self.aa.log_entries
        data_read = []
        with open(dir + '/red/test.csv', 'r') as fp:
            reader = csv.reader(fp, delimiter=',', quotechar='"')
            # next(reader, None)  # skip the headers
            data_read = [row for row in reader]
        print(data_read)

        for row in data_read:
            l = LogEntry.LogEntry(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            a.append(l)

        x = self.vector_table_widgets['tbl_logs']
        for i in range(len(a)):
            x.setItem(i, 0, QTableWidgetItem(a[i].visibility))
            x.setItem(i, 1, QTableWidgetItem(a[i].id))
            x.setItem(i, 2, QTableWidgetItem(a[i].name))
            x.setItem(i, 3, QTableWidgetItem(a[i].description))
            x.setItem(i, 4, QTableWidgetItem(a[i].timestamp))
            x.setItem(i, 5, QTableWidgetItem(a[i].reference))
            x.setItem(i, 6, QTableWidgetItem(a[i].creator))
            x.setItem(i, 7, QTableWidgetItem(a[i].type))
            x.setItem(i, 8, QTableWidgetItem(a[i].icon))
            x.setItem(i, 9, QTableWidgetItem(a[i].source))

        pass

    def vector_ui_clicked(self):
        self.load(self.vector_widgets)

    def vector_add_clicked(self):
        x = self.vector_widgets['tbl_vector']
        x.insertRow(x.rowCount())

    def vector_delete_clicked(self):
        x = self.vector_widgets['tbl_vector']
        x.removeRow(x.currentRow())

    def vector_save_clicked(self):
        x = self.vector_widgets['tbl_vector']
        for i in range(x.rowCount()):
            self.aa.vector.append(Vector.Vector(x.item(i, 0), x.item(i, 1)))
            print('w')

    def log_file_ui_clicked(self):
        # self.load(self.log_file_widgets)
        pass

    def filter_ui_clicked(self):
        # self.load(self.filter_widgets)
        pass

    def log_entry_ui_clicked(self):
        # self.load(self.log_entry_widgets)
        pass

    def export_ui_clicked(self):
        # self.load(self.export_widgets)
        pass

    def change_ui_clicked(self):
        # self.load(self.change_widgets)
        pass

    def vector_db_ui_clicked(self):
        # self.load(self.vector_db_widgets)
        pass

    def icon_ui_clicked(self):
        # self.load(self.icon_widgets)
        pass

    def graph_builder_ui_clicked(self):
        # self.load(self.graph_builder_widgets)
        pass

    def table_ui_clicked(self):
        self.load(self.vector_table_widgets)

    def graph_ui_clicked(self):
        # self.load(self.vector_graph_widgets)
        pass

    def relationship_ui_clicked(self):
        # self.load(self.relationships_widgets)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
