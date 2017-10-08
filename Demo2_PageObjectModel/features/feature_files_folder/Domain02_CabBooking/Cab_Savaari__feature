@book_cab @desktop @SAVAARI
Feature: Booking car rentals website validation - SAVAARI

  Background: SAVAARI.com website functionality validation
    Given Init "firefox" browser
    Given SAVAARI website under test "http://www.savaari.com" and short name is "SAVAARI"

  #==================================================================================
  @homepage
  Scenario Outline: SAVAARI Home page functionality, look-n-feel validation
    When SAVAARI User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then SAVAARI Test result should be successful or log the error meessage
    And SAVAARI Quit the test scenari8o

    Examples: 
      | home page attribute list       | expected attribute value list                                                                  |
      | "home page URL"                | "http://www.savaari.com"                                                                       |
      | "home page title"              | "Savaari Car Rentals - Car Booking, Online Taxi Hire Services - Lowest Prices"                 |
      | "home page logo"               | "default SAVAARI logo"                                                                         |
      | "home page loading time"       | "general home page loading time"                                                               |
      | "important home page elements" | "btn__Outstation btn__Local btn__Airport Transfer"                                             |
      | "important home page elements" | "img__Clean Car img__On Time Service img__Courteous Driver img__Complimentary"                 |
      | "important home page elements" | "labl_Car Rentals & Online Cab Booking labl_Contact number lnk_Send Enquiry lnk__Download App" |
      | "important home page elements" | "lnk_feedback_and_suppor"                                                                      |
      | "important home page elements" | "img__All New Android App lnk__All New Android App"                                            |
      | "pop up"                       | "no_popup __ no_screenshot"                                                                            |
      | "home button"                  | "img__SAVAARI"                                                                                 |
      | "sign up"                      | "sign up link"                                                                                 |
      | "sign in"                      | "sign in link"                                                                                 |
      | "social plugin facebook"       | "social_plugin__ facebook"                                                                     |
      | "social plugin twitter"        | "social_plugin__ twitter"                                                                      |
      | "social plugin googleplus"     | "social_plugin__ googleplus"                                                                   |
      | "home page web elements"       | "all elements __ all frames"                                                                   |
      | "download app check"           | "android"                                                                                      |

  #==================================================================================
  Scenario Outline: SAVAARI Booking car rentals GUI options validation
    When SAVAARI User validates booking car rentals GUI options from <GUI options list> with <expected GUI options value>
    Then SAVAARI Test result should be successful or log the error meessage
    And SAVAARI Quit the test scenari8o

    Examples: 
      | GUI options list                                                     | expected GUI options value                                               |
      | "tab__Outstation__ List of names under from city"                    | "As available from DB or excel file"                                     |
      | "tab__Outstation__ List of names under to city"                      | "As available from DB or excel file"                                     |
      | "tab__Outstation__ Onward journey date selection"                    | "Check__current_date_month_year Check__one_month_drop_down_at_a_time"    |
      | "tab__Outstation__ Onward journey time selection"                    | "Check__full_day_time_with_15_minute_delay"                              |
      | "tab__Outstation__ Onward journey total days selection"              | "Check__options_from_1_to_10_days"                                       |
      | "tab__Local__ List of names under from city"                         | "As available from DB or excel file"                                     |
      | "tab__Local__ Onward journey date selection"                         | "Check__current_date_month_year Check_one_month_drop_down_at_a_time"     |
      | "tab__Local__ Onward journey time selection"                         | "Check__full_day_time_with_15_minute_delay"                              |
      | "tab__Local__ Onward journey duration selection"                     | "Check__Unlimited_8_Hr Unlimited_10_Hr Unlimited_12_Hr Unlimited_8_80Km" |
      | "tab__Airport_Transfer__ List of names under from city"              | "As available from DB or excel file"                                     |
      | "tab___Airport_Transfer__ Onward journey date selection"             | "Check__current_date_month_year Check_one_month_drop_down_at_a_time"     |
      | "tab__Airport_Transfer__ Onward journey time selection"              | "Check__full_day_time_with_15_minute_delay"                              |
      | "tab__Airport_Transfer__ List of names under to local area optional" | "As available from DB or excel file"                                     |
      | "tab__Outstation__ Invalid city name check"                          | "errmsg__Select a city from the list"                                    |

  #==================================================================================
  Scenario Outline: SAVAARI Booking car rentals search scenarions combination validation
    When SAVAARI User validates search scenarion by selecting main option from <main option list>
    And SAVAARI For search scenarion user selects from city from <from city list> and to city from <to city list> and date from <date list>
    And SAVAARI User selects duration from <duration list> and journey time <time list> and compares <expected search scenario result>
    Then SAVAARI Test result should be successful or log the error meessage
    And SAVAARI Quit the test scenari8o

    Examples: 
      | main option list               | from city list | to city list | date list         | duration list | time list | expected search scenario result               |
      | "tab__Outstation"              | "valid"        | "valid"      | "upcoming friday" | "valid"       | "valid"   | "valid car rental result"                     |
      | "tab__Outstation"              | "valid"        | "invalid"    | "upcoming friday" | "valid"       | "valid"   | "errmsg__Select a city from the list"         |
      | "tab__Outstation"              | "invalid"      | "valid"      | "upcoming friday" | "valid"       | "valid"   | "errmsg__Select a city from the list"         |
      | "tab__Outstation"              | "invalid"      | "invalid"    | "upcoming friday" | "valid"       | "valid"   | "errmsg__Select a city from the list"         |
      | "tab__Local"                   | "valid"        | "NA"         | "upcoming friday" | "valid"       | "valid"   | "valid car rental result"                     |
      | "tab__Local"                   | "invalid"      | "NA"         | "upcoming friday" | "valid"       | "valid"   | "errmsg__Select a city from the list"         |
      | "tab__Airport_Transfer_pickup" | "valid"        | "valid"      | "upcoming friday" | "NA"          | "valid"   | "valid car rental result"                     |
      | "tab__Airport_Transfer_pickup" | "invalid"      | "valid"      | "upcoming friday" | "NA"          | "valid"   | "errmsg__Select a city from the list"         |
      | "tab__Airport_Transfer_pickup" | "valid"        | "invalid"    | "upcoming friday" | "NA"          | "valid"   | "errmsg__Please choose an area from the list" |
      | "tab__Airport_Transfer_drop"   | "valid"        | "valid"      | "upcoming friday" | "NA"          | "valid"   | "valid car rental result"                     |
      | "tab__Airport_Transfer_drop"   | "invalid"      | "valid"      | "upcoming friday" | "NA"          | "valid"   | "errmsg__Select a city from the list"         |
      | "tab__Airport_Transfer_drop"   | "valid"        | "invalid"    | "upcoming friday" | "NA"          | "valid"   | "errmsg__Please choose an area from the list" |

  #==================================================================================
  Scenario Outline: SAVAARI Booking car rentals search result information validation
    When SAVAARI User performs valid search with default parameters
    Then SAVAARI Basic search result information from <search result information item check list> should be shown
    And SAVAARI Quit the test scenari8o

    Examples: 
      | search result information item check list                                                                                        |
      | "General_options__ btn__Outstation __ btn__Local __ btn__Airport_Transfer __ btn__Login"                                         |
      | "General_options__ Search summary text __ Modify option"                                                                         |
      | "General_options__ Car logo __ Car name __ Car type __ Short rate __ Total fare __ lnk__Fare breakup __ btn__Select or Sold Out" |
      | "General_options__ labl_Contact number __ lnk_Send Enquiry __ lnk__Download App"                                                 |

  #==================================================================================
  #==================== case list type first, second, third is NA for SAVAARI
  #==================================================================================
  Scenario Outline: SAVAARI Booking car rentals End-To-End scenario validation type fourth
    Given SAVAARI User parameter are select main option from <main option list> and from city as "Mumbai" and to city as "Pune"
    And SAVAARI  User selects date as "next Friday" and time as "10:00 AM" and duration as "first option"
    And SAVAARI User validates end to end ticket booking case type fourth from <case list type fourth>
    Then SAVAARI Test result should be successful or log the error meessage
    And SAVAARI Quit the test scenari8o

    Examples: 
      | main option list               | case list type fourth                                                                               |
      | "tab__Outstation"              | "type_fourth_01  Select first search result and book with default parameters until payment section" |
      | "tab__Local"                   | "type_fourth_02  Select first search result and book with default parameters until payment section" |
      | "tab__Airport_Transfer_pickup" | "type_fourth_02  Select first search result and book with default parameters until payment section" |
      | "tab__Airport_Transfer_drop"   | "type_fourth_02  Select first search result and book with default parameters until payment section" |

  #==================================================================================
  @payment
  Scenario Outline: SAVAARI Payment scenario validation
    Given SAVAARI User parameter are select main option from <main option list> and from city as "Mumbai" and to city as "Pune"
    And SAVAARI  User selects date as "next Friday" and time as "10:00 AM" and duration as "first option"
    When SAVAARI Book a simple ticket with default details until payment section
    And SAVAARI Use payment type from <payment type list>
    Then SAVAARI Test result should be successful or log the error meessage
    And SAVAARI Quit the test scenari8o

    Examples: 
      | payment type list                                                               |
      | "Credit_card_type__ VISA __ MasterCard"                                         |
      | "Netbanking_type_top_banks__ SBI __ Axis __ ICICI __ HDFC __ Citibank __ Kotak" |
      | "Amex"                                                                          |
      | "PayUMoney"                                                                     |
      | "MobiKwik"                                                                      |
      | "paytm"                                                                         |
      | "Internatinal card"                                                             |

  #==================================================================================
  # @offers - NA for SAVAARI
  #==================================================================================
  Scenario Outline: SAVAARI Support functionality validation
    When SAVAARI User validates support functionality from <support functionality list>
    Then SAVAARI Test result should be successful or log the error meessage
    And SAVAARI Quit the test scenari8o

    Examples: 
      | support functionality list  |
      | "Send Enquiry"              |
      | "Feedback Conntact Support" |
      | "Feedback Give Feedback"    |

  #==================================================================================
  Scenario Outline: SAVAARI User profile and user managemennt validation
    When SAVAARI User validates user management case from <user management case list>
    Then SAVAARI Test result should be successful or log the error meessage
    And SAVAARI Quit the test scenari8o

    Examples: 
      | user management case list                                          |
      | "Sign_up__ with dummy users and dummy details"                     |
      | "Sign_in__ with pre regstered user and sign out"                   |
      | "Edit_profile__ update few details and conform __ forget password" |

  #==================================================================================
  Scenario Outline: SAVAARI Specific other items validation
    When SAVAARI User validates SAVAARI specific other items from <SAVAARI specific other items list>
    Then SAVAARI Test result should be successful or log the error meessage
    And SAVAARI Quit the test scenari8o

    Examples: 
      | SAVAARI specific other items list                                                                                                 |
      | "Top_Cities__ lnk__Banglore __ lnk__Chennai __ lnk__Hyderabad __ lnk__Pune __ lnk__Mumbai"                                        |
      | "Top_Cities__ lnk__Delhi __ lnk__Kolkata __ lnk__Cochin __ lnk__Chandigadh __ lnk__Jaipur"                                        |
      | "lnk_grup__ Banglore Taxi Service"                                                                                                |
      | "lnk_grup__ Mumai Taxi Service"                                                                                                   |
      | "lnk_grup__ Chennai Taxi Service"                                                                                                 |
      | "lnk_grup__ Hyderabad Taxi Service"                                                                                               |
      | "lnk_grup__ Pune Taxi Service"                                                                                                    |
      | "lnk_grup__ Agra Taxi Service"                                                                                                    |
      | "lnk_grup__ Delhi Taxi Service"                                                                                                   |
      | "lnk_grup__ JaipurTaxi Service"                                                                                                   |
      | "City_specific_item__ Kochi Car Rental __ Place To Visit In Kochi __ Destination and Routes from Kochi __ Locations in Kochi"     |
      | "City_specific_item__ Jaipur Car Rental __ Place To Visit In Jaipur __ Destination and Routes from Jaipur __ Locations in Jaipur" |
      | "Booking Summary after selecting any car rental"                                                                                  |
      | "Fare Details after selecting any car rental"                                                                                     |

  #==================================================================================
  Scenario Outline: SAVAARI Consistancy of elements across pages validation
    When SAVAARI User navigates between different pages by selecting different options from <SAVAARI navigation case list>
    And SAVAARI User validates consistancy of common web elements "img__SAVAARI_logo lnk__SAVAARI_Home lnk__Feedback and Support"
    And SAVAARI User validates consistancy of common web elements "labl_Contact number lnk_Send Enquiry lnk__Download App"
    And SAVAARI User validates consistancy of common web elements "lnk__About Us lnk__Contact Us"
    Then SAVAARI Test result should be successful or log the error meessage
    And SAVAARI Quit the test scenari8o

    Examples: 
      | SAVAARI navigation case list                     |
      | "navigate_01 Mumbai to Pune Taxi Service screen" |
      | "navigate_02 About Us screen"                    |
      | "navigate_03 Contact Us screen"                  |

  #==================================================================================
  @homepageother
  Scenario Outline: SAVAARI Home page functionality other items validation
    When SAVAARI User validates home page other attribute from <home page other attribute list> with <expected other attribute value list>
    Then SAVAARI Test result should be successful or log the error meessage
    And SAVAARI Quit the test scenari8o

    Examples: 
      | home page other attribute list | expected other attribute value list |
      | "About Us"                     | "url__About Us"                     |
      | "Press Release"                | "url__Press Release"                |
      | "Careers"                      | "url__Careers"                      |
      | "Savaari For Business"         | "form__Signup Form"                 |
      | "One Way Cabs"                 | "check__links"                      |
