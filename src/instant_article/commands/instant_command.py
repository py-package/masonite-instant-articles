import os
import shutil
from pathlib import Path

from cleo import Command


class InstantCommand(Command):
    """
    Publishes the instant_article resources to the application.

    instant_article
        {--o|--option1 : Option 1 description}
    """

    def handle(self):
        current_path = Path(__file__).parent.parent.resolve()
        destination = os.path.join(os.getcwd(), "config")

        template_destination = os.path.join(os.getcwd(), "templates/instant_article")

        shutil.copy2(
            os.path.join(current_path, "config/instant_article.py"), destination
        )

        os.makedirs(
            os.path.join(os.getcwd(), "templates/instant_article"), exist_ok=True
        )
        shutil.copy(
            os.path.join(current_path, "views/feeds.html"),
            template_destination + "/feeds.html",
        )
        shutil.copy(
            os.path.join(current_path, "views/instant-article.html"),
            template_destination + "/instant-article.html",
        )

        self.info("Resources published, please update config as per requirement!")
