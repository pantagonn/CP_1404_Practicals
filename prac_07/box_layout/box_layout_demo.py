from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class BoxLayoutDemo(App):
    """Box layout demo"""

    output_label = StringProperty

    def build(self):
        """Build function"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_clear(self):
        """Handle name clearing & input"""
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""

    def handle_greet(self):
        """Handle greeting with entered name"""
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text


BoxLayoutDemo().run()
