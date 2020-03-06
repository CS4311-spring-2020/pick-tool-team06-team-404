#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
PICK Tool: Team6 - Team404
Program Purpose:
        - GUI prototype for the clients
Date:
        - 05 March 2020
Dependencies:
        - pyqt5
NOTES:
'''


import sys
import PyQt5
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# View

# QStackedWidget
# Trigger.Connect()
# Clicked.Connet()


class PICK_TOOL(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''Builds the UI for the user'''

        self.stackedWidget = QStackedWidget(self)
        config_dict = {}

        widgets = [
            'home','team', 'event', 'directory', 'vector', 'log_file',
            'filter', 'log_entry', 'export', 'change', 'vector_db',
            'icon', 'graph_builder', 'nodes_tabular', 'nodes_graphical', 'relationship'
        ]

        # PAGES THAT USER INTERACTS WITH
        for item in widgets:
            config_dict[item] = QWidget()

        # CLICKABLE WIDGETS THAT APPEAR ATOP PAGES
        for key in config_dict:
            self.stackedWidget.addWidget(config_dict[key])

        # CREATE UI PAGES
        self.home_page(config_dict['home'])
        self.team_configuration(config_dict['team'])
        self.event_configuration(config_dict['event'])
        self.directory_configuration(config_dict['directory'])
        self.vector_configuration(config_dict['vector'])
        self.log_file_configuration(config_dict['log_file'])
        self.filter_configuration(config_dict['filter'])
        self.log_entry_configuration(config_dict['log_entry'])
        self.export_configuration(config_dict['export'])
        self.change_configuration(config_dict['change'])
        self.vector_db_configuration(config_dict['vector_db'])
        self.icon_configuration(config_dict['icon'])
        self.graph_builder_configuration(config_dict['graph_builder'])
        self.nodes_tabular_configuration(config_dict['nodes_tabular'])
        self.nodes_graphical_configuration(config_dict['nodes_graphical'])
        self.relationship_configuration(config_dict['relationship'])

        # INITALIZE THE MAIN WINDOW
        self.setFixedSize(1600, 1000)
        self.center()
        self.setWindowTitle('PMR Insight Collective Knowledge System (PICK) Tool')
        self.setCentralWidget(self.stackedWidget)
        self._createToolBar()
        self._createStatusBar()
        self.show()

    # 'HOME' PAGE
    def home_page(self, home_page_widget):
        layout = QGridLayout()
        
        # Page Heading
        left_spacer = QWidget()
        right_spacer = QWidget()
        left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        heading = QLabel('<center><h1>Prevent Mitigate Recover (PMR) Insight Collective Knowledge System<br><br>PICK Tool</h1><br><h2>Government Warning Notice</h2> This is a U.S. Government computer system, which may be accessed and used only for authorized Government business by authorized personnel. Unauthorized access or use of this computer system may subject violators to criminal, civil, and/or administrative action. All information on this computer system may be intercepted, recorded, read, copied, and disclosed by and to authorized personnel for official purposes, including criminal investigations. Such information includes sensitive data encrypted to comply with confidentiality and privacy requirements. Access or use of this computer system by any person, whether authorized or unauthorized, constitutes consent to these terms. There is no right of privacy in this system.</center>')
        heading.setWordWrap(True) 

        # Team404 Logo
        image = QLabel()
        pixmap = QPixmap('src/gui/team_404_logo.PNG')
        smaller_pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.FastTransformation)
        image.setPixmap(smaller_pixmap)
        image.setAlignment(QtCore.Qt.AlignCenter)

        # Connect Button
        connect_button = QPushButton('Connect')
        connect_button.resize(100,32)

        # Compile Widgets
        layout.addWidget(left_spacer,1,0)
        layout.addWidget(heading,1,0)
        layout.addWidget(right_spacer,1,0)
        layout.addWidget(image, 0, 0)
        layout.addWidget(connect_button, 3, 0)

        home_page_widget.setLayout(layout)


    # 'TEAM CONFIGURATION' PAGE
    def team_configuration(self, team_configuration_page_widget):
        team_layout = QGridLayout()
        team_title_label = QLabel('<h1>Team Configuration<\h1>')

        team_lead_checkbox = QCheckBox()
        team_lead_checkbox.setText('Lead')
        team_lead_ip_address_label_label = QLabel('Lead IP Address')

        # 255.255.255.255 is an example, this needs to be changed later
        team_lead_ip_address_address_label = QLabel('255.255.255.255')
        team_no_of_connections_label_label = QLabel(
            'Number of established connections to the lead\' IP address')

        # 4 is an example, this needs to be changed later
        team_no_of_connections_label = QLabel('4')
        team_connect_button = QPushButton('Connect')

        team_layout.addWidget(team_title_label, 0, 0)
        team_layout.addWidget(team_lead_checkbox, 1, 0)
        team_layout.addWidget(team_lead_ip_address_label_label, 2, 0)
        team_layout.addWidget(team_lead_ip_address_address_label, 2, 1)
        team_layout.addWidget(team_no_of_connections_label_label, 3, 0)
        team_layout.addWidget(team_no_of_connections_label, 3, 1)
        team_layout.addWidget(team_connect_button, 4, 0)

        team_configuration_page_widget.setLayout(team_layout)

    def event_configuration(self, event_configuration_page_widget):
        # 'EVENT CONFIGURATION' PAGE
        event_layout = QGridLayout()
        event_layout.setVerticalSpacing(100)
        event_title_label = QLabel('<h1>Event Configuration<\h1>')

        event_event_name_label = QLabel('Event Name: ')
        event_event_name = QLineEdit()

        event_event_description_label = QLabel('Event description: ')
        event_event_description = QLineEdit()

        event_event_start_timestamp_label = QLabel('Start Timestamp: ')
        event_event_start_timestamp = QLineEdit()

        event_event_end_timestamp_label = QLabel('End Timestamp: ')
        event_event_end_timestamp = QLineEdit()

        event_event_save = QPushButton('Apply')

        event_layout.addWidget(event_title_label, 0, 0)
        event_layout.addWidget(event_event_name_label, 1, 0)
        event_layout.addWidget(event_event_name, 1, 1)
        event_layout.addWidget(event_event_description_label, 2, 0)
        event_layout.addWidget(event_event_description, 2, 1)
        event_layout.addWidget(event_event_start_timestamp_label, 3, 0)
        event_layout.addWidget(event_event_start_timestamp, 3, 1)
        event_layout.addWidget(event_event_end_timestamp_label, 4, 0)
        event_layout.addWidget(event_event_end_timestamp, 4, 1)
        event_layout.addWidget(event_event_save, 5, 0)

        event_configuration_page_widget.setLayout(event_layout)

    def directory_configuration(self, directory_configuration_page_widget):
        # SYSTEM BUILDS 'DIRECTORY CONFIGURATION' PAGE GUI
        directory_layout = QGridLayout()
        directory_layout.setVerticalSpacing(100)
        directory_title_label = QLabel('<h1>Directory Configuration<\h1>')

        directory_root_directory_label = QLabel('Root Directory')
        directory_root_directory = QLineEdit()

        directory_red_folder_label = QLabel('Red folder')
        directory_red_folder = QLineEdit()

        directory_blue_folder_label = QLabel('Blue Folder')
        directory_blue_folder = QLineEdit()

        directory_white_folder_label = QLabel('White Folder')
        directory_white_folder = QLineEdit()

        directory_start_data_ingestion_button = QPushButton()
        directory_start_data_ingestion_button.setText('Start Data Ingestion')

        directory_layout.addWidget(directory_title_label, 0, 0)
        directory_layout.addWidget(directory_root_directory_label, 1, 0)
        directory_layout.addWidget(directory_root_directory, 1, 1)
        directory_layout.addWidget(directory_red_folder_label, 2, 0)
        directory_layout.addWidget(directory_red_folder, 2, 1)
        directory_layout.addWidget(directory_blue_folder_label, 3, 0)
        directory_layout.addWidget(directory_blue_folder, 3, 1)
        directory_layout.addWidget(directory_white_folder_label, 4, 0)
        directory_layout.addWidget(directory_white_folder, 4, 1)
        directory_layout.addWidget(directory_start_data_ingestion_button, 5, 0)

        directory_configuration_page_widget.setLayout(directory_layout)

    def vector_configuration(self, vector_configuration_page_widget):
        # SYSTEM BUILDS 'VECTOR CONFIGURATION' PAGE GUI
        vector_layout = QGridLayout()
        vector_title_label = QLabel('<h1>Vector Configuration<\h1>')

        vector_table = QTableWidget()
        vector_table.setRowCount(34)
        vector_table.setColumnCount(2)
        vector_table.setHorizontalHeaderLabels(
            ['Vector Name', 'Vector Description'])

        vector_add_button = QPushButton()
        vector_add_button.setText('Add Vector')
        vector_delete_button = QPushButton()
        vector_delete_button.setText('Delete Vector')
        vector_edit_button = QPushButton()
        vector_edit_button.setText('Edit Vector')

        vector_layout.addWidget(vector_title_label)
        vector_layout.addWidget(vector_table)
        vector_layout.addWidget(vector_add_button)
        vector_layout.addWidget(vector_delete_button)
        vector_layout.addWidget(vector_edit_button)

        vector_configuration_page_widget.setLayout(vector_layout)

    def log_file_configuration(self, log_file_configuration_page_widget):
        # SYSTEM BUILDS 'LOG FILE CONFIGURATION' PAGE GUI
        log_file_layout = QGridLayout()
        log_file_title_label = QLabel('<h1>Log File Configuration<\h1>')

        log_file_log_file_table = QTableWidget()
        log_file_log_file_table.setRowCount(34)
        log_file_log_file_table.setColumnCount(6)
        log_file_log_file_table.setHorizontalHeaderLabels(
            ['File Name', 'Source', 'Cleansing Status', 'Validation', 'Ingestion Status', 'View EA Report'])

        log_file_action_report_table = QTableWidget()
        log_file_action_report_table.setRowCount(34)
        log_file_action_report_table.setColumnCount(3)
        log_file_action_report_table.setHorizontalHeaderLabels(
            ['File Name', 'Line Number', 'Error Message'])

        log_file_validate_button = QPushButton()
        log_file_validate_button.setText('Validate')

        log_file_cancel_button = QPushButton('Cancel')
        # log_file_cancel_button.setText('Cancel

        log_file_layout.addWidget(log_file_title_label)
        log_file_layout.addWidget(log_file_log_file_table)
        log_file_layout.addWidget(log_file_action_report_table)

        log_file_configuration_page_widget.setLayout(log_file_layout)

    def filter_configuration(self, filter_configuration_page_widget):
        # makes filter config page widget
        filter_layout = QGridLayout()
        filter_title_label = QLabel('<h1>Filter Configuration<\h1>')

        filter_keyword_search_textbox_label = QLabel('Keyword Search: ')
        filter_keyword_search_textbox = QLineEdit()
        filter_creator_label = QLabel('Creator')
        filter_red_checkbox = QCheckBox()
        filter_red_checkbox.setText('Red')
        filter_blue_checkbox = QCheckBox()
        filter_blue_checkbox.setText('Blue')
        filter_white_checkbox = QCheckBox()
        filter_white_checkbox.setText('White')
        filter_start_timestamp_label = QLabel('Start Timestamp')
        filter_start_timestamp = QLineEdit()
        filter_end_timestamp_label = QLabel('End Timestamp')
        filter_end_timestamp = QLineEdit()

        filter_layout.addWidget(filter_title_label, 0, 0)
        filter_layout.addWidget(filter_keyword_search_textbox_label, 1, 0)
        filter_layout.addWidget(filter_keyword_search_textbox, 1, 1)
        filter_layout.addWidget(filter_creator_label, 2, 0)
        filter_layout.addWidget(filter_red_checkbox, 2, 1)
        filter_layout.addWidget(filter_blue_checkbox, 3, 1)
        filter_layout.addWidget(filter_white_checkbox, 4, 1)
        filter_layout.addWidget(filter_start_timestamp_label, 5, 0)
        filter_layout.addWidget(filter_start_timestamp, 5, 1)
        filter_layout.addWidget(filter_end_timestamp_label, 6,  0)
        filter_layout.addWidget(filter_end_timestamp, 6, 1)

        filter_configuration_page_widget.setLayout(filter_layout)

    def log_entry_configuration(self, log_entry_configuration_page_widget):
        # makes log entry config page widget
        log_entry_layout = QGridLayout()
        log_entry_title_label = QLabel('<h1>Log Entry Configuration<\h1>')

        log_entry_table = QTableWidget()
        log_entry_table.setRowCount(34)
        log_entry_table.setColumnCount(5)
        log_entry_table.setHorizontalHeaderLabels(
            ['', 'List Number', 'Log Entry Timestamp', 'Log Entry Event', 'Vector'])

        log_entry_layout.addWidget(log_entry_title_label)
        log_entry_layout.addWidget(log_entry_table)

        log_entry_configuration_page_widget.setLayout(log_entry_layout)

    def export_configuration(self, export_configuration_page_widget):
        # makes export config page widget
        export_layout = QGridLayout()
        export_layout.setVerticalSpacing(200)
        export_title_label = QLabel('<h1>Export Configuration<\h1>')
        export_menu_label = QLabel('Export as: ')

        export_dropdown_menu = QComboBox()
        export_dropdown_menu.addItem('PDF')
        export_dropdown_menu.addItem('GIF')
        export_dropdown_menu.addItem('ABC')

        export_export_button = QPushButton()
        export_export_button.setText('Export')

        export_layout.addWidget(export_title_label, 0, 0)
        export_layout.addWidget(export_menu_label, 1, 0)
        export_layout.addWidget(export_dropdown_menu, 1, 1)
        export_layout.addWidget(export_export_button, 2, 0)

        export_configuration_page_widget.setLayout(export_layout)

    def change_configuration(self, change_configuration_page_widget):
        # makes change config page widget
        change_layout = QGridLayout()
        change_change_list_label = QLabel('Change List: ')

        change_undo_button = QPushButton()
        change_undo_button.setText('Undo')
        change_commit_button = QPushButton()
        change_commit_button.setText('Commit')

        change_layout.addWidget(change_change_list_label)
        change_layout.addWidget(change_undo_button)
        change_layout.addWidget(change_commit_button)

        change_configuration_page_widget.setLayout(change_layout)

    def vector_db_configuration(self, vector_db_configuration_page_widget):
        # make vector db config page widget
        vector_db_layout = QGridLayout()
        vector_db_connection_label = QLabel('Connection status to lead: ')

        # 4 is just and example, this needs to be changed later
        vector_db_actual_connection_number = QLabel('4')
        vector_db_pulled_vector_table = QLabel(
            'PULLED vector DB table (Analyst)')

        vector_db_pulled_table = QTableWidget()
        vector_db_pulled_table.setRowCount(34)
        vector_db_pulled_table.setColumnCount(1)

        vector_db_pull_button = QPushButton()
        vector_db_pull_button.setText('Pull')

        vector_db_pushed_vector_label = QLabel(
            'PUSHED vector DB table (Analyst)')
        vector_db_pushed_table = QTableWidget()
        vector_db_pushed_table.setRowCount(34)
        vector_db_pushed_table.setColumnCount(1)
        vector_db_push_button = QPushButton()
        vector_db_push_button.setText('Push')

        vector_db_layout.addWidget(vector_db_connection_label)
        vector_db_layout.addWidget(vector_db_actual_connection_number)
        vector_db_layout.addWidget(vector_db_pulled_table)
        vector_db_layout.addWidget(vector_db_pull_button)
        vector_db_layout.addWidget(vector_db_pushed_vector_label)
        vector_db_layout.addWidget(vector_db_pushed_table)
        vector_db_layout.addWidget(vector_db_push_button)

        vector_db_configuration_page_widget.setLayout(vector_db_layout)

    def icon_configuration(self, icon_configuration_page_widget):
        # makes icon config page
        icon_layout = QGridLayout()
        icon_title_label = QLabel('<h1>Icon Configuration<\h1>')

        icon_table = QTableWidget()
        icon_table.setRowCount(34)
        icon_table.setColumnCount(4)
        icon_table.setHorizontalHeaderLabels(
            ['Select', 'Icon Name', 'Icon Source', 'Image Preview'])

        icon_add_icon_button = QPushButton()
        icon_add_icon_button.setText('Add Icon')
        icon_delete_icon_button = QPushButton()
        icon_delete_icon_button.setText('Delete Icon')
        icon_edit_icon_button = QPushButton()
        icon_edit_icon_button.setText('Edit Icon')

        icon_layout.addWidget(icon_title_label)
        icon_layout.addWidget(icon_table)
        icon_layout.addWidget(icon_add_icon_button)
        icon_layout.addWidget(icon_delete_icon_button)
        icon_layout.addWidget(icon_edit_icon_button)

        icon_configuration_page_widget.setLayout(icon_layout)

    def graph_builder_configuration(self, graph_builder_configuration_page_widget):
        # makes Graph builder Config page widget
        graph_builder_layout = QGridLayout()
        graph_builder_vector_label = QLabel('Vector: ')

        graph_builder_vector_dropdown_menu = QComboBox()
        graph_builder_vector_dropdown_menu.addItem('example vector 1')
        graph_builder_vector_dropdown_menu.addItem('example vector 2')
        graph_builder_description_label_label = QLabel('Description')
        graph_builder_description_label = QLineEdit()
        graph_builder_description_label.setText('Example description')
        graph_builder_add_node_button = QPushButton()
        graph_builder_add_node_button.setText('Add Node')
        graph_builder_add_relationship_button = QPushButton()
        graph_builder_add_relationship_button.setText('Add Relationship')
        graph_builder_delete_node_button = QPushButton()
        graph_builder_delete_node_button.setText('Delete Node')
        graph_builder_delete_relationship_button = QPushButton()
        graph_builder_delete_relationship_button.setText('Delete Relationship')
        graph_builder_edit_node_button = QPushButton()
        graph_builder_edit_node_button.setText('Edit Node')
        graph_builder_edit_relationship_button = QPushButton()
        graph_builder_edit_relationship_button.setText('Edit Relationship')

        graph_builder_layout.addWidget(graph_builder_vector_label)
        graph_builder_layout.addWidget(graph_builder_vector_dropdown_menu)
        graph_builder_layout.addWidget(graph_builder_description_label_label)
        graph_builder_layout.addWidget(graph_builder_description_label)
        graph_builder_layout.addWidget(graph_builder_add_node_button)
        graph_builder_layout.addWidget(graph_builder_add_relationship_button)
        graph_builder_layout.addWidget(graph_builder_delete_node_button)
        graph_builder_layout.addWidget(
            graph_builder_delete_relationship_button)
        graph_builder_layout.addWidget(graph_builder_edit_node_button)
        graph_builder_layout.addWidget(graph_builder_edit_relationship_button)

        graph_builder_configuration_page_widget.setLayout(graph_builder_layout)

    def nodes_tabular_configuration(self, nodes_tabular_configuration_page_widget):
        # makes nodes config table page widget
        nodes_tabular_layout = QGridLayout()
        nodes_tabular_title_label = QLabel(
            '<h1>Nodes Configuration in Tabular Format<\h1>')

        nodes_tabular_table = QTableWidget()
        nodes_tabular_table.setRowCount(34)
        nodes_tabular_table.setColumnCount(11)
        nodes_tabular_table.setHorizontalHeaderLabels(['Node Property Visibility', 'Node ID', 'Node Name', 'Node Timestamp',
                                                       'Node Description', 'Log Entry Reference', 'Log Creator', 'Event Type', 'Icon Type', 'Source', 'Node Visibility'])

        nodes_tabular_layout.addWidget(nodes_tabular_title_label)
        nodes_tabular_layout.addWidget(nodes_tabular_table)

        nodes_tabular_configuration_page_widget.setLayout(nodes_tabular_layout)

    def nodes_graphical_configuration(self, nodes_graphical_configuration_page_widget):
        # makes nodes config graph page widget
        nodes_graphical_layout = QGridLayout()
        nodes_graphical_title_label = QLabel(
            '<h1>Nodes Configuration in Graphical Format<\h1>')

        nodes_graphical_timeline_orientation_label = QLabel(
            'Timeline Orientation')
        nodes_graphical_timeline_orientation_dropdown = QComboBox()
        nodes_graphical_timeline_orientation_dropdown.addItem(
            'example orientation')

        nodes_graphical_interval_units_label = QLabel('Interval Units')
        nodes_graphical_interval_units_dropdown = QComboBox()
        nodes_graphical_interval_units_dropdown.addItem(
            'example interval unit')
        nodes_graphical_timeline = QLabel('A TIMELINE IS SUPPOSED TO GO HERE')
        nodes_graphical_zoom_in_button = QPushButton()
        nodes_graphical_zoom_in_button.setText('Zoom In')
        nodes_graphical_zoom_out_button = QPushButton()
        nodes_graphical_zoom_out_button.setText('Zoom Out')

        nodes_graphical_layout.addWidget(nodes_graphical_title_label)
        nodes_graphical_layout.addWidget(
            nodes_graphical_timeline_orientation_label)
        nodes_graphical_layout.addWidget(
            nodes_graphical_timeline_orientation_dropdown)
        nodes_graphical_layout.addWidget(nodes_graphical_interval_units_label)
        nodes_graphical_layout.addWidget(
            nodes_graphical_interval_units_dropdown)
        nodes_graphical_layout.addWidget(nodes_graphical_timeline)
        nodes_graphical_layout.addWidget(nodes_graphical_zoom_in_button)
        nodes_graphical_layout.addWidget(nodes_graphical_zoom_out_button)

        nodes_graphical_configuration_page_widget.setLayout(
            nodes_graphical_layout)

    def relationship_configuration(self, relationship_configuration_page_widget):
        # makes relationships config page widget
        relationship_layout = QGridLayout()
        relationship_title_label = QLabel(
            '<h1>Relationship Configuration<\h1>')

        relationship_table = QTableWidget()

        relationship_table.setRowCount(34)
        relationship_table.setColumnCount(7)

        relationship_layout.addWidget(relationship_title_label)
        relationship_layout.addWidget(relationship_table)

        relationship_configuration_page_widget.setLayout(relationship_layout)

    def home_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        self.buttonClicked()

    def team_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.buttonClicked()

    def team_configuration_connect_button_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        self.buttonClicked()

    def event_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(3)
        self.buttonClicked()

    def directory_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(4)
        self.buttonClicked()

    def vector_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(5)
        self.buttonClicked()

    def log_file_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(6)
        self.buttonClicked()

    def filter_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(7)
        self.buttonClicked()

    def log_entry_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(8)
        self.buttonClicked()

    def export_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(9)
        self.buttonClicked()

    def change_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(10)
        self.buttonClicked()

    def vector_db_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(11)
        self.buttonClicked()

    def icon_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(12)
        self.buttonClicked()

    def graph_builder_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(13)
        self.buttonClicked()

    def nodes_table_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(14)
        self.buttonClicked()

    def nodes_graph_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(15)
        self.buttonClicked()

    def relationships_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(16)
        self.buttonClicked()

    def buttonClicked(self):
        sender = self.sender()
        #self.statusBar().showMessage(sender.text() + ' was clicked')

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)

        # SPACERS WIDGETS FOR CENTERING TOOLBAR
        left_spacer = QWidget()
        right_spacer = QWidget()

        left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        tools.addWidget(left_spacer)
        tools.addAction('Home', self.home_tool_button_clicked)
        tools.addAction('Team', self.team_tool_button_clicked)
        tools.addAction('Event', self.event_tool_button_clicked)
        tools.addAction('Directory', self.directory_tool_button_clicked)
        tools.addAction('Vector', self.vector_tool_button_clicked)
        tools.addAction('Log File', self.log_file_tool_button_clicked)
        tools.addAction('Filter', self.filter_tool_button_clicked)
        tools.addAction('Log Entry', self.log_entry_tool_button_clicked)
        tools.addAction('Export', self.export_tool_button_clicked)
        tools.addAction('Change', self.change_tool_button_clicked)
        tools.addAction('Vector DB', self.vector_db_tool_button_clicked)
        tools.addAction('Icon', self.icon_tool_button_clicked)
        tools.addAction('Graph Builder', self.graph_builder_tool_button_clicked)
        tools.addAction('Nodes Table', self.nodes_table_tool_button_clicked)
        tools.addAction('Nodes Graph', self.nodes_graph_tool_button_clicked)
        tools.addAction('Relationships', self.relationships_tool_button_clicked)
        tools.addWidget(right_spacer)

    def _createStatusBar(self):        
        status = QStatusBar()
        left_spacer = QWidget()
        left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        message = QLabel('<strong>A Team404: Good Times, Inc. Production</strong><br>')

        status.addWidget(left_spacer)
        status.addWidget(message)
        self.setStatusBar(status)

    # CENTER UI WINDOW ON USER'S DISPLAY
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    ex = PICK_TOOL()
    sys.exit(app.exec_())
