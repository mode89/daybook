Feature: Encryption

    Scenario: encrypt/decrypt journal
        Given application
        And journal with random content
        And random password
        When encrypt journal
        Then content of journal is not identical to initial content
        When decrypt journal
        Then content of journal is identical to initial content

    Scenario: execute encryption command
        Given application
        And mock journal loading/saving
        And mock journal encryption
        And enter random password
        When execute command "encrypt"
        Then encrypt journal

    Scenario: enter password
        Given application
        And mock journal loading/saving
        And enter random password
        When execute command "encrypt"
        Then password is identical to entered password
