from masonite.configuration import config


class InstantArticle:
    _id = ""
    _title = ""
    _subtitle = ""
    _kicker = ""
    _summary = ""
    _description = ""
    _link = ""
    _cover = ""
    _author = ""
    _updated = ""
    _published = ""

    def __init__(self, data: list = []):
        # get key value for loop
        for key, value in data.items():
            # set key value
            setattr(self, key, value)

    @staticmethod
    def create(data: list = []):
        return InstantArticle(data)

    def id(self, id):
        self._id = id
        return self

    def title(self, title: str):
        self._title = title
        return self

    def subtitle(self, subtitle: str):
        self._subtitle = subtitle
        return self

    def kicker(self, kicker: str):
        self._kicker = kicker
        return self

    def cover(self, cover: str):
        self._cover = cover
        return self

    def published(self, published: str):
        self._published = published
        return self

    def updated(self, updated: str):
        self._updated = updated
        return self

    def description(self, description: str):
        self._description = description
        return self

    def link(self, link: str):
        self._link = link
        return self

    def author(self, author: str):
        self._author = author
        return self

    def validate(self):
        force = (
            config("instant_article")
            .get("instant_article")
            .get("force_validate", False)
        )
        _required_fields = [
            "id",
            "title",
            "updated",
            "summary",
            "description",
            "published",
            "link",
            "author",
        ]
        for field in _required_fields:
            if not self.__get(field):
                if force:
                    raise Exception(f"{field} is required")
                else:
                    return False
        return True

    def __get(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        raise Exception(f"{key} is not a valid key")
