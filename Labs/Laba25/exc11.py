from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        layout = FloatLayout()
        BUTTON_SIZE = (0.2, 0.1)
        
        button1 = Button(text = "Кнопка 1", 
                         size_hint = BUTTON_SIZE, 
                         pos_hint = {"x": 0, "top": 1})
        button2 = Button(text = "Кнопка 2", 
                         size_hint = BUTTON_SIZE, 
                         pos_hint = {"x": 0.2, "top": 1})
        
        layout.add_widget(button1)
        layout.add_widget(button2)
        
        return layout

if __name__ == "__main__":
    MainApp().run()