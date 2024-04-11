from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        layout = FloatLayout()
        
        BUTTON_SIZE = (0.2, 0.1)
        
        button1 = Button(text = "Кнопка 1",
                         size_hint = BUTTON_SIZE, 
                         pos_hint = {"center_x": 0.5, "y": 0.6}
                         )
        button2 = Button(text = "Кнопка 2", 
                         size_hint = BUTTON_SIZE, 
                         pos_hint = {"x": 0.3, "y": 0.5}
                         )
        button3 = Button(text = "Кнопка 3", 
                         size_hint = BUTTON_SIZE, 
                         pos_hint = {"x": 0.5, "y": 0.5}
                         )
        
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        
        return layout

if __name__ == "__main__":
    MainApp().run()