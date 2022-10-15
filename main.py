from kivy.properties import NumericProperty, StringProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy import utils
from kivymd.toast import toast
from database import DataBase as DB
from insults import insults

Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"

if utils.platform != 'android':
    Window.size = (412, 732)


class MainApp(MDApp):
    # APP
    size_x, size_y = NumericProperty(0), NumericProperty(0)

    # datas
    day_counter = StringProperty("0")
    month_counter = StringProperty("0")
    today_date = StringProperty("0")
    total = StringProperty("0")
    insult = StringProperty("")
    previous_d = StringProperty("")

    # progress
    star_one = StringProperty("0")
    star_two = StringProperty("0")
    star_three = StringProperty("0")

    def on_start(self):
        self.query_data()


    def week_progress(self):
        progress = self.root.ids.progress
        day_3 = self.root.ids.dy3
        day_7 = self.root.ids.dy7
        self.insult = insults()[0]
        progress.value = int(self.day_counter)
        if progress.value >= 3:
            day_3.text_color = 1, 1, 0, 1
        else:
            day_3.text_color = .3, .3, .3, 1
        if progress.value == 7:
            day_7.text_color = 1, 1, 0, 1
        else:
            day_7.text_color = .3, .3, .3, 1

        if not DB.check_status(DB()):
            chk = self.root.ids.check
            chk.icon = "check"
        elif DB.check_status(DB()):
            chk = self.root.ids.check
            chk.icon = "dots-horizontal"
        if self.previous_d == "yes":

            txt = self.root.ids.emo_text
            txt.text = "NoIcE"
            emo_icon = self.root.ids.emotion
            emo_icon.icon = "emoticon"
            emo_icon.theme_text_color = "Custom"
            emo_icon.text_color = .8, .7, 0, 1

        elif self.previous_d == "no":
            emo_icon = self.root.ids.emotion
            emo_icon.icon = "emoticon-angry"
            txt = self.root.ids.emo_text
            txt.text = "Sad"
            emo_icon.theme_text_color = "Custom"
            emo_icon.text_color = .8, 0, 0, 1




    def trophies(self):
        self.star_one_trophy()
        self.star_two_trophy()
        self.star_three_trophy()
        self.gentleman()
        self.knight()
        self.top_g()

    def star_one_trophy(self):
        if int(self.star_one) >= 30:
            star = self.root.ids.star_one_trophy
            star.theme_text_color = "Custom"
            star.text_color = 1, 1, 0, 1

    def star_two_trophy(self):
        print(self.star_two)
        if int(self.star_two) >= 60:
            star = self.root.ids.star_two_trophy
            star.theme_text_color = "Custom"
            star.text_color = 1, 1, 0, 1

    def star_three_trophy(self):
        if int(self.star_three) >= 90:
            star = self.root.ids.star_three_trophy
            star.theme_text_color = "Custom"
            star.text_color = 1, 1, 0, 1

    def gentleman(self):
        if int(self.total) >= 7:
            gentle = self.root.ids.gentle
            gent_text = self.root.ids.gentle_text
            tie = self.root.ids.tie

            gent_text.markup = False
            gent_text.text = "Gentleman"
            gent_text.text_color = 1, 1, 1, 1
            gentle.color = 1, 1, 0, 1
            tie.md_bg_color = 1, 1, 0, 1

    def top_g(self):
        if int(self.total) >= 30:
            topG = self.root.ids.topG
            topG_text = self.root.ids.topG_text
            top_g = self.root.ids.top_g

            topG_text.markup = False
            topG_text.text = "Top G"
            topG_text.text_color = 1, 1, 1, 1
            topG.color = 1, 1, 0, 1
            top_g.md_bg_color = 1, 1, 0, 1

    def knight(self):
        if int(self.total) >= 90:
            knight_t = self.root.ids.knight_t
            knight_text = self.root.ids.knight_text
            knight = self.root.ids.knight

            knight_text.markup = False
            knight_text.text = "Top G"
            knight_text.text_color = 1, 1, 1, 1
            knight_t.color = 1, 1, 0, 1
            knight.md_bg_color = 1, 1, 0, 1

    def today_no(self):
        if not DB.check_status(DB()):
            if self.day_counter < "7":
                self.day_counter = str(int(self.day_counter) + 1)
                DB.update_week(DB(), self.day_counter)
                self.query_data()
                emo_icon = self.root.ids.emotion
                emo_icon.icon = "emoticon-cool"
                txt = self.root.ids.emo_text
                txt.text = "Cool"
                emo_icon.theme_text_color = "Custom"
                emo_icon.text_color = .8, .7, 0, 1
            else:
                self.day_counter = "0"
                self.day_counter = str(int(self.day_counter) + 1)
                self.query_data()
                emo_icon = self.root.ids.emotion
                emo_icon.icon = "emoticon-cool"
                txt = self.root.ids.emo_text
                txt.text = "Cool"
                emo_icon.theme_text_color = "Custom"
                emo_icon.text_color = .8, .7, 0, 1
        elif DB.check_status(DB()):
            toast("Come on man! wait for at least a day")


    def insult_you(self):
        self.insult = insults()[0]

    def day_missed(self):
        txt = self.root.ids.emo_text
        if self.previous_d == "yes":
            txt.text = "Mad"
            toast("Nice you did not miss a day")
        elif self.previous_d == "no":
            toast("You missed a day, stupid fuck!")
            txt.text = "Mad"

    def query_data(self):
        data = DB.query_data(DB())
        self.total = data[0]
        self.day_counter = data[1]
        self.month_counter = data[2]
        self.star_one = str(data[5])
        self.star_two = str(data[6])
        self.star_three = str(data[7])
        self.previous_d = str(data[4])
        self.today_date = DB.date_format(DB())
        self.week_progress()
        self.trophies()

    def build(self):
        self.size_x, self.size_y = Window.size
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "DeepPurple"
        # self.theme_cls.accent = "Brown"
        self.size_x, self.size_y = Window.size
        self.title = "Tate"


MainApp().run()
