"""
The app analyzes the trend of the dental market and show the most word used within the selected period.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class DentalTrendAnalysis(toga.App):
    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        input_label = toga.Label(
            'Please select the range of the months\n\n',
            style=Pack(padding=(0, 5))
        )
        self.main_box.add(input_label)

        input_label_month_from = toga.Label(
            'from (type 1-10):',
            style=Pack(padding=(0, 5))
        )
        input_box_month_from = toga.Box(style=Pack(direction=ROW, padding=5))
        self.month_input_from = toga.TextInput(style=Pack(flex=1))
        input_box_month_from.add(input_label_month_from)
        input_box_month_from.add(self.month_input_from)

        input_label_month_to = toga.Label(
            'to (type 1-10):',
            style=Pack(padding=(0, 5))
        )
        input_box_month_to = toga.Box(style=Pack(direction=ROW, padding=5))
        self.month_input_to = toga.TextInput(style=Pack(flex=1))
        input_box_month_to.add(input_label_month_to)
        input_box_month_to.add(self.month_input_to)

        self.main_box.add(input_box_month_from)
        self.main_box.add(input_box_month_to)

        # button = toga.Button(
        #     'press it',
        #     on_press=self.month_input_from
        # )
        button = toga.Button(
            'What is the magic word?',
            on_press=self.show_trend_word,
            style=Pack(padding=5)
        )
        self.main_box.add(button)
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()


    def show_trend_word(self, widget):
        month_from = 1
        month_to = 10
        if self.month_input_from.value:
            month_from = int(self.month_input_from.value)
        if self.month_input_to.value:
            month_to = int(self.month_input_to.value)
        
        stopwords = set(STOPWORDS)  # 제외할 단어 객체 예:stopwords.add('word')
        df = pd.read_csv('data.csv')
        df = df.iloc[:, 1:]

        text = []
        for i in (range(len(df))):
            if int(df['date'][i][5:7]) >= month_from and int(df['date'][i][5:7]) <= month_to:
                text.append(df['text'][i])
        wc = WordCloud(max_font_size=200, stopwords=stopwords, font_path='BlackHanSans-Regular.ttf',
                    background_color='white', width=800, height=800)
        wc.generate(str(text))

        plt.figure(figsize=(10, 8))
        plt.imshow(wc)
        plt.tight_layout(pad=0) # 패딩 제거
        plt.axis('off') # axis 제거
        plt.savefig('./src/dentaltrendanalysis/data_img.png')
        
        img_view = toga.ImageView(id="img_view", image="data_img.png")
        self.main_box.add(img_view)

    # def month_from(self):
    #     if self.name_input.value:
    #         name = self.name_input.value
    #     else:
    #         name = 'stranger'
    # )


    # def say_hello(self, widget):
    #     if self.name_input.value:
    #         name = self.name_input.value
    #     else:
    #         name = 'stranger'

    #     self.main_window.info_dialog(
    #     'Hello, {}'.format(name),
    #     'Hi there!'
    # )

def main():
    return DentalTrendAnalysis()
