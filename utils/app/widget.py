from kivy.uix.widget import Widget


class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text = "0"

    def button_value(self, number):
        if (prev_number := self.ids.input_box.text) == "0":
            self.ids.input_box.text = ""
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    def sings(self, sing):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f"{prev_number}{sing}"

    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

    def results(self):
        prev_number = self.ids.input_box.text
        arr = list(prev_number)
        for index, item in enumerate(arr):
            if arr[index] == "x":
                arr[index] = "*"
            elif arr[index] == "÷":
                arr[index] = "/"
        try:
            result = eval("".join(arr))
        except:
            self.ids.input_box.text = "wrong equation"
        else:
            self.ids.input_box.text = f"{result}"

    def positive_negative(self):
        if "-" in (prev_number := self.ids.input_box.text):
            self.ids.input_box.text = f'{prev_number.replace("-", "")}'
        else:
            self.ids.input_box.text = f"-{prev_number}"

    def dot(self):
        if "." in (prev_number := self.ids.input_box.text):
            pass
        else:
            prev_number = f"{prev_number}."
            self.ids.input_box.text
