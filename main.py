from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

Window.size = (300, 600)
Window.clearcolor = (1, 1, 1)

class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line1 = BoxLayout(pos_hint = {"y" : 0})
        btn_0 = Button(text = "0", size_hint = (1, 0.1))

        line2 = BoxLayout(pos_hint = {"y" : 0.1})
        btn_1 = Button(text = "1", size_hint = (1, 0.1))
        btn_2 = Button(text = "2", size_hint = (1, 0.1))
        btn_3 = Button(text = "3", size_hint = (1, 0.1))

        line3 = BoxLayout(pos_hint = {"y" : 0.2})
        btn_4 = Button(text = "4", size_hint = (1, 0.1))
        btn_5 = Button(text = "5", size_hint = (1, 0.1))
        btn_6 = Button(text = "6", size_hint = (1, 0.1))

        line4 = BoxLayout(pos_hint = {"y" : 0.3})
        btn_7 = Button(text = "7", size_hint = (1, 0.1))
        btn_8 = Button(text = "8", size_hint = (1, 0.1))
        btn_9 = Button(text = "9", size_hint = (1, 0.1))

        line5 = BoxLayout(pos_hint = {"y" : 0.41})
        btn_clear = Button(text = "C", size_hint = (1, 0.1), font_size = 30)
        btn_plus = Button(text = "+", size_hint = (1, 0.1), font_size = 30)
        btn_minus = Button(text = "-", size_hint = (1, 0.1), font_size = 30)

        line6 = BoxLayout(pos_hint = {"y" : 0.51})
        btn_result = Button(text = "=", size_hint = (1, 0.1), font_size = 30)
        btn_mnozh = Button(text = "*", size_hint = (1, 0.1), font_size = 30)
        btn_dil = Button(text = "/", size_hint = (1, 0.1), font_size = 30)

        line7 = BoxLayout()
        self.label_result = Label(text="", color = "black", font_size = 30, pos_hint = {"y" : 0.2})

        line1.add_widget(btn_0)
        line2.add_widget(btn_1)
        line2.add_widget(btn_2)
        line2.add_widget(btn_3)
        line3.add_widget(btn_4)
        line3.add_widget(btn_5)
        line3.add_widget(btn_6)
        line4.add_widget(btn_7)
        line4.add_widget(btn_8)
        line4.add_widget(btn_9)
        line5.add_widget(btn_clear)
        line5.add_widget(btn_plus)
        line5.add_widget(btn_minus)
        line6.add_widget(btn_result)
        line6.add_widget(btn_mnozh)
        line6.add_widget(btn_dil)
        line7.add_widget(self.label_result)

        btn_0.bind(on_press= lambda x: self.add_number("0"))  
        btn_1.bind(on_press= lambda x: self.add_number("1"))  
        btn_2.bind(on_press= lambda x: self.add_number("2"))  
        btn_3.bind(on_press= lambda x: self.add_number("3"))  
        btn_4.bind(on_press= lambda x: self.add_number("4"))  
        btn_5.bind(on_press= lambda x: self.add_number("5"))  
        btn_6.bind(on_press= lambda x: self.add_number("6"))  
        btn_7.bind(on_press= lambda x: self.add_number("7"))  
        btn_8.bind(on_press= lambda x: self.add_number("8"))  
        btn_9.bind(on_press= lambda x: self.add_number("9"))  

        btn_clear.bind(on_press= lambda x: self.clear_label())  
        btn_plus.bind(on_press= lambda x: self.add_number("+"))  
        btn_minus.bind(on_press= lambda x: self.add_number("-"))  
        btn_result.bind(on_press= lambda x: self.print_result())  
        btn_mnozh.bind(on_press= lambda x: self.add_number("*"))  
        btn_dil.bind(on_press= lambda x: self.add_number("/"))  

        self.add_widget(line1)
        self.add_widget(line2)
        self.add_widget(line3)
        self.add_widget(line4)
        self.add_widget(line5)
        self.add_widget(line6)
        self.add_widget(line7)

    def add_number(self, value):
        if len(self.label_result.text) == 0 and value.isdigit():
            self.label_result.text += str(value)

        elif self.label_result.text[-1].isdigit():
            self.label_result.text += str(value)
        
        if not self.label_result.text[-1].isdigit() and not value.isdigit():
            alist = list()
            for i in self.label_result.text:
                alist.append(i)
            alist[-1] = str(value)
            self.label_result.text = "".join(alist)

        if not self.label_result.text[-1].isdigit() and value.isdigit():
            self.label_result.text += str(value)

    def clear_label(self):
        self.label_result.text = ""

    def print_result(self):
        self.label_result.text = str(eval(self.label_result.text))

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        return sm

app = HeartCheck()
app.run()