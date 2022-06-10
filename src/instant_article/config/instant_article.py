"""instant-articles Settings"""

"""
|--------------------------------------------------------------------------
| Masonite Instant Articles
|--------------------------------------------------------------------------
|
| You can configure various routes for either rss feeds or
| instant articles depending upon your needs.
|
"""

INSTANT_ARTICLE = {
    "force_validate": False,
    "feed_details": {
        "route-name.xml": {
            "model": "app.models.User",
            "title": "",
            "description": "",
            "lang": "en-us",
            "brand": "",
            "type": "instant-article",  # feed, instant-article
        }
    },
}
