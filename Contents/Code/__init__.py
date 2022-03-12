import os
import urllib2

FANVIDDB_URL = 'https://fanviddb.com/'
FANVIDDB_PATH = 'api/fanvids/'
API_KEY = Prefs['fanviddb_api_key']
Log.Info('API Key')
Log.Info(API_KEY)

def Start():
    Log.Info('Starting FanvidDB metadata agent!')


def search_fanviddb(data):
    Log.Info('API key is')
    Log.Info(API_KEY)
    http_headers = {'x-api-key': API_KEY}
    url = FANVIDDB_URL + FANVIDDB_PATH
    return JSON.ObjectFromURL(url, headers=http_headers, sleep=1.0)

class FanvidDBAgent(Agent.Movies):
    name = 'FanvidDB'
    primary_provider = True
    fallback_agent = False
    contributes_to = None
    accepts_from = None
    languages = [Locale.Language.NoLanguage]

    def search(self, results, media, lang, manual=False):
        Log.Info('asdf')
        for a in dir(media):
            if not a.startswith('_'):
                Log.Info('%s: %s', a, getattr(media, a))
        Log.Info('fdsa')
        results.Append(MetadataSearchResult(
            id='youtube-dl|{}|{}'.format(media.filename, media.openSubtitlesHash),
            name=media.title,
            year=None,
            lang=lang,
            score=100
        ))

        results.Sort('score', descending=True)

    def update(self, metadata, media, lang):
        # extract all the useful information we can get out of the file
        vid = media.items[0].parts[0]
        filename = os.path.basename(vid.file)
        directory = os.path.dirname(vid.file)
        duration = vid.duration
        Log.Info('duration: %s', duration)
        art = vid.art
        id_i_guess = vid.id
        Log.Info('id: %s', id_i_guess)
        size = vid.size
        Log.Info('size: %s', size)
        subs = vid.subtitles
        thumbs = vid.thumbs
        # can we look in the metadata of the file itself? seems like no
        # so we have: filename, file path, duration, size

        # maybe see if we've cached data but that might be a feature for v2

        search_results = search_fanviddb(metadata)
        Log.Info(search_results)
        # get as much data as possible
        metadata.rating = 4.2  # out of 10 lmao
        metadata.content_rating = 'mature rating'
        #metadata.art
        #metadata.chapters
#       metadata.themes = ['theme a', 'theme b']
#       metadata.quotes = ['quote me once', 'quote me twice']
        metadata.year = 2222
        #metadata.duration
        metadata.rating_count = 5
#       metadata.genres = ['genre a', 'genre b']
        metadata.title = 'a title'
        metadata.tagline = 'tagline believe it'
        metadata.content_rating_age = 56
        #metadata.writers
        #metadata.collections
        metadata.trivia = 'sounds trivial to me'
        #metadata.tags
        #metadata.audience_rating_image
        #metadata.rating_image
        #metadata.producers = ['producer a', 'producer b']
        metadata.audience_rating = 6.9
        metadata.studio = 'Studio 60'
        #metadata.posters
        #metadata.countries
        #metadata.roles
        #metadata.originally_available_at
        #metadata.title_sort
        #metadata.original_title
        metadata.summary = 'summarize but good'
        #metadata.reviews
        #metadata.directors
        #metadata.extras
        #metadata.banners
        #metadata.similar
