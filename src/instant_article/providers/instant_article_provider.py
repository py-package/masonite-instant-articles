from masonite.packages import PackageProvider


class InstantArticleProvider(PackageProvider):
    def configure(self):
        (
            self.root("instant_article")
            .name("instant_article")
            .config("config/instant_article.py", publish=True)
            .views("templates", publish=False)
            .routes("routes/route.py")
        )

    def register(self):
        super().register()

    def boot(self):
        """Boots services required by the container."""
        pass
