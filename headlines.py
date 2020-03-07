import requests
import json


def get_top_story_ids():
    ''' Returns a list of the current top 20 stories on
    hacker news by id reference.
    '''
    data = requests.get(
        'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
    parsed_story_ids = json.loads(data.text)
    return get_story_data(parsed_story_ids[:5])


def get_story_data(storyIds):
    ''' Recieves a list of story ids and returns the rest of
    the information perstaining to that data. For now just story title and url.
    '''
    stories = {}
    count = 0
    for val in storyIds:
        story_data = requests.get(
            f'https://hacker-news.firebaseio.com/v0/item/{val}.json?print=pretty')
        parsed_story = json.loads(story_data.text)
        try:
            url = parsed_story['url']
        except:
            url = 'URL Not Found'

        stories[count] = {'url': url,
                          'title': parsed_story['title']}
        count += 1
    return stories


# data = get_top_story_ids()
# for num in range(0, 20):
#     print(data[num])

# <a href="/news/articles/2020-03-07/trump-virus-adviser-is-a-rarity-in-white-house-ruled-by-loyalty?srnd=premium" class="single-story-module__headline-link">Trump Virus Adviser Is a Rarity in White House Ruled by Loyalty</a>
