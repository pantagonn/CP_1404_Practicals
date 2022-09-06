"""
Distance Converter App
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class DistanceConverterApp(App):
    """Distance Converter Application from miles to kilometers"""
    km_output = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Miles to Km"
        Window.size = (400, 300)
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def check_value(self):
        """Perform error checking on user's input and return zero if it is invalid"""
        if self.root.ids.m_input.text == '':
            return 0.0
        else:
            try:
                value = float(self.root.ids.m_input.text)
                return value
            except ValueError:
                return 0.0

    def handle_increment(self, integer):
        """Handle the incremental change of user's input"""
        user_input = self.check_value()
        self.root.ids.m_input.text = str(user_input + integer)
        self.handle_calculate()

    def handle_calculate(self):
        """Handle the calculation of distance conversion"""
        m_value = self.check_value()
        km_value = m_value * MILES_TO_KM
        self.root.ids.km_output.text = str(km_value)


DistanceConverterApp().run()
