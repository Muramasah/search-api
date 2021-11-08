class Website:
    def __init__(self, url: str, title: str, text: str):
        # Domain validation should be abstracted in value objects. These
        # validations can be done in a application service, such as a
        # controller or middleware.
        if len(url) and len(title) and len(text):
            self.url = url
            self.title = title
            self.text = text
        else:
            raise ValueError("Invalid arguments.")
