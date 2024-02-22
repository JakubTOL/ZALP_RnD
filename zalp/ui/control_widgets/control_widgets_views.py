import os

from kivy.app import App
from kivy.clock import mainthread
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel

from zalp.ui.control_widgets.rx import CanTreeView, TrafficSignWidget, CameraStatusWidget, LineDetectionWidget
from zalp.ui.control_widgets.tx import OtherEcusWidget, PsuControlWidget, CarSignalsWidget, DiagnosticWidget, VideoPlayerWidget

__filename = os.path.splitext(os.path.basename(__file__))[0] + '.kv'
__directory = os.path.dirname(__file__)
Builder.load_file(os.path.join(__directory, __filename))


class ControlWidgetTabbedPanel(TabbedPanel):
    pass


class RxControlWidgetTabbedPanel(ControlWidgetTabbedPanel):
    rx_tabbed_panel_item = ObjectProperty(None)
    rx_tabbed_panel_content = ObjectProperty(None)
    can_analyzer_tabbed_panel_item = ObjectProperty(None)
    can_traffic_analyzer_widget_content = ObjectProperty(None)

    def add_dummy(self):
        self.switch_to_default_tab()

        scroll_view = ControlWidgetsScrollView()
        scroll_view.layout.add_widget(CameraStatusWidget())
        scroll_view.layout.add_widget(TrafficSignWidget())
        scroll_view.layout.add_widget(LineDetectionWidget())
        self.rx_tabbed_panel_content.add_widget(scroll_view)

        can_scroll_view = ControlWidgetsScrollView()
        can_treeview = CanTreeView()
        can_scroll_view.layout.add_widget(can_treeview)
        self.can_traffic_analyzer_widget_content.add_widget(can_scroll_view)

    @mainthread
    def switch_to_default_tab(self):
        self.switch_to(self.rx_tabbed_panel_item)


class TxControlWidgetTabbedPanel(ControlWidgetTabbedPanel):
    tx_tabbed_panel_item = ObjectProperty(None)
    tx_tabbed_panel_content = ObjectProperty(None)
    diagnostic_tabbed_panel_item = ObjectProperty(None)
    diagnostic_tabbed_panel_content = ObjectProperty(None)
    video_tabbed_panel_item = ObjectProperty(None)
    video_tabbed_panel_content = ObjectProperty(None)

    def add_dummy(self):
        self.switch_to_default_tab()

        scroll_view = ControlWidgetsScrollView()
        scroll_view.layout.add_widget(PsuControlWidget())
        scroll_view.layout.add_widget(CarSignalsWidget())
        scroll_view.layout.add_widget(OtherEcusWidget())
        self.tx_tabbed_panel_content.add_widget(scroll_view)

        # diagnostic_scroll_view = ControlWidgetsScrollView()
        # diagnostic_scroll_view.layout.add_widget(DiagnosticWidget())
        # self.diagnostic_tabbed_panel_content.add_widget(diagnostic_scroll_view)
        diagnostic_widget = DiagnosticWidget()
        diagnostic_widget.populate()
        self.diagnostic_tabbed_panel_content.add_widget(diagnostic_widget)

        # video_scroll.layout.add_widget(VideoControlWidget())
        # self.video_tabbed_panel_content.add_widget(video_scroll)
        # video_control = VideoControlWidget(pos_hint={'center_x': .5, 'top': .975})
        # self.video_tabbed_panel_content.add_widget(video_control)
        video_list = VideoPlayerWidget()
        video_list.populate()
        self.video_tabbed_panel_content.add_widget(video_list)

    @mainthread
    def switch_to_default_tab(self):
        self.switch_to(self.tx_tabbed_panel_item)

class ControlWidgetsScrollView(ScrollView):
    layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        # print(self.__dir__())
        # layout = self.layout
        # layout = self.ids['layout']
        # layout.bind(minimum_height=layout.setter('height'))

        # layout.add_widget(Button(size_hint_y=None, height=40))
        # layout.add_widget(Button(size_hint_y=None))
        # layout.add_widget(Button(size_hint_y=None))
        # layout.add_widget(Button())
        # layout.add_widget(Button())
        # layout.add_widget(Button())
        # layout.add_widget(Button())

        # layout.add_widget(DetectedSignWidget())
        # layout.add_widget(DetectedSignWidget())
        # layout.add_widget(DetectedSignWidget())
        # layout.add_widget(Widget())

        # for i in range(20):
        #     btn = Button(text=str(i), size_hint_y=None, height=40)
        #     layout.add_widget(btn)
        # self.add_widget(layout)

    # def add_dummy(self):
    #     self.layout.add_widget(PsuControlWidget())

class MyApp(App):
    def __init__(self):
        super().__init__()

    def build(self):
        # root = SignalScrollView(size=(Window.width - 300, Window.height - 100))
        root = ControlWidgetsScrollView()
        # root = DetectedSignWidget(size=(Window.width, Window.height))
        # print(root.ids['layout'].size)
        # print(root.size)
        # print(root.children)
        # print(root.children[0].size)

        a = GridLayout(rows=3)
        a.add_widget(Button())
        a.add_widget(Button())
        a.add_widget(root)
        return a


if __name__ == '__main__':
    # load_dotenv()
    MyApp().run()
