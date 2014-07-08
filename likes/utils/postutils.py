from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.parser import parse
from urlparse import urlparse
from likes.utils.stringutils import *
import requests
import urllib2
import re
import simplejson
from likes.utils import goose


def get_postinfo(url):

    post_dict = {}
    title = ''
    image = ''
    meta_description = ''

    full_content = requests.get(url).text
    soup = BeautifulSoup(full_content)

    title = soup.find('title').text
    title = spiral_unicode(title).strip()

    g = goose.Goose()
    article = g.extract(raw_html=str(soup))
    image =  spiral_unicode(article.top_image.src)

    try:
        meta_description = soup.find_all("meta", {"name":"description"})
        if meta_description == []:
            meta_description = soup.find_all("meta", {"name":"og:description"})
        meta_description = meta_description[0]['content']
    except:
        meta_description = ''

    if meta_description == '':
        try:
            meta_description = soup.find_all("meta", {"property":"og:description"})
            meta_description = meta_description[0]['content']
        except:
            meta_description = ''

            

    meta_description = spiral_unicode(meta_description).strip()
    
    
    post_dict['title'] = title
    post_dict['image'] = image
    post_dict['content'] = meta_description

    return post_dict



# if __name__=="__main__":

# urls = ["http://stackoverflow.com/questions/3774571/get-data-from-the-meta-tags-using-beautifulsoup",
#         "http://timesofindia.indiatimes.com/home/science/Drug-from-Indian-spices-to-fight-hypertension/articleshow/37146069.cms?intenttarget=no&utm_source=TOI_AShow_OBWidget&utm_medium=Int_Ref&utm_campaign=TOI_AShow",
#         "http://www.thehindu.com/opinion/op-ed/marching-to-its-own-tune/article5171125.ece?topicpage=true&topicId=1280",
#         "http://www.realpython.com/blog/python/migrating-your-django-project-to-heroku/",
#         "http://blog.cafecoffeeday.com/ccdletters/?p=305"
# ]

# url = urls[-1]
# post_dict = get_postinfo(url)

# print post_dict['title']
# print post_dict['image']
# print post_dict['content']
