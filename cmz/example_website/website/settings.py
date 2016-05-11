#IDEAS

# Languages: tuples with code/name and options
# FIRST ONE IS THE BASE ONE

SITE_LANGUAGES = [
    
    ('it', 'Italiano', {}),
    ('en', 'English', {}),

]


LANGUAGE_SELECTORS = ['prefix'] # 'query_string', 'cookie', 'header', ...


SITE_MODULES = [
    'cms_theme_bootstrap',
    'cms_content',
    'cms_news',
    'cms_cookieconsent'
]


COOKIECONSENT_OPTIONS = {
    "message" : "This is a custom message from CMZ!",
    "theme" : "dark-bottom",
    "link" : "/example-cookie-policy/",
    "dismiss" : "OK!",
    "learnMore" : "More Info"
}