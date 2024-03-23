from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QHBoxLayout, QComboBox, QPushButton, QPlainTextEdit
from PyQt6.QtCore import Qt

from src.app.model import Model
from src.app.controller import Controller, convert, save
from src.app.view import View

OUTPUT_STYLE = 'padding: 15px 10px; font-size: 18px; font-family: Inter; background-color: #E9EBF8; border: 1px solid #B4B8C5; border-radius: 10px'

def main():
    app = QApplication([])
    model = Model()
    view = View()
    controller = Controller(model, view)
    app.exec()

# def main():
#     app = QApplication([])
    
#     window = QWidget()
#     window.setWindowTitle('Decimal128 floating point converter')
#     window.setGeometry(100, 100, 1500, 800)
#     window.setStyleSheet('background-color: #FEFFFE;')

#     layout = QGridLayout()
#     layout.setContentsMargins(200, 80, 200, 80)
#     layout.setHorizontalSpacing(50)


#     title_label = QLabel('<h1>Decimal128 Converter</h1>')
#     title_label.setStyleSheet('font-size: 20px; font-family: Inter; margin: 0; ')
#     title_label.setFixedHeight(60)
#     layout.addWidget(title_label, 0, 0, 1, 5)
    

#     base10_label = QLabel('<strong>Base-10<strong/>')
#     base10_label.setStyleSheet('font-size: 18px; font-family: Inter;')
#     layout.addWidget(base10_label, 1, 0)

#     base10_container = QHBoxLayout()
#     base10_base = QLineEdit()
#     base10_times_10 = QLabel('x 10')
#     base10_times_10.setStyleSheet('padding: 15px 10px; font-size: 18px; font-family: Inter; ')
#     base10_base.setStyleSheet('padding: 15px 10px; font-size: 18px; font-family: Inter; border: 1px solid #B4B8C5; border-radius: 10px;')
#     base10_exp = QLineEdit()
#     base10_base.setFixedWidth(180)
#     base10_exp.setFixedWidth(100)
#     base10_exp.setAlignment(Qt.AlignmentFlag.AlignTop)
#     base10_exp.setStyleSheet('padding: 7.5px 5px; font-size: 15px; font-family: Inter; border: 1px solid #B4B8C5; border-radius: 5px;')
#     base10_container.addWidget(base10_base)
#     base10_container.addWidget(base10_times_10)
#     base10_container.addWidget(base10_exp, 0)
#     layout.addLayout(base10_container, 1, 1, 1, 2)

#     rounding_method_dropdown = QComboBox()
#     rounding_method_dropdown.addItems(['Round nearest-ties to even', 'Round up', 'Round down'])
#     rounding_method_dropdown.setStyleSheet('QComboBox::drop-down:button { border: none; border-radius: 5px; width: 50px; background-color: #B4B8C5; padding: 10px 0px 10px; image: url(\'src/assets/caret-down-solid.svg\') } QComboBox { padding: 15px 10px; font-size: 18px; font-family: Inter; border: 1px solid #B4B8C5; border-radius: 10px;  } QComboBox::drop-down { padding: 15px 10px; }')
#     rounding_method_label = QLabel('<strong>Rounding method</strong>')
#     rounding_method_label.setStyleSheet('font-size: 18px; font-family: Inter;')
#     layout.addWidget(rounding_method_label, 2, 0)
#     layout.addWidget(rounding_method_dropdown, 2, 1, 1, 2)

#     convert_button = QPushButton('Convert')
#     convert_button.setStyleSheet('QPushButton { padding: 18px 10px; font-size: 18px; font-family: Inter; background-color: #B4B8C5; border: 1px solid #E9EBF8; border-radius: 10px; color: #FEFFFE; }')
#     convert_button.setCursor(Qt.CursorShape.PointingHandCursor)
#     # convert_button.setFixedWidth(200)
#     layout.addWidget(convert_button, 6, 0, 1, 3)

#     output_label = QLabel('<strong>Decimal128 Representation</strong>')
#     output_label.setStyleSheet('font-size: 18px; font-family: Inter;')
#     output_binary = QPlainTextEdit()
#     output_binary.setStyleSheet(OUTPUT_STYLE)
#     output_binary.setFixedHeight(150)
#     output_hex = QPlainTextEdit()
#     output_hex.setFixedHeight(150)
#     output_hex.setStyleSheet(OUTPUT_STYLE)
#     layout.addWidget(output_label, 0, 3, 1, 3)
#     layout.addWidget(output_binary, 1, 3, 1, 3)
#     layout.addWidget(output_hex, 2, 3, 1, 3)

#     save_button = QPushButton('Save')
#     save_button.setStyleSheet('QPushButton { padding: 18px 10px; font-size: 18px; font-family: Inter; background-color: #FEFFFE; border: 1px solid #E9EBF8; border-radius: 10px; color: #B4B8C5; }')
#     save_button.setCursor(Qt.CursorShape.PointingHandCursor)
#     layout.addWidget(save_button, 6, 3, 1, 3)

#     convert_button.clicked.connect(lambda: convert(base10_base, base10_exp, output_binary, output_hex))
#     save_button.clicked.connect(lambda: save(base10_base, base10_exp, output_binary, output_hex))

#     window.setLayout(layout)

#     window.show()
#     app.exec()


main()
