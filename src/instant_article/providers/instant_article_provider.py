from masonite.packages import PackageProvider

from ..commands.instant_command import InstantCommand
from ..routes import ROUTES


class InstantArticleProvider(PackageProvider):
    def configure(self):
        (
            self.root("instant_article")
            .name("instant_article")
            .config("config/instant_article.py", publish=True)
            .views("views", publish=True)
        )

    def register(self):
        self.application.make("router").add(ROUTES)
        self.application.make("commands").add(InstantCommand())

    def boot(self):
        pass
