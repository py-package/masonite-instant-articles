"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates
from src.instant_article.interfaces.instant_article_interface import InstantArticleInterface
from src.instant_article.models.instant_article import InstantArticle


class User(Model, SoftDeletesMixin, Authenticates, InstantArticleInterface):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __hidden__ = ["password"]
    __auth__ = "email"

    @staticmethod
    def get_feed_items():
        return User.all()  # can be any query returning proper values

    def format_feed(self):
        return InstantArticle.create({
            'id': self.id,  # required | integer
            'title': self.name,  # required | string
            'subtitle': '',  # nullable | string
            'kicker': '',  # nullable | string
            'summary': '',  # required | string
            'description': '',  # required | string
            'cover': '',  # nullable | string
            'updated': self.updated_at,  # required | date
            'published': self.created_at,  # required | date
            'link': '',  # full url to item...
            'author': ''  # nullable | email | string
        })
