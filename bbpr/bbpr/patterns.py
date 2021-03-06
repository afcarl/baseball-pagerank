import re


TERMS = [
    'wp-content/uploads',
    'plus.google.com',
    'facebook.com',
    'simplesharebuttons.com',
    'reddit.com/submit',
    'twitter.com/',
    'baseball-reference.com',
    'amazon.com',
    'fanduel',
    'draftkings',
    'mlb.mlb.com/',
    'feedburner',
    'minorleaguesplits.com',
    'baseball-encyclopedia.com/subscribe.htm',
    'heatermagazine.com',
    'actasports.com',
    'ebay.com',
    'createspace.com',
    'mcfarlandpub.com',
    'itunes.apple.com',
    'baseballsavant.com',
    'brooksbaseball.net',
    '-chat-',

    # fangraphs
    'fangraphs.com/?$',
    'fangraphs.com/.*\.aspx',
    'fangraphs.com/not/',
    'fangraphs.com/author/',
    'fangraphs.com/.*/feed/',

    # bpro
    'baseballprospectus.com/?$',
    'baseballprospectus.com/player_search.php',
    'baseballprospectus.com/card/',
    'baseballprospectus.com/sortable',
    'baseballprospectus.com/statistics',
    'baseballprospectus.com/author/',
    'baseballprospectus.com/contact.php',
    'baseballprospectus.com/store/',
    'baseballprospectus.com/team_audit.php',
    'baseballprospectus.com/subscriptions',
    'baseballprospectus.com/glossary/',
    'baseballprospectus.com/fantasy/',
    'baseballprospectus.com/download.php',
    'baseballprospectus.com/tag/',
    'baseballprospectus.com/dt/',
    'baseballprospectus.com/p/',
    'baseballprospectus.com/pecota/',
    'baseballprospectus.com/.*\.xml',
    'baseballprospectus.com/prospects',
    'baseballprospectus.com/column/',
    'baseballprospectus.com/news/',
    'baseballprospectus.com/other/',
    'baseballprospectus.com/podcast',

    # tht
    'hardballtimes.com/?$',
    'hardballtimes.com/tools/',
    'hardballtimes.com/our-favorite-things/',
    'hardballtimes.com/wpa-inquirer/',
    'hardballtimes.com/who-we-are',
    'hardballtimes.com/our-',
    'hardballtimes.com/bookstore',
    'hardballtimes.com/privacy-policy',
    'hardballtimes.com/terms-of-use',
    'hardballtimes.com/forecasts',
    'hardballtimes.com/main',
    'hardballtimes.com/thtstats/main'
    'hardballtimes.com/author',

    # espn
    'espnradio/podcast',
]

IGNORE = [
    re.compile(r'(' + r'|'.join(TERMS) + r')'),
    re.compile(r'\.(jpe?g|png|gif|xlsx?)$'),
    re.compile(r'mailto'),
]
