import os
from masonite.providers import Provider
from masonite.packages import PackageProvider
from ..routes import ROUTES

class InstantArticleProvider(PackageProvider):
    def configure(self): (
        # self.root("instant_article")
        # .name("instant_article")
        # .config("scaffold/instant_article.py", publish=True)
    )
    
    def register(self):
        super().register()
        self.application.make("router").add(ROUTES)
        # current_path = Path(__file__).parent.parent.resolve()
        # self.application.make("view").add_location(os.path.join(current_path, 'views'), loader=FileSystemLoader)
        
    def boot(self):
        pass