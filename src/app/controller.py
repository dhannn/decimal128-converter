from model import convert_to_decimal
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QHBoxLayout, QComboBox, QPushButton, QMessageBox, QPlainTextEdit

from src.utils.dfp import RoundingMethod

def verify_input():
    pass

def flush_input():
    pass

def convert(base_field: QLineEdit, exp_field: QLineEdit, 
            bin_field: QPlainTextEdit, hex_field: QPlainTextEdit):

    try:
        base = base_field.text()
        exp = exp_field.text()

        _base = float(base)
        _exp = float(exp)
        original_value = _base ** _exp
        
    except ValueError:
        original_value = float('NaN')
        
    decimal128 = convert_to_decimal(original_value, RoundingMethod.ROUND_TNE)

    bin_field.setPlainText(str(decimal128))
    hex_field.setPlainText(decimal128.to_hex())

def save(base_field: QLineEdit, exp_field: QLineEdit, 
         output_binary: QPlainTextEdit, output_hex: QPlainTextEdit):
    base = base_field.text()
    exp = exp_field.text()
    bin_ = output_binary.toPlainText()
    hex_ = output_hex.toPlainText()

    with open(f'Decimal128_{ base }e{exp}.txt', 'w') as file:
        file.write(f'Base-10:\t\t{base}e{exp}\nDecimal128:\t\t{bin_} (binary)\n\t\t\t\t{hex_} (hex)')
    
    message = QMessageBox()
    message.setWindowTitle('Saved your output! :)')
    message.setText(f'We saved your output to the text file, Decimal128_{ base }e{exp}.txt')
    message.exec()
