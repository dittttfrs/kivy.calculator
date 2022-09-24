from utils import CalculatorApp
from kivy.core.window import Window
from kivy.lang.builder import Builder


if __name__ == "__main__":
    Builder.load_file("./utils/kv/calculator.kv")
    Window.size = (350, 550)
    CalculatorApp().run()
