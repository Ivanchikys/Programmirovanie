from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App

class GridLayoutApp(App):
    def build(self):
        layout = GridLayout(cols = 4, rows = 2) 


        for num in range(8):
            button = Button(text = str(num))
            layout.add_widget(button)
      
        
        return layout

if __name__ == '__main__':
    GridLayoutApp().run()
