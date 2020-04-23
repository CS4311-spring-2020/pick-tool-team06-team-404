import socket
from PyQt5.QtWidgets import *

window = None


def Label(self, name, x, y):
    item = QLabel(name, window)
    item.move(x, y)
    item.adjustSize()
    self.widgets.append(item)
    return item


def Button(self, name, x, y):
    item = QPushButton(name, window)
    item.move(x, y)
    item.adjustSize()
    self.widgets.append(item)
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

        self.team_ui = TeamView()
        self.event_ui = EventView()
        self.directory_ui = DirectoryView()
        self.vector_ui = VectorView()
        self.log_file_ui = LogFileView()
        self.filter_ui = FilterView()
        self.log_entry_ui = LogEntryView()
        self.export_ui = ExportView()
        self.change_ui = ChangeView()
        self.vector_db_ui = VectorDBUI
        self.icon_ui = IconView()
        self.graph_builder_ui = GraphBuilderView()
        self.vector_table_ui = VectorTableView()
        self.vector_graph_ui = VectorGraphView()
        self.relationships_ui = RelationshipsView()
        self.menu = self.Menu()

        self.ui = View()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.load(self.team_ui)
        self.show()

    class Menu:
        def __init__(self):
            self.widgets = []
            self.exit = Button(self, 'Exit', 0, 0)
            self.team = Button(self, 'Team', 80, 0)
            self.event = Button(self, 'Event', 160, 0)
            self.directory = Button(self, 'Directory', 240, 0)
            self.vector = Button(self, 'Vector', 320, 0)
            self.log_file = Button(self, 'Log File', 400, 0)
            self.filter = Button(self, 'Filter', 480, 0)
            self.log_entry = Button(self, 'Log Entry', 560, 0)
            self.export = Button(self, 'Export', 640, 0)
            self.change = Button(self, 'Change', 720, 0)
            self.vector_db = Button(self, 'Vector DB', 800, 0)
            self.icon = Button(self, 'Icon', 880, 0)
            self.graph_builder = Button(self, 'Graph Builder', 960, 0)
            self.vector_table = Button(self, 'Vector Table', 1040, 0)
            self.vector_graph = Button(self, 'Vector Graph', 1120, 0)
            self.relationships = Button(self, 'Relationships', 1200, 0)
            self.exit.show()
            self.team.show()
            self.event.show()
            self.directory.show()
            self.vector.show()
            self.log_file.show()
            self.filter.show()
            self.log_entry.show()
            self.export.show()
            self.change.show()
            self.vector_db.show()
            self.icon.show()
            self.graph_builder.show()
            self.vector_table.show()
            self.vector_graph.show()
            self.relationships.show()

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
        self.lbl_name = Label(self, 'Event Name: ', 300, 200)
        self.lin_name = LineEdit(self, '', 400, 200)
        self.lbl_description = Label(self, 'Event Description: ', 300, 250)
        self.txt_description = TextBox(self, 400, 250)
        self.lbl_start_time = Label(self, 'Start Time: ', 300, 450)
        self.lin_start_date = LineEdit(self, '', 400, 450)
        self.lin_start_time = LineEdit(self, '', 480, 450)
        self.lbl_end_time = Label(self, 'End Time: ', 300, 500)
        self.lin_end_date = LineEdit(self, '', 400, 500)
        self.lin_end_time = LineEdit(self, '', 480, 500)
        self.btn_save = Button(self, 'Save', 1000, 600)
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
        self.btn_ingestion = Button(self, 'Start Ingestion', 1000, 600)
        self.lin_root_dir.resize(340, 20)

        self.clear()


class VectorView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Vector Configuration<\\h1>', 50, 50)
        self.tbl_vector = Table(self, 100, 200)
        self.btn_add = Button(self, 'Add Vector', 400, 600)
        self.btn_delete = Button(self, 'Delete Vector', 600, 600)
        self.btn_save = Button(self, 'Save Changes', 800, 600)
        self.tbl_vector.setRowCount(1)
        self.tbl_vector.setColumnCount(2)
        self.tbl_vector.setMinimumSize(1050, 360)
        self.tbl_vector.setColumnWidth(0, 200)
        self.tbl_vector.setColumnWidth(1, 800)
        self.tbl_vector.setHorizontalHeaderLabels(['Vector Name', 'Vector Description'])

        self.clear()


class LogFileView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Log File Configuration<\\h1>', 50, 50)
        self.tbl_log_file = Table(self, 100, 100)
        self.tbl_file_action_report = Table(self, 100, 300)
        self.btn_validate = Button(self, "Validate", 100, 300)
        self.btn_cancel = Button(self, "Cancel", 100, 300)
        self.tbl_log_file.setHorizontalHeaderLabels(
            ['File Name', 'Source', 'Cleansing Status', 'Validation', 'Ingestion Status', 'View EA Report'])
        self.tbl_log_file.setRowCount(34)
        self.tbl_log_file.setColumnCount(6)
        self.tbl_file_action_report.setRowCount(34)
        self.tbl_file_action_report.setColumnCount(3)
        self.tbl_file_action_report.setHorizontalHeaderLabels(['File Name', 'Line Number', 'Error Message'])

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


class LogEntryView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Log Entry<\\h1>', 50, 50)
        self.tbl_log_entry = Table(self, 100, 100)
        self.tbl_log_entry.setRowCount(34)
        self.tbl_log_entry.setColumnCount(5)
        self.tbl_log_entry.setHorizontalHeaderLabels(
            ['', 'List Number', 'Log Entry Timestamp', 'Log Entry Event', 'Vector'])

        self.clear()


class ExportView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Export<\\h1>', 50, 50)
        self.cmb_export = ComboBox(self, 200, 200)
        self.btn_export = Button(self, 'Export', 300, 300)
        self.cmb_export.addItem('PDF')
        self.cmb_export.addItem('GIF')
        self.cmb_export.addItem('ABC')

        self.clear()


class ChangeView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Change List<\\h1>', 50, 50)
        self.btn_undo = Button(self, 'Undo', 100, 100)
        self.btn_commit = Button(self, 'Commit', 100, 200)

        self.clear()


class VectorDBUI(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Vector Data Base<\\h1>', 50, 50)
        self.lbl_connection = Label(self, 'Connection status to lead: ', 200, 200)
        self.lbl_connection_val = Label(self, '4', 200, 200)
        self.lbl_pulled_table = Label(self, 'PULLED vector DB table (Analyst)', 200, 200)
        self.tbl_pulled = Table(self, 300, 300)
        self.btn_pull = Button(self, 'Pull', 500, 500)
        self.lbl_pushed_table = Label(self, 'PUSHED vector DB table (Analyst)', 200, 400)
        self.tbl_pushed = Table(self, 300, 300)
        self.btn_push = Button(self, 'Push', 500, 500)
        self.tbl_pulled.setRowCount(34)
        self.tbl_pulled.setColumnCount(1)
        self.tbl_pushed.setRowCount(34)
        self.tbl_pushed.setColumnCount(1)

        self.clear()


class IconView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Icon Configuration<\\h1>', 50, 50)
        self.tbl_icon = Table(self, 100, 200)
        self.btn_add_icon = Button(self, 'Add Icon', 100, 100)
        self.btn_delete_icon = Button(self, 'Delete Icon', 100, 100)
        self.btn_edit_icon = Button(self, 'Edit Icon', 100, 100)
        self.tbl_icon.setRowCount(34)
        self.tbl_icon.setColumnCount(4)
        self.tbl_icon.setHorizontalHeaderLabels(['Select', 'Icon Name', 'Icon Source', 'Image Preview'])

        self.clear()


class GraphBuilderView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1Graph Builder<\\h1>', 50, 50)
        self.cmb_graph_builder = ComboBox(self, 200, 200)
        self.lbl_description = Label(self, 'Description: ', 200, 200)
        self.lin_description = LineEdit(self, '', 200, 200)
        self.btn_add_node = Button(self, 'Add Node', 200, 200)
        self.btn_delete_node = Button(self, 'Delete Node', 200, 200)
        self.btn_edit_node = Button(self, 'Edit Node', 200, 200)
        self.btn_add_relationship = Button(self, 'Add Relationship', 200, 200)
        self.btn_delete_relationship = Button(self, 'Delete Relationship', 200, 200)
        self.btn_edit_relationship = Button(self, 'Edit Relationship', 200, 200)
        self.cmb_graph_builder.addItem('example vector 1')
        self.cmb_graph_builder.addItem('example vector 2')

        self.clear()


class VectorTableView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Vector Table<\\h1>', 50, 50)
        self.tbl_logs = Table(self, 50, 100)
        self.tbl_logs.setRowCount(2)
        self.tbl_logs.setColumnCount(10)
        self.tbl_logs.setHorizontalHeaderLabels(
            ['Visible', 'Node ID', 'Node Name', 'Node Timestamp', 'Node Description',
             'Reference', 'Log Creator', 'Event Type', 'Icon Type', 'Source'])
        self.tbl_logs.setMinimumSize(1150, 560)

        self.clear()


class VectorGraphView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Vector Graph<\\h1>', 50, 50)
        self.lbl_timeline_orientation = Label(self, 'Timeline Orientation', 200, 200)
        self.cmb_timeline_orientation = ComboBox(self, 200, 200)
        self.lbl_interval_units = Label(self, 'Interval Units', 300, 300)
        self.cmb_interval_units = ComboBox(self, 300, 300)
        self.lbl_timeline = Label(self, 'A TIMELINE IS SUPPOSED TO GO HERE', 200, 200)
        self.btn_zoom_in = Button(self, 'Zoom In', 300, 300)
        self.btn_zoom_out = Button(self, 'Zoom Out', 300, 300)
        self.cmb_timeline_orientation.addItem('example orientation')
        self.cmb_interval_units.addItem('example interval unit')

        self.clear()


class RelationshipsView(View):
    def __init__(self):
        super().__init__()
        self.lbl_title = Label(self, '<h1>Relationship Configuration<\\h1>', 50, 50),
        self.tbl_relationship = Table(self, 200, 200)
        self.tbl_relationship.setRowCount(34)
        self.tbl_relationship.setColumnCount(7)

        self.clear()
