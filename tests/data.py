from dataclasses import dataclass


@dataclass
class Repo:
    user: str = 'eroshenkoam'
    rep_name: str = 'allure-example'
    issue_num: str = '68'
    issue_subj: str = 'Listeners NamedBy'
    app_link_url: str = "https://github.com"
    app_link_title: str = "QA Automation"

