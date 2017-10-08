@property @desktop @grabhouse
Feature: Property website validation - grabhouse

  Background: grabhouse.com website functionality validation
    Given Init "firefox" browser
    Given grabhouse website under test "https://grabhouse.com" and short name is "grabhouse"

  #==================================================================================
  @homepage
  Scenario Outline: grabhouse Home page functionality, look-n-feel validation
    When grabhouse User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then grabhouse Test result should be successful or log the error meessage
    And grabhouse Quit the test scenario

    Examples: 
      | home page attribute list         | expected attribute value list                                                                                                 |
      | "home page URL"                  | "http://grabhouse.com"                                                                                                        |
      | "home page title"                | "Flats, PG, House for rent without broker"                                                                                    |
      | "home page logo"                 | "default grabhouse logo"                                                                                                      |
      | "home page loading time"         | "general home page loading time"                                                                                              |
      | "important home page elements"   | "tab__Full Flat __ tab__Roommates & PG __ lnk__List your property __ lnk__Post your requirement __ txt_box__Search text"      |
      | "important home page elements"   | "icon__Notification bubble __ icon__Menu __ lnk__ Menu_CASH COUNTER __ lnk__ Menu_WE ARE HIRING __ lnk__ Menu_URBAN COCKTAIL" |
      | "important home page elements"   | "frame_Contact Grabhouse team __ lnk__Flat __ lnk__Room __ lnk__PG __ lnk__Read More"                                         |
      | "pop up"                         | "no_popup __ no_screenshot"                                                                                                           |
      | "home button"                    | "img__grabhouse"                                                                                                              |
      | "sign up"                        | "sign up link"                                                                                                                |
      | "sign in"                        | "sign in link"                                                                                                                |
      | "social plugin facebook"         | "social_plugin__ facebook"                                                                                                    |
      | "social plugin twitter"          | "social_plugin__ twitter"                                                                                                     |
      | "social plugin googleplus"       | "social_plugin__ googleplus"                                                                                                  |
      | "social plugin instagram"        | "social_plugin__ instagram"                                                                                                   |
      | "home page web elements"         | "all elements __ all frames"                                                                                                  |
      | "direct link of cities for Flat" | "Banglore __ Mumbai __ Delhi __ Kolkata __ Chennai"                                                                           |
      | "direct link of cities for Room" | "Banglore __ Mumbai __ Delhi __ Kolkata __ Chennai"                                                                           |
      | "direct link of cities for PG"   | "Banglore __ Mumbai __ Delhi __ Kolkata __ Chennai"                                                                           |
      | "download app check"             | "NA"                                                                                                                          |

  #==================================================================================
  #	Scenario Outline: grabhouse Property searching GUI options validation - NA for grabhouse
  #==================================================================================
  Scenario Outline: grabhouse Property searching scenarions combination validation
    When grabhouse User validates search scenario for <section type> and <search text> with <expected search scenario result>
    Then grabhouse Test result should be successful or log the error meessage
    And grabhouse Quit the test scenario

    Examples: 
      | section type    | search text      | expected search scenario result                        |
      | "Full Flat"     | "valid location" | "valid results"                                        |
      | "Roommate & PG" | "valid location" | "valid results"                                        |
      | "Full Flat"     | "invalid text"   | "error_message__Er! Let's try the locality name again" |
      | "Roommate & PG" | "invalid text"   | "error_message__Er! Let's try the locality name again" |

  #==================================================================================
  Scenario Outline: grabhouse Property searching result information validation - Full Flat or Roommates & PG
    When grabhouse User performs valid search for Full Flat or Roommates & PG with default parameters
    Then grabhouse Search result information from <view type> with <search result information item check list for Full Flat> should be shown
    And grabhouse Test result should be successful or log the error meessage
    And grabhouse Quit the test scenario

    Examples: 
      | view type   | search result information item check list for Full Flat                                                                                            |
      | "Common"    | "chk_box__Full Flat __ chk_box__Roommates __ chk_box__PG slider__Budget Range Min __ chk_box__PG slider__Budget Range Max __ drpdwn__More Filters" |
      | "Common"    | "tab__List of properties __ tab__Shortlisted __ tab__Owners Contacted __ txt_box__Search text entered __ btn__Map or List View"                    |
      | "Common"    | "lnk__Search path City Area name __ btn__more filters"                                                                                             |
      | "List view" | "drpdwn__Sort by options __ labl__total results count __ btn__previous page __ btn__current page btn__next page"                                   |
      | "List view" | "labl__Others looked at __ lnk__Suggested links"                                                                                                   |
      | "List view" | "Property_options__ img__Thumbnail __ labl__Title __ labl__Available for category __ labl__Short Address __ labl__Actual rent"                     |
      | "List view" | "Property_options__ labl__Posted date __ btn__Shortlist icon __ btn__Report spam __ icon__More info"                                               |
      | "List view" | "Property_options__ labl__Security Deposit __ labl__Available From __ labl__Furnishing Status __ btn__Contact person"                              |
      | "Map view"  | "Property_options__ img__Thumbnail __ labl__Title __ labl__Available for category __ labl__Actual rent"                                            |
      | "Map view"  | "Property_options__ labl__Posted date __ btn__Shortlist icon __ btn__Contact person"                                                               |
      | "Map view"  | "Map_options_check__ Main area highlight __ Found property pointers __ Zoom in button __ Zoom out button"                                          |

  #==================================================================================
  Scenario Outline: grabhouse Property searching result information validation - Individual property details
    When grabhouse User performs valid search for Full Flat or Roommates & PG with default parameters and navigates to individual property details page
    Then grabhouse Search result information from <individual property information item check list> should be shown
    And grabhouse Test result should be successful or log the error meessage
    And grabhouse Quit the test scenario

    Examples: 
      | individual property information item check list                                                                                         |
      | "labl__Short title __ labl__Short address __ labl__Contact person name __ lnk__Search path City Area name __ btn__Report spam"          |
      | "btn__Shortlist icon __ btn__Contact person __ lnk__View all photos __ img__Property images __ labl__Property description"              |
      | "labl__FLAT TYPE __ labl__RENT __ labl__SECURITY DEPOSIT __ labl__AVAILABLE FOR __ labl__FURNISHING STATUS __ labl__ADDRESS"            |
      | "labl__AVAILABLE FROM __ labl__LANDMARK __ labl__HOUSE AMENITIES __ labl__BUILDING AMENITIES"                                           |
      | "lnk__TRANSPORTATION __ lnk__RESTAURANTS AND BARS __ lnk__SCHOOLS/COLLEGES __ lnk__HOSPITALS __ lnk__PHARMACIES __ lnk__SHOPPING MALLS" |
      | "lnk__GARDENS AND RECREATION __ lnk__MOVIE HALLS __ lnk__ATMs __ lnk__GAS STATIONs"                                                     |

  #==================================================================================
  Scenario Outline: grabhouse Property search End-To-End search scenario validation type first
    When grabhouse User performs valid search from <search type> and search case from <search case details type first> and validates result
    Then grabhouse Test result should be successful or log the error meessage
    And grabhouse Quit the test scenario

    Examples: 
      | search type     | search case details type first                                                                               |
      | "Full Flat"     | "type_first_01 Select first search result and browse photos and contact person"                              |
      | "Roommate & PG" | "type_first_02 Select first search result and browse photos and contact person"                              |
      | "Full Flat"     | "type_first_03 Select map view and first search result and browse photos and contact person"                 |
      | "Roommate & PG" | "type_first_04 Select map view and first search result and browse photos and contact person"                 |
      | "Full Flat"     | "type_first_05 Select first search result and report spam"                                                   |
      | "Roommate & PG" | "type_first_06 Select first search result and shortlist it and navigate to shortlist tab and contact person" |
      | "Full Flat"     | "type_first_07 Select first search result and browse photos and navigate back to home page"                  |
      | "Roommate & PG" | "type_first_08 Navigate between tabs Shortlisted and Owners contacted"                                       |

  #==================================================================================
  Scenario Outline: grabhouse Property search End-To-End search scenario validation type second
    When grabhouse User performs valid search from <search type> and search case from <search case details type second> and validates result
    Then grabhouse Test result should be successful or log the error meessage
    And grabhouse Quit the test scenario

    Examples: 
      | search type     | search case details type second                                                                                |
      | "Full Flat"     | "type_second_01 Filter search result by BHK Type and select first result and contact person"                   |
      | "Roommate & PG" | "type_second_02 Filter search result by Furnishing type and select first result and contact person"            |
      | "Full Flat"     | "type_second_03 Filter search result by BHK Type and Available for and select first result and contact person" |

  #==================================================================================
  Scenario Outline: grabhouse Property search End-To-End search scenario validation type third
    When grabhouse User performs valid search from <search type> and search case from <search case details type third> and validates result
    Then grabhouse Test result should be successful or log the error meessage
    And grabhouse Quit the test scenario

    Examples: 
      | search type     | search case details type third                                                                             |
      | "Full Flat"     | "type_third_01 Without any filter sort results by Low Price and select first result and contact person"    |
      | "Roommate & PG" | "type_third_02 Without any filter sort results by Newely Added and select first result and contact person" |
      | "Full Flat"     | "type_third_03 Without any filter sort results by Date and select first result and contact person"         |
      | "Roommate & PG" | "type_third_04 Without any filter sort results by Relevance and select first result and contact person"    |

  #==================================================================================
  Scenario Outline: grabhouse User profile and user managemennt validation
    When grabhouse User validates user management case from <user management case list>
    Then grabhouse Test result should be successful or log the error meessage
    And grabhouse Quit the test scenario

    Examples: 
      | user management case list                                          |
      | "Sign_up__ with dummy users and dummy details"                     |
      | "Sign_in__ with pre registered user and sign out"                  |
      | "Edit_profile__ update few details and conform __ forget password" |

  #==================================================================================
  Scenario Outline: grabhouse Specific other items validation
    When grabhouse User validates specific other items from <grabhouse specific other items list>
    Then grabhouse Test result should be successful or log the error meessage
    And grabhouse Quit the test scenario

    Examples: 
      | grabhouse specific other items list |
      | "See all shortlisted properties"    |
      | "List your property"                |
      | "Post your requirement"             |

  #==================================================================================
  Scenario Outline: grabhouse Consistancy of elements across pages validation
    When grabhouse User navigates between different pages by selecting different options from <grabhouse navigation case list>
    And grabhouse User validates consistancy of common web elements "btn__Home __ lnk__List your property __ lnk__Post your requirement"
    Then grabhouse Test result should be successful or log the error meessage
    And grabhouse Quit the test scenario

    Examples: 
      | redBus navigation case list      |
      | "navigate_01 Full flat property" |
      | "navigate_02 Roommate & PG"      |

  #==================================================================================
  @homepageother
  Scenario Outline: grabhouse Home page functionality other items validation
    When grabhouse User validates home page other attribute from <home page other attribute list> with <expected other attribute value list>
    Then grabhouse Test result should be successful or log the error meessage
    And grabhouse Quit the test scenario

    Examples: 
      | home page other attribute list | expected other attribute value list |
      | "We are hiring"                | "url__We are hiring"                |
      | "Blog"                         | "url__Blog"                         |
      | "Contact Us"                   | "url__Contact Us"                   |
