from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CanvasWidget(Widget):
     
    def __init__(self, **kwargs):
 
        super(CanvasWidget, self).__init__(**kwargs)
 
        with self.canvas:
 
            Color(.1, 3.3, 3.3, .8)  
 
            self.rect = Rectangle(pos = self.center,
                                  size = (self.width / 2.,
                                        self.height / 2.))

            self.bind(pos = self.update_rect,
                      size = self.update_rect)
 
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
 

class CanvasApp(App):
    
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        button = Button(text = 'button',
                        size_hint = (0.3, 0.3),
                        pos_hint = {'center_x': 0.5, 'center_y': 0.2}
                        )
        
        layout.add_widget(CanvasWidget())
        layout.add_widget(button)

        return layout
 

CanvasApp().run()