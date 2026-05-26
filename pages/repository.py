class RepositoryPage:

    def __init__(self, page):
        self.page = page
        self.readmeContent = page.locator(
            '//article[contains(@class, "markdown")] | //div[contains(@class, "markdown-body")]')

    def getText(self):
        self.readmeContent.wait_for(state="visible", timeout=10000)
        return self.readmeContent.inner_text()

    def isText(self, text):
        return text in self.getText()

    def getUrl(self):
        return self.page.url