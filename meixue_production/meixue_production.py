import matplotlib.pyplot as plot
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import random
import jieba

text = open('repo.txt','r').read()
text = ' '.join(jieba.cut(text))
print('cut' + text)

backgroundImg = plot.imread('icon.jpg')
wc = WordCloud(
    background_color='white',
    font_path="/System/Library/Fonts/PingFang.ttc",
    scale=2,
    mask=backgroundImg,
    max_font_size=100,
    )

wc.generate_from_text(text)
image_colors = ImageColorGenerator(backgroundImg)
wc.recolor(color_func = image_colors)
plot.imshow(wc)
plot.axis('off')
wc.to_file("yy.png")

