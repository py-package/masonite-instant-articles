from masonite.routes import Route
from ..controllers.instant_article_controller import InstantArticleController

ROUTES = Route.group(
    [
        Route.get("/iarticle", InstantArticleController.index),
        Route.get("/iarticle/@model", InstantArticleController.feeds),
    ]
)
