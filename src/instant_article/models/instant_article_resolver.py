import importlib
from datetime import datetime

from masonite.response import Response

from ..interfaces.instant_article_interface import InstantArticleInterface
from .instant_article import InstantArticle


class InstantArticleResolver:
    _title = ""
    _description = ""
    _language = "en-us"
    _url = ""
    _brand = ""
    _view = ""
    _items = ""
    _response = None

    def __init__(self, feed, url, resolver, feed_type, response, view) -> None:
        self._title = feed.get("title", None)
        self._brand = feed.get("brand", None)
        self._description = feed.get("description", None)
        self._language = feed.get("language", None)
        self._url = url
        self._feed_type = feed_type
        self._items = self._resolve_items(resolver)
        self._view = view
        self._response = response

    def to_response(self) -> Response:
        data = {
            "title": self._title,
            "description": self._description,
            "language": self._language,
            "link": self._url,
            "brand": self._brand,
            "view": self._view,
            "articles": self._items,
            "last_updated": self._last_updated(),
            "year": datetime.now().year,
        }

        self._response.header("Content-Type", "application/xml;charset=UTF-8")
        if self._feed_type == "feed":
            return self._view.render("instant_article.feeds", data)
        return self._view.render("instant_article.instant-article", data)

    def _resolve_items(self, resolver):
        try:
            module = importlib.import_module(resolver)

            model = getattr(module, resolver.split(".")[-1])

            items = []
            items = model.get_feed_items()

            # map through items and cast to feed item
            items = list(map(lambda item: self._cast_to_feed_item(item), items))

            return items

        except Exception as e:
            raise Exception(e)

    def _last_updated(self) -> str:
        if self._items:
            return self._items[0]._updated
        return ""

    def _cast_to_feed_item(self, instant_article) -> InstantArticle:
        if isinstance(instant_article, list):
            instant_article = InstantArticle(instant_article)

        if isinstance(instant_article, InstantArticle):
            instant_article.validate()
            return instant_article

        if not isinstance(instant_article, InstantArticleInterface):
            raise Exception(
                "InstantArticle must be an instance of InstantArticleInterface"
            )

        feed_item = instant_article.format_feed()

        if not isinstance(feed_item, InstantArticle):
            raise Exception("InstantArticle must return an instance of InstantArticle")

        feed_item.validate()
        return feed_item
