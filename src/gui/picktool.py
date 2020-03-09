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
        self.team_page(config_dict['team'])
        self.event_page(config_dict['event'])
        self.directory_page(config_dict['directory'])
        self.vector_page(config_dict['vector'])
        self.log_file_page(config_dict['log_file'])
        self.filter_page(config_dict['filter'])
        self.log_entry_page(config_dict['log_entry'])
        self.export_page(config_dict['export'])
        self.change_page(config_dict['change'])
        self.vector_db_page(config_dict['vector_db'])
        self.icon_page(config_dict['icon'])
        self.graph_builder_page(config_dict['graph_builder'])
        self.nodes_tabular_page(config_dict['nodes_tabular'])
        self.nodes_graphical_page(config_dict['nodes_graphical'])
        self.relationship_page(config_dict['relationship'])

        # INITALIZE THE MAIN WINDOW
        self.setFixedSize(1600, 1000)
        self.center()
        self.setWindowTitle('PICK System')
        self.setCentralWidget(self.stackedWidget)
        #self._createToolBar()
        self._createStatusBar()
        self.show()

    # 'HOME' PAGE
    def home_page(self, home_page_widget):
        page_layout = QGridLayout()
        
        # Team404 Logo
        team_logo = QLabel()
        image = QPixmap('src/gui/team_404_logo.PNG')
        smaller_image = image.scaled(500, 500, Qt.KeepAspectRatio, Qt.FastTransformation)
        team_logo.setPixmap(smaller_image)
        team_logo.setAlignment(QtCore.Qt.AlignCenter)

        # Page Heading
        page_header = QLabel('<center><h1>Prevent Mitigate Recover (PMR) Insight Collective Knowledge System<br><br>PICK Tool</h1><br><h2>Government Warning Notice</h2> This is a U.S. Government computer system, which may be accessed and used only for authorized Government business by authorized personnel. Unauthorized access or use of this computer system may subject violators to criminal, civil, and/or administrative action. All information on this computer system may be intercepted, recorded, read, copied, and disclosed by and to authorized personnel for official purposes, including criminal investigations. Such information includes sensitive data encrypted to comply with confidentiality and privacy requirements. Access or use of this computer system by any person, whether authorized or unauthorized, constitutes consent to these terms. There is no right of privacy in this system.</center>')
        page_header.setWordWrap(True) 

        # Connect Button
        connect_button = QPushButton('Connect')
        connect_button.clicked.connect(self.home_connect_button_clicked)

        # Compile Page Widgets
        page_layout.addWidget(page_header, 1, 0)
        page_layout.addWidget(team_logo, 0, 0)
        page_layout.addWidget(connect_button, 3, 0)

        home_page_widget.setLayout(page_layout)


    # 'TEAM CONFIGURATION' PAGE
    def team_page(self, team_page_widget):
        page_layout = QGridLayout()
        page_layout.setVerticalSpacing(60)
        page_header = QLabel('<h1>Team<br>Configuration</h1>')
        lead_ip_address = QLabel('<strong>Lead IP Address:</strong>')

        # 255.255.255.255 is an example, this needs to be changed later
        ip_address = QLineEdit('255.255.255.255')
        established_connections = QLabel('<strong>No. of Established Connections to the lead\'s IP address:</strong>')
        established_connections.setWordWrap(True) 

        # 4 is an example, this needs to be changed later
        connections_value = QLabel('4')
        lead = QLabel('<strong>Lead</strong>')
        lead_checkbox = QCheckBox()
        connect_button = QPushButton('Connect')

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        page_layout.addWidget(page_header, 0, 0)
        page_layout.addWidget(lead_ip_address, 1, 1)
        page_layout.addWidget(ip_address, 1, 3)
        page_layout.addWidget(established_connections, 2, 1)
        page_layout.addWidget(connections_value, 2, 3)
        page_layout.addWidget(lead, 3, 1)
        page_layout.addWidget(lead_checkbox, 3, 3)

        for i in range (0, 5):
            page_layout.addWidget(spacer, 4, i)

        page_layout.addWidget(connect_button, 5, 2)

        team_page_widget.setLayout(page_layout)

    # 'EVENT CONFIGURATION' PAGE GUI
    def event_page(self, event_page_widget): 
        page_layout = QGridLayout()
        page_layout.setVerticalSpacing(60)
        page_header = QLabel('<h1>Event<br>Configuration<\h1>')

        event_name = QLabel('<strong>Event Name:</strong>')
        event_name.setWordWrap(True) 

        event_name_textbox = QLineEdit()

        event_description = QLabel('<strong>Event description:</strong>')
        event_description_textbox = QLineEdit()

        start_timestamp = QLabel('<strong>Event Start Timestamp:</strong>')
        start_timestamp.setWordWrap(True) 
        start_timestamp_textbox = QLineEdit()

        end_timestamp = QLabel('<strong>Event End Timestamp:</strong>')
        start_timestamp.setWordWrap(True) 
        end_timestamp_textbox = QLineEdit()

        save_button = QPushButton('Save Event')

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        page_layout.addWidget(page_header, 0, 0)
        page_layout.addWidget(event_name, 1, 1)
        page_layout.addWidget(event_name_textbox, 1, 3)
        page_layout.addWidget(event_description, 2, 1)
        page_layout.addWidget(event_description_textbox, 2, 3)
        page_layout.addWidget(start_timestamp, 3, 1)
        page_layout.addWidget(start_timestamp_textbox, 3, 3)
        page_layout.addWidget(end_timestamp, 4, 1)
        page_layout.addWidget(end_timestamp_textbox, 4, 3)
        for i in range (0, 5):
            page_layout.addWidget(spacer, 5, i)
        page_layout.addWidget(save_button, 6, 2)

        event_page_widget.setLayout(page_layout)

    # 'DIRECTORY CONFIGURATION' PAGE GUI
    def directory_page(self, directory_page_widget):
        
        page_layout = QGridLayout()
        page_layout.setVerticalSpacing(60)
        page_header = QLabel('<h1>Directory<br>Configuration<\h1>')
        page_header.setWordWrap(True) 

        root_dir = QLabel('<strong>Root Directory</strong>')
        root_dir_text_box = QLineEdit()

        ### TODO: ADD TKINTER SUPPORT FOR DIRECRTORY-SEARCH SUPPORT ###

        # root_dir_search = TKinter()

        red_folder = QLabel('<strong>Red Folder</strong>')
        red_folder_text_box = QLineEdit()
        
        ### TODO: ADD TKINTER SUPPORT FOR DIRECRTORY-SEARCH SUPPORT ###

        # red_folder_search = TKinter()

        blue_folder = QLabel('<strong>Blue Folder</strong>')
        blue_folder_text_box = QLineEdit()
        
        ### TODO: ADD TKINTER SUPPORT FOR DIRECRTORY-SEARCH SUPPORT ###

        # blue_folder_search = TKinter()

        white_folder = QLabel('<strong>White Folder</strong>')
        white_folder_text_box = QLineEdit()

        ### TODO: ADD TKINTER SUPPORT FOR DIRECRTORY-SEARCH SUPPORT ###

        # white_folder_search = TKinter()

        data_ingestion_button = QPushButton('Start Data Ingestion')

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        page_layout.addWidget(page_header, 0, 0)
        page_layout.addWidget(root_dir, 1, 1)
        page_layout.addWidget(root_dir_text_box, 1, 3)
        page_layout.addWidget(red_folder, 2, 1)
        page_layout.addWidget(red_folder_text_box, 2, 3)
        page_layout.addWidget(blue_folder, 3, 1)
        page_layout.addWidget(blue_folder_text_box, 3, 3)
        page_layout.addWidget(white_folder, 4, 1)
        page_layout.addWidget(white_folder_text_box, 4, 3)
        for i in range (0, 5):
            page_layout.addWidget(spacer, 5, i)
        page_layout.addWidget(data_ingestion_button, 6, 2)

        directory_page_widget.setLayout(page_layout)

    def vector_page(self, vector_page_widget):
        
        # SYSTEM BUILDS 'VECTOR CONFIGURATION' PAGE GUI
        page_layout = QGridLayout()
        page_header = QLabel('<h1>Vector<br>Configuration<\h1>')

        vector_table = QTableWidget()
        vector_table.setRowCount(34)
        vector_table.setColumnCount(2)
        vector_table.setHorizontalHeaderLabels(['Vector Name', 'Vector Description'])
        vector_table.resizeColumnsToContents()

        vector_configuration_table_header = QLabel('<h3><center>Vector Table</center></h3>')

        add_button = QPushButton('Add Vector')
        delete_button = QPushButton('Delete Vector')
        edit_button = QPushButton('Edit Vector')

        page_layout.addWidget(page_header,0,0)
        page_layout.addWidget(vector_configuration_table_header,1,1)
        page_layout.addWidget(vector_table,2,1)
        page_layout.addWidget(add_button,3,0)
        page_layout.addWidget(delete_button,4,0)
        page_layout.addWidget(edit_button,5,0)

        vector_page_widget.setLayout(page_layout)

    # 'LOG FILE' PAGE GUI
    def log_file_page(self, log_file_page_widget):
        
        '''Creates Log File Configuration Page Widget'''

        page_layout = QGridLayout()
        page_header = QLabel('<h1>Log File<br>Configuration<\h1>')

        #TODO: ABSTRACT THE TABLE CREATION
        log_file_table = QTableWidget()
        log_file_table.setRowCount(34)
        log_file_table.setColumnCount(6)
        log_file_table.setHorizontalHeaderLabels(['File Name', 'Source', 'Cleansing Status', 'Validation Status', 'Ingestion Status', 'View EA Report'])
        log_file_table.resizeColumnsToContents()

        action_report_table = QTableWidget()
        action_report_table.setRowCount(34)
        action_report_table.setColumnCount(4)
        action_report_table.setHorizontalHeaderLabels(['File Name', 'Log File Name', 'Line Number', 'Error Message'])
        action_report_table.resizeColumnsToContents()

        log_file_table_header = QLabel('<h3><center>Log File Table</center></h3>')
        action_report_table_header = QLabel('<h3><center><br>Enforcement Action Report Table</center></h3>')

        validate_button = QPushButton('Validate')
        cancel_button = QPushButton('Cancel')
        
        page_layout.addWidget(page_header,0,0)
        page_layout.addWidget(log_file_table_header,1,1)
        page_layout.addWidget(log_file_table,2,1)
        page_layout.addWidget(action_report_table_header,3,1)
        page_layout.addWidget(action_report_table,4,1)
        page_layout.addWidget(validate_button,5,0)
        page_layout.addWidget(cancel_button,6,0)

        log_file_page_widget.setLayout(page_layout)


    # 'FILTER' PAGE GUI
    def filter_page(self, filter_page_widget):        
        '''Creates Filter Configuration Page Widget'''
        
        page_layout = QGridLayout()
        page_layout.setVerticalSpacing(30)
        page_header = QLabel('<h1>Filter<br>Configuration<\h1>')

        keyword_search = QLabel('<strong>Keyword Search:</strong>')
        keyword_search_textbox = QLineEdit()

        creator_label = QLabel('<strong>Creator</strong>')
        creator_red_checkbox = QCheckBox('Red')
        creator_blue_checkbox = QCheckBox('Blue')
        creator_white_checkbox = QCheckBox('White')

        event_type_label = QLabel('<strong>Event Type</strong>')
        event_red_checkbox = QCheckBox('Red')
        event_blue_checkbox = QCheckBox('Blue')
        event_white_checkbox = QCheckBox('White')
        
        start_timestamp = QLabel('<strong>Start Timestamp</strong>')
        start_timestamp_textbox = QLineEdit()
        end_timestamp = QLabel('<strong>End Timestamp</strong>')
        end_timestamp_textbox = QLineEdit()

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        apply_button = QPushButton('Apply Filter')

        page_layout.addWidget(page_header, 0, 0)
        page_layout.addWidget(keyword_search, 1, 1)
        page_layout.addWidget(keyword_search_textbox, 1, 3)
        page_layout.addWidget(creator_label, 2, 1)
        page_layout.addWidget(creator_red_checkbox, 2, 3)
        page_layout.addWidget(creator_blue_checkbox, 3, 3)
        page_layout.addWidget(creator_white_checkbox, 4, 3)
        for i in range (0, 5):
            page_layout.addWidget(spacer, 5, i)
        page_layout.addWidget(event_type_label, 6, 1)
        page_layout.addWidget(event_red_checkbox, 6, 3)
        page_layout.addWidget(event_blue_checkbox, 7, 3)
        page_layout.addWidget(event_white_checkbox, 8, 3)
        page_layout.addWidget(start_timestamp, 9, 1)
        page_layout.addWidget(start_timestamp_textbox, 9, 3)
        page_layout.addWidget(end_timestamp, 10,  1)
        page_layout.addWidget(end_timestamp_textbox, 10, 3)
        page_layout.addWidget(apply_button, 11, 2)

        filter_page_widget.setLayout(page_layout)

    # 'LOG ENTRY' PAGE GUI
    def log_entry_page(self, log_entry_page_widget):
        page_layout = QGridLayout()
        page_header = QLabel('<h1>Log Entry<br>Configuration<\h1>')

        log_entry_table_header = QLabel('<h3><center>Log Entry Table</center></h3>')

        log_entry_table = QTableWidget()
        rows = 34
        log_entry_table.setRowCount(rows)
        log_entry_table.setColumnCount(5)

        #FIXME: SET CHECKBOXES IN THE LOG ENTRY TABLE
        log_entry_table.setHorizontalHeaderLabels(['', 'List Number', 'Log Entry Timestamp', 'Log Entry Event', 'Vector'])
        for i in range (rows):
            log_entry_table.setCellWidget(0, rows, QCheckBox())

        log_entry_table.resizeColumnsToContents()

        page_layout.addWidget(page_header,0,0)
        page_layout.addWidget(log_entry_table_header,1,1)
        page_layout.addWidget(log_entry_table,2,1)

        log_entry_page_widget.setLayout(page_layout)


    def export_page(self, export_page_widget):
        # makes export config page widget
        page_layout = QGridLayout()
        page_layout.setVerticalSpacing(100)
        page_header = QLabel('<h1>Export<br>Configuration<\h1>')
        export_menu_label = QLabel('<strong>Export As:</strong>')

        export_dropdown_menu = QComboBox()
        export_dropdown_menu.addItem('PDF')
        export_dropdown_menu.addItem('GIF')
        export_dropdown_menu.addItem('ABC')

        export_export_button = QPushButton()
        export_export_button.setText('Export')

        page_layout.addWidget(page_header, 0, 0)
        page_layout.addWidget(export_menu_label, 1, 0)
        page_layout.addWidget(export_dropdown_menu, 1, 1)
        page_layout.addWidget(export_export_button, 2, 0)

        export_page_widget.setLayout(page_layout)


    def change_page(self, change_page_widget): 
        # makes change config page widget
        page_layout = QGridLayout()
        page_header = QLabel('<h1><strong>Change List:</strong></h1>')

        undo_button = QPushButton()
        undo_button.setText('Undo')
        commit_button = QPushButton()
        commit_button.setText('Commit')

        page_layout.addWidget(page_header)
        page_layout.addWidget(undo_button)
        page_layout.addWidget(commit_button)

        change_page_widget.setLayout(page_layout)


    def vector_db_page(self, vector_db_page_widget):        
        # make vector db config page widget
        page_layout = QGridLayout()
        page_header = QLabel('<h1>Vector DB<br>Configuration<\h1>')
        connection_status = QLabel('<strong><center><br>Connection Status<br>To Lead:<br></center></strong>')
        connection_status.setWordWrap(True)

        ### TODO: ADD FUNCTIONAL NUMBER OF CONNECTED HOSTS ###
        connected_hosts = QLabel('<br>4<br>')
        pulled_table_header = QLabel('<h3><center>Pulled Vector DB Table (Analyst)</center></h3>')
        pushed_table_header = QLabel('<h3><center><br>Pushed Vector DB Table (Analyst)</center></h3>')

        pulled_table = QTableWidget()
        pulled_table.setRowCount(34)
        pulled_table.setColumnCount(1)
        pulled_table.resizeColumnsToContents()

        pushed_table = QTableWidget()
        pushed_table.setRowCount(34)
        pushed_table.setColumnCount(1)
        pushed_table.resizeColumnsToContents()

        pull_button = QPushButton('Pull')
        push_button = QPushButton('Push')

        page_layout.addWidget(page_header, 0,0)
        page_layout.addWidget(pulled_table_header,1,1)
        page_layout.addWidget(pulled_table,2,1)
        page_layout.addWidget(pushed_table_header,5,1)
        page_layout.addWidget(pushed_table,6,1)
        page_layout.addWidget(connection_status,7,0)
        page_layout.addWidget(connected_hosts,7,1)
        page_layout.addWidget(pull_button,8,0)
        page_layout.addWidget(push_button,9,0)
 
        vector_db_page_widget.setLayout(page_layout)


    def icon_page(self, icon_page_widget):
        # makes icon config page
        page_layout = QGridLayout()
        page_header = QLabel('<h1>Icon<br>Configuration<\h1>')

        icon_table = QTableWidget()
        icon_table.setRowCount(34)
        icon_table.setColumnCount(4)
        icon_table.setHorizontalHeaderLabels(['Select', 'Icon Name', 'Icon Source', 'Image Preview'])
        icon_table.resizeColumnsToContents()
        icon_table_header = QLabel('<h3><center>Icon Table (Analyst)</center></h3>')

        add_button = QPushButton()
        add_button.setText('Add Icon')
        icon_delete_icon_button = QPushButton()
        icon_delete_icon_button.setText('Delete Icon')
        icon_edit_icon_button = QPushButton()
        icon_edit_icon_button.setText('Edit Icon')

        page_layout.addWidget(page_header,0,0)
        page_layout.addWidget(icon_table_header,1,1)
        page_layout.addWidget(icon_table,2,1)
        page_layout.addWidget(add_button,3,0)
        page_layout.addWidget(icon_delete_icon_button,4,0)
        page_layout.addWidget(icon_edit_icon_button,5,0)

        icon_page_widget.setLayout(page_layout)


    def graph_builder_page(self, graph_builder_page_widget):        
        # makes Graph builder Config page widget
        page_layout = QGridLayout()        
        page_layout.setVerticalSpacing(100)
        page_header = QLabel('<h1>Graph Builder<br>Configuration</h1>')
        vector_label = QLabel('<strong>Vector:</strong>')

        vector_dropdown_menu = QComboBox()
        vector_dropdown_menu.addItem('Sample Vector 1')
        vector_dropdown_menu.addItem('Sample Vector 2')
        description_label = QLabel('<strong>Description:</strong>')
        graph_builder_description_label = QLineEdit('Example Description')

        add_node_button = QPushButton('Add Node')
        add_relationship_button = QPushButton('Add Relationship')
        delete_node_button = QPushButton('Delete Node')
        delete_relationship_button = QPushButton('Delete Relationship')
        edit_node_button = QPushButton('Edit Node')
        edit_relationship_button = QPushButton('Edit Relationship')

        page_layout.addWidget(page_header,0,0)
        page_layout.addWidget(vector_label,1,1)
        page_layout.addWidget(vector_dropdown_menu,1,2)

        page_layout.addWidget(description_label,2,1)
        page_layout.addWidget(graph_builder_description_label,2,2)

        page_layout.addWidget(add_node_button,3,0)
        page_layout.addWidget(add_relationship_button,3,2)
        page_layout.addWidget(delete_node_button,4,0)
        page_layout.addWidget(delete_relationship_button,4,2)
        page_layout.addWidget(edit_node_button,5,0)
        page_layout.addWidget(edit_relationship_button,5,2)

        graph_builder_page_widget.setLayout(page_layout)


    def nodes_tabular_page(self, nodes_tabular_page_widget):        
        # makes nodes config table page widget
        page_layout = QGridLayout()
        page_header = QLabel('<h1>Nodes<br>Configuration<\h1><h2>In Tabular Format<\h2>')
        page_header.setWordWrap(True) 

        node_table = QTableWidget()
        node_table.setRowCount(34)
        node_table.setColumnCount(11)
        node_table.setHorizontalHeaderLabels(['Node Property Visibility', 'Node ID', 'Node Name', 'Node Timestamp',
                                                       'Node Description', 'Log Entry Reference', 'Log Creator', 'Event Type', 'Icon Type', 'Source', 'Node Visibility'])
        node_table.resizeColumnsToContents()
        node_table_header = QLabel('<h3><center>Node Table</center></h3>')

        page_layout.addWidget(page_header,0,0)
        page_layout.addWidget(node_table_header,1,1)
        page_layout.addWidget(node_table,2,1)

        nodes_tabular_page_widget.setLayout(page_layout)


    def nodes_graphical_page(self, nodes_graphical_page_widget):        
        # makes nodes config graph page widget
        page_layout = QGridLayout()
        page_layout.setVerticalSpacing(60)
        page_header = page_header = QLabel('<h1>Nodes<br>Configuration<\h1><h2>In Graphical Format<\h2>')
        page_header.setWordWrap(True) 

        nodes_graphical_timeline_orientation_label = QLabel('<strong>Timeline Orientation</strong>')
        nodes_graphical_timeline_orientation_dropdown = QComboBox()
        nodes_graphical_timeline_orientation_dropdown.addItem('example orientation')

        nodes_graphical_interval_units_label = QLabel('<strong>Interval Units</strong>')
        nodes_graphical_interval_units_dropdown = QComboBox()
        nodes_graphical_interval_units_dropdown.addItem('example interval unit')
        nodes_graphical_timeline = QLabel('<strong>A TIMELINE IS SUPPOSED TO GO HERE</strong>')
        nodes_graphical_zoom_in_button = QPushButton()
        nodes_graphical_zoom_in_button.setText('Zoom In')
        nodes_graphical_zoom_out_button = QPushButton()
        nodes_graphical_zoom_out_button.setText('Zoom Out')

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        page_layout.addWidget(page_header,0,0)
        page_layout.addWidget(nodes_graphical_timeline_orientation_label,1,1)
        page_layout.addWidget(nodes_graphical_timeline_orientation_dropdown,1,2)
        page_layout.addWidget(nodes_graphical_interval_units_label,2,1)
        page_layout.addWidget(nodes_graphical_interval_units_dropdown,2,2)
        page_layout.addWidget(nodes_graphical_timeline,3,1)
        page_layout.addWidget(nodes_graphical_zoom_in_button,4,1)
        page_layout.addWidget(nodes_graphical_zoom_out_button,4,2)
        for i in range (0, 5):
            page_layout.addWidget(spacer, 5, i)

        nodes_graphical_page_widget.setLayout(page_layout)


    def relationship_page(self, relationship_page_widget):
        # makes relationships config page widget
        page_layout = QGridLayout()
        page_header = QLabel('<h1>Relationship<br>Configuration<\h1>')

        relationship_table = QTableWidget()
        relationship_table.setRowCount(34)
        relationship_table.setColumnCount(7)
        relationship_table_header = QLabel('<h3><center>Relationship Table</center></h3>')

        page_layout.addWidget(page_header,0,0)
        page_layout.addWidget(relationship_table_header,1,1)
        page_layout.addWidget(relationship_table,2,1)

        relationship_page_widget.setLayout(page_layout)


    # IN-PAGE BUTTONS
    def home_connect_button_clicked(self):        
        self.stackedWidget.setCurrentIndex(1)
        self.buttonClicked()
        self._createToolBar()

    # TOOLBAR BUTTONS
    def team_button_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.buttonClicked()

    def team_page_connect_button_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        self.buttonClicked()

    def event_button_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        self.buttonClicked()

    def directory_button_clicked(self):
        self.stackedWidget.setCurrentIndex(3)
        self.buttonClicked()

    def vector_button_clicked(self):
        self.stackedWidget.setCurrentIndex(4)
        self.buttonClicked()

    def log_file_button_clicked(self):
        self.stackedWidget.setCurrentIndex(5)
        self.buttonClicked()

    def filter_button_clicked(self):
        self.stackedWidget.setCurrentIndex(6)
        self.buttonClicked()

    def log_entry_button_clicked(self):
        self.stackedWidget.setCurrentIndex(7)
        self.buttonClicked()

    def export_button_clicked(self):
        self.stackedWidget.setCurrentIndex(8)
        self.buttonClicked()

    def change_button_clicked(self):
        self.stackedWidget.setCurrentIndex(9)
        self.buttonClicked()

    def vector_db_button_clicked(self):
        self.stackedWidget.setCurrentIndex(10)
        self.buttonClicked()

    def icon_button_clicked(self):
        self.stackedWidget.setCurrentIndex(11)
        self.buttonClicked()

    def graph_builder_button_clicked(self):
        self.stackedWidget.setCurrentIndex(12)
        self.buttonClicked()

    def nodes_table_button_clicked(self):
        self.stackedWidget.setCurrentIndex(13)
        self.buttonClicked()

    def nodes_graph_button_clicked(self):
        self.stackedWidget.setCurrentIndex(14)
        self.buttonClicked()

    def relationships_button_clicked(self):
        self.stackedWidget.setCurrentIndex(15)
        self.buttonClicked()

    def buttonClicked(self):
        sender = self.sender()

    def nav_button_clicked(self, toolbar_index):
        stackedWidget.setCurrentIndex(toolbar_index)
        buttonClicked()


    def _createToolBar(self):
        navigation = QToolBar()
        self.addToolBar(navigation)

        # SPACERS WIDGETS FOR CENTERING TOOLBAR
        left_spacer = QWidget()
        right_spacer = QWidget()

        left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        navigation.addWidget(left_spacer)
        #navigation.addAction('Home', self.home_button_clicked)
        navigation.addAction('Team', self.team_button_clicked)
        navigation.addAction('Event', self.event_button_clicked)
        navigation.addAction('Directory', self.directory_button_clicked)
        navigation.addAction('Vector', self.vector_button_clicked)
        navigation.addAction('Log File', self.log_file_button_clicked)
        navigation.addAction('Filter', self.filter_button_clicked)
        navigation.addAction('Log Entry', self.log_entry_button_clicked)
        navigation.addAction('Export', self.export_button_clicked)
        navigation.addAction('Change', self.change_button_clicked)
        navigation.addAction('Vector DB', self.vector_db_button_clicked)
        navigation.addAction('Icon', self.icon_button_clicked)
        navigation.addAction('Graph Builder', self.graph_builder_button_clicked)
        navigation.addAction('Nodes Table', self.nodes_table_button_clicked)
        navigation.addAction('Nodes Graph', self.nodes_graph_button_clicked)
        navigation.addAction('Relationships', self.relationships_button_clicked)
        navigation.addWidget(right_spacer)

    def _createStatusBar(self):        
        status = QStatusBar()
        left_spacer = QWidget()
        left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        message = QLabel('<strong><center>PICK Tool, Version 0.4.0.<br><br>A Team404: Good Times, Inc. Production</center></strong>')

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
