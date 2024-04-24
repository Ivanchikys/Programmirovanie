from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.properties import ListProperty, BooleanProperty
from kivy.lang import Builder

class ToDoItem(BoxLayout):
    def __init__(self, text, **kwargs):
        super(ToDoItem, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 50
        self.completed = BooleanProperty(False)

        self.checkbox = CheckBox(size_hint_x = 0.1)
        self.checkbox.bind(active = self.on_checkbox_active)
        self.add_widget(self.checkbox)
        
        data = FloatLayout()
        data.bind(on_touch_down = self.on_text_touch_down)   

        self.text_label = Label(text = text,
                                 size_hint = (0.9, 1.0), 
                                 halign = "left", 
                                 pos_hint = {"x": 0.02, "center_y": 0.8}
                                 )  
        self.text_label.bind(size = self.text_label.setter('text_size'))   
        data.add_widget(self.text_label)

        self.add_widget(data)

        delete_button = Button(text = "Удалить", size_hint_x = 0.15)
        delete_button.bind(on_press = lambda _: app.remove_task(self))
        self.add_widget(delete_button)

    def on_text_touch_down(self, instance, touch):
        if self.text_label.collide_point(*touch.pos):
            self.checkbox.active = not self.checkbox.active

    def on_checkbox_active(self, instance, value):
        self.completed = value
        if value:
            self.text_label.color = (0.1, 0.1, 0.5, 1)
        else:
            self.text_label.color = (1, 1, 1, 1)

class ToDoListApp(App):
    tasks = ListProperty()

    def add_task(self, text):
        self.tasks.append({"text": text})
        self.root.ids.task_list.add_widget(ToDoItem(text = text))

    def add_new_task(self, text_input):
        text = text_input.text
        if text:
            self.add_task(text)
            text_input.text = ""
    

    def remove_task(self, item_to_remove):
        self.tasks.remove({"text": item_to_remove.children[1].children[0].text})
        self.root.ids.task_list.remove_widget(item_to_remove)
        
    def build(self):
        return Builder.load_file("todolist.kv")

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()