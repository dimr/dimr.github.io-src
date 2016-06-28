#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'dimitris'
SITENAME = u'dmtrs'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Twitter', 'www.in.gr'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/dim__r'),
          ('Github','https://github.com/dimr'),)

FEEDS = (
    ('All posts','feeds/all.atom.xml'),

)

DEFAULT_PAGINATION = 10
STATIC_PATHS=['images']

#Flex Theme Configuration   https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings
THEME='themes/Flex'
SITEURL='/'
SITETITLE="Dimitris Rongotis"
SITESUBTITLE='Programming and Stuff'
DISQUS_SITENAME='dmtrsblog'
# SITELOGO = SITEURL+'content/images/profile.png'
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU =  True
MENUITEMS = (
('Archives', '/archives.html'),
       )

LINKS=(('posts','www.in.gr'),)
SOCIAL=(('github','https://github.com/dimr'),
    ('twitter','https://twitter.com/dim__r'),
    ('linkedin', 'https://br.linkedin.com/in/alexandrevicenzi/en'),
    ('rss', '/feeds/all.atom.xml'),
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
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'
#PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# PLUGINS = [u"disqus_static"]
#
# DISQUS_SITENAME = u'pelican-blog'
# DISQUS_SECRET_KEY = u'YOUR_SECRET_KEY'
# DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY'
