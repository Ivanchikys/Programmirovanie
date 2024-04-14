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
        self.memory = []
        self.memory_operand = ''

    def on_button_press(self, instance):
        if len(self.text_null.text) > 19:
            return False

        if self.equals_pressed:                    #ГРАНИЦА ВВОДА ЧИСЕЛ И НАЖАТИЕ
            self.text_null.text = instance.text
            self.equals_pressed = False
            return False
        
        self.text_null.text += instance.text

    def on_operands_press (self, operand):
        self.memory_operand = operand
        if self.operand and not self.memory:
            self.memory.append(self.memory, self.memory_operand)

    def on_plus_press(self, instance):
        self.on_operands_press('+')
    def on_minus_press(self, instance):
        self.on_operands_press('-')
    def on_devide_press(self, instance):
        self.on_operands_press('/')                   #ФУНКЦИЯ ОПЕРАНД
    def on_multiply_press(self, instance):
        self.on_operands_press('*')

    def on_clear_press(self, instance):
        self.text_null.text = ''

    def subtext(self,operand):
        self.operand = operand


    def on_equal_press(self, instance):
        self.equals_pressed = True





    def build(self):
        app_layout = BoxLayout (orientation = 'vertical')

        Display_layout = FloatLayout(size_hint_y = None,
                                     height =  150
                                    )




        self.text_null = Label(text = '', 
                               size_hint = (0.75, 1), 
                               pos_hint = ({"right": 0.85 , "top": 0.65}),
                               font_size = '50px', 
                               halign = "right", 
                               valign = "top"
                               )                                                          #LABEL
        self.subtext_null = Label(text = '',
                                  size_hint = (0.75, 1), 
                                  pos_hint = ({"right": 0.85 , "top": 0.65}),
                                  font_size = '50px', 
                                  halign = "right", 
                                  valign = "top"
                                  )
        
        self.text_null.bind(size = self.text_null.setter('text_size'))

        Display_layout.add_widget(self.subtext_null)
        Display_layout.add_widget(self.text_null)
        Display_layout.add_widget(CanvasWidget())




        Calculater_layout = BoxLayout(orientation = 'vertical')

        Numpad_numbers_layout = GridLayout(cols = 3, rows = 3) 
        BUTTON_SIZE = (0.2, 0.2)
        numbers_of_numpad = [7, 8, 9, 4, 5, 6, 3, 2, 1]
        for num in numbers_of_numpad:
            button_1 = Button(text = str(num),
                              size_hint = (BUTTON_SIZE),
                              )
            Numpad_numbers_layout.add_widget(button_1)
            button_1.bind(on_press = self.on_button_press)
 
        Numpad_operand_layout = GridLayout(cols = 4, rows = 1,
                                           size_hint_y = 0.25
                                           ) 
        operands_of_numpad = [('/', self.on_devide_press),
                              ('-', self.on_minus_press),
                              ('+', self.on_plus_press),
                              ('*', self.on_multiply_press)
                              ]
        for operand in operands_of_numpad:
            button_2 = Button(text = str(operand[0]),
                              size_hint = (BUTTON_SIZE),
                              )
            Numpad_operand_layout.add_widget(button_2)
            button_2.bind(on_press = self.on_button_press)
            

        Numpad_adit_layout = GridLayout(cols = 1, rows = 3,
                                        size_hint_x = 0.335) 
        adits_of_numpad = [('C', self.on_clear_press),
                           ('=', self.on_equal_press),
                           ('0', self.on_button_press)
                          ]
        for adit in adits_of_numpad:
            button_3 = Button(text = str(adit[0]),
                              size_hint = (BUTTON_SIZE),
                              )
            Numpad_adit_layout.add_widget(button_3)
            button_3.bind(on_press = self.on_button_press)

        FullNumpads = BoxLayout()
        FullNumpads.add_widget(Numpad_numbers_layout)
        FullNumpads.add_widget(Numpad_adit_layout)

        Calculater_layout.add_widget(Numpad_operand_layout)
        Calculater_layout.add_widget(FullNumpads)

        app_layout.add_widget(Display_layout)
        app_layout.add_widget(Calculater_layout)


        return app_layout

if __name__ == '__main__':
    GridLayoutApp().run()
