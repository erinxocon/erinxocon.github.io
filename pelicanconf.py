#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Erin O'Connell"
SITENAME = 'The Trans Pythonista'
SITEURL = '/'

# Categories
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True

# Pages
DISPLAY_PAGES_ON_MENU = True

PATH = 'content'
STATIC_PATHS = ['images']
TIMEZONE = 'America/Denver'
DEFAULT_LANG = 'en'

# Will change this to 10 when publishing; 3 is easier to do theme dev with
DEFAULT_PAGINATION = 4

# Period Archive formats
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'

# URL settings -- leads to clean slug urls instead of having .html after everything
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

# Theme Settings
THEME = 'themes/brutalist'
## used for OG tags and Twitter Card data on index page
# SITEIMAGE = 'site-cover.jpg'
## used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'The ramblings of a transgender python programmer.'
## path to favicon
FAVICON = 'icon.png'
## path to logo for nav menu (optional)
LOGO = 'icon.png'
## first name for nav menu if logo isn't provided
FIRST_NAME = 'Erin'
## google analytics (fake code commented out)
GOOGLE_ANALYTICS = 'UA-72839614-3'
## Twitter username for Twitter Card data
TWITTER_USERNAME = '@erinxocon'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = False
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern
MENUITEMS = [('tags', '/tags')]
## Social icons for footer
## Set these to whatever your unique public URL is for that platform
## I've left mine here as a example
TWITTER = 'https://twitter.com/erinxocon'
INSTAGRAM = 'https://instagram.com/erinxocon'
GITHUB = 'https://github.com/erinxocon'

## Disqus Sitename for comments on posts
## Commenting mine out for this theme site
# DISQUS_SITENAME = 'brutalistpelican'

## Gravatar
## Commenting mine out so you can see how the theme looks without one
## See https://mamcmanus.com to see what it looks like with a Gravatar
# GRAVATAR = 'https://secure.gravatar.com/avatar/56d01a819864fb6d017485cfd88c53ed?s=256'


# PLUGINS
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'w3c_validate', 'gzip_cache']

## SITEMAP PLUGIN
SITEMAP = {
    'format': 'xml',
    'priorities': {'articles': 0.99, 'pages': 0.75, 'indexes': 0.5},
    'changefreqs': {'articles': 'daily', 'pages': 'daily', 'indexes': 'daily'},
}

TYPOGRIFY = True
FEED_ALL_ATOM = False
FEED_ALL_RSS = False

CATEGORY_FEED_ATOM = False
CATEGORY_FEED_RSS = False
TAG_FEED_ATOM = False
TAG_FEED_RSS = False
