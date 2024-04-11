from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from random import random

class MainApp(App):
    def move_button(self, instance):
        instance.pos_hint = {"x": random(), "y": random()}

    def build(self):
        layout = FloatLayout()

        BUTTON_SIZE = (0.2, 0.1)

        button = Button(text = "Тыкни на меня",
                        size_hint = BUTTON_SIZE,
                        pos_hint = {"center_x": 0.5, "center_y": 0.5})
        button.bind(on_press = self.move_button)
        
        layout.add_widget(button)
        
        return layout
    
if __name__ == "__main__":
    MainApp().run()