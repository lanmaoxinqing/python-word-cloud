import matplotlib.pyplot as plot
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import json
import random

with open('category.txt', 'r') as data:
    dataArr = json.load(data)

text = ''
textDict = {}

preDict = {
    "美TV" : random.uniform(0.8, 1),
    "美学调查局" : random.uniform(0.8, 1),
    "新品抢鲜报" : random.uniform(0.8, 1),
    "专家问答" : random.uniform(0.8, 1),
}

for dataDict in dataArr:
    name = dataDict['name']
    isHot = dataDict['isHot']
    hasIcon = dataDict['icon'] is not None
    # text += (name.replace(' ', '')) + ' '
    if name in preDict :
      textDict[name] = preDict[name]
    elif isHot and hasIcon:
        textDict[name] = random.uniform(0.5, 0.8)
    elif isHot or hasIcon:
        textDict[name] = random.uniform(0.3, 0.5)
    else:
        textDict[name] = random.uniform(0.1, 0.3)

backgroundImg = plot.imread('icon.jpg')
wc = WordCloud(
    background_color='white',
    font_path="/System/Library/Fonts/PingFang.ttc",
    scale=2,
    mask=backgroundImg,
    max_font_size=100,
    # colormap='rainbow',
    )
# wc.generate(text)
wc.generate_from_frequencies(textDict)
image_colors = ImageColorGenerator(backgroundImg)
wc.recolor(color_func = image_colors)
plot.imshow(wc)
plot.axis('off')
wc.to_file("yy.png")