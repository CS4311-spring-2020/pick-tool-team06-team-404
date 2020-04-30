import sys
import os
import datetime
import csv

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from src.controllers.splunk import SplunkTest
from src.models import LogEntry, Vector
from src.models.AdversarialAssessment import AdversarialAssessment
from src.views.gui import PICK_UI

UI = None


def convert_date(date):
    return datetime.datetime.strptime(date, '%a %b %d %Y').strftime('%m/%d/%Y')


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


def file_dialog():
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


def set_menu_buttons():
    x = UI.menu
    x.exit.clicked.connect(UI.close)
    x.team.clicked.connect(team_ui_clicked)
    x.event.clicked.connect(event_ui_clicked)
    x.directory.clicked.connect(directory_ui_clicked)
    x.vector.clicked.connect(vector_ui_clicked)
    x.log_file.clicked.connect(log_file_ui_clicked)
    x.filter.clicked.connect(filter_ui_clicked)
    x.log_entry.clicked.connect(log_entry_ui_clicked)
    x.export.clicked.connect(export_ui_clicked)
    x.change.clicked.connect(change_ui_clicked)
    x.vector_db.clicked.connect(vector_db_ui_clicked)
    x.icon.clicked.connect(icon_ui_clicked)
    x.graph_builder.clicked.connect(graph_builder_ui_clicked)
    x.vector_table.clicked.connect(table_ui_clicked)
    x.vector_graph.clicked.connect(graph_ui_clicked)
    x.relationships.clicked.connect(relationship_ui_clicked)


def set_team_buttons():
    x = UI.team_ui
    x.chk_lead.clicked.connect(team_chk_lead_clicked)
    x.btn_connect.clicked.connect(team_btn_connect_clicked)
    x.btn_continue.clicked.connect(team_btn_continue_clicked)


def set_event_buttons():
    x = UI.event_ui
    x.btn_save.clicked.connect(event_btn_save_clicked)
    x.btn_cal_start_date.clicked.connect(x.cal_start_date.show)
    x.cal_start_date.clicked[QDate].connect(start_calendar_clicked)
    x.btn_cal_end_date.clicked.connect(x.cal_end_date.show)
    x.cal_end_date.clicked[QDate].connect(end_calendar_clicked)


def start_calendar_clicked():
    x = UI.event_ui
    x.lin_start_date.setText(convert_date(x.cal_start_date.selectedDate().toString()))
    x.cal_start_date.hide()


def end_calendar_clicked():
    x = UI.event_ui
    x.lin_end_date.setText(convert_date(x.cal_end_date.selectedDate().toString()))
    x.cal_end_date.hide()


def set_directory_buttons():
    x = UI.directory_ui
    x.lin_root_dir.textChanged.connect(directory_directory_changed)
    x.btn_browse.clicked.connect(directory_browse_clicked)
    x.btn_ingestion.clicked.connect(directory_ingest_clicked)


def set_vector_buttons():
    x = UI.vector_ui
    x.btn_add.clicked.connect(vector_add_clicked)
    x.btn_delete.clicked.connect(vector_delete_clicked)
    x.btn_save.clicked.connect(vector_save_clicked)
    x.tbl_vector.clicked.connect(vector_table_clicked)


def vector_table_clicked():
    x = UI.vector_ui
    try:
        x.lbl_val_active.setText(x.tbl_vector.item(x.tbl_vector.currentRow(), 0).text())
    except:
        pass


def set_vector_table_buttons():
    x = UI.vector_table_ui
    x.btn_graph.clicked.connect(graph_ui_clicked)
    pass


def vector_btn_graph_clicked():
    UI.load(UI.graph_ui)


def set_vector_graph_buttons():
    pass


def set_buttons():
    set_menu_buttons()
    set_team_buttons()
    set_event_buttons()
    set_directory_buttons()
    set_vector_buttons()
    #     set_log_file_buttons()
    #     set_filter_buttons()
    #     set_log_entry_buttons()
    #     set_export_buttons()
    #     set_change_buttons()
    #     set_vector_db_buttons()
    #     set_icon_buttons()
    #     set_graph_builder_buttons()
    set_vector_table_buttons()
    set_vector_graph_buttons()


#     set_relationships_buttons()


def team_chk_lead_clicked():
    x = UI.team_ui
    b = False if x.chk_lead.isChecked() else True
    x.lin_lead_ip_value.setEnabled(b)
    x.btn_continue.setVisible(not b)
    x.btn_connect.setVisible(b)


def team_btn_connect_clicked():
    pass


def team_btn_continue_clicked():
    UI.load(UI.event_ui)


def team_ui_clicked():
    UI.load(UI.team_ui)


def event_ui_clicked():
    UI.load(UI.event_ui)


def event_btn_save_clicked():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setStyleSheet("QLabel{min-width: 200px;}")
    x = UI.event_ui
    if x.lin_name.text() == '':
        msg.setText("Event name can't be empty")
        msg.exec_()
        return
    if not validate_date(x.lin_start_date.text()):
        msg.setText("Wrong 'Start date' format")
        msg.exec_()
        return
    if not validate_time(x.lin_start_time.text()):
        msg.setText("Wrong 'Start time' format")
        msg.exec_()
    if not validate_date(x.lin_end_date.text()):
        msg.setText("Wrong 'End date' format")
        msg.exec_()
        return
    if not validate_time(x.lin_end_time.text()):
        msg.setText("Wrong 'End time' format")
        msg.exec_()
        return
    a = datetime.datetime.strptime(x.lin_start_date.text(), "%m/%d/%Y")
    b = datetime.datetime.strptime(x.lin_end_date.text(), "%m/%d/%Y")
    if a > b:
        msg.setText("Start time can't be after end time")
        msg.exec_()
        return
    AA.name = x.lin_name.text()
    AA.description = x.txt_description.toPlainText()
    AA.time_start = x.lin_start_date.text() + '-' + x.lin_start_time.text()
    AA.time_end = x.lin_end_date.text() + '-' + x.lin_end_time.text()

    UI.load(UI.directory_ui)


def directory_ui_clicked():
    UI.load(UI.directory_ui)


def directory_browse_clicked():
    UI.directory_ui.lin_root_dir.setText(file_dialog())


def directory_directory_changed():
    x = UI.directory_ui
    d = x.lin_root_dir.text()
    x.lin_red_dir.setText(d + '/red')
    x.lin_white_dir.setText(d + '/white')
    x.lin_blue_dir.setText(d + '/blue')
    x.lin_red_dir.resize(400, 20)
    x.lin_white_dir.resize(400, 20)
    x.lin_blue_dir.resize(400, 20)


def directory_ingest_clicked():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setStyleSheet("QLabel{min-width: 200px;}")
    directory = UI.directory_ui.lin_root_dir.text()
    AA.root_dir = directory
    read_files(directory)

    # debug
    print("BEGIN")
    # testing = SplunkTest.Splunkimport()
    # testing.upload_logfiles(UI.directory_ui.lin_root_dir.text())
    # testing.transform_log_entry()
    print("END")
    UI.load(UI.vector_ui)

    return
    # ignore
    if not os.path.isdir(directory):
        msg.setText("Root directory not found")
        msg.exec_()
        return
    if not os.path.isdir(directory + '/red'):
        msg.setText("Red directory not found")
        msg.exec_()
        return
    if not os.path.isdir(directory + '/blue'):
        msg.setText("Blue directory not found")
        msg.exec_()
        return
    if not os.path.isdir(directory + '/white'):
        msg.setText("White directory not found")
        msg.exec_()
        return

    AA.root_dir = directory
    read_files(directory)

    print("BEGIN")
    # testing = SplunkTest.Splunkimport()
    # testing.upload_logfiles(UI.directory_ui.lin_root_dir.text())
    # testing.transform_log_entry()
    print("END")
    UI.load(UI.vector_ui)


def read_files(directory):
    a = AA.log_entries
    with open(directory + '/red/test.csv', 'r') as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='"')
        data_read = [row for row in reader]
    print(data_read)

    for row in data_read:
        log = LogEntry.LogEntry(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        a.append(log)

    x = UI.vector_table_ui.tbl_logs
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

############
#  VECTOR  #
############

def vector_ui_clicked():
    UI.load(UI.vector_ui)


def vector_add_clicked():
    x = UI.vector_ui.tbl_vector
    x.insertRow(x.rowCount())


def vector_delete_clicked():
    x = UI.vector_ui.tbl_vector
    x.removeRow(x.currentRow())


def vector_save_clicked():
    x = UI.vector_ui.tbl_vector
    for i in range(x.rowCount()):
        try:
            AA.vector.append(Vector.Vector(x.item(i, 0).text(), x.item(i, 1).text()))
        except:
            pass

##############
#  LOG FILE  #
##############


def log_file_ui_clicked():
    # UI.load(UI.log_file_ui)
    pass


def filter_ui_clicked():
    # UI.load(UI.filter_ui)
    pass


def log_entry_ui_clicked():
    # UI.load(UI.log_entry_ui)
    pass


def export_ui_clicked():
    # UI.load(UI.export_ui)
    pass


def change_ui_clicked():
    # UI.load(UI.change_ui)
    pass


def vector_db_ui_clicked():
    # UI.load(UI.vector_db_ui)
    pass


def icon_ui_clicked():
    # UI.load(UI.icon_ui)
    pass


def graph_builder_ui_clicked():
    # UI.load(UI.graph_builder_ui)
    pass


def table_ui_clicked():
    UI.load(UI.vector_table_ui)


def graph_ui_clicked():
    x = UI.graph_ui
    UI.load(x)
    for v in AA.vector:
        x.cmb_graph_builder.addItem(v.name)


def relationship_ui_clicked():
    # UI.load(UI.relationships_ui)
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    AA = AdversarialAssessment()
    UI = PICK_UI()
    set_buttons()
    sys.exit(app.exec_())
