Feature: Page object model test

  @tag_me
  Scenario: Page object model test scenario
    Given Perform initial browser setup
    When Perform some action on home page "http://parabank.parasoft.com/parabank/index.htm"
    When Perform some action on about us page
    And Perform some action on admin page
	And Perform some action on registration page
	Then All actions should be successful
