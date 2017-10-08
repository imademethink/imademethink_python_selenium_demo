@airlines @desktop @AmericanAirlines
Feature: Airlines website validation - AmericanAirlines

  Background: AmericanAirlines.in website functionality validation
    Given Init "firefox" browser
    Given AmericanAirlines website under test "https://www.americanairlines.in" and short name is "AmericanAirlines"

  #==================================================================================
  #==================================================================================
  @homepage
  Scenario Outline: AmericanAirlines Home page functionality, look-n-feel validation
    When AmericanAirlines User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | home page attribute list       | expected attribute value list                                                                                         |
      | "home page URL"                | "https://www.americanairlines.in"                                                                                      |
      | "home page title"              | "Airline Tickets and Airline Reservations from American Airlines"                                                     |
      | "home page logo"               | "default AmericanAirlines logo"                                                                                       |
      | "home page loading time"       | "general home page loading time"                                                                                      |
      | "important home page elements" | "btn__HOME __ lnk__Plan Travel __ lnk__Travel Information __ lnk__AAdvantage __ img__oneworld"                        |
      | "important home page elements" | "drpdwn__Language selection __ drpdwn__Country selection __ slider__Images __ btn__Slider Left __ btn__Slider Right"  |
      | "important home page elements" | "tab__Book __ tab__My Trips __ tab__Check-In __ tab__Flight Status"                                                   |
      | "important home page elements" | "img__Explore AAdvantage __ lnk__Explore our new award map __ lnk__My AAdvantage Account"                             |
      | "important home page elements" | "img__Travelling Today __ lnk__Travelling today learn more __ lnk__International travel"                              |
      | "important home page elements" | "img__Discover the oneworld alliance __ lnk__one world alliance learn more __ lnk__Baggage Information"               |
      | "important home page elements" | "img__Fly better __ lnk__Fly better __ lnk__Join AAdvantage Loyalty Program"                                          |
      | "important home page elements" | "lnk__Fishing mail alert __ lnk__Explore AAdvantage map __ lnk__AA and BA offer __ lnk__Redeem your miles for hotels" |
      | "important home page elements" | "lnk__Redeem your miles online __ lnk__See More Video on Youtube"                                                     |
      | "pop up"                       | "no_popup __ no_screenshot"                                                                                           |
      | "sign up"                      | "NA"                                                                                                                  |
      | "sign in"                      | "NA"                                                                                                                  |
      | "social plugin facebook"       | "social_plugin__ facebook"                                                                                            |
      | "social plugin twitter"        | "social_plugin__ twitter"                                                                                             |
      | "home page other web elements" | "broken links __ broken images __ all frame title"                                                                    |
      | "mobile app download check"    | "ios __ android"                                                                                                      |

  #==================================================================================
  #==================================================================================
  Scenario Outline: AmericanAirlines Airlines ticket searching scenarions combination validation
    When AmericanAirlines User validates search scenario for <section type> and <search text> with <expected search scenario result>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | section type    | search text             | expected search scenario result                                         |
      | "Book"          | "no return city"        | "error_message__ Please provide us with a return city and try again."   |
      | "Book"          | "no date"               | "error_message__ Departure date is missing."                            |
      | "My Trips"      | "invalid text"          | "error_message__ Please enter a valid six character booking reference." |
      | "Check-In"      | "invalid text"          | "error_message__ Please enter a valid six character booking reference." |
      | "Flight Status" | "valid flight number"   | "valid results"                                                         |
      | "Flight Status" | "invalid flight number" | "error_message__ Something went wrong"                                  |

  #==================================================================================
  #==================================================================================
  Scenario Outline: AmericanAirlines Airlines GUI sub options validation
    When AmericanAirlines User validates airlines top row sub page <sub page name> elements from <GUI sub page options list>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | sub page name          | GUI sub page options list                                                                             |
      | "Plan Travel"          | "lnk__Travel Offers __ lnk__Flights __ lnk__Travel Destinations __ lnk__Gates & Times"                |
      | "Travel Information"   | "lnk__At the airport __ lnk__During the flight __ lnk__Planes __ lnk__Clubs and lounges"              |
      | "Travel Information"   | "lnk__Baggage __ lnk__International travel __ lnk__Special assistance"                                |
      | "Travel Information"   | "lnk__Airlines partners __ lnk__oneworld alliance"                                                    |
      | "AAdvantage"           | "lnk__AAdvantage Home __ lnk__Elite Status __ lnk__Earn Miles __ lnk__Redeem Miles"                   |
      | "AAdvantage"           | "lnk__Award Travel __ lnk__Buy & Share Miles"                                                         |
      | "All sub pages common" | "lnk__Flight Status __ lnk__Online check-in __ lnk__My Trips __ lnk__Join AAdvantage Loyalty Program" |

  #==================================================================================
  #==================================================================================
  Scenario Outline: AmericanAirlines Airlines ticket searching scenarions combination validation
    When AmericanAirlines User validates search scenario for <section type> and <search text> with <expected search scenario result>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | section type    | search text             | expected search scenario result                                         |
      | "Book"          | "valid location"        | "valid results"                                                         |
      | "Book"          | "no return city"        | "error_message__ Please provide us with a return city and try again."   |
      | "Book"          | "no date"               | "error_message__ Departure date is missing."                            |
      | "My Trips"      | "invalid text"          | "error_message__ Please enter a valid six character booking reference." |
      | "Check-In"      | "invalid text"          | "error_message__ Please enter a valid six character booking reference." |
      | "Flight Status" | "valid flight number"   | "valid results"                                                         |
      | "Flight Status" | "invalid flight number" | "error_message__ Something went wrong"                                  |

  #==================================================================================
  #==================================================================================
  Scenario Outline: AmericanAirlines Airlines ticket flight booking search result information validation
    When AmericanAirlines User performs simple valid flight search with default parameters for one way flight type
    And AmericanAirlines Basic search result information from <search result information item check list> should be shown
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | search result information item check list                                                                                               |
      | "General_options__ labl__Short Summary __ btn__Modify Your Search __ lnk__baggage charges __ labl__Flight results table for seven days" |
      | "General_options__ radiobtn__Flight selection __ btn__SELECT __ lnk__Start Over"                                                        |

  #==================================================================================
  #==================================================================================
  Scenario Outline: AmericanAirlines Airlines ticket booking End-To-End scenario validation type first
    When AmericanAirlines User performs simple valid flight search with default parameters for one way flight type
    And AmericanAirlines User validates end to end ticket booking case type first from <case list type first>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | case list type first                                                                                       |
      | "type_first_01 Select first search result and enter user details and continue"                             |
      | "type_first_02 Modify search and book return ticket and select first search result and cancel the same"    |
      | "type_first_03 Select first search result from highest quota and cancel the same"                          |
      | "type_first_04 Navigate to next day and select first search result from Premium quota and cancel the same" |
      | "type_first_05 Select first search result with limited seats and enter user details and continue"          |

  #==================================================================================
  # AmericanAirlines Airlines ticket booking End-To-End scenario validation type second - NA
  #==================================================================================
  #==================================================================================
  Scenario Outline: AmericanAirlines Airlines Ticket booking End-To-End scenario validation type third
    When AmericanAirlines User performs simple valid flight search with default parameters for one way flight type
    And AmericanAirlines User validates end to end ticket booking case type third from <case list type third>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | case list type third                                                                                             |
      | "type_third_01 Sort results by Departure time and book the first ticket from medium quota until payment section" |
      | "type_third_02 Sort results by Arrival time and book the cheapest ticket until payment section"                  |
      | "type_third_03 Sort results by Orgin and book the first ticket from lowest quota and start over"                 |
      | "type_third_04 Sort results by Destination and book the second ticket from lowest quota until payment section"   |
      | "type_third_05 Sort results by Durations and book the last ticket from lowest quota until payment section"       |

  #==================================================================================
  #==================================================================================
  Scenario Outline: AmericanAirlines Airlines Ticket booking End-To-End scenario validation type third
    When AmericanAirlines User performs simple valid flight search with default parameters for one way flight type
    And AmericanAirlines User validates end to end ticket booking case type fourth from <case list type fourth>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | case list type fourth                                                                                                                                 |
      | "type_fourth_01 Modify your search and add two infant and handle error message book ticket until payment section"                                     |
      | "type_fourth_02 Select first search result and Modify Your Search and add Children and reduce flexibility and select random seat and book the ticket" |
      | "type_fourth_03 Select first search result and select any seat and try to book the ticket after timeout period of ten minutes"                        |

  #==================================================================================
  #==================================================================================
  Scenario Outline: AmericanAirlines Airlines Ticket booking End-To-End scenario validation type third
    When AmericanAirlines User performs simple valid flight search with default parameters for one way flight type until payment section
    And AmericanAirlines Use payment type from <payment type list>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | payment type list                                                                          |
      | "Credit_card_type__ American Express __ MasterCard __ Diners Club __ Visa __ JCB"          |
      | "Other_payment_options__ Pay Later popup __ Pay by Bank Transfer __ Pay by Online Banking" |

  #==================================================================================
  #==================================================================================
  @offers
  Scenario Outline: AmericanAirlines Home page offers check
    When AmericanAirlines User validates offers from <AmericanAirlines offers list>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | AmericanAirlines offers list |
      | "tab__ Book Travel"          |
      | "tab__ Award Travel"         |
      | "tab__ Manage My Trip"       |
      | "tab__ Online Check-In"      |
      | "tab__ Flight Status"        |

  #==================================================================================
  #==================================================================================
  Scenario Outline: AmericanAirlines Support functionality validation
    When AmericanAirlines User validates support functionality in <support functionality list>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | support functionality list                             |
      | "Support_Functionality__ Items under About Us"         |
      | "Support_Functionality__ Items under Customer Service" |
      | "Support_Functionality__ Items under More"             |

  #==================================================================================
  #  AmericanAirlines User profile and user managemennt validation - NA
  #==================================================================================
  #==================================================================================
  Scenario Outline: AmericanAirlines Specific other items validation
    When AmericanAirlines User validates AmericanAirlines specific other items from <AmericanAirlines specific other items list>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | AmericanAirlines specific other items list                                           |
      | "Validate__ drpdwn__Home page top items __ btn__Home page top items drop down close" |
      | "Validate__ lnk__Travel Information sub items"                                       |
      | "Validate__ lnk__AAdvantage sub items"                                               |
      | "Validate__ lnk__oneworldalliance URL"                                               |

  #==================================================================================
  #==================================================================================
  Scenario Outline: AmericanAirlines Consistancy of elements across pages validation
    When AmericanAirlines User navigates between different pages by selecting different options from <AmericanAirlines navigation case list>
    And AmericanAirlines User validates consistancy of common web elements "btn__HOME __ img__AmericanAirlines logo __ lnk__oneworldalliance"
    And AmericanAirlines User validates consistancy of common web elements "lnk__Plan Travel __ lnk__Travel Information __ lnk__AAdvantage"
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | AmericanAirlines navigation case list                  |
      | "navigate_01__ Ticket booking Select Dates stage page" |
      | "navigate_02__ Ticket booking Select Flights page"     |
      | "navigate_03__ Ticket booking Price page"              |
      | "navigate_04__ Ticket booking Payments page"           |

  #==================================================================================
  #==================================================================================
  @homepageother
  Scenario Outline: AmericanAirlines Home page functionality other items validation
    When AmericanAirlines User validates home page other attribute from <home page other attribute list> with <expected other attribute value list>
    Then AmericanAirlines Test result should be successful or log the error meessage
    And AmericanAirlines Quit the test scenario

    Examples: 
      | home page other attribute list | expected other attribute value list |
      | "lnk__Travel Agency"           | "txtbox__IATA login number"         |
      | "lnk__Customer Service Plan"   | "url__Customer Service Plan"        |
