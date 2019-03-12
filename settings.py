from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
       'name': 'izzat_t2',
       'display_name': "T2",
       'num_demo_participants': 4,
       'app_sequence': ['izzat_t2'],
    },
    {
       'name': 'izzat_t3',
       'display_name': "T3",
       'num_demo_participants': 4,
       'app_sequence': ['izzat_t3'],
    },
{
       'name': 'izzat_t4',
       'display_name': "T4",
       'num_demo_participants': 4,
       'app_sequence': ['izzat_t4'],
    },
]

if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'INR'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '#4_htwpvlrn87u1=3(kg+cjhu!3pa1(s=++bdp%^qy*k)@s20h'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
