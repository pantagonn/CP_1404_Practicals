from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class BoxLayoutDemo(App):

    output_label = StringProperty

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_clear(self):
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""

    def handle_greet(self):
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text


BoxLayoutDemo().run()
