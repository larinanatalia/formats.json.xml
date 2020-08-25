import json
import xml.etree.ElementTree as ET
from pprint import pprint
from collections import Counter

with open('C:/Users/79035/Desktop/py-33/hw-data_format/newsafr.json', encoding="utf-8") as f:
    json_file = json.load(f)

def top_10_json(file_name):
    file_1 = file_name["rss"]["channel"]["items"]
    words_list = []
    final_words = []
    for news in file_1:
        news_descr = news['description']
        words_list = news_descr.split(' ')
        for words in words_list:
            if len(words) > 6:
                final_words.append(words)
    final_dict= Counter(final_words)
    for word, quantity in final_dict.most_common(10):
        pprint(word)



parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("C:/Users/79035/Desktop/py-33/hw-data_format/newsafr.xml", parser)
root = tree.getroot()

def top_10_xml(file_name):
    news_list = file_name.findall("channel/item")
    words_list = []
    final_words = []
    for i, news in enumerate(news_list):
        descript = news.find("description").text
        words_list = descript.split(' ')
        for words in words_list:
            if len(words) > 6:
                final_words.append(words)
    final_dict = Counter(final_words)
    for word, quantity in final_dict.most_common(10):
        pprint(word)

