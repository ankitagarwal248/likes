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
	post_dict['title'] = "Heading"
	post_dict['image'] = "http://imageurl"
	post_dict['content'] = "some content"

	return post_dict