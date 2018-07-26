Feature: Getting some mock SQL

  Scenario: Testing we can get SQL
    Given I want SQL
    When I generate test SQL with start day 1 and end day 3
    Then I get SQL
    And teardown

  Scenario Outline: Testing we can get SQL in mutiple ways
    Given I want SQL
    When I generate SQL with start day <start> and end day <end>
    Then The SQL file should contain <SQL_Term>
    And teardown
    Examples:
      | start | end | SQL_Term |
      | 1     | 1   | Insert   |

