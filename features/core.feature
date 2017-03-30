Feature: Core functionality

    Scenario: edit text
        Given application with temp journal and mocked config
        And mock composing of record
        When run application
        Then should compose record

    Scenario: append record
        Given application with temp journal and mocked config
        And composed record is
            """
            New record
            """
        And time is "2000-01-02 03:04"
        When run application
        Then content of journal is
            """
            2000-01-02 03:04 New record

            """

    Scenario: skip empty record
        Given application with temp journal and mocked config
        And composed record is
            """
            """
        When run application
        Then content of journal is
            """
            """

    Scenario: save journal
        Given application with temp journal and mocked config
        And composed record is
            """
            Another record
            """
        And time is "2000-01-02 03:04"
        When run application
        Then content of journal file is
            """
            2000-01-02 03:04 Another record

            """

    Scenario: load journal file name from config file
        Given application
        And load config from file "features/data/example.config"
        And mock composing of record
        When run application
        Then journal file name is "example.journal"
