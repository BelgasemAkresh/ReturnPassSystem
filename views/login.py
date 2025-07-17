from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QApplication
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class Login_View(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        # Set layout direction to right-to-left
        self.setLayoutDirection(Qt.RightToLeft)

        main_layout = QVBoxLayout(self)

        # First header line (State of Libya)
        text_label_layout = QHBoxLayout()
        text_label = QLabel('دولة ليبيا')
        header_font = QFont("Arial", 26)
        text_label.setFont(header_font)
        text_label.setAlignment(Qt.AlignCenter)
        text_label_layout.addStretch()
        text_label_layout.addWidget(text_label)
        text_label_layout.addStretch()
        main_layout.addLayout(text_label_layout)

        # Second header line (Ministry of Foreign Affairs)
        text_label_layout = QHBoxLayout()
        text_label = QLabel('وزارة الخارجية و التعاون الدولي')
        text_label.setFont(header_font)
        text_label.setAlignment(Qt.AlignCenter)
        text_label_layout.addStretch()
        text_label_layout.addWidget(text_label)
        text_label_layout.addStretch()
        main_layout.addLayout(text_label_layout)

        # Image logo at the top
        image_layout = QHBoxLayout()
        image_path = 'Bilder/logo.png'
        pixmap = QPixmap(image_path).scaled(300, 300, Qt.KeepAspectRatio)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_layout.addStretch()
        image_layout.addWidget(image_label)
        image_layout.addStretch()
        main_layout.addLayout(image_layout)

        # Add space between sections
        main_layout.addStretch()

        # System title
        text_label_layout = QHBoxLayout()
        text_label = QLabel('منظومة إصدار وثائق العودة بالقنصلية العامة دوسلدورف')
        text_label.setFont(header_font)
        text_label.setAlignment(Qt.AlignCenter)
        text_label_layout.addStretch()
        text_label_layout.addWidget(text_label)
        text_label_layout.addStretch()
        main_layout.addLayout(text_label_layout)

        # Login panel
        login_panel_layout = QVBoxLayout()

        # Password row (label and input field side by side)
        password_row_layout = QHBoxLayout()
        password_row_layout.addStretch()

        self.label = QLabel('أدخل كلمة المرور:')
        label_font = QFont("Arial", 16)
        self.label.setFont(label_font)
        password_row_layout.addWidget(self.label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedSize(200, 40)
        input_font = QFont("Arial", 12)
        self.password_input.setFont(input_font)
        password_row_layout.addWidget(self.password_input)

        password_row_layout.addStretch()
        login_panel_layout.addLayout(password_row_layout)

        # Spacing between input row and buttons
        login_panel_layout.addSpacing(10)

        # Button layout under password field
        buttons_under_label_layout = QHBoxLayout()
        buttons_under_label_layout.addStretch()

        buttons_column = QVBoxLayout()
        buttons_column.setAlignment(Qt.AlignRight)

        # Calculate button width based on label and input field
        btn_width = self.label.sizeHint().width() + self.password_input.width()
        btn_height = 40
        button_font = QFont("Arial", 12)

        # Login button
        self.login_button = QPushButton('تسجيل الدخول')

        # Set size with fixed style that can't be overridden
        self.login_button.setStyleSheet(f"""
            QPushButton {{
                min-width: {btn_width}px;
                max-width: {btn_width}px;
                min-height: {btn_height}px;
                max-height: {btn_height}px;
            }}
        """)
        self.login_button.setFont(button_font)

        # Exit button
        self.exit_button = QPushButton('خروج')

        # Set size with fixed style that can't be overridden
        self.exit_button.setStyleSheet(f"""
            QPushButton {{
                min-width: {btn_width}px;
                max-width: {btn_width}px;
                min-height: {btn_height}px;
                max-height: {btn_height}px;
            }}
        """)
        self.exit_button.setFont(button_font)

        buttons_column.addWidget(self.login_button)
        buttons_column.addSpacing(200)
        buttons_column.addWidget(self.exit_button)

        buttons_under_label_layout.addLayout(buttons_column)
        buttons_under_label_layout.addStretch()

        login_panel_layout.addLayout(buttons_under_label_layout)

        # Connect exit button to quit application
        self.exit_button.clicked.connect(QApplication.quit)

        # Center the login panel
        main_layout.addStretch()
        main_layout.addLayout(login_panel_layout)
        main_layout.addStretch()

        # Footer
        footer_layout = QHBoxLayout()
        footer_text = QLabel('2025 Developed by ')
        footer_text.setStyleSheet("font-size: 16px;")
        logo_path = 'Bilder/itp1.png'
        logo_pixmap = QPixmap(logo_path).scaled(150, 150, Qt.KeepAspectRatio)
        logo_label = QLabel()
        logo_label.setPixmap(logo_pixmap)
        link_label = QLabel(
            '<a href="https://www.itpandmore.com" style="color:#ffffff; text-decoration: none;">www.itpandmore.com</a>')
        link_label.setStyleSheet("color: white; font-size: 16px;")
        link_label.setOpenExternalLinks(True)
        footer_layout.addStretch()
        footer_layout.addWidget(footer_text)
        footer_layout.addWidget(logo_label)
        footer_layout.addWidget(link_label)
        footer_layout.addStretch()
        main_layout.addLayout(footer_layout)

        self.setLayout(main_layout)

    # Zusätzliche Methode, um sicherzustellen, dass Buttons-Größen nicht überschrieben werden
    def showEvent(self, event):
        """Wird aufgerufen, wenn das Widget angezeigt wird"""
        super().showEvent(event)
        # Recalculate button width and enforce it
        btn_width = self.label.sizeHint().width() + self.password_input.width() - 5
        btn_height = 30

        # Aktualisiert die Stylesheet-Eigenschaften beim Anzeigen
        self.login_button.setStyleSheet(f"""
            QPushButton {{
                min-width: {btn_width}px;
                max-width: {btn_width}px;
                min-height: {btn_height}px;
                max-height: {btn_height}px;
            }}
        """)

        self.exit_button.setStyleSheet(f"""
            QPushButton {{
                min-width: {btn_width}px;
                max-width: {btn_width}px;
                min-height: {btn_height}px;
                max-height: {btn_height}px;
            }}
        """)