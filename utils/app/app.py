from kivy.app import App
from .widget import CalculatorWidget


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()
