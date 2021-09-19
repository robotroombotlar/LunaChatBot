HEROKU = True # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "2004087378:AAGNIZit77YYkeO8-dLm7-yC-jWAny97U0Q"
    ARQ_API_KEY = "GTHRMK-TZQQMN-IGAVRV-PXDUGL-ARQ"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/tr/latest/#googletrans-languages
    LANGUAGE = "tr"

# Leave it as it is
ARQ_API_BASE_URL = "https://thearq.tech"
