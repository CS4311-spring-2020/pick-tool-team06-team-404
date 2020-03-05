#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
PICK Tool: Team6 - Team404
Program Purpose:
        - GUI prototype for the clients
Date:
        - 04 March 2020
Dependencies:
        - pyqt5
NOTES:
'''


import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# View
#   QStackedWidget

# Config/Control
#       Trigger.Connect()
#       Clicked.Connet()


class Pick(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        '''Builds the UI for the user'''
        
        # PAGES THAT USER INTERACTS WITH
        team_configuration_page_widget = QWidget()
        event_configuration_page_widget = QWidget()
        directory_configuration_page_widget = QWidget()
        vector_configuration_page_widget = QWidget()
        log_file_configuration_page_widget = QWidget()
        filter_configuration_page_widget = QWidget()
        log_entry_configuration_page_widget = QWidget()
        export_configuration_page_widget = QWidget()
        change_configuration_page_widget = QWidget()
        vector_db_configuration_page_widget = QWidget()
        icon_configuration_page_widget = QWidget()
        graph_builder_configuration_page_widget = QWidget()
        nodes_tabular_configuration_page_widget = QWidget()
        nodes_graphical_configuration_page_widget = QWidget()
        relationship_configuration_page_widget = QWidget()

        # CLICKABLE WIDGETS THAT APPEAR ATOP PAGES
        self.stackedWidget = QStackedWidget(self)

        self.stackedWidget.addWidget(team_configuration_page_widget)
        self.stackedWidget.addWidget(event_configuration_page_widget)
        self.stackedWidget.addWidget(directory_configuration_page_widget)
        self.stackedWidget.addWidget(vector_configuration_page_widget)
        self.stackedWidget.addWidget(log_file_configuration_page_widget)
        self.stackedWidget.addWidget(filter_configuration_page_widget)
        self.stackedWidget.addWidget(log_entry_configuration_page_widget)
        self.stackedWidget.addWidget(export_configuration_page_widget)
        self.stackedWidget.addWidget(change_configuration_page_widget)
        self.stackedWidget.addWidget(vector_db_configuration_page_widget)
        self.stackedWidget.addWidget(icon_configuration_page_widget)
        self.stackedWidget.addWidget(graph_builder_configuration_page_widget)
        self.stackedWidget.addWidget(nodes_tabular_configuration_page_widget)
        self.stackedWidget.addWidget(nodes_graphical_configuration_page_widget)
        self.stackedWidget.addWidget(relationship_configuration_page_widget)

        # CREATE UI PAGES
        self.team_configuration_ui(team_configuration_page_widget)
        self.event_configuration_ui(event_configuration_page_widget)
        self.directory_configuration_ui(directory_configuration_page_widget)
        self.vector_configuration_ui(vector_configuration_page_widget)
        self.log_file_configuration_ui(log_file_configuration_page_widget)
        self.filter_configuration_ui(filter_configuration_page_widget)
        self.log_entry_configuration(log_entry_configuration_page_widget)
        self.export_configuration(export_configuration_page_widget)
        self.change_configuration(change_configuration_page_widget)
        self.vector_db_configuration(vector_db_configuration_page_widget)
        self.icon_configuration(icon_configuration_page_widget)
        self.graph_builder_configuration(graph_builder_configuration_page_widget)
        self.nodes_tabular_configuration(nodes_tabular_configuration_page_widget)
        self.nodes_graphical_configuration(nodes_graphical_configuration_page_widget)
        self.relationship_configuration(relationship_configuration_page_widget)

        # INITALIZE THE MAIN WINDOW
        self.resize(1920,1080)
        self.center()
        self.setWindowTitle('PMR Insight Collective Knowledge System (PICK) Tool')
        self.setCentralWidget(self.stackedWidget)
        self._createToolBar()
        self._createStatusBar()
        self.show()

    def team_configuration_ui(self, team_configuration_page_widget):
        # 'TEAM CONFIGURATION' PAGE
        team_configuration_layout = QGridLayout()
        team_configuration_title_label = QLabel('<h1>Team Configuration<\h1>')

        team_configuration_lead_checkbox = QCheckBox()
        team_configuration_lead_checkbox.setText('Lead')
        team_configuration_lead_ip_address_label_label = QLabel('Lead IP Address')

        # 255.255.255.255 is an example, this needs to be changed later
        team_configuration_lead_ip_address_address_label = QLabel('255.255.255.255')
        team_configuration_no_of_connections_label_label = QLabel('Number of established connections to the lead\' IP address')

        # 4 is an example, this needs to be changed later
        team_configuration_no_of_connections_label = QLabel('4')
        team_configuration_connect_button = QPushButton('Connect')

        team_configuration_layout.addWidget(team_configuration_title_label, 0, 0)
        team_configuration_layout.addWidget(team_configuration_lead_checkbox, 1, 0)
        team_configuration_layout.addWidget(team_configuration_lead_ip_address_label_label, 2, 0)
        team_configuration_layout.addWidget(team_configuration_lead_ip_address_address_label, 2, 1)
        team_configuration_layout.addWidget(team_configuration_no_of_connections_label_label, 3, 0)
        team_configuration_layout.addWidget(team_configuration_no_of_connections_label, 3, 1)
        team_configuration_layout.addWidget(team_configuration_connect_button, 4, 3)

        team_configuration_page_widget.setLayout(team_configuration_layout)

    def event_configuration_ui(self, event_configuration_page_widget):    
        # 'EVENT CONFIGURATION' PAGE
        event_configuration_layout = QGridLayout()
        event_configuration_title_label = QLabel('<h1>Event Configuration<\h1>')

        event_configuration_event_name = QLineEdit()
        event_configuration_event_name.setText('Event Name: ')

        event_configuration_event_description = QLineEdit()
        event_configuration_event_description.setText('Event description: ')

        event_configuration_event_start_timestamp = QLineEdit()
        event_configuration_event_start_timestamp.setText('Start timestamp: ')

        event_configuration_event_end_timestamp = QLineEdit()
        event_configuration_event_end_timestamp.setText('End timestamp: ')

        event_configuration_layout.addWidget(event_configuration_title_label)
        event_configuration_layout.addWidget(event_configuration_event_name)
        event_configuration_layout.addWidget(event_configuration_event_description)
        event_configuration_layout.addWidget(event_configuration_event_start_timestamp)
        event_configuration_layout.addWidget(event_configuration_event_end_timestamp)

        event_configuration_page_widget.setLayout(event_configuration_layout)

    def directory_configuration_ui(self, directory_configuration_page_widget):    
        # SYSTEM BUILDS 'DIRECTORY CONFIGURATION' PAGE GUI
        directory_configuration_layout = QGridLayout()
        directory_configuration_title_label = QLabel('<h1>Directory Configuration<\h1>')


        directory_configuration_root_directory = QLineEdit()
        directory_configuration_root_directory.setText('Root Directory')

        directory_configuration_red_folder = QLineEdit()
        directory_configuration_red_folder.setText('Red folder')

        directory_configuration_blue_folder = QLineEdit()
        directory_configuration_blue_folder.setText('Blue Folder')

        directory_configuration_white_folder = QLineEdit()
        directory_configuration_white_folder.setText('White Folder')

        directory_configuration_start_data_ingestion_button = QPushButton()
        directory_configuration_start_data_ingestion_button.setText('Start Data Ingestion')

        directory_configuration_layout.addWidget(directory_configuration_title_label)
        directory_configuration_layout.addWidget(directory_configuration_root_directory)
        directory_configuration_layout.addWidget(directory_configuration_red_folder)
        directory_configuration_layout.addWidget(directory_configuration_blue_folder)
        directory_configuration_layout.addWidget(directory_configuration_white_folder)
        directory_configuration_layout.addWidget(directory_configuration_start_data_ingestion_button)

        directory_configuration_page_widget.setLayout(directory_configuration_layout)

    def vector_configuration_ui(self, vector_configuration_page_widget):    
        # SYSTEM BUILDS 'VECTOR CONFIGURATION' PAGE GUI
        vector_configuration_layout = QGridLayout()
        vector_configuration_title_label = QLabel('<h1>Vector Configuration<\h1>')

        vector_configuration_table = QTableWidget()
        vector_configuration_table.setRowCount(34)
        vector_configuration_table.setColumnCount(2)
        vector_configuration_table.setHorizontalHeaderLabels(['Vector Name', 'Vector Description'])

        vector_configuration_add_button = QPushButton()
        vector_configuration_add_button.setText('Add Vector')
        vector_configuration_delete_button = QPushButton()
        vector_configuration_delete_button.setText('Delete Vector')
        vector_configuration_edit_button = QPushButton()
        vector_configuration_edit_button.setText('Edit Vector')

        vector_configuration_layout.addWidget(vector_configuration_title_label)
        vector_configuration_layout.addWidget(vector_configuration_table)
        vector_configuration_layout.addWidget(vector_configuration_add_button)
        vector_configuration_layout.addWidget(vector_configuration_delete_button)
        vector_configuration_layout.addWidget(vector_configuration_edit_button)

        vector_configuration_page_widget.setLayout(vector_configuration_layout)

    def log_file_configuration_ui(self, log_file_configuration_page_widget):    
        # SYSTEM BUILDS 'LOG FILE CONFIGURATION' PAGE GUI
        log_file_configuration_layout = QGridLayout()
        log_file_configuration_title_label = QLabel('<h1>Log File Configuration<\h1>')

        log_file_configuration_log_file_table = QTableWidget()
        log_file_configuration_log_file_table.setRowCount(34)
        log_file_configuration_log_file_table.setColumnCount(6)
        log_file_configuration_log_file_table.setHorizontalHeaderLabels(['File Name', 'Source', 'Cleansing Status', 'Validation', 'Ingestion Status', 'View EA Report'])
        
        log_file_configuration_action_report_table = QTableWidget()
        log_file_configuration_action_report_table.setRowCount(34)
        log_file_configuration_action_report_table.setColumnCount(3)
        log_file_configuration_action_report_table.setHorizontalHeaderLabels(['File Name', 'Line Number', 'Error Message'])
        
        log_file_configuration_validate_button = QPushButton()
        log_file_configuration_validate_button.setText('Validate')
        
        log_file_configuration_cancel_button = QPushButton()
        log_file_configuration_cancel_button.setText('Cancel')

        log_file_configuration_layout.addWidget(log_file_configuration_title_label)
        log_file_configuration_layout.addWidget(log_file_configuration_log_file_table)
        log_file_configuration_layout.addWidget(log_file_configuration_action_report_table)

        log_file_configuration_page_widget.setLayout(log_file_configuration_layout)

    def filter_configuration_ui(self, filter_configuration_page_widget):    
        # makes filter config page widget
        filter_configuration_layout = QGridLayout()
        filter_configuration_title_label = QLabel('<h1>Filter Configuration<\h1>')

        filter_configuration_keyword_search_textbox = QLineEdit()
        filter_configuration_keyword_search_textbox.setText('Keyword Search')
        filter_configuration_creator_label = QLabel('Creator')
        filter_configuration_red_checkbox = QCheckBox()
        filter_configuration_red_checkbox.setText('Red')
        filter_configuration_blue_checkbox = QCheckBox()
        filter_configuration_blue_checkbox.setText('Blue')
        filter_configuration_white_checkbox = QCheckBox()
        filter_configuration_white_checkbox.setText('White')
        filter_configuration_start_timestamp = QLineEdit()
        filter_configuration_start_timestamp.setText('Start Timestamp')
        filter_configuration_end_timestamp = QLineEdit()
        filter_configuration_end_timestamp.setText('End Timestamp')

        filter_configuration_layout.addWidget(filter_configuration_title_label)
        filter_configuration_layout.addWidget(filter_configuration_keyword_search_textbox)
        filter_configuration_layout.addWidget(filter_configuration_creator_label)
        filter_configuration_layout.addWidget(filter_configuration_red_checkbox)
        filter_configuration_layout.addWidget(filter_configuration_blue_checkbox)
        filter_configuration_layout.addWidget(filter_configuration_white_checkbox)
        filter_configuration_layout.addWidget(filter_configuration_start_timestamp)
        filter_configuration_layout.addWidget(filter_configuration_end_timestamp)

        filter_configuration_page_widget.setLayout(filter_configuration_layout)

    def log_entry_configuration(self, log_entry_configuration_page_widget):    
        # makes log entry config page widget
        log_entry_configuration_layout = QGridLayout()
        log_entry_configuration_title_label = QLabel('<h1>Log Entry Configuration<\h1>')
        
        log_entry_configuration_table = QTableWidget()
        log_entry_configuration_table.setRowCount(34)
        log_entry_configuration_table.setColumnCount(5)
        log_entry_configuration_table.setHorizontalHeaderLabels(['', 'List Number', 'Log Entry Timestamp', 'Log Entry Event', 'Vector'])

        log_entry_configuration_layout.addWidget(log_entry_configuration_title_label)
        log_entry_configuration_layout.addWidget(log_entry_configuration_table)

        log_entry_configuration_page_widget.setLayout(log_entry_configuration_layout)

    def export_configuration(self, export_configuration_page_widget):   
        # makes export config page widget
        export_configuration_layout = QGridLayout()
        export_configuration_menu_label = QLabel('Export as: ')

        export_configuration_dropdown_menu = QComboBox()
        export_configuration_dropdown_menu.addItem('PDF')
        export_configuration_dropdown_menu.addItem('GIF')
        export_configuration_dropdown_menu.addItem('ABC')
        
        export_configuration_export_button = QPushButton()
        export_configuration_export_button.setText('Export')

        export_configuration_layout.addWidget(export_configuration_menu_label)
        export_configuration_layout.addWidget(export_configuration_dropdown_menu)
        export_configuration_layout.addWidget(export_configuration_export_button)

        export_configuration_page_widget.setLayout(export_configuration_layout)

    def change_configuration(self, change_configuration_page_widget):   
        # makes change config page widget
        change_configuration_layout = QGridLayout()
        change_configuration_change_list_label = QLabel('Change List: ')

        change_configuration_undo_button = QPushButton()
        change_configuration_undo_button.setText('Undo')
        change_configuration_commit_button = QPushButton()
        change_configuration_commit_button.setText('Commit')

        change_configuration_layout.addWidget(change_configuration_change_list_label)
        change_configuration_layout.addWidget(change_configuration_undo_button)
        change_configuration_layout.addWidget(change_configuration_commit_button)

        change_configuration_page_widget.setLayout(change_configuration_layout)

    def vector_db_configuration(self, vector_db_configuration_page_widget):   
        # make vector db config page widget
        vector_db_configuration_layout = QGridLayout()
        vector_db_configuration_connection_label = QLabel('Connection status to lead: ')

        # 4 is just and example, this needs to be changed later
        vector_db_configuration_actual_connection_number = QLabel('4')
        vector_db_configuration_pulled_vector_table = QLabel('PULLED vector DB table (Analyst)')
        
        vector_db_configuration_pulled_table = QTableWidget()
        vector_db_configuration_pulled_table.setRowCount(34)
        vector_db_configuration_pulled_table.setColumnCount(1)
        
        vector_db_configuration_pull_button = QPushButton()
        vector_db_configuration_pull_button.setText('Pull')

        vector_db_configuration_pushed_vector_label = QLabel('PUSHED vector DB table (Analyst)')
        vector_db_configuration_pushed_table = QTableWidget()
        vector_db_configuration_pushed_table.setRowCount(34)
        vector_db_configuration_pushed_table.setColumnCount(1)
        vector_db_configuration_push_button = QPushButton()
        vector_db_configuration_push_button.setText('Push')

        vector_db_configuration_layout.addWidget(vector_db_configuration_connection_label)
        vector_db_configuration_layout.addWidget(vector_db_configuration_actual_connection_number)
        vector_db_configuration_layout.addWidget(vector_db_configuration_pulled_table)
        vector_db_configuration_layout.addWidget(vector_db_configuration_pull_button)
        vector_db_configuration_layout.addWidget(vector_db_configuration_pushed_vector_label)
        vector_db_configuration_layout.addWidget(vector_db_configuration_pushed_table)
        vector_db_configuration_layout.addWidget(vector_db_configuration_push_button)

        vector_db_configuration_page_widget.setLayout(vector_db_configuration_layout)

    def icon_configuration(self, icon_configuration_page_widget):   
        # makes icon config page
        icon_configuration_layout = QGridLayout()
        icon_configuration_title_label = QLabel('<h1>Icon Configuration<\h1>')

        icon_configuration_table = QTableWidget()
        icon_configuration_table.setRowCount(34)
        icon_configuration_table.setColumnCount(4)
        icon_configuration_table.setHorizontalHeaderLabels(['Select', 'Icon Name', 'Icon Source', 'Image Preview'])

        icon_configuration_add_icon_button = QPushButton()
        icon_configuration_add_icon_button.setText('Add Icon')
        icon_configuration_delete_icon_button = QPushButton()
        icon_configuration_delete_icon_button.setText('Delete Icon')
        icon_configuration_edit_icon_button = QPushButton()
        icon_configuration_edit_icon_button.setText('Edit Icon')

        icon_configuration_layout.addWidget(icon_configuration_title_label)
        icon_configuration_layout.addWidget(icon_configuration_table)
        icon_configuration_layout.addWidget(icon_configuration_add_icon_button)
        icon_configuration_layout.addWidget(icon_configuration_delete_icon_button)
        icon_configuration_layout.addWidget(icon_configuration_edit_icon_button)

        icon_configuration_page_widget.setLayout(icon_configuration_layout)

    def graph_builder_configuration(self, graph_builder_configuration_page_widget):   
        # makes Graph builder Config page widget
        graph_builder_configuration_layout = QGridLayout()
        graph_builder_configuration_vector_label = QLabel('Vector: ')

        graph_builder_configuration_vector_dropdown_menu = QComboBox()
        graph_builder_configuration_vector_dropdown_menu.addItem('example vector 1')
        graph_builder_configuration_vector_dropdown_menu.addItem('example vector 2')
        graph_builder_configuration_description_label_label = QLabel('Description')
        graph_builder_configuration_description_label = QLineEdit()
        graph_builder_configuration_description_label.setText('Example description')
        graph_builder_configuration_add_node_button = QPushButton()
        graph_builder_configuration_add_node_button.setText('Add Node')
        graph_builder_configuration_add_relationship_button = QPushButton()
        graph_builder_configuration_add_relationship_button.setText('Add Relationship')
        graph_builder_configuration_delete_node_button = QPushButton()
        graph_builder_configuration_delete_node_button.setText('Delete Node')
        graph_builder_configuration_delete_relationship_button = QPushButton()
        graph_builder_configuration_delete_relationship_button.setText('Delete Relationship')
        graph_builder_configuration_edit_node_button = QPushButton()
        graph_builder_configuration_edit_node_button.setText('Edit Node')
        graph_builder_configuration_edit_relationship_button = QPushButton()
        graph_builder_configuration_edit_relationship_button.setText('Edit Relationship')

        graph_builder_configuration_layout.addWidget(graph_builder_configuration_vector_label)
        graph_builder_configuration_layout.addWidget(graph_builder_configuration_vector_dropdown_menu)
        graph_builder_configuration_layout.addWidget(graph_builder_configuration_description_label_label)
        graph_builder_configuration_layout.addWidget(graph_builder_configuration_description_label)
        graph_builder_configuration_layout.addWidget(graph_builder_configuration_add_node_button)
        graph_builder_configuration_layout.addWidget(graph_builder_configuration_add_relationship_button)
        graph_builder_configuration_layout.addWidget(graph_builder_configuration_delete_node_button)
        graph_builder_configuration_layout.addWidget(graph_builder_configuration_delete_relationship_button)
        graph_builder_configuration_layout.addWidget(graph_builder_configuration_edit_node_button)
        graph_builder_configuration_layout.addWidget(graph_builder_configuration_edit_relationship_button)

        graph_builder_configuration_page_widget.setLayout(graph_builder_configuration_layout)

    def nodes_tabular_configuration(self, nodes_tabular_configuration_page_widget):   
        # makes nodes config table page widget
        nodes_tabular_configuration_layout = QGridLayout()
        nodes_tabular_configuration_title_label = QLabel('<h1>Nodes Configuration in Tabular Format<\h1>')

        nodes_tabular_configuration_table = QTableWidget()
        nodes_tabular_configuration_table.setRowCount(34)
        nodes_tabular_configuration_table.setColumnCount(11)
        nodes_tabular_configuration_table.setHorizontalHeaderLabels(['Node Property Visibility', 'Node ID', 'Node Name', 'Node Timestamp', 'Node Description', 'Log Entry Reference', 'Log Creator', 'Event Type', 'Icon Type', 'Source', 'Node Visibility'])
        
        nodes_tabular_configuration_layout.addWidget(nodes_tabular_configuration_title_label)
        nodes_tabular_configuration_layout.addWidget(nodes_tabular_configuration_table)

        nodes_tabular_configuration_page_widget.setLayout(nodes_tabular_configuration_layout)

    def nodes_graphical_configuration(self, nodes_graphical_configuration_page_widget):
        # makes nodes config graph page widget
        nodes_graphical_configuration_layout = QGridLayout()
        nodes_graphical_configuration_title_label = QLabel('Nodes Configuration in Graphical Format')

        nodes_graphical_configuration_timeline_orientation_label = QLabel('Timeline Orientation')
        nodes_graphical_configuration_timeline_orientation_dropdown = QComboBox()
        nodes_graphical_configuration_timeline_orientation_dropdown.addItem('example orientation')

        nodes_graphical_configuration_interval_units_label = QLabel('Interval Units')
        nodes_graphical_configuration_interval_units_dropdown = QComboBox()
        nodes_graphical_configuration_interval_units_dropdown.addItem('example interval unit')
        nodes_graphical_configuration_timeline = QLabel('A TIMELINE IS SUPPOSED TO GO HERE')
        nodes_graphical_configuration_zoom_in_button = QPushButton()
        nodes_graphical_configuration_zoom_in_button.setText('Zoom In')
        nodes_graphical_configuration_zoom_out_button = QPushButton()
        nodes_graphical_configuration_zoom_out_button.setText('Zoom Out')

        nodes_graphical_configuration_layout.addWidget(nodes_graphical_configuration_title_label)
        nodes_graphical_configuration_layout.addWidget(nodes_graphical_configuration_timeline_orientation_label)
        nodes_graphical_configuration_layout.addWidget(nodes_graphical_configuration_timeline_orientation_dropdown)
        nodes_graphical_configuration_layout.addWidget(nodes_graphical_configuration_interval_units_label)
        nodes_graphical_configuration_layout.addWidget(nodes_graphical_configuration_interval_units_dropdown)
        nodes_graphical_configuration_layout.addWidget(nodes_graphical_configuration_timeline)
        nodes_graphical_configuration_layout.addWidget(nodes_graphical_configuration_zoom_in_button)
        nodes_graphical_configuration_layout.addWidget(nodes_graphical_configuration_zoom_out_button)

        nodes_graphical_configuration_page_widget.setLayout(nodes_graphical_configuration_layout)

    def relationship_configuration(self, relationship_configuration_page_widget):
        # makes relationships config page widget
        relationship_config_layout = QGridLayout()
        relationship_config_title_label = QLabel('<h1>Relationship Configuration<\h1>')

        relationship_config_table = QTableWidget()

        relationship_config_table.setRowCount(34)
        relationship_config_table.setColumnCount(7)

        relationship_config_layout.addWidget(relationship_config_title_label)
        relationship_config_layout.addWidget(relationship_config_table)

        relationship_configuration_page_widget.setLayout(relationship_config_layout)

    def team_configuration_connect_button_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.buttonClicked()

    def team_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        self.buttonClicked()

    def event_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.buttonClicked()

    def directory_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        self.buttonClicked()

    def vector_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(3)
        self.buttonClicked()

    def log_file_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(4)
        self.buttonClicked()

    def filter_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(5)
        self.buttonClicked()

    def log_entry_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(6)
        self.buttonClicked()

    def export_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(7)
        self.buttonClicked()

    def change_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(8)
        self.buttonClicked()

    def vector_db_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(9)
        self.buttonClicked()

    def icon_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(10)
        self.buttonClicked()

    def graph_builder_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(11)
        self.buttonClicked()

    def nodes_table_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(12)
        self.buttonClicked()

    def nodes_graph_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(13)
        self.buttonClicked()

    def relationships_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(14)
        self.buttonClicked()

    def buttonTwoClicked(self):
        self.buttonClicked()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was clicked')

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)

        tools.addAction('Exit', self.close)
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
        tools.addAction('Graph Builder',
                        self.graph_builder_tool_button_clicked)
        tools.addAction('Nodes Table', self.nodes_table_tool_button_clicked)
        tools.addAction('Nodes Graph', self.nodes_graph_tool_button_clicked)
        tools.addAction('Relationships',
                        self.relationships_tool_button_clicked)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

    # all this does is center the qwidget called window
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    ex = Pick()
    sys.exit(app.exec_())
