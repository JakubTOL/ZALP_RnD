from dotenv import load_dotenv
from kivy.app import App
from kivy.clock import Clock, mainthread
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout

from zalp.application.psu import PsuService

load_dotenv()


class PsuWidget(BoxLayout):
    voltage = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.psu_service = PsuService()
        Clock.schedule_interval(self.update_voltage, 0.5)

    def update_voltage(self, info):
        print(info)
        self.psu_service.get_voltage(callback=self.update_voltage_callback)

    @mainthread
    def update_voltage_callback(self, voltage):
        self.voltage = voltage


class MyApp(App):
    def build(self):
        return PsuWidget()


if __name__ == '__main__':
    MyApp().run()
