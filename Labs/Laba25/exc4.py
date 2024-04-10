from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

Builder.load_string('''
<ListViewer>: 
    viewclass: 'Button'
    orientation: "vertical"
                    
    RecycleBoxLayout: 
        color:(0, 0.7, 0.4, 0.8) 
        default_size: None, dp(56) 
        default_size_hint: 0.4, None 
        size_hint_y: None
        height: self.minimum_height 
        orientation: 'vertical'
''')

class ListViewer(RecycleView): 
    def __init__(self, **kwargs): 
        super(ListViewer, self).__init__(**kwargs) 
        self.data = [{'text': 'Элемент '+str(x)} for x in range(1,21)] 
  
class MainApp(App): 
    def build(self): 
        return ListViewer() 
  
MainApp().run() 