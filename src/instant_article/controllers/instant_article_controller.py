from masonite.configuration import config
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from ..models.instant_article_resolver import InstantArticleResolver


class InstantArticleController(Controller):
    def index(self, response: Response):
        return response.json({"message": "Index Page"})

    def feeds(self, slug, view: View, response: Response, request: Request):
        articles = config("instant_article").get("instant_article").get("feed_details")

        # get keys
        keys = list(articles.keys())

        if slug not in keys:
            return response.json({"message": "Feed not found"})

        feed = articles.get(slug)

        url = "{}://{}".format(
            request.environ.get("wsgi.url_scheme"), request.environ.get("HTTP_HOST")
        )

        return InstantArticleResolver(
            feed=feed,
            url=url,
            resolver=feed.get("model", ""),
            feed_type=feed.get("type", "feeds"),
            response=response,
            view=view,
        ).to_response()
