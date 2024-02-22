import os

from dotenv import load_dotenv
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

# DPI fix on Windows
if os.name == 'nt':
    from ctypes import windll, c_int64

    # DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2
    windll.user32.SetProcessDpiAwarenessContext(c_int64(-4))


class SignalsWidget(BoxLayout):
    title = ObjectProperty(None)
    def __init__(self, title, **kwargs):
        super().__init__(**kwargs)
        # self.ids['title'].text = title
        self.title.text = title


class DetectedSignWidget(SignalsWidget):
    def __init__(self, **kwargs):
        super().__init__(title='Detected sign', **kwargs)


class DetectedLinesWidget(SignalsWidget):
    def __init__(self, **kwargs):
        super().__init__(title='Detected lanes', **kwargs)


class SignalScrollView(ScrollView):
    layout = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout = self.layout
        # layout = self.ids['layout']
        layout.bind(minimum_height=layout.setter('height'))

        # layout.add_widget(Button(size_hint_y=None, height=40))
        # layout.add_widget(Button(size_hint_y=None))
        # layout.add_widget(Button(size_hint_y=None))
        # layout.add_widget(Button())
        # layout.add_widget(Button())
        # layout.add_widget(Button())
        # layout.add_widget(Button())

        layout.add_widget(DetectedSignWidget())
        layout.add_widget(DetectedLinesWidget())
        layout.add_widget(DetectedSignWidget())
        # layout.add_widget(DetectedSignWidget())
        # layout.add_widget(DetectedSignWidget())
        # layout.add_widget(DetectedSignWidget())
        # layout.add_widget(Widget())

        # for i in range(20):
        #     btn = Button(text=str(i), size_hint_y=None, height=40)
        #     layout.add_widget(btn)
        # self.add_widget(layout)


class MyApp(App):
    def __init__(self):
        super().__init__()

    def build(self):
        # root = SignalScrollView(size=(Window.width - 300, Window.height - 100))
        root = SignalScrollView()
        # root = DetectedSignWidget(size=(Window.width, Window.height))
        # print(root.ids['layout'].size)
        print(root.size)
        print(root.children)
        print(root.children[0].size)

        a = GridLayout(rows=3)
        a.add_widget(Button())
        a.add_widget(Button())
        a.add_widget(root)
        return a
        return root


if __name__ == '__main__':
    load_dotenv()
    MyApp().run()
