from masonite.commands import Command


class InstantCommand(Command):
    """
    New command description

    instant_article
        {arg1 : Argument 1 description}
        {--o|--option1 : Option 1 description}
    """

    def __init__(self, application):
        super().__init__()
        self.app = application

    def handle(self):
        # do whatever you want !

        self.info("Success !")
