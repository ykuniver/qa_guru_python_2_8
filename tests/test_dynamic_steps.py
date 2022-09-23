import allure
from allure_commons.types import Severity

from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from tests.data import Repo


def test_dynamic_steps():

    allure.dynamic.tag("Web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Issues in Repository")
    allure.dynamic.story("Unauthorized user is unable to create a new issue")
    allure.dynamic.link(Repo.app_link_url, name=Repo.app_link_title)

    with allure.step("Open Main Page"):
        browser.open("/")

    with allure.step("Look for the repository"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys(f'{Repo.user}/{Repo.rep_name}')
        s(".header-search-input").submit()

    with allure.step("Click repository"):
        s(by.link_text(f'{Repo.user}/{Repo.rep_name}')).click()

    with allure.step("Open Issues Tab"):
        s("#issues-tab").click()

    with allure.step("Look for the issue with given number and title"):
        s(by.xpath(f"//div[contains(string(), '#{Repo.issue_num}')]/ancestor::div[contains(a, '{Repo.issue_subj}')]")).\
            should(be.visible)
