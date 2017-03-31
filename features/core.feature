Feature: Core functionality

    Scenario: edit text
        Given application with temp journal and mocked config
        And mock composing of entry
        When run application
        Then should compose entry

    Scenario: append entry
        Given application with temp journal and mocked config
        And composed entry is
            """
            New entry
            """
        And time is "2000-01-02 03:04"
        When run application
        Then content of journal is
            """
            2000-01-02 03:04 New entry

            """

    Scenario: skip empty entry
        Given application with temp journal and mocked config
        And composed entry is
            """
            """
        When run application
        Then content of journal is
            """
            """

    Scenario: load journal
        Given application with temp journal and mocked config
        And content of journal file is
            """
            2000-01-02 03:04 First entry


            """
        And composed entry is
            """
            Second entry
            """
        And time is "2000-01-02 03:05"
        When run application
        Then content of journal file is
            """
            2000-01-02 03:04 First entry

            2000-01-02 03:05 Second entry

            """

    Scenario: save journal
        Given application with temp journal and mocked config
        And composed entry is
            """
            Another entry
            """
        And time is "2000-01-02 03:04"
        When run application
        Then content of journal file is
            """
            2000-01-02 03:04 Another entry

            """

    Scenario: load journal file name from config file
        Given application
        And load config from file "features/data/example.config"
        And mock composing of entry
        When run application
        Then journal file name is "example.journal"

    Scenario: execute 'edit' command
        Given application with temp journal and mocked config
        And mock text editing
        And command line is "edit"
        When run application
        Then should edit text

    Scenario: edit journal
        Given application with temp journal and mocked config
        And command line is "edit"
        And content of journal file is
            """
            2000-01-02 03:04 First record

            Some text

            """
        And edited text is
            """
            Edited text
            """
        When run application
        Then content of journal file is
            """
            Edited text
            """

    Scenario: raise exception on unknown command
        Given application with temp journal and mocked config
        And command line is "pumpurum"
        Then run and catch RuntimeError("Unknown command: pumpurum")
