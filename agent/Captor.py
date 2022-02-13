
class Captor:

    def __init__(self, cli_envirennement):
        self.cli_envirennement = cli_envirennement

    def Detect_New_Env(self):
        if self.cli_envirennement.isNew:
            self.cli_envirennement.isNew = False
            return True

