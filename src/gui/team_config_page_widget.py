def team_configuration(self, team_configuration_page_widget):
        team_layout = QGridLayout()
        team_layout.setVerticalSpacing(50)
        team_title_label = QLabel('<h1>Team Configuration<\h1>')

        team_lead_checkbox = QCheckBox()
        team_lead_checkbox.setText('Lead')
        team_lead_ip_address_label_label = QLabel('Lead IP Address')

        # 255.255.255.255 is an example, this needs to be changed later
        team_lead_ip_address_address_label = QLineEdit('255.255.255.255')
        team_no_of_connections_label_label = QLabel(
            'Number of established connections to the lead\' IP address')

        # 4 is an example, this needs to be changed later
        team_no_of_connections_label = QLineEdit('4')
        team_connect_button = QPushButton('Connect')

        team_layout.addWidget(team_title_label, 0, 0)
        team_layout.addWidget(team_lead_checkbox, 1, 0)
        team_layout.addWidget(team_lead_ip_address_label_label, 2, 0)
        team_layout.addWidget(team_lead_ip_address_address_label, 2, 1)
        team_layout.addWidget(team_no_of_connections_label_label, 3, 0)
        team_layout.addWidget(team_no_of_connections_label, 3, 1)
        team_layout.addWidget(team_connect_button, 4, 0)

        team_configuration_page_widget.setLayout(team_layout)