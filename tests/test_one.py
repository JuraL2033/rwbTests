import pytest
from pages.home import HomePage
from pages.results import SearchResultsPage
from pages.repository import RepositoryPage

class TestSearch:
    def test_search(self, page):
        homePage = HomePage(page)
        homePage.open()
        page.wait_for_timeout(2000)
        homePage.search("copilot")
        page.wait_for_timeout(3000)

        resultsPage = SearchResultsPage(page)
        assert resultsPage.isRepositoryPresent("CopilotKit"), "Ошибка, репозиторий не найден"
        resultsPage.clickRepo("CopilotKit")

        repoPage = RepositoryPage(page)
        page.wait_for_timeout(2000)
        assert repoPage.isText("CopilotKit"), "Ошибка, текст в репозитории не найден"