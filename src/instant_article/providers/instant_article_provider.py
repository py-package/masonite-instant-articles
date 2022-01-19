from masonite.packages import PackageProvider

from ..commands.instant_command import InstantCommand
from ..routes import ROUTES


class InstantArticleProvider(PackageProvider):
    
    def configure(self):
        (
            self.root("instant_article")
            .name("instant_article")
            .commands(InstantCommand)
            .config("config/instant_article.py", publish=True)
            .views("views", publish=True)
            
        )
        print('fuck')

    def register(self):
        # super().register()
        self.application.make("router").add(ROUTES)
        # self.application.make("commands").add(InstantCommand)
        # current_path = Path(__file__).parent.parent.resolve()
        # self.application.make("view").add_location(os.path.join(current_path, 'views'), loader=FileSystemLoader)

    def boot(self):
        pass
