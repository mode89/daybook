Feature: Encryption

    Scenario: encrypt journal
        Given application
        And journal with random content
        And random password
        When encrypt journal
        Then content of journal is not identical to initial content
