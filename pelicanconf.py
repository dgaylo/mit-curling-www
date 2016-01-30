#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'MIT Curling Club'
SITENAME = 'MIT Curling Club'
SITEURL = ''

PATH = 'content'
THEME = '../pelican-themes/pelican-bootstrap3'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

TWITTER_USERNAME = 'mitcurling'
TWITTER_WIDGET_ID = '693521676382965761'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 3

CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['image', 'extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    }

MENUITEMS = (
    ('People', '/people'),
    ('Links', '/links'),
    ('Contact Us', '/contact'),
    )

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('twitter', 'http://twitter.com/mitcurling'),
#           ('instagram', 'http://instagram.com/mitcurling'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True