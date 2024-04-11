from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Builder.load_string('''
<ListViewer>: 
    viewclass: 'Button'
    orientation: "vertical"
                    
    RecycleBoxLayout: 
        color:(0, 0.7, 0.4, 0.8) 
        default_size: None, dp(56) 
        default_size_hint: 0.4, None 
        size_hint_y: None
        pos
        height: self.minimum_height 
        orientation: 'vertical'
''')

class ListViewer(RecycleView): 
    def __init__(self, **kwargs): 
        super(ListViewer, self).__init__(**kwargs) 
        self.data = [{'text': 'Элемент ' + str(x)} for x in range(1,21)] 
  
class MainApp(App): 
    def build(self): 
        layout = BoxLayout(orientation = 'vertical', spacing = 35)
        button = Button(text = 'button',
                        size_hint = (0.3, 0.1),
                        pos_hint = {'center_x': 0.5, 'center_y': 0.2}
                        ) 
        
        layout.add_widget(ListViewer())
        layout.add_widget(button)

        return layout 
  
MainApp().run() 