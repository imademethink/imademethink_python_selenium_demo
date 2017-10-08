@book_cab @desktop @GetMeCabTemp
Feature: Booking car rentals website validation - GetMeCab

  Background: GetMeCab.com website functionality validation
    Given Init "firefox" browser
    Given GetMeCab website under test "http://www.getmecab.com" and short name is "GetMeCab"

  #==================================================================================
  @homepage
  Scenario Outline: GetMeCab Home page functionality, look-n-feel validation
    When GetMeCab User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then GetMeCab Test result should be successful or log the error meessage
    And getmecab Quit the test scenari8o

    Examples: 
      | home page attribute list       | expected attribute value list                                                                             |
      | "home page URL"                | "http://www.getmecab.com"                                                                                 |
      | "home page title"              | "India's Largest Intercity Cab service"                                                                   |
      | "home page logo"               | "default GetMeCab logo"                                                                                   |
      | "home button"                  | "img__GetMeCab"                                                                                           |
      | "home page loading time"       | "general home page loading time"                                                                          |
      | "important home page elements" | "btn_radio__ROUND-TRIP __ btn_radio__MULTI-CITY btn_radio__ONE-WAY"                                       |
      | "important home page elements" | "img__Clean Cab __ img__On Time __ img__Courteous Driver __ img__24*7 Support _ img__Transparent Billing" |
      | "important home page elements" | "labl_Customer care number __ frame__Offline_Leave_a_message"                                             |
      | "pop up"                       | "no_popup __ no_screenshot"                                                                               |
      | "sign up"                      | "sign up link"                                                                                            |
      | "sign in"                      | "sign in link"                                                                                            |
      | "social plugin facebook"       | "social_plugin__ facebook"                                                                                |
      | "social plugin twitter"        | "social_plugin__ twitter"                                                                                 |
      | "social plugin googleplus"     | "social_plugin__ googleplus"                                                                              |
      | "home page web elements"       | "all elements __ all frames"                                                                              |
      | "download app check"           | "NA"                                                                                                      |

  #==================================================================================
  Scenario Outline: GetMeCab Booking car rentals GUI options validation
    When GetMeCab User validates booking car rentals GUI options from <GUI options list> with <expected GUI options value>
    Then GetMeCab Test result should be successful or log the error meessage
    And getmecab Quit the test scenari8o

    Examples: 
      | GUI options list                                        | expected GUI options value                                            |
      | "btn_ROUND-TRIP__ List of names under from city"        | "As available from DB or excel file"                                  |
      | "btn_ROUND-TRIP__ List of names under to city"          | "As available from DB or excel file"                                  |
      | "btn_ROUND-TRIP__ Onward journey date selection"        | "Check__current_date_month_year Check__two_month_drop_down_at_a_time" |
      | "btn_ROUND-TRIP__ Onward journey pickup time selection" | "Check__full_day_time_with_30_minute_delay"                           |
      | "btn_ROUND-TRIP__ Onward journey total days selection"  | "Check__options_from_1_to_21_days"                                    |
      | "btn_MULTI-CITY__ List of names under from city"        | "As available from DB or excel file"                                  |
      | "btn_MULTI-CITY__ List of names under to city"          | "As available from DB or excel file"                                  |
      | "btn_MULTI-CITY__ Onward journey date selection"        | "Check__current_date_month_year Check__two_month_drop_down_at_a_time" |
      | "btn_MULTI-CITY__ Onward journey pickup time selection" | "Check__full_day_time_with_30_minute_delay"                           |
      | "btn_MULTI-CITY__ Onward journey total days selection"  | "Check__options_from_1_to_21_days"                                    |
      | "btn_MULTI-CITY__ Multi city add button"                | "Check__options_add_multicity"                                        |
      | "btn_MULTI-CITY__ Multi city remove button"             | "Check__options_remove_multicity"                                     |
      | "btn_ONE-WAY__ List of names under from city"           | "As available from DB or excel file"                                  |
      | "btn_ONE-WAY__ List of names under to city"             | "As available from DB or excel file"                                  |
      | "btn_ONE-WAY__ Onward journey date selection"           | "Check__current_date_month_year Check__two_month_drop_down_at_a_time" |
      | "btn_ONE-WAY__ Onward journey pickup time selection"    | "Check__full_day_time_with_30_minute_delay"                           |
      | "btn_ROUND-TRIP__ Invalid city name check"              | "NA"                                                                  |

  #==================================================================================
  Scenario Outline: GetMeCab Booking car rentals search scenarions combination validation
    When GetMeCab User validates search scenarion by selecting main option from <main option list>
    And GetMeCab For search scenarion user selects from city from <from city list> and to city from <to city list> and date from <date list>
    And GetMeCab User selects duration from <duration list> and journey time <time list> and compares <expected search scenario result>
    Then GetMeCab Test result should be successful or log the error meessage
    And getmecab Quit the test scenari8o

    Examples: 
      | main option list | from city list | to city list | date list         | duration list | time list | expected search scenario result |
      | "btn_ROUND-TRIP" | "valid"        | "valid"      | "upcoming friday" | "valid"       | "valid"   | "valid car rental result"       |
      | "btn_MULTI-CITY" | "valid"        | "valid"      | "upcoming friday" | "valid"       | "valid"   | "valid car rental result"       |
      | "btn_ONE-WAY"    | "valid"        | "valid"      | "upcoming friday" | "valid"       | "valid"   | "valid car rental result"       |

  #==================================================================================
  Scenario Outline: GetMeCab Booking car rentals search result information validation
    When GetMeCab User performs valid search with default parameters
    Then GetMeCab Basic search result information from <search result information item check list> should be shown
    And getmecab Quit the test scenari8o

    Examples: 
      | search result information item check list                                                                                                         |
      | "General_options__ Search summary text __ Modify Search option"                                                                                   |
      | "General_options__ Car logo __ Car name __ Car type __ Seats count __ Short rate __ Total fare __ lnk__Fare breakup __ btn__Book Now or Sold Out" |
      | "General_options__ labl_Contact number __ lnk_Feedback"                                                                                           |

  #==================================================================================
  #==================== case list type first, second, third is NA for GetMeCab
  Scenario Outline: GetMeCab Booking car rentals End-To-End scenario validation type fourth
    Given GetMeCab User parameter are select main option from <main option list> and from city as "Mumbai" and to city as "Pune"
    And GetMeCab  User selects date as "next Friday" and time as "10:00 AM" and duration as "first option"
    And GetMeCab User validates end to end ticket booking case type fourth from <case list type fourth>
    Then GetMeCab Test result should be successful or log the error meessage
    And getmecab Quit the test scenari8o

    Examples: 
      | main option list | case list type fourth                                                                               |
      | "btn_ROUND-TRIP" | "type_fourth_01  Select first search result and book with default parameters until payment section" |
      | "btn_MULTI-CITY" | "type_fourth_02  Select first search result and book with default parameters until payment section" |
      | "btn_ONE-WAY"    | "type_fourth_02  Select first search result and book with default parameters until payment section" |

  #==================================================================================
  @payment
  Scenario Outline: GetMeCab Payment scenario validation
    Given GetMeCab Book a simple ticket with default details until payment section
    And GetMeCab Use payment type from <payment type list>
    Then GetMeCab Test result should be successful or log the error meessage
    And getmecab Quit the test scenari8o

    Examples: 
      | payment type list                                                                |
      | "Credit_card_type__ VISA __ American Express __ MasterCard __ JCB __ Diner club" |
      | "Debit_card_type__ VISA __ MasterCard __ RuPay"                                  |
      | "Netbanking_type_top_banks__ SBI __ Axis __ ICICI __ HDFC __ Citibank __ Kotak"  |
      | "CashCards__ ICash __ Itz Cash __ OxygenWallet __ PayCash"                       |
      | "Mobile_Payments__ IMPS __ PayMate"                                              |
      | "MobiKwik"                                                                       |
      | "Wallet__ Jana Cash Wallet __ MobiKwik __ Paytm __ Payzapp"                      |

  #==================================================================================
  # @offers - NA for GetMeCab
  #==================================================================================
  Scenario Outline: GetMeCab Support functionality validation
    When GetMeCab User validates support functionality from <support functionality list>
    Then GetMeCab Test result should be successful or log the error meessage
    And getmecab Quit the test scenari8o

    Examples: 
      | support functionality list |
      | "Online Chat"              |

  #==================================================================================
  Scenario Outline: GetMeCab User profile and user managemennt validation
    When GetMeCab User validates user management case from <user management case list>
    Then GetMeCab Test result should be successful or log the error meessage
    And getmecab Quit the test scenari8o

    Examples: 
      | user management case list                                          |
      | "Sign_up__ with dummy users and dummy details"                     |
      | "Sign_in__ with pre regstered user and sign out"                   |
      | "Edit_profile__ update few details and conform __ forget password" |

  #==================================================================================
  Scenario Outline: GetMeCab Specific other items validation
    When GetMeCab User validates GetMeCab specific other items from <GetMeCab specific other items list>
    Then GetMeCab Test result should be successful or log the error meessage
    And getmecab Quit the test scenari8o

    Examples: 
      | GetMeCab specific other items list                                          |
      | "POPULAR_ROUND_TRIP_CAB_DESTINATIONS__ lnk__Delhi to* __ lnk__Banglore to*" |
      | "POPULAR_ONE_WAY_CAB_DESTINATIONS__ lnk__Delhi to*"                         |
      | "POPULAR_CARS_FOR_HIRE__ lnk__Tata Indigo in *"                             |
      | "Booking Summary after selecting any car rental"                            |
      | "Fare Details after selecting any car rental"                               |
      | "lnk__Change Pickup Address"                                                |

  #==================================================================================
  Scenario Outline: GetMeCab Consistancy of elements across pages validation
    When GetMeCab User navigates between different pages by selecting different options from <GetMeCab navigation case list>
    And GetMeCab User validates consistancy of common web elements "img__GetMeCab_logo lnk__GetMeCab_Home lnk__Feedback"
    And GetMeCab User validates consistancy of common web elements "lnk__ABOUT US lnk__CONTACT US"
    Then GetMeCab Test result should be successful or log the error meessage
    And getmecab Quit the test scenari8o

    Examples: 
      | GetMeCab navigation case list              |
      | "navigate_01__ Any ONE-WAY rental case"    |
      | "navigate_02__ Any MULTI-CITY rental case" |
      | "navigate_03__ Any ROUND-TRIP rental case" |
      | "navigate_04__ ABOUT US screen"            |
      | "navigate_05__ CONTACT US screen"          |

  #==================================================================================
  @homepageother
  Scenario Outline: GetMeCab Home page functionality other items validation
    When GetMeCab User validates home page other attribute from <home page other attribute list> with <expected other attribute value list>
    Then GetMeCab Test result should be successful or log the error meessage
    And getmecab Quit the test scenari8o

    Examples: 
      | home page other attribute list | expected other attribute value list |
      | "ABOUT US"                     | "url__ ABOUT US"                    |
      | "BLOG"                         | "url__ BLOG"                        |
      | "CAREERS"                      | "url__ CAREERS"                     |
      | "LOWEST PRICE OFFER"           | "url__ LOWEST PRICE OFFER"          |
      | "PARTNER"                      | "url__ PARTNER"                     |
