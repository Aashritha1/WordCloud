from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

oswald_mask = np.array(Image.open('Oswald.gif'))

ss = set(STOPWORDS)
ss.add("said")
ss.add("are")
ss.add("Mr")
ss.add("is")
ss.add("you")
ss.add("with")
ss.add("by")
ss.add("A")
ss.add("I")
ss.add("him")
ss.add("he")
ss.add("What")
ss.add("and")
ss.add("your")
ss.add("in")
ss.add("the")
ss.add("said")
ss.add("?")
wc = WordCloud(background_color="gray", max_words=50, mask=oswald_mask,width=1500,height=1000,
               stopwords=ss)
text = open('pg4300.txt.txt').read()
wc.generate(text)

wc.to_file('wordcloud.png')
image = wc.to_image()
image.show()