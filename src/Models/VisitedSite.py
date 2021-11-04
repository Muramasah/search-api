class VisitedSite:
    def __init__(self, url: str, title: str, text: str):
        # These validation should be abstracted in value objects.
        if len(url) and len(title) and len(text):
            self.url = url
            self.title = title
            self.text = text
        else:
            raise ValueError("Invalid arguments.")
