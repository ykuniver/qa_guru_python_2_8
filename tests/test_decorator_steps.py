import allure
from allure_commons.types import Severity

from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from tests.data import Repo


@allure.tag("WWW")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", Repo.user)
@allure.feature("Just issues in Repository")
@allure.story("Long story short: to be or not to be")
@allure.link(Repo.app_link_url, name=Repo.app_link_title)
def test_decorator_steps():
    open_main_page()
    search_for_repository(f'{Repo.user}/{Repo.rep_name}')
    go_to_repository(f'{Repo.user}/{Repo.rep_name}')
    open_issue_tab()
    should_see_issue_with_number_and_subject(Repo.issue_num, Repo.issue_subj)


@allure.step("Open Main Page")
def open_main_page():
    browser.open("/")


@allure.step("Look for the repository {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Go to the repository {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Open Issues Tab")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Look for the Issue with given number and title {number}")
def should_see_issue_with_number_and_subject(number, subject):
    s(by.xpath("//div[contains(string(), '#" + number + "')]/ancestor::div[contains(a, '" + subject + "')]")).\
            should(be.visible)
