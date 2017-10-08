@tkt_flight @desktop @cleartrip
Feature: Travel ticket booking website validation - cleartrip

  Background: cleartrip.com website functionality validation
    Given Init "firefox" browser
    Given cleartrip website under test "http://www.cleartrip.com" and short name is "cleartrip"

  #==================================================================================
  #==================================================================================
  @homepage
  Scenario Outline: cleartrip Home page functionality, look-n-feel validation
    When cleartrip User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | home page attribute list       | expected attribute value list                                                                                       |
      | "home page URL"                | "http://www.cleartrip.com"                                                                                          |
      | "home page title"              | "Cleartrip"                                                                                                         |
      | "home page loading time"       | "general home page loading time"                                                                                    |
      | "important home page elements" | "lnk__Home __ btn__Flights __ btn__Hotels __ btn__Flight+Hotel __ btn__Trains __ btn__Buses"                        |
      | "important home page elements" | "btn__Activities __ btn__Weekend_getaways __ btn__Mobile __ btn_Manage_trip __ btn__More"                           |
      | "important home page elements" | "More_button_Options__ Planner __ Collections __ Waytogo __ Air_fare_calendar __ Air_fare_graphs __ Air_Fare_alert" |
      | "important home page elements" | "lnk__Tell_us_what_you_think __ btn__Currency __ btn__Country_Selection"                                            |
      | "important home page elements" | "labl__DEALS __ lnk__Rewards_Know_More"                                                                             |
      | "pop up"                       | "no_popup __ no_screenshot"                                                                                         |
      | "sign up"                      | "sign up link"                                                                                                      |
      | "sign in"                      | "sign in link"                                                                                                      |
      | "social plugin facebook"       | "social_plugin__ facebook"                                                                                          |
      | "social plugin twitter"        | "social_plugin__ twitter"                                                                                           |
      | "home page other web elements" | "broken links __ broken images __ all frame title"                                                                  |
      | "mobile app download check"    | "ios __ android __ windows __ blackberry"                                                                           |

  #==================================================================================
  #==================================================================================
  Scenario Outline: cleartrip Ticket booking GUI options validation
    When cleartrip User validates ticket booking GUI options from <GUI options list> with <expected GUI options value>
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | GUI options list                  | expected GUI options value                                                                   |
      | "List of names under from city"   | "As available from DB or excel file"                                                         |
      | "List of names under to city"     | "As available from DB or excel file"                                                         |
      | "Common options for person count" | "drp_dwn__Adults __ drp_dwn__Children __ drp_dwn__Infants"                                   |
      | "Onward journey date selection"   | "Check__current_date_month_year __ Check__two_months_drop_down_at_a_time"                    |
      | "Return journey date drop down"   | "Check__two_months_drop_down_at_a_time"                                                      |
      | "Multicity journey options"       | "text_box__each_for_from_and_to_city __ Check__two_months_drop_down_at_a_time"               |
      | "Multicity journey options"       | "btn__Add_one_more __ btn__Remove_last_city __ drpdown__class_of_travel"                     |
      | "Flight+Hotel"                    | "txt_box__Depart_on __ txt_box__Return_on __ Check__two_months_drop_down_at_a_time"          |
      | "Class of travel"                 | "lnk__More options Class of travel __ Airline preference"                                    |
      | "Invalid city name error check"   | "error_message__ Sorry, but we can't continue until you fix everything that's marked in RED" |

  #==================================================================================
  #==================================================================================
  Scenario Outline: cleartrip Ticket booking search scenarions combination validation
    When cleartrip User validates search scenario with <depart city> and <arrive city> and <search date> with <expected search scenario result>
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | depart city | arrive city | search date            | expected search scenario result                                                                                   |
      | "valid"     | "valid"     | "next friday"          | "valid flight result"                                                                                             |
      | "valid"     | "invalid"   | "next friday"          | "error_message__ Sorry, but we can't continue until you fix everything that's marked in RED"                      |
      | "invalid"   | "valid"     | "next friday"          | "error_message__ Sorry, but we can't continue until you fix everything that's marked in RED"                      |
      | "invalid"   | "invalid"   | "next friday"          | "error_message__ Sorry, but we can't continue until you fix everything that's marked in RED"                      |
      | "valid"     | "valid"     | "long date from today" | "error_message_long_date__ Sorry, there aren't any flights available for your search __ btn__Try_searching_again" |

  #==================================================================================
  #==================================================================================
  Scenario Outline: cleartrip Ticket booking search result information validation
    When cleartrip User performs simple valid flight search with default parameters for one way flight type
    And cleartrip Basic search result information from <search result information item check list> should be shown
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | search result information item check list                                                                                                        |
      | "General_options__ Modify search __ List and Calender __ From To route name __ Booking day date month passener count"                            |
      | "General_options__ icon__Flights __ icon__Hotels __ icon__Packages __ icon_Trains __ icon__Buses __ lnk__Feedback"                               |
      | "General_options__ labl__n_out_of_total_flights __ lnk__Set a fare alert __ labl__Flexible with dates?"                                          |
      | "General_options__ slider__Price_Range __ tick_box__Show only refundable fares __ tick_box__Stops"                                               |
      | "General_options__ tick_box__Airlines __ slider__Departure time __ slider__Trip duration __ slider__Layover duration"                            |
      | "Sortby_options__ Airline __ Depart __ Arrive __ Duration __ Price"                                                                              |
      | "General_options_individual_flight__ lnk__Deals Know more __ img__Airlines_logo_main __ labl__Depart_time __ labl__Arrive_time __ labl_Duration" |
      | "General_options_individual_flight__ lnk__Flight itinerary __ lnk__Fare rules __ lnk__Baggage Information"                                       |
      | "General_options_individual_flight__ img__Long layover optional __ labl__Fare value __ btn__Book"                                                |
      | "General_options_individual_flight__ lnk__Deals more info __ labl__City Name From and To __ labl__Journey date"                                  |
      | "General_options_individual_flight__ labl__Airlines name __ labl__Flight number __ labl__Journey class __ img__Airlines logo"                    |

  #==================================================================================
  #==================== case list type first, second, fourth is NA for cleartrip
  #==================================================================================
  #==================================================================================
  Scenario Outline: cleartrip Ticket booking End-To-End scenario validation type third
    When cleartrip User performs simple valid flight search with default parameters for one way flight type
    When cleartrip User validates end to end ticket booking case type third from <case list type third>
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | case list type third                                                                                                             |
      | "type_third_01 Sort results by airlines in ascending order and book the first ticket until payment section"                      |
      | "type_third_02 Sort results by airlines in descending order and for second result check baggage information"                     |
      | "type_third_03 Sort results by departure time in ascending order and for last flight check cash back offer"                      |
      | "type_third_04 Sort results by departure time in descending order and modify search for maximum adults"                          |
      | "type_third_05 Sort results by arrival time in ascending order and click on calender and select any date in next month calender" |
      | "type_third_06 Sort results by arrival time in descending order and uncheck all stops tick box"                                  |
      | "type_third_07 Sort results by duration in ascending order and for third result check cash back offer in detailed view"          |
      | "type_third_08 Sort results by any three types in ascending order"                                                               |
      | "type_third_09 Sort results by price in ascending order and reduce price slider bar slightly"                                    |
      | "type_third_10 Sort results by price in descending order and use ny two sliders to refine search"                                |
      | "type_third_11 Sign in and select any search result and book any ticket with any combination until payment section"              |

  #==================================================================================
  #==================================================================================
  @payment
  Scenario Outline: cleartrip Payment scenario validation
    When cleartrip User performs simple valid flight search with default parameters for one way flight type until payment section
    And cleartrip Use payment type from <payment type list>
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | payment type list                                 |
      | "Credit_card_type__ Visa __ Master Card"          |
      | "Credit_card_type__ Diners Club __ Amex"          |
      | "Debit_card_type__ Visa __ Mastero Card"          |
      | "Debit_card_type__ RuPay __ Visa"                 |
      | "Netbanking_type_top_banks__ SBI Bank"            |
      | "Netbanking_type_top_banks__ Axis Corporate Bank" |
      | "Netbanking_type_top_banks__ HDFC Bank"           |

  #==================================================================================
  #==================================================================================
  @offers
  Scenario Outline: cleartrip Home page offers check
    When cleartrip User validates cleartrip offers from <cleartrip offers list>
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | cleartrip offers list         |
      | "offer_01__ App Offer"        |
      | "offer_02__ Activities offer" |

  #==================================================================================
  #==================================================================================
  Scenario Outline: cleartrip Support functionality validation
    When cleartrip User validates support functionality from <support functionality list>
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | support functionality list                          |
      | "Support_Functionality__ Cancel and change flights" |
      | "Support_Functionality__ Check flight status"       |
      | "Support_Functionality__ Check PNR Status"          |

  #==================================================================================
  #==================================================================================
  Scenario Outline: cleartrip User profile and user managemennt validation
    When cleartrip User validates user management case from <user management case list>
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | user management case list                        |
      | "Sign_up__ with dummy users and dummy details"   |
      | "Sign_in__ with pre regstered user and sign out" |
      | "Edit_profile__ update few details and conform"  |

  #==================================================================================
  #==================================================================================
  Scenario Outline: cleartrip Specific other items validation
    When cleartrip User validates cleartrip specific other items from <cleartrip specific other items list>
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | cleartrip specific other items list |
      | "Cheap air tickets"                 |
      | "Flight tickets"                    |
      | "India hotels"                      |
      | "IRCTC Railway Reservation"         |
      | "Cheap Domestic Air Tickets"        |
      | "Domestic Flights"                  |
      | "Travel guide"                      |
      | "Holiday Packages"                  |
      | "Bus Booking"                       |

  #==================================================================================
  #==================================================================================
  Scenario Outline: cleartrip Consistancy of elements across pages validation
    When cleartrip User navigates between different pages by selecting different options from <cleartrip navigation case list>
    And cleartrip User validates consistancy of common web elements "btn__Home __ txtbox_Find Cities"
    And cleartrip User validates consistancy of common web elements "lnk__Sign Up __ lnk__Sign In"
    And cleartrip User validates consistancy of common web elements "lnk__About Us __ icon_Transportbooking icons"
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | cleartrip navigation case list        |
      | "navigate_01 Change flight screen"    |
      | "navigate_01 Check PNR status screen" |
      | "navigate_01 Print ticket screen"     |

  #==================================================================================
  #==================================================================================
  @homepageother
  Scenario Outline: cleartrip Home page functionality other items validation
    When cleartrip User validates home page other attribute from <home page other attribute list> with <expected other attribute value list>
    Then cleartrip Test result should be successful or log the error meessage
    And cleartrip Quit the test scenario

    Examples: 
      | home page other attribute list | expected other attribute value list                                                                   |
      | "About cleartrip"              | "lnk__About lnk__Investors lnk__People lnk__Press Info lnk__Contact lnk__Jobs lnk__Support lnk__Blog" |
      | "Careers"                      | "url__Careers"                                                                                        |
      | "FAQs"                         | "lnk__within India lnk__International lnk__Hotel Bookings lnk__Fare Alerts"                           |
      | "Support"                      | "url__Support"                                                                                        |
      | "Blog"                         | "url__Blog"                                                                                           |
      | "Cleartrip for Business"       | "lnk__Track & save lnk__Manage travellers lnk__Take control lnk_Streamline payments"                  |
      | "Mobile"                       | "lnk__ios lnk__android lnk__windows lnk__blackberry"                                                  |

