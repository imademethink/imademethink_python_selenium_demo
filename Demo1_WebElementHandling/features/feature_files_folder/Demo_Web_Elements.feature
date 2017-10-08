Feature: Demo Web Elements

  @tagCurrent
  Scenario: Web element - pop up type 1
    Given  Web element pop up example1 "http://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html"

  Scenario: Web element - pop up type 2 javascript
    Given  Web element pop up example2 javascript "http://www.seleniumeasy.com/test/bootstrap-modal-demo.html"

  Scenario: Web element - tabular elements
    Given  Web element tabular elements "http://demoqa.com/"
	
  Scenario: Web element - form elements part 1
    Given  Web element form elements part1 "http://demoqa.com/registration/"
	
  Scenario: Web element - form elements part 2
    Given  Web element form elements part2 "http://demoqa.com/registration/"

  Scenario: Web element - element drag and drop
    Given  Web element drag and drop "http://demoqa.com/droppable/"
	
  Scenario: Web element - element resize
    Given  Web element resize "http://demoqa.com/resizable/"

  Scenario: Web element - date pick
    Given  Web element date pick "http://demoqa.com/datepicker/"
	
  Scenario: Web element - slider
    Given  Web element slider "http://demoqa.com/slider/"
	
  Scenario: Web element - frame handling
    Given  Web element frame handling "http://demoqa.com/wp-content/themes/wp-knowledge-base/frame1.html"
	
  Scenario: Web element - window handling
    Given  Web element window handling "http://demoqa.com/frames-and-windows/"
