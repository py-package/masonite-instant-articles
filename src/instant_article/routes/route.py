from masonite.routes import Route

from ..controllers.instant_article_controller import InstantArticleController

ROUTES = Route.group(
    [
        Route.get("/rss/@content", InstantArticleController.feeds),
    ]
)
