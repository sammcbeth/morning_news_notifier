import time
from win10toast import ToastNotifier
from headlines import get_top_story_ids

# icon for notifications
ICON_PATH = 'news_icon.ico'

# get top story headlines and urls
news_items = get_top_story_ids()

# One-time initialization
toaster = ToastNotifier()

# print(len(news_items))

for num in range(len(news_items)):

    # Show notification whenever needed
    toaster.show_toast(news_items[num]['title'], news_items[num]['url'],
                       threaded=True, icon_path=ICON_PATH, duration=3)  # 3 seconds
    print('succeeded')
    # short delay between notifications
    time.sleep(5)
