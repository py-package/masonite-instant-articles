from masonite.packages import PackageProvider


class InstantArticleProvider(PackageProvider):
    def configure(self):
        (
            self.root("instant_article")
            .name("instant_article")
            .config("config/instant_article.py", publish=True)
            .views("views", publish=True)
            .routes("routes/route.py")
        )

    def register(self):
        super().register()