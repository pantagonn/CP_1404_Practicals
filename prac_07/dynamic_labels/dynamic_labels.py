"""
Dynamic Label App
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Constructor"""
        super().__init__(**kwargs)
        self.list_of_names = ["Boonyanuch", "Rachatorn", "Sreewong", "Apinya "]

    def build(self):
        """Build the Kivy App from the kv file """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from given list of names"""
        for name in self.list_of_names:
            label_name = Label(text=name)
            self.root.ids.main.add_widget(label_name)


DynamicLabelsApp().run()
