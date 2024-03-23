from model import Model
from view import View
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QHBoxLayout, QComboBox, QPushButton, QMessageBox, QPlainTextEdit

from src.utils.dfp import RoundingMethod

class Controller:

    view: View
    model: Model

    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

        self.view.bind_controller(self)

    def handle_convert(self):
        if self.view.is_input_valid():
            self.convert()
        else: 
            message = QMessageBox()
            message.setWindowTitle('Invalid input!')
            message.setText('Kindly put in the necessary input :>')
            message.exec()

    def handle_save(self):
        self.save()

    def convert(self):

        try:
            rounding_method, base, exp = self.view.get_inputs()

            _base = float(base)
            _exp = float(exp)
            original_value = _base ** _exp
            print(original_value)
            
        except ValueError:
            rounding_method, base, exp = rounding_method, float('NaN'), float('NaN')

        self.model.set_vars(base, exp, rounding_method)
        decimal128 = self.model.convert_to_decimal()
        
        dfp_bin = str(decimal128)
        dfp_hex = decimal128.to_hex()

        self.view.set_outputs(dfp_bin, dfp_hex)

    
    def save(self):

        self.model.save_to_text_file()
    
        message = QMessageBox()
        message.setWindowTitle('Saved your output! :)')
        message.setText(f'We saved your output to the text file, Decimal128_{ self.model.significand }e{ self.model.exponent }.txt')
        message.exec()
        

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
