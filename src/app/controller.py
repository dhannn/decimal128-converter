from app.model import Model
from app.view import View
from PyQt6.QtWidgets import QMessageBox

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