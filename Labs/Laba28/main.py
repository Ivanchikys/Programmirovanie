from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.properties import ListProperty, BooleanProperty

class ToDoItem(BoxLayout):
    def __init__(self, title, description, **kwargs):
        super(ToDoItem, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 50
        self.completed = BooleanProperty(False)

        self.checkbox = CheckBox(size_hint_x = 0.1)
        self.checkbox.bind(active = self.on_checkbox_active)
        self.add_widget(self.checkbox)
        
        data = FloatLayout()
        data.bind(on_touch_down = self.on_title_touch_down)   

        self.title_label = Label(text = title, 
                                 size_hint = (0.9, 1.0), 
                                 halign = "left", 
                                 pos_hint = {"x": 0, "center_y": 1}
                                 )  
        self.title_label.bind(size = self.title_label.setter('text_size'))   
        data.add_widget(self.title_label)

        self.description_label = Label(text = description, 
                                       size_hint = (0.9, 1.0), 
                                       halign = "left", 
                                       pos_hint = {"x": 0, "center_y": 0.6}
                                       )  
        self.description_label.bind(size = self.description_label.setter('text_size'))    
        data.add_widget(self.description_label)

        self.add_widget(data)

        delete_button = Button(text = "Удалить", 
                               size_hint_x = 0.15
                               )
        delete_button.bind(on_press = lambda _: app.remove_task(self))
        self.add_widget(delete_button)

    def on_title_touch_down(self, instance, touch):
        if self.title_label.collide_point(*touch.pos):
            self.checkbox.active = not self.checkbox.active

    def on_checkbox_active(self, instance, value):
        self.completed = value
        if value:
            self.title_label.color = (0.5, 0.5, 0.5, 1)
            self.description_label.color = (0.5, 0.5, 0.5, 1)
        else:
            self.title_label.color = (1, 1, 1, 1)
            self.description_label.color = (1, 1, 1, 1)

class ToDoListApp(App):
    tasks = ListProperty()

    def add_task(self, title, description):
        self.tasks.append({"title": title, "description": description})
        self.task_list.add_widget(ToDoItem(title, description))

    def build(self):
        root_layout = BoxLayout(orientation = 'vertical')

        header = BoxLayout(orientation = 'vertical',
                           size_hint_y = None, height = 150
                           )
        title_input = TextInput(hint_text = "Введите заголовок")
        description_input = TextInput(hint_text = "Введите описание")
        add_button = Button(text = "Добавить задачу")
        add_button.bind(on_press = lambda _: self.add_new_task(title_input, description_input))
        header.add_widget(title_input)
        header.add_widget(description_input)
        header.add_widget(add_button)

        self.task_list = GridLayout(cols = 1, 
                                    size_hint_y = 0.8, 
                                    padding = 10, 
                                    spacing = 10
                                    ) 
        root_layout.add_widget(header)
        root_layout.add_widget(self.task_list)

        for task in self.tasks:
            item = ToDoItem(task["title"], task["description"])
            self.task_list.add_widget(item)

        return root_layout

    def add_new_task(self, title_input, description_input):
        title = title_input.text
        description = description_input.text
        if title:
            self.add_task(title, description)
            title_input.text = ""
            description_input.text = ""

    def remove_task(self, item_to_remove):
        self.tasks.remove({"title": item_to_remove.children[1].children[1].text, 
                           "description": item_to_remove.children[1].children[0].text})
        self.task_list.remove_widget(item_to_remove)

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()