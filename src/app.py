from PyQt6.QtWidgets import QApplication

from app.model import Model
from app.controller import Controller
from app.view import View

OUTPUT_STYLE = 'padding: 15px 10px; font-size: 18px; font-family: Inter; background-color: #E9EBF8; border: 1px solid #B4B8C5; border-radius: 10px'

def main():
    app = QApplication([])
    model = Model()
    view = View()
    controller = Controller(model, view)
    
    view.bind_controller(controller)

    app.exec()
    
main()
