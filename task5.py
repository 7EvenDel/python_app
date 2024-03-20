from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout 


class MyApp(App):

    def build(self):
        self.i = 0
        self.txt = Label(text="This is Text")
        btn = Button(text="This is Button")
        btn.on_press = self.set_txt
        layout = Boxlayout()
        layout.add_widget(self.txt)
        layout.add_widget(btn)
        return layout

    def set_txt(self):

        self.txt.text = str(self.i)
        self.i += 1

app = MyApp()
app.run()