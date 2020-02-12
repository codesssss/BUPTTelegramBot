import telepot
import telegram
import requests
import schedule
from bs4 import BeautifulSoup

HOME_URL = 'https://news.bupt.edu.cn/'
TOKEN = '1070997324:AAGpdlQiOo5MPxB9pHWMeJ7JoRd_3Hbzj1I'


def check(tag):
    return tag.name == "a" and tag.parent.name == "span"


def insert(original, new, pos):
    return original[:pos] + new + original[pos:]


def start():
    bot = telepot.Bot(TOKEN)
    page = requests.get(HOME_URL)
    html = page.content
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all(check)
    bot.sendMessage('@BUPTnews', text='今日新闻：')
    for item in news:
        if str(item).find('info') == -1:
            print()
            bot.sendMessage('@BUPTnews',
                            text=str(item),
                            parse_mode=telegram.ParseMode.HTML)
        else:
            final_text = insert(str(item), 'https://news.bupt.edu.cn/', str(item).find('info'))
            print(final_text)
            bot.sendMessage('@BUPTnews',
                            text=final_text,
                            parse_mode=telegram.ParseMode.HTML)


schedule.every().day.at("10:00").do(start)
