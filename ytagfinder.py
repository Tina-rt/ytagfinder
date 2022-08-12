from bs4 import BeautifulSoup
import requests
class YTagFinder:
    """
        YTageFinder is a module to fetch a 
    """
    result = []
    def __init__(self):
        pass

    def find_tags(self, youtube_video_url:str, return_type='list') -> list:
        page = requests.get('https://www.youtube.com/watch?v=CK_BCMA9yoY')
        b = BeautifulSoup(page.content, features='html.parser')
        f = b.findAll("meta", {"name":"keywords"})
        tags = f[0]['content']
        list_tags = tags.split(', ')
        return list_tags


y = YTagFinder()
print(y.find_tags('https://www.youtube.com/watch?v=CK_BCMA9yoY'))