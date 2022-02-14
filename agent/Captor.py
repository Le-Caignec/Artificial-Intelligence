
class Captor:

    def __init__(self, cli_environment):
        self.cli_environment = cli_environment

    #Function that will detect and inform the agent if the environment has changed
    def Detect_New_Env(self):
        if self.cli_environment.isNew:
            self.cli_environment.isNew = False
            return True
        else:
            return False

