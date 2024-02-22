import kivy

from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty, BoundedNumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label

class Gauge(Widget):
    # load dashboard gauge image
    file_gauge = StringProperty("C:/zf-adas-learning-platform/resources/dashgauge.png")
    # load needle image
    file_needle = StringProperty("C:/zf-adas-learning-platform/resources/needle3.png")
    unit = NumericProperty(1.8)
    # value range for speedmeter widget
    value = BoundedNumericProperty(0, min=0, max=100, errorvalue=0)
    size_gauge = BoundedNumericProperty(128, min=128, max=256, errorvalue=128)
    size_text = NumericProperty(10)

    def __init__(self, **kwargs):
        super(Gauge, self).__init__(**kwargs)

        self.gauge = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False
        )

        img_gauge = Image(source=self.file_gauge, size=(self.size_gauge,
                                                         self.size_gauge))

        self.needle = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False
        )

        img_needle = Image(source=self.file_needle, size=(self.size_gauge,
                                                           self.size_gauge))

        # display digitalized speed value as a text
        self.DigitSpeed = Label(font_size=self.size_text, markup=True)

        self.gauge.add_widget(img_gauge)
        self.needle.add_widget(img_needle)

        self.add_widget(self.gauge)
        self.add_widget(self.needle)
        # add label widget for digitalized speed
        self.add_widget(self.DigitSpeed)

        self.bind(pos=self.update)
        self.bind(size=self.update)
        self.bind(value=self.turn)

    def update(self, *args):
        self.gauge.pos = self.pos
        self.needle.pos = (self.x, self.y)
        self.needle.center = self.gauge.center
        # update digitalized speed text position
        self.DigitSpeed.center_x = self.gauge.center_x
        self.DigitSpeed.center_y = self.gauge.center_y + (self.size_gauge / 4)

    def turn(self, *args):
        """
        Turn needle, 1 degree = 1 unit, 0 degree point start on 50 value.
        """
        self.needle.center_x = self.gauge.center_x
        self.needle.center_y = self.gauge.center_y
        self.needle.rotation = (50 * self.unit) - (self.value * self.unit)
        # update digitalized speed value
        self.DigitSpeed.text = "[b]{0:.0f}[/b]".format(self.value) + "km/h"


class GaugeApp(App):
    def build(self):
        from kivy.uix.slider import Slider
        from kivy.uix.textinput import TextInput

        # get data from TextInput after "enter"
        def DataUpdate(self):
            print(self.text)
            gauge.value = int(self.text)

        def DataUpdate1(*ars):
            gauge.value = s1.value
            print(s1.value)

        box = BoxLayout(orientation='horizontal', spacing=10, padding=10)
        gauge = Gauge(value=50, size_gauge=256, size_text=19)

        box.add_widget(gauge)

        #s1 = Slider(min=0, max=100, value=50)
        #s1.bind(value=DataUpdate)
        s1 = TextInput(multiline=False,
                       hint_text="Put speed value and press enter")
        s1.bind(on_text_validate=DataUpdate)
        box.add_widget(s1)

        return box


if __name__ == '__main__':
    GaugeApp().run()