from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QHBoxLayout, QComboBox, QPushButton, QPlainTextEdit
from PyQt6.QtCore import Qt

from src.app.model import Model
from src.app.controller import Controller
from src.app.view import View

OUTPUT_STYLE = 'padding: 15px 10px; font-size: 18px; font-family: Inter; background-color: #E9EBF8; border: 1px solid #B4B8C5; border-radius: 10px'

def main():
    app = QApplication([])
    model = Model()
    view = View()
    controller = Controller(model, view)
    
    view.bind_controller(controller)

    app.exec()
    
main()
