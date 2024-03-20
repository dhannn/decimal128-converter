from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QHBoxLayout, QComboBox, QPushButton, QPlainTextEdit
from PyQt6.QtCore import Qt

from controller import convert

def main():
    app = QApplication([])
    
    window = QWidget()
    window.setWindowTitle('Decimal128 floating point converter')
    window.setGeometry(100, 100, 1500, 800)

    layout = QGridLayout()

    base10_label = QLabel('Base-10')
    base10_label.setStyleSheet('font-size: 18px; font-family: Inter;')
    layout.addWidget(base10_label, 1, 0)

    base10_container = QHBoxLayout()
    base10_base = QLineEdit()
    base10_times_10 = QLabel('x 10')
    base10_times_10.setStyleSheet('padding: 15px 10px; font-size: 18px; font-family: Inter;')
    base10_base.setStyleSheet('padding: 15px 10px; font-size: 18px; font-family: Inter;')
    base10_exp = QLineEdit()
    base10_exp.setFixedWidth(100)
    base10_exp.setAlignment(Qt.AlignmentFlag.AlignTop)
    base10_exp.setStyleSheet('padding: 7.5px 5px; font-size: 15px; font-family: Inter;')
    base10_container.addWidget(base10_base)
    base10_container.addWidget(base10_times_10)
    base10_container.addWidget(base10_exp, 0)
    layout.addLayout(base10_container, 1, 1, 1, 2)

    rounding_method_dropdown = QComboBox()
    rounding_method_dropdown.addItems(['Round nearest-ties to even', 'Round up', 'Round down'])
    rounding_method_dropdown.setStyleSheet('padding: 15px 10px; font-size: 18px; font-family: Inter;')
    rounding_method_label = QLabel('Rounding method')
    rounding_method_label.setStyleSheet('font-size: 18px; font-family: Inter;')
    layout.addWidget(rounding_method_label, 2, 0)
    layout.addWidget(rounding_method_dropdown, 2, 1, 1, 2)

    convert_button = QPushButton('Convert')
    convert_button.setStyleSheet('padding: 15px 10px; font-size: 18px; font-family: Inter;')
    layout.addWidget(convert_button, 6, 0, 1, 3)

    output_label = QLabel('Decimal128 Representation')
    output_label.setStyleSheet('font-size: 18px; font-family: Inter;')
    output_binary = QPlainTextEdit()
    output_binary.setStyleSheet('padding: 15px 10px; font-size: 18px; font-family: Inter;')
    output_binary.setFixedHeight(100)
    output_hex = QPlainTextEdit()
    output_hex.setFixedHeight(100)
    output_hex.setStyleSheet('padding: 15px 10px; font-size: 18px; font-family: Inter;')
    layout.addWidget(output_label, 1, 3, 1, 3)
    layout.addWidget(output_binary, 2, 3, 1, 3)
    layout.addWidget(output_hex, 3, 3, 1, 3)

    save_button = QPushButton('Save')
    save_button.setStyleSheet('padding: 15px 10px; font-size: 18px; font-family: Inter;')
    layout.addWidget(save_button, 6, 3, 1, 3)

    convert_button.clicked.connect(lambda: convert(base10_base, base10_exp, output_binary, output_hex))

    window.setLayout(layout)

    window.show()
    app.exec()


main()
