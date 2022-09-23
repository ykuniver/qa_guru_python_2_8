from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from tests.data import Repo


def test_github():

    browser.open('/')

    s(".header-search-input").click()
    s(".header-search-input").send_keys(f'{Repo.user}/{Repo.rep_name}')
    s(".header-search-input").submit()

    s(by.link_text(f'{Repo.user}/{Repo.rep_name}')).click()

    s("#issues-tab").click()

    s(by.xpath(f"//div[contains(string(), '#{Repo.issue_num}')]/ancestor::div[contains(a, '{Repo.issue_subj}')]"))\
        .should(be.visible)
