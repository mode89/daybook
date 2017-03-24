Feature: Core functionality

    Scenario: edit text
        Given application
        When run application
        Then should edit text

    Scenario: add record
        Given application
        And composed text is "New record"
        And time is "2000-01-02 03:04"
        When run application
        Then content of journal is
            """
            2000-01-02 03:04 New record
            """
