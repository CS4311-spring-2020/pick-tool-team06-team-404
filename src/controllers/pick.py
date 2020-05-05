import datetime
import sys
import os

from src.controllers.splunk import SplunkTest

sys.path.append(os.path.dirname(__file__) + "/..")
from QGraphViz.DotParser import Graph

sys.path.append(sys.path[0][:-16])

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from src.models.Vector import Vector
from src.models.LogEntry import LogEntry
from src.models.AdversarialAssessment import AdversarialAssessment
from src.views.gui import PICK_UI
import src.views.gui as gui

UI = None
currentUI = None


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
    x.btn_back.clicked.connect(team_ui_clicked)


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
    x.btn_save.clicked.connect(vector_btn_continue_clicked)


def set_buttons():
    set_team_buttons()
    set_event_buttons()
    set_directory_buttons()
    set_vector_buttons()
    set_log_file_buttons()
    #     set_log_entry_buttons()
    #     set_export_buttons()
    #     set_vector_db_buttons()
    set_vector_table_buttons()
    set_graph_buttons()
    set_relationships_buttons()


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
    x = UI.team_ui
    UI.load(x)
    if x.chk_lead.isChecked():
        x.btn_connect.hide()


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

    if not os.path.isdir(directory):
        msg.setText("Root directory not found")
        msg.exec_()
        return

    if not read_files(directory):
        return
    print("BEGIN")
    testing = SplunkTest.Splunkimport()
    testing.upload_logfiles(UI.directory_ui.lin_root_dir.text())
    testing.transform_log_entry()
    print("END")
    UI.load(UI.log_file_ui)


def read_files(directory):
    a = AA.log_entries
    id = 1
    err = False
    for creator in ['red', 'blue', 'white']:
        try:
            for file in os.listdir(directory + '/' + creator):
                for line in open(directory + '/' + creator + '/' + file, 'r').readlines():
                    if line == '':
                        continue
                    strsplit = line.split()
                    if len(strsplit) < 8:
                        continue
                    log = LogEntry()
                    log.id = id
                    log.name = ' '.join(strsplit[5:7])
                    log.timestamp = ' '.join(strsplit[0:5])
                    log.description = ' '.join(strsplit[7:])
                    log.creator = creator
                    log.source = directory + '/' + creator + '/' + file
                    a[str(log.id)] = log
                    id += 1
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setStyleSheet("QLabel{min-width: 200px;}")
            msg.setText(creator + " directory not found")
            msg.exec_()
            err = True

    if err:
        return False

    x = UI.log_file_ui.tbl_logs
    x.setRowCount(id - 1)
    i = 0
    for log in a:
        x.setItem(i, 0, QTableWidgetItem(a[log].name))
        x.setItem(i, 1, QTableWidgetItem(a[log].timestamp))
        x.setItem(i, 2, QTableWidgetItem(a[log].description))
        x.setItem(i, 3, QTableWidgetItem(a[log].creator))
        x.setItem(i, 4, QTableWidgetItem(a[log].source))
        i += 1

    return True


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


def vector_btn_continue_clicked():
    x = UI.vector_ui.tbl_vector
    i = 0
    while i < x.rowCount():
        if x.item(i, 0) is None and x.item(i, 0) is None:
            x.removeRow(i)
        else:
            i += 1

    for i in range(x.rowCount()):
        try:
            key = x.item(i, 0).text()
            if key not in AA.vector:
                AA.vector[key] = Vector(key, x.item(i, 1).text())
                AA.current_vector = key
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setStyleSheet("QLabel{min-width: 200px;}")
            msg.setText("Vector in row " + str(i + 1) + " is missing a field")
            msg.exec_()
            return

    for x in [UI.graph_ui, UI.relationships_ui, UI.vector_table_ui]:
        if x != UI.vector_table_ui:
            x.cmb_vectors.clear()
        for v in AA.vector:
            x.cmb_vectors.addItem(v)
        if AA.current_vector in set([v for v in AA.vector]):
            x.cmb_vectors.setCurrentText(AA.current_vector)
        else:
            AA.current_vector = [v for v in AA.vector][0]

    btn_vector = gui.Button(gui.window, 'Vector', 200, 0)
    btn_vector.show()
    btn_team = gui.Button(gui.window, 'Team', 0, 0)
    btn_team.show()
    btn_event = gui.Button(gui.window, 'Event', 100, 0)
    btn_event.show()
    btn_event.clicked.connect(event_ui_clicked)
    btn_vector.clicked.connect(vector_ui_clicked)
    btn_team.clicked.connect(team_ui_clicked)
    table_ui_clicked()


##############
#  LOG FILE  #
##############


def log_file_ui_clicked():
    UI.load(UI.log_file_ui)
    # generate EAR


def set_log_file_buttons():
    x = UI.log_file_ui
    x.btn_continue.clicked.connect(vector_ui_clicked)


##########
# FILTER #
##########

def filter_ui_clicked():
    # UI.load(UI.filter_ui)
    pass


def vector_db_ui_clicked():
    # UI.load(UI.vector_db_ui)
    pass


#########
# Table #
#########

def table_ui_clicked():
    global currentUI
    currentUI = 'table'
    x = UI.vector_table_ui
    UI.load(x)

    x.tbl_logs.setRowCount(len(AA.log_entries))
    tbl = x.tbl_logs
    i = 0
    c_vector = AA.vector[AA.current_vector]
    for log in AA.log_entries:
        log_entry = AA.log_entries[log]
        tbl.setCellWidget(i, 0, QCheckBox())
        if log in c_vector.log_entries:
            tbl.cellWidget(i, 0).setChecked(True)
        tbl.setCellWidget(i, 1, QCheckBox())
        if log in c_vector.log_visible:
            tbl.cellWidget(i, 1).setChecked(True)
        log_entry.id = str(i + 1)
        tbl.setItem(i, 2, QTableWidgetItem(log_entry.id))
        tbl.setItem(i, 3, QTableWidgetItem(log_entry.name))
        tbl.setItem(i, 4, QTableWidgetItem(log_entry.timestamp))
        tbl.setItem(i, 5, QTableWidgetItem(log_entry.description))
        tbl.setItem(i, 6, QTableWidgetItem(log_entry.creator))
        tbl.setItem(i, 7, QTableWidgetItem(log_entry.type))
        tbl.setItem(i, 8, QTableWidgetItem(log_entry.icon))
        tbl.setItem(i, 9, QTableWidgetItem(log_entry.source))

        i += 1


def set_vector_table_buttons():
    x = UI.vector_table_ui
    x.btn_graph.clicked.connect(vector_table_btn_save)
    x.btn_relationships.clicked.connect(relationship_ui_clicked)
    x.cmb_vectors.currentTextChanged.connect(cmb_box_change)


def cmb_box_change():
    AA.current_vector = str(UI.vector_table_ui.cmb_vectors.currentText())
    if currentUI == 'table':
        table_ui_clicked()
    elif currentUI == 'graph':
        graph_ui_clicked()
    elif currentUI == 'relationship':
        relationship_ui_clicked()


def vector_table_btn_save():
    x = UI.vector_table_ui.tbl_logs
    cv = AA.vector[AA.current_vector]
    for i in range(x.rowCount()):
        log = LogEntry()
        error = ''
        try:
            error = 'ID'
            log.id = x.item(i, get_column(x, 'ID')).text()
            error = 'Name'
            log.name = x.item(i, get_column(x, 'Name')).text()
            error = 'Timestamp'
            log.timestamp = x.item(i, get_column(x, 'Timestamp')).text()
            error = 'Description'
            log.description = x.item(i, get_column(x, 'Description')).text()
            error = 'Creator'
            log.creator = x.item(i, get_column(x, 'Creator')).text()
            error = 'Event Type'
            log.type = x.item(i, get_column(x, 'Event Type')).text()
            error = 'Icon'
            log.icon = x.item(i, get_column(x, 'Icon')).text()
            error = 'Source'
            log.source = x.item(i, get_column(x, 'Source')).text()
            if x.cellWidget(i, get_column(x, 'Visible')).isChecked():
                cv.log_visible.add(log.id)
            elif log.id in cv.log_visible:
                cv.log_visible.remove(log.id)
            if x.cellWidget(i, get_column(x, 'Significant')).isChecked():
                cv.log_entries.add(log.id)
            elif log.id in cv.log_entries:
                cv.log_entries.remove(log.id)
            if log.id in AA.log_entries:
                AA.log_entries.pop(log.id)
            AA.log_entries[log.id] = log
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setStyleSheet("QLabel{min-width: 200px;}")
            msg.setText("Row " + str(i + 1) + " contains invalid " + error)
            msg.exec_()

        graph_ui_clicked()


def get_column(widget, column):
    for x in range(widget.columnCount()):
        if column == widget.horizontalHeaderItem(x).text():
            return x
    return -1


#########
# Graph #
#########

def set_graph_buttons():
    x = UI.graph_ui
    x.btn_table.clicked.connect(table_ui_clicked)
    x.btn_relationships.clicked.connect(relationship_ui_clicked)
    x.btn_save.clicked.connect(graph_btn_save)
    x.cmb_vectors.currentTextChanged.connect(cmb_box_change)
    pass


def graph_btn_save():
    fname = QFileDialog.getSaveFileName(UI.graph_ui.graph, "Save", "", "*.json")
    if fname[0] != "":
        UI.graph_ui.graph.saveAsJson(fname[0])


def graph_ui_clicked():
    global currentUI
    currentUI = 'graph'
    x = UI.graph_ui
    UI.load(x)
    display_graph(AA.current_vector)


def display_graph(vector):
    x = UI.graph_ui
    graph = x.graph
    graph.engine.graph = Graph("MainGraph")
    graph.build()
    graph.repaint()

    nodes = {}
    for log in AA.vector[vector].log_visible:
        le = AA.log_entries[log]
        nodes[le.id] = graph.addNode(graph.engine.graph, "Node", label=le.id + '\n' + le.name,
                                     fillcolor=le.type)

    tbl_rel = UI.relationships_ui.tbl_relationships
    for row in range(tbl_rel.rowCount()):
        try:
            node1 = AA.log_entries[tbl_rel.item(row, 0).text()].id
            node2 = AA.log_entries[tbl_rel.item(row, 1).text()].id
            graph.addEdge(nodes[node1], nodes[node2], {"width": 5, "color": "black"})
        except:
            pass

    x.graph.build()


################
# Relationship #
################

def relationship_ui_clicked():
    UI.load(UI.relationships_ui)
    global currentUI
    currentUI = 'relationship'


def set_relationships_buttons():
    x = UI.relationships_ui
    x.btn_table.clicked.connect(table_ui_clicked)
    x.btn_graph.clicked.connect(graph_ui_clicked)
    x.cmb_vectors.currentTextChanged.connect(cmb_box_change)
    x.btn_add.clicked.connect(add_row)


def add_row():
    x = UI.relationships_ui.tbl_relationships
    x.insertRow(x.rowCount())


########
# MAIN #
########

if __name__ == '__main__':
    app = QApplication(sys.argv)
    AA = AdversarialAssessment()
    UI = PICK_UI()
    set_buttons()
    sys.exit(app.exec_())
