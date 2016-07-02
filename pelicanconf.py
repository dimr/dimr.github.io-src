#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'dimitris'
SITENAME = u'Dimitris Rongotis'
SITEURL = 'http://localhost:8000'
PYGMENTS_STYLE = 'monokai'
PATH = 'content'

TIMEZONE = 'Europe/Athens'
TYPOGRIFY = False
DEFAULT_LANG = u'en'
DATE_FORMATS={
'en': '%a %d %b %Y',
}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
GITHUB_URL='https://github.com/dimr'
# TWITTER_USERNAME='dim__r'

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('Twitter', 'www.in.gr'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/dim__r'),
          ('Github','https://github.com/dimr'),)

FEEDS = (
    ('All posts','feeds/all.atom.xml'),

)

DEFAULT_PAGINATION = 10
STATIC_PATHS=['images','static']

#Flex Theme Configuration   https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings
# THEME='themes/Flex'
THEME = 'themes/Flex'
SITETITLE="Dimitris Rongotis"
SITESUBTITLE='Programming stuff, notes and thoughts'
DISQUS_SITENAME='dmtrsblog'
# BROWSER_COLOR = '#333333'

SITELOGO = 'http://localhost:8000/images/profile/mypic.png'
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU =  True
MENUITEMS = (
('Archives', '/archives.html'),
('Tags','/tags.html',)
       )

# LINKS=(('posts','http://www.in.gr'),)
SOCIAL=(('github','https://github.com/dimr'),
    ('twitter','https://twitter.com/dim__r'),
    # ('linkedin', ''),
    ('rss', '/feeds/all.atom.xml'),
    ('envelope-o','mailto:dimitris.rongotis@gmail.com',),
    ('vimeo','http://www.vimeo.com',),
)
CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }
FEED_ALL_ATOM = 'feeds/all.atom.xml'



############PLUGINS################################
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['sitemap','neighbors',
    'pelican_fontawesome',
    'render_math',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

#PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# PLUGINS = [u"disqus_static"]
#
# DISQUS_SITENAME = u'pelican-blog'
# DISQUS_SECRET_KEY = u'YOUR_SECRET_KEY'
# DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY'
