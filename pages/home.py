class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://github.com")

    def search(self, query):
        self.page.keyboard.press("/")
        self.page.wait_for_timeout(500)
        self.page.keyboard.type(query)
        self.page.keyboard.press("Enter")