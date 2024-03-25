from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QLabel,QWidget, QGridLayout, QLineEdit,\
    QHBoxLayout, QComboBox, QPushButton, QPlainTextEdit

from src.utils.RoundingMethod import RoundingMethod

class View(QWidget):

    OUTPUT_STYLE = 'padding: 15px 10px; font-size: 18px; font-family: Inter; background-color: #E9EBF8; border: 1px solid #B4B8C5; border-radius: 10px'

    base10_base: QLineEdit
    base10_exp: QLineEdit
    rounding_method_dropdown: QComboBox
    output_binary: QPlainTextEdit
    output_hex: QPlainTextEdit
    convert_button: QPushButton
    save_button: QPushButton
    layout: QGridLayout

    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.add_styles_to_ui()
        self.add_to_layout()
        self.show()
    
    def bind_controller(self, controller):
        self.controller = controller

        self.convert_button.clicked.connect(self.controller.handle_convert)
        self.save_button.clicked.connect(self.controller.handle_save)
        
    def initialize_ui(self):
        self.setWindowTitle('Decimal128 floating point converter')
        self.setGeometry(100, 100, 1500, 800)
        self.setStyleSheet('background-color: #FEFFFE;')

        self.title_label = QLabel('<h1>Decimal128 Converter</h1>')
        self.base10_label = QLabel('<strong>Base-10<strong/>')
        self.base10_container = QHBoxLayout()
        self.base10_base = QLineEdit()
        self.base10_times_10 = QLabel('x 10')
        self.base10_exp = QLineEdit()
        self.rounding_method_dropdown = QComboBox()
        self.rounding_method_label = QLabel('<strong>Rounding method</strong>')
        self.convert_button = QPushButton('Convert')
        self.output_label = QLabel('<strong>Decimal128 Representation</strong>')
        self.output_binary = QPlainTextEdit()
        self.output_hex = QPlainTextEdit()
        self.save_button = QPushButton('Save')

        self.layout = QGridLayout()

    
    def add_styles_to_ui(self):
        self.layout.setContentsMargins(200, 80, 200, 80)
        self.layout.setHorizontalSpacing(50)
        
        self.title_label.setStyleSheet('font-size: 20px; font-family: Inter; margin: 0; ')
        self.title_label.setFixedHeight(60)

        self.base10_label.setStyleSheet('font-size: 18px; font-family: Inter;')
        self.base10_times_10.setStyleSheet('padding: 15px 10px; font-size: 18px; font-family: Inter; ')
        self.base10_base.setStyleSheet('padding: 15px 10px; font-size: 18px; font-family: Inter; border: 1px solid #B4B8C5; border-radius: 10px;')
        self.base10_base.setFixedWidth(180)
        self.base10_exp.setFixedWidth(100)
        self.base10_exp.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.base10_exp.setStyleSheet('padding: 7.5px 5px; font-size: 15px; font-family: Inter; border: 1px solid #B4B8C5; border-radius: 5px;')
        self.base10_container.addWidget(self.base10_base)
        self.base10_container.addWidget(self.base10_times_10)
        self.base10_container.addWidget(self.base10_exp, 0)

        self.rounding_method_dropdown.addItems(['Round nearest-ties to even', 'Round up', 'Round down'])
        self.rounding_method_dropdown.setStyleSheet('QComboBox::drop-down:button { border: none; border-radius: 5px; width: 50px; background-color: #B4B8C5; padding: 10px 0px 10px; image: url(\'assets/caret-down-solid.svg\') } QComboBox { padding: 15px 10px; font-size: 18px; font-family: Inter; border: 1px solid #B4B8C5; border-radius: 10px;  } QComboBox::drop-down { padding: 15px 10px; }')
        self.rounding_method_label.setStyleSheet('font-size: 18px; font-family: Inter;')

        self.convert_button.setStyleSheet('QPushButton { padding: 18px 10px; font-size: 18px; font-family: Inter; background-color: #B4B8C5; border: 1px solid #E9EBF8; border-radius: 10px; color: #FEFFFE; }')
        self.convert_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.output_label.setStyleSheet('font-size: 18px; font-family: Inter;')
        self.output_binary.setStyleSheet(self.OUTPUT_STYLE)
        self.output_binary.setFixedHeight(150)
        self.output_hex.setFixedHeight(150)
        self.output_hex.setStyleSheet(self.OUTPUT_STYLE)

        self.save_button.setStyleSheet('QPushButton { padding: 18px 10px; font-size: 18px; font-family: Inter; background-color: #FEFFFE; border: 1px solid #E9EBF8; border-radius: 10px; color: #B4B8C5; }')
        self.save_button.setCursor(Qt.CursorShape.PointingHandCursor)


    def add_to_layout(self):

        self.layout.addWidget(self.title_label, 0, 0, 1, 5)
        
        self.layout.addWidget(self.base10_label, 1, 0)

        self.layout.addLayout(self.base10_container, 1, 1, 1, 2)
        self.layout.addWidget(self.rounding_method_label, 2, 0)
        self.layout.addWidget(self.rounding_method_dropdown, 2, 1, 1, 2)
        self.layout.addWidget(self.convert_button, 6, 0, 1, 3)
        self.layout.addWidget(self.output_label, 0, 3, 1, 3)
        self.layout.addWidget(self.output_binary, 1, 3, 1, 3)
        self.layout.addWidget(self.output_hex, 2, 3, 1, 3)
        self.layout.addWidget(self.save_button, 6, 3, 1, 3)

        self.setLayout(self.layout)

    def get_inputs(self):

        round_opts = [
            RoundingMethod.ROUND_TNE,
            RoundingMethod.ROUND_UP,
            RoundingMethod.ROUND_DOWN
        ]

        rounding_option = round_opts[self.rounding_method_dropdown.currentIndex()]
        base = self.base10_base.text()
        exp = self.base10_exp.text()

        return rounding_option, base, exp

    def set_outputs(self, dfp_bin, dfp_hex):
        self.output_binary.setPlainText(dfp_bin)
        self.output_hex.setPlainText(dfp_hex)

    def is_input_valid(self) -> bool:
        return self.base10_base.text() != '' and self.base10_exp.text() != ''
