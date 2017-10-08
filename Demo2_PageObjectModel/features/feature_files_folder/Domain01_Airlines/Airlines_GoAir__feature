@airlines @desktop @GoAir
Feature: Airlines website validation - GoAir

  Background: GoAir.in website functionality validation
    Given Init "firefox" browser
    Given GoAir website under test "https://www.goair.in" and short name is "GoAir"

  #==================================================================================
  #==================================================================================
  @homepage
  Scenario Outline: GoAir Home page functionality, look-n-feel validation
    When GoAir User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | home page attribute list       | expected attribute value list                                                                                                    |
      | "home page URL"                | "https://www.goair.in"                                                                                                           |
      | "home page title"              | "Cheapest Domestic Flight Tickets"                                                                                               |
      | "home page logo"               | "default GoAir logo"                                                                                                             |
      | "home page loading time"       | "general home page loading time"                                                                                                 |
      | "important home page elements" | "btn__HOME __ hover__Plan my trip __ btn__GoBusiness __ btn__GoHolidays __ btn__Careers"                                         |
      | "important home page elements" | "hover__Promotions __ hover__Services __ hover__About Us __ btn__Partner Login __ slider__image sliders"                         |
      | "important home page elements" | "tab__Book Flights __ tab__Web Check-in __ tab__Manage Booking __ tab__Flight Status __ tab__Flight Schedule __ tab__Route Map"  |
      | "important home page elements" | "slider__fare offer sliders __ img__Carry More for less __ img__Pre book preferred seats __ btn__Smart SME"                      |
      | "important home page elements" | "tab__Air Inclusive Deals __ tab__Honeymoon __ tab__Hill Station __ tab__Popular __ tab__Beaches"                                |
      | "important home page elements" | "labl__GoAir Customer Care __ labl__Call: 092 - 2322 - 2111/020 - 2566 - 2111 __ labl__Fog Helpline: __ labl__020 - 6689 - 5050" |
      | "pop up"                       | "no_popup __ no_screenshot"                                                                                                      |
      | "sign up"                      | "NA"                                                                                                                             |
      | "sign in"                      | "NA"                                                                                                                             |
      | "social plugin facebook"       | "social_plugin__ facebook"                                                                                                       |
      | "social plugin twitter"        | "social_plugin__ twitter"                                                                                                        |
      | "social plugin googleplus"     | "social_plugin__ googleplus"                                                                                                     |
      | "social plugin instagram"      | "social_plugin__ instagram"                                                                                                      |
      | "home page other web elements" | "broken links __ broken images __ all frame title"                                                                               |
      | "mobile app download check"    | "ios __ android"                                                                                                                 |

  #==================================================================================
  #==================================================================================
  Scenario Outline: GoAir Airlines home page GUI options validation
    When GoAir User validates airlines home page elements from <category name> with <GUI options list> with <expected GUI options value>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | category name        | GUI options list                                                                           |
      | "Book Flight"        | "btn__Return __ btn__One way __ labl__Group bookings __ txtbox__Adult count"               |
      | "Book Flight"        | "txtbox__Children count __ txtbox__Infant count __ drpdwn__Select promo __ btn__Book Now"  |
      | "Book Flight"        | "drpdwn__From city __ drpdwn__To city __ drpdwn__Depart date __ drpdwn__Arrive date"       |
      | "Book Flight"        | "btn__Adult count arrows __ btn__Children count arrows __ btn__Infant count arrows"        |
      | "Web Check-in"       | "txtbox__Last name __ txtbox__PNR __ tickbox__Permission box __ btn__Login"                |
      | "Manage Bookings"    | "txtbox__Last name __ txtbox__PNR __ btn__Retrieve booking"                                |
      | "Flight Status"      | "drpdwn__Flight date __ btn__Departure __ btn__Arrival __ btn__Flight Number"              |
      | "Flight Status"      | "btn__By City __ drpdwn__Flight code __ btn__SHOW ALL"                                     |
      | "Flight Schedule"    | "btn__Flight Schedule"                                                                     |
      | "Route Map"          | "btn__Route Map"                                                                           |
      | "Book Flight"        | "special__from city name list __ special__to city name list __ special__select promo list" |
      | "Book Flight"        | "special__calender depart date __ special__calender arrive date"                           |
      | "Bottom options bar" | "btn__BOOK FLIGHTS __ btn__WEB CHEC-IN __ btn__MANAGE BOOKING"                             |
      | "Bottom options bar" | "btn__FLIGHT STATUS __ btn__FLIGHT SCHEDULE __ btn__ROUTE MAP"                             |

  #==================================================================================
  #==================================================================================
  Scenario Outline: GoAir Airlines Plan my trip sub page GUI options validation
    When GoAir User validates airlines Plan my trip sub page elements from <category name> with <GUI options list>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | category name     | GUI options list                                                               |
      | "Manage Bookings" | "txtbox__Last name __ txtbox__PNR __ btn__Retrieve booking"                    |
      | "Web Check-In"    | "txtbox__Last name __ txtbox__PNR __ tickbox__Permission box __ btn__Continue" |
      | "Flight Status"   | "drpdwn__Flight date __ btn__Departure __ btn__Arrival __ btn__Flight Number"  |
      | "Flight Status"   | "btn__By City __ drpdwn__Flight code __ btn__SHOW ALL"                         |
      | "Travel Guide"    | "lnk__Bengaluru __ lnk__Mumbai __ lnk__Chennai __ lnk__Delhi __ lnk__Kolkata"  |
      | "Route Map"       | "labl__Route Map __ img_shockwave adobe image"                                 |
      | "Group Bookings"  | "txtbox__Username __ txtbox__Password __ btn__Login"                           |
      | "Flight Schedule" | "btn__Download Full Schedule __ lnk__Jaipur __ lnk__Goa"                       |
      | "Charters"        | "labl__groupdesk@goair.in"                                                     |

  #==================================================================================
  #==================================================================================
  Scenario Outline: GoAir Airlines Promotions sub page GUI options validation
    When GoAir User validates airlines Promotions sub page elements from <category name> with <GUI options list>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | category name       | GUI options list                 |
      | "Defence Promotion" | "labl__Few Terms & Conditions"   |
      | "Additional Flight" | "labl__Additional flights table" |

  #==================================================================================
  #==================================================================================
  Scenario Outline: GoAir Airlines Services sub page GUI options validation
    When GoAir User validates airlines Services page elements from <category name> with <GUI options list>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | category name       | GUI options list                              |
      | "SMS Services"      | "labl__SMS information"                       |
      | "Inflight Menu"     | "labl__Food menu details"                     |
      | "Priority Check-in" | "labl__Priority Check-in charges information" |
      | "Pre-Book Seats"    | "labl__Pre-Book Seats charges information"    |

  #==================================================================================
  #==================================================================================
  Scenario: GoAir Airlines GUI sub options validation
    When GoAir User validates airlines GoBusiness sub page elements for "labl__Go Business related information"
    And GoAir User validates airlines GoHolidays sub page elements for "url__Subpages __ tab__Honeymoon"
    And GoAir User validates airlines Careers sub page elements for "lnk__General Openings"
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

  #==================================================================================
  #   GoAir Ticket booking search scenarions combination validation - NA
  #==================================================================================
  #==================================================================================
  Scenario Outline: GoAir Ticket flight booking search result information validation
    When GoAir User performs simple valid flight search with default parameters for one way flight type
    Then GoAir Basic search result information from <search result information item check list> should be shown
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | search result information item check list                                                                                                |
      | "pop up__book return ticket"                                                                                                             |
      | "General_options__ btn__Change search __ pop_up__Change search __ labl__Short Summary __ lnk__Prev Day __  lnk__Next day"                |
      | "General_options__ tab__Economy __ tab__Premium __ labl__Depart Arrival Time City Terminal __ labl__Duration __ labl__Stops"             |
      | "General_options__ labl__Ticket Fare Types for GoValue GoPromo GoSmart GoLite __ btn__Go back __ btn__Continue __ lnk__Chat with expert" |
      | "General_options__ labl__Total fare __ labl__Booking Summary __ lnk__Show full Tax breakdown __ hoover__Any fare details hoover"         |

  #==================================================================================
  #==================================================================================
  Scenario Outline: GoAir Ticket booking End-To-End scenario validation type first
    When GoAir User performs simple valid flight search with default parameters for one way flight type
    And GoAir User validates end to end ticket booking case type first from <case list type first>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | case list type first                                                                                         |
      | "type_first_01 Select first search result and enter user details and continue"                               |
      | "type_first_02 Modify search and book return ticket and select first search result and cancel the same"      |
      | "type_first_03 Select first search result and select special seat and book the ticket until payment section" |
      | "type_first_04 Select first search result from Premium quota and cancel the same"                            |
      | "type_first_05 Navigate to next day and select first search result from Premium quota and cancel the same"   |

  #==================================================================================
  #==================== case list type second is NA for GoAir
  #==================================================================================
  #==================================================================================
  Scenario Outline: GoAir Ticket booking End-To-End scenario validation type third
    When GoAir User performs simple valid flight search with default parameters for one way flight type
    And GoAir User validates end to end ticket booking case type third from <case list type third>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | case list type third                                                                                                 |
      | "type_third_01 Sort results by departure time in ascending order and book first ticket until payment section"        |
      | "type_third_02 Sort results by GoSmart in descending order and book last ticket from until payment section"          |
      | "type_third_03 Sort results by duration in ascending order and book first ticket and choose middle seat"             |
      | "type_third_04 For next day sort results by duration in descending order and enter user details"                     |
      | "type_third_05 Sort results by stops in ascending order and go to next day book first ticket until payment section"  |
      | "type_third_06 Sort results by stops in descending order and book last ticket and choose seat from highest quota"    |
      | "type_third_07 Sort results by non sold out category of price in ascending order and change search"                  |
      | "type_third_08 Sort business class results by price in descending order and book first ticket until payment section" |

  #==================================================================================
  #==================== case list type fourth is NA for GoAir
  #==================================================================================
  #==================================================================================
  @payment
  Scenario Outline: GoAir Payment scenario validation
    When GoAir User performs simple valid flight search with default parameters until payment section
    And GoAir Use payment type from <payment type list>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | payment type list                                 |
      | "Credit_card_type__ Amex __ Visa __ Master Card"  |
      | "Debit_card_type__ Visa __ RuPay __ Mastero Card" |
      | "Netbanking_type_top_banks__ SBI Bank"            |
      | "Netbanking_type_top_banks__ Axis Corporate Bank" |
      | "Netbanking_type_top_banks__ ICICI Bank"          |
      | "Netbanking_type_top_banks__ HDFC Bank"           |

  #==================================================================================
  #==================================================================================
  @offers
  Scenario Outline: GoAir Home page offers check
    When GoAir User validates GoAir offers from <GoAir offers list>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | GoAir offers list                                          |
      | "offer_01__ Verify special fare offers from image sliders" |
      | "offer_02__ Verify first Honeymoon deal"                   |

  #==================================================================================
  #==================================================================================
  Scenario Outline: GoAir Support functionality validation
    When GoAir User validates support functionality from <support functionality list>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | support functionality list                                 |
      | "labl__GoAir Customer Care numbers __ labl__Tele Check-in" |
      | "labl__GoAir Marquee scrolling text user checkin advice"   |
      | "Support_Functionality__ lnk__Validate Web Check-in"       |
      | "Support_Functionality__ lnk__Manage Bookings"             |
      | "Support_Functionality__ lnk__Flight Status"               |

  #==================================================================================
  #  GoAir User profile and user managemennt validation - NA
  #==================================================================================
  #==================================================================================
  Scenario Outline: GoAir Specific other items validation
    When GoAir User validates GoAir specific other items from <GoAir specific other items list>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | GoAir specific other items list       |
      | "Validate__ Smart SME"                |
      | "Validate__ Carry More For Less"      |
      | "Validate__ Pre-Book Preferred Seats" |
      | "Validate__ Partner Registration"     |
      | "Validate__ Advertise With Us"        |

  #==================================================================================
  #==================================================================================
  Scenario Outline: GoAir Consistancy of elements across pages validation
    When GoAir User navigates between different pages by selecting different options from <GoAir navigation case list>
    And GoAir User validates consistancy of common web elements "btn__Home __ img__GoAir_logo __ lnk__Download App"
    And GoAir User validates consistancy of common web elements "btn__BOOK FLIGHTS at bottom bar __ btn__Partner Login"
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | GoAir navigation case list                             |
      | "navigate_01__ Plan my trip and Manage Booking screen" |
      | "navigate_02__ Go Business screen"                     |
      | "navigate_03__ Promotions screen"                      |
      | "navigate_04__ Services screen"                        |

  #==================================================================================
  #==================================================================================
  @homepageother
  Scenario Outline: GoAir Home page functionality other items validation
    When GoAir User validates home page other attribute from <home page other attribute list> with <expected other attribute value list>
    Then GoAir Test result should be successful or log the error meessage
    And GoAir Quit the test scenario

    Examples: 
      | home page other attribute list | expected other attribute value list                                                      |
      | "Contact Us"                   | "lnk__Refunds __ lnk__Customer Feedback __ lnk__Call Centre __ lnk__Grievance Redressal" |
      | "TravelGuide"                  | "lnk__Bengaluru detail __ lnk__Pune detail"                                              |
