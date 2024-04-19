import string

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label



class GridLayoutApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_result_showed = False

    def calculate(self, text_null):
        try:
            self.text_null.text = str(eval(self.text_null.text))
        except Exception:
            self.text_null.text = "error"
        
    def button_works(self, text_null: Button):
        
        if len(self.text_null.text) > 25:
            return False
        
        if text_null.text not in string.digits and self.text_null.text.endswith(text_null.text):
            return

        if self.is_result_showed and text_null.text in string.digits:
            self.text_null.text = ''

        if text_null.text == '=':
            self.is_result_showed = True
            self.calculate(text_null)
        elif text_null.text == 'C':
            self.text_null.text = ''
        else:
            self.is_result_showed = False
            self.text_null.text += text_null.text

    def build(self):
        App = BoxLayout(orientation = 'vertical')

        Numpad_layout = GridLayout(cols = 4, rows = 4)
        numpad_ = [['/', '-', '+', '*'],
                   ['7', '8', '9' , 'C'],
                   ['4', '5', '6', '='],
                   ['3', '2' , '1', '0']
                   ]
        for blocks in numpad_:
            for symbol in blocks:
                button = Button(text = f'{symbol}',
                                )
                button.bind(on_press = self.button_works)
                Numpad_layout.add_widget(button)

        self.text_null = Label(size_hint = (1, 0.2),
                             height = 30,
                             font_size = 45,
                             on_text_validate = self.calculate
                            )

        App.add_widget(self.text_null)
        App.add_widget(Numpad_layout)

        return  App


if __name__ == '__main__':
    GridLayoutApp().run()