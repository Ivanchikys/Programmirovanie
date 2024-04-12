from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.button import Button
from kivy.app import App


class CanvasWidget(Widget):
     
    def __init__(self, **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(0.419, 419, 163, .6)  
 
            self.rect = Rectangle(pos = self.center,
                                  size = (self.width / 2.,
                                        self.height / 2.))

            self.bind(pos = self.update_rect,
                      size = self.update_rect)
 
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.pos_hint = {'x': 0.12, 'y': 0.15}
        self.size_hint = (0.75, 0.75)


class GridLayoutApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.equals_pressed = False

         
    def on_button_press(self, instance):
        if len(self.text_null.text) > 20:
            return False

        if self.equals_pressed:
            self.text_null.text = instance.text
            self.equals_pressed = False
            return False
        
        self.text_null.text += instance.text

    # def on_clear_press(self, instance):
    #     if self.clear_pressed :
    #         self.memory.clear()

    def on_equal_press(self, instance):
        self.equals_pressed = True

        if self.text_null.text != '':
            self.memory.append(int(self.text_null.text))

        self.text_null.text = str(sum(self.memory))
        self.memory.clear()

    def on_plus_press(self, instance):
        self.memory.append(int(self.text_null.text))
        self.text_null.text = ''

    def build(self):
        self.memory = []

        Calculater_layout = BoxLayout(orientation = 'vertical')

        Display_layout = FloatLayout(size_hint_y = None,
                                     height =  150
                                    )

        self.text_null = Label(text = '', 
                               size_hint = (0.75, 1), 
                               pos_hint = ({"right": 0.85 , "top": 0.65}),
                               font_size = '50px', 
                               halign = "right", 
                               valign = "top"
                               )
        self.text_null.bind(size = self.text_null.setter('text_size'))

        Display_layout.add_widget(self.text_null)
        Display_layout.add_widget(CanvasWidget())

        self.button_Clear = Button (text = 'C',
                              size_hint = (0.1, 0.1),
                              pos_hint = ({"right": 0.11 , "top": 0.65}), 
                               halign = "left", 
                               valign = "top"
                              )
        self.button_Clear.bind(on_press = self.on_clear_press)
        Display_layout.add_widget(self.button_Clear)

        Numpad_layout = GridLayout(cols = 3, rows = 4) 
        BUTTON_SIZE = (0.2, 0.2)


        for num in range(10):
            button = Button(text = str(num),
                            size_hint = (BUTTON_SIZE)
                            )
            Numpad_layout.add_widget(button)
            button.bind(on_press = self.on_button_press)
 
        button_Plus = Button (text = '+',
                              size_hint = (BUTTON_SIZE),
                              )
        button_Plus.bind(on_press = self.on_plus_press)
        Numpad_layout.add_widget(button_Plus)


        button_Equals = Button (text = '=',
                                size_hint = (BUTTON_SIZE)
                                )
        button_Equals.bind(on_press = self.on_equal_press)
        Numpad_layout.add_widget(button_Equals)


        Calculater_layout.add_widget(Display_layout)
        Calculater_layout.add_widget(Numpad_layout)
       


        return Calculater_layout

if __name__ == '__main__':
    GridLayoutApp().run()
