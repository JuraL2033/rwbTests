class SearchResultsPage:

    def __init__(self, page):
        self.page = page

    def getRepLink(self, repoName):
        xpath = f'//a[contains(@href, "/{repoName}")] | //a[contains(text(), "{repoName}")]'
        return self.page.locator(xpath).first

    def clickRepo(self, repoName):
        self.getRepLink(repoName).click()

    def isRepositoryPresent(self, repoName):
        return self.getRepLink(repoName).is_visible()