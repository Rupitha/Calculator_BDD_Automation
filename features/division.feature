
Feature:Division

    Scenario: 5 divided 2
        Given I load the website
        When Calc 5/2
        Then returns 2.5

    Scenario: 2 divided 5
        Given I load the website
        When Calc 2/5
        Then returns 0.4

    Scenario: 5 divided -2
        Given I load the website
        When Calc 5/-2
        Then returns 3

    Scenario: -5 divided 2
        Given I load the website
        When Calc -5/2
        Then returns -2.5

    Scenario: 6 divided 0
        Given I load the website
        When Calc 6/0
        Then returns Error

    Scenario: 0 divided 3
        Given I load the website
        When Calc 0/3
        Then returns 0