@tkt_bus @desktop @redbus
Feature: Travel ticket booking website validation - redbus

  Background: redBus.com website functionality validation
    Given Init "firefox" browser
    Given redBus website under test "https://www.redbus.in" and short name is "redBus"

  #==================================================================================
  #==================================================================================
  @homepage
  Scenario Outline: redBus Home page functionality, look-n-feel validation
    When redBus User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | home page attribute list       | expected attribute value list                                                |
      | "home page URL"                | "https://www.redbus.in"                                                      |
      | "home page title"              | "Online Bus Ticket Booking, Book Volvo AC Bus Tickets, Reservation"          |
      | "home page logo"               | "default redbus logo"                                                        |
      | "home page loading time"       | "general home page loading time"                                             |
      | "important home page elements" | "lnk__BUSES __ lnk_HOTELS __ img__Promotional_side_image"                    |
      | "important home page elements" | "btn__Track_My_Bus_Learn_More __ labl__ibibo_Group __ labl__goibibo"         |
      | "important home page elements" | "lnk__Print/SMS_Ticket __ lnk__EasyCancel/Refund __ drpdwn_Toll_Number_list" |
      | "pop up"                       | "no_popup __ no_screenshot"                                                  |
      | "sign up"                      | "sign up link"                                                               |
      | "sign in"                      | "sign in link"                                                               |
      | "social plugin facebook"       | "NA"                                                                         |
      | "social plugin twitter"        | "NA"                                                                         |
      | "mobile app download check"    | "android __ ios __ windows"                                                  |

  #==================================================================================
  #==================================================================================
  Scenario Outline: redBus Ticket booking GUI options validation
    When redBus User validates ticket booking GUI options from <GUI options list> with <expected GUI options value>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | GUI options list                | expected GUI options value                                                |
      | "List of names under from city" | "As available from DB or excel file"                                      |
      | "List of names under to city"   | "As available from DB or excel file"                                      |
      | "Onward journey date selection" | "Check__current_date_month_year __ Check__two_months_drop_down_at_a_time" |
      | "Return journey date drop down" | "Check__two_months_drop_down_at_a_time"                                   |
      | "Invalid city name error check" | "error_message__ Invalid_City"                                            |

  #==================================================================================
  #==================================================================================
  Scenario Outline: redBus Ticket booking search scenarions combination validation
    When redBus User validates search scenario with <from city> and <to city> and <search date> with <expected search scenario result>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | from city | to city   | search date            | expected search scenario result                                               |
      | "valid"   | "valid"   | "next friday"          | "valid travels result"                                                        |
      | "valid"   | "invalid" | "next friday"          | "error_message__ Invalid City"                                                |
      | "invalid" | "valid"   | "next friday"          | "error_message__ Invalid City"                                                |
      | "invalid" | "invalid" | "next friday"          | "error_message__ Invalid City"                                                |
      | "valid"   | "valid"   | "long date from today" | "error_message_long_date__ Oops! bookings have not yet opened for this route" |

  #==================================================================================
  #==================================================================================
  Scenario Outline: redBus Ticket booking search result information validation
    When redBus User performs simple valid bus ticket search with default parameters for one way journey type
    Then redBus Basic search result information from <search result information item check list> should be shown
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | search result information item check list                                                                                                        |
      | "General_options__ Modify option __ Exchange from and to city option __ From To route name __ Return booking option __ Next day __ Previous day" |
      | "Filterby_optios__ Travels __ Bus Type __ Amenities __ Boarding __ Dropping __ Ratings"                                                          |
      | "Government bus group options expand and collapse"                                                                                               |
      | "General_information__ Travel company name __ Journey duration __ Available seat count __ Window seat count __ Rating value __ Total rating"     |
      | "General_information__ Journey start time __ Journey end time"                                                                                   |
      | "General_information__ Per seat rate __ Seat availability __ Sold out __ Hide seat or view seat"                                                 |
      | "General_information__ Cancellation policy __ Bus Photos __ mTicket availability"                                                                |
      | "Seat_information__ Available user seat count __ Reserved for ladies __ Selected seat __ Booked by gents __ Booked by ladies __ Lower and Upper" |

  #==================================================================================
  #==================================================================================
  Scenario Outline: redBus Ticket booking End-To-End scenario validation type first
    When redBus User performs simple valid bus ticket search with default parameters for one way journey type
    When redBus User validates end to end ticket booking case type first from <case list type first>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | case list type first                                                                                                                                                              |
      | "type_first_01 Select first search result with atleast one seat available and select seat and very first boarding point and no return ticket and enter user details and continue" |
      | "type_first_02 Select first search result and select random seat and cancel the same"                                                                                             |
      | "type_first_03 Select third search result and select ladies seat and book the ticket until payment section"                                                                       |
      | "type_first_04 Select first search result and select ladies and gents seat and cancel the same"                                                                                   |
      | "type_first_05 Select last search result and select any upper seat and book the ticket until payment section"                                                                     |
      | "type_first_06 Select first search result from government bus group and select any lower seat and book the ticket until payment section"                                          |

  #==================================================================================
  #==================================================================================
  Scenario Outline: redBus Ticket booking End-To-End scenario validation type second
    When redBus User performs simple valid bus ticket search with default parameters for one way journey type
    When redBus User validates end to end ticket booking case type second from <case list type second>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | case list type second                                                                                                                                     |
      | "type_second_01 Filter search result by first travel company name among the list and select first result and book the ticket until payment section"       |
      | "type_second_02 Filter search result by any bus type option and select first result among the list and clear the filter list"                             |
      | "type_second_03 Filter search result by second travel company name among the list and select first result and book return ticket and choose first result" |
      | "type_second_04 Filter search result by first two boarding point among the list and select first result book two ticket"                                  |
      | "type_second_05 Filter search result by last dropping point among the list and select second result book the ticket until payment section"                |
      | "type_second_06 Filter search result by first rating type among the list and check cancellation policy for the first result"                              |
      | "type_second_07 Filter search result by any three type and confirm search results and clear the filter list"                                              |

  #==================================================================================
  #==================================================================================
  Scenario Outline: redBus Ticket booking End-To-End scenario validation type third
    When redBus User performs simple valid bus ticket search with default parameters for one way journey type
    When redBus User validates end to end ticket booking case type third from <case list type third>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | case list type third                                                                                                                      |
      | "type_third_01 Without any filter sort results by travel company name in ascending order and book the first ticket until payment section" |
      | "type_third_02 Without any filter sort results by travel company name in descending order and check mTicket message"                      |
      | "type_third_03 Without any filter sort results by departure time in ascending order and book second ticket and ladies seat"               |
      | "type_third_04 Without any filter sort results by departure time in descending order and sort results by seat count in ascending order"   |
      | "type_third_05 Without any filter sort results by ratings in ascending order and book ticket where min fifteen seats available"           |
      | "type_third_06 Without any filter sort results by seat count in descending order and check ratings message"                               |
      | "type_third_07 Without any filter sort results by any three types in ascending order"                                                     |
      | "type_third_08 Without any filter sort results by fare value in ascending order and book the last ticket until payment section"           |
      | "type_third_09 Sort results by fare value in descending order and filter search result by first rating type and print first fare value"   |

  #==================================================================================
  #==================================================================================
  Scenario Outline: redBus Ticket booking End-To-End scenario validation type fourth
    When redBus User performs simple valid bus ticket search with default parameters for one way journey type
    When redBus User validates end to end ticket booking case type fourth from <case list type fourth>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | case list type fourth                                                                                                          |
      | "type_fourth_01 Select first search result and select any seat and book a return ticket using RETURN option"                   |
      | "type_fourth_02 Use RETURN option and book return ticket"                                                                      |
      | "type_fourth_03 Select first search result and select any seat and try to book the ticket after timeout period of ten minutes" |
      | "type_fourth_04 Sign in and select any search result and book any ticket with any combination until payment section"           |

  #==================================================================================
  #==================================================================================
  @payment
  Scenario Outline: redBus Payment scenario validation
    Given redBus User performs simple valid flight search with default parameters for one way flight type until payment section
    And redBus Use payment type from <payment type list>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | payment type list                                 |
      | "Credit_card_type__ Amex __ MasterCard __ VISA"   |
      | "Debit_card_type__ VISA __ MasterCard __ Mastero" |
      | "Netbanking_type_top_banks__ SBI Bank"            |
      | "Netbanking_type_top_banks__ Axis Corporate Bank" |
      | "Netbanking_type_top_banks__ ICICI Bank"          |
      | "Netbanking_type_top_banks__ HDFC Bank"           |
      | "Cash_on_delivery"                                |

  #==================================================================================
  #==================================================================================
  @offers
  Scenario Outline: redBus Home page offers check
    When redBus User validates redBus offers from <redBus offers list>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | redBus offers list |
      | "Travel smart"     |
      | "On Hotels"        |

  #==================================================================================
  #==================================================================================
  Scenario Outline: redBus Support functionality validation
    When redBus User validates support functionality in <support functionality list>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | support functionality list                         |
      | "Support_Functionality__ Cancel ticket and refund" |
      | "Support_Functionality__ Print ticket / SMS"       |
      | "Support_Functionality__ Customer care contact"    |

  #==================================================================================
  #==================================================================================
  Scenario Outline: redBus User profile and user managemennt validation
    When redBus User validates user management case from <user management case list>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | user management case list                                          |
      | "Sign_up__ with dummy users and dummy details"                     |
      | "Sign_in__ with pre regstered user and sign out"                   |
      | "Edit_profile__ update few details and conform __ forget password" |

  #==================================================================================
  #==================================================================================
  Scenario Outline: redBus Specific other items validation
    When redBus User validates redBus specific other items from <redBus specific other items list>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | redBus specific other items list                                                         |
      | "lnk__Top Bus routes names"                                                              |
      | "lnk__Bus operator names list"                                                           |
      | "lnk__RTC or regional transport corporation or government transport agencies list check" |

  #==================================================================================
  #==================================================================================
  Scenario Outline: redBus Consistancy of elements across pages validation
    When redBus User navigates between different pages by selecting different options from <redBus navigation case list>
    And redBus User validates consistancy of common web elements "btn__Home __ img__redBus_logo __ lnk__Print/SMS_Ticket __ lnk__EasyCancel/Refund"
    And redBus User validates consistancy of common web elements "drpdwn_Toll_Number_list"
    And redBus User validates consistancy of common web elements "lnk__About redBus __ labl__ibibo_Group __ labl_goibibo"
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | redBus navigation case list                                                       |
      | "navigate_01 Print/SMS ticket screen"                                             |
      | "navigate_02 EasyCancel/Refund screen"                                            |
      | "navigate_03 Any ticket booking result screen"                                    |
      | "navigate_04 Any ticket booking confirm and customer information provider screen" |
      | "navigate_05 About us screen"                                                     |
      | "navigate_06 redBus on Mobile screen"                                             |
      | "navigate_07 Track_My_Bus screen"                                                 |

  #==================================================================================
  #==================================================================================
  @homepageother
  Scenario Outline: redBus Home page functionality other items validation
    When redBus User validates home page other attribute from <home page other attribute list> with <expected other attribute value list>
    Then redBus Test result should be successful or log the error meessage
    And redbus Quit the test scenario

    Examples: 
      | home page other attribute list | expected other attribute value list                                                                                                            |
      | "About redBus"                 | "lnk__OurStory __ lnk__Channels __ lnk__Culture __ lnk__Technology __ lnk__Mentors __ lnk__Contact __ lnk__Parting_Words __ lnk__Testimonials" |
      | "FAQ"                          | "lnk__General __ lnk__Ticket-related __ lnk__Booking-related __ lnk__Cancellation-related __ lnk__Refund-related __ lnk__Phone-booking"        |
      | "Careers"                      | "url__Careers"                                                                                                                                 |
      | "Coupons"                      | "url__Coupons __ Check__first_offer_and_pop_up"                                                                                                |
      | "Hotel offers"                 | "url__Hotel offers __ Check__first_offer_and_pop_up"                                                                                           |
      | "Contact Us"                   | "Check__city_name_Banglore __ Check__city_name_Mumbai"                                                                                         |
      | "Terms of Use"                 | "Disclaimer"                                                                                                                                   |
      | "Privacy Policy"               | "url__Privacy Policy"                                                                                                                          |
      | "redbus On Mobile"             | "Check__mobile_app_download_link_for_andriod_ios_windows"                                                                                      |
      | "redBus Singapore"             | "url__redBus Singapore"                                                                                                                        |
      | "Bus Agent Registration"       | "form__Registration_formalities"                                                                                                               |
      | "Blog"                         | "lnk__recent_post"                                                                                                                             |
