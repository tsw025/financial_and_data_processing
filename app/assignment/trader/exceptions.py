class TraderServiceValidationException(Exception):

    def __init__(self, message: list):
        self.message = message
        super().__init__(str(self.message))

    def __str__(self):
        return str(self.message)
