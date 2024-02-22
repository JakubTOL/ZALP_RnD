from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


# Display Pixles

class MainApp(MDApp):
    def build(self):
        # Define Screen
        screen = Screen()
        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.9, 0.6),
            check=True,
            column_data=[
                ("MsgID", dp(30)),
                ("CAN channel", dp(30)),
                ("Data", dp(30)),
                ("Action", dp(30))
            ],
            row_data=[
                ("1", "0", "0x11, 0x22, 0x33", "test frame"),
                ("2", "1", "0xFF, 0x12, 0x5C", "another test frame"),

            ]

        )

        # Bind the table
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # return Builder.load_file('table.kv')
        # Add table widget to screen
        screen.add_widget(table)
        return screen

    # Function for check presses
    def checked(self, instance_table, current_row):
        print(instance_table, current_row)

    # Function for row presses
    def row_checked(self, instance_table, instance_row):
        print(instance_table, instance_row)


MainApp().run()