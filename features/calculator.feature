Feature: Subtraction

    Scenario: 5 minus 2
        Given I load the website
        When Calc 5-2
        Then returns 3

    Scenario: 5 minus 0
        Given I load the website
        When Calc 5-2
        Then returns 3

    Scenario: 0 minus 5
        Given I load the website
        When Calc 0-5
        Then returns -5

    Scenario: 1 minus 2
        Given I load the website
        When Calc 1-2
        Then returns -1

    Scenario: 1 minus -5
        Given I load the website
        When Calc 1--5
        Then returns -4

    Scenario: -5 minus 2
        Given I load the website
        When Calc -5-2
        Then returns -7
