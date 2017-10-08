@property @desktop @HOUSING
Feature: Property website validation - HOUSING

  Background: HOUSING.com website functionality validation
    Given Init "firefox" browser
    Given HOUSING website under test "https://housing.com" and short name is "HOUSING"

  #==================================================================================
  @homepage
  Scenario Outline: HOUSING Home page functionality, look-n-feel validation
    When HOUSING User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then HOUSING Test result should be successful or log the error meessage
    And HOUSING Quit the test scenario

    Examples: 
      | home page attribute list       | expected attribute value list                                                                                                          |
      | "home page URL"                | "http://housing.com"                                                                                                                   |
      | "home page title"              | "Look Up a place to Buy in India"                                                                                                      |
      | "home page logo"               | "default HOUSING logo"                                                                                                                 |
      | "home page loading time"       | "general home page loading time"                                                                                                       |
      | "important home page elements" | "drp_dwn__Buy __ drp_dwn__Rent __ drp_dwn__PG & Hostels __ drp_dwn__Home Loans __ drp_dwn__Online Rental Agreements __ drp_dwn__Aents" |
      | "important home page elements" | "tab__BUY __ tab__RENT __ tab__PG & HOSTELS __ tab__HOME LOANS __ tab__RENTAL AGREEMENTS"                                              |
      | "important home page elements" | "lnk__LIST YOUR PROPERTY __ lnk__BLOG lnk__SHORTLIST PROPERTY ICON __ lnk__MENU __ lnk__SubmenuOptions"                                |
      | "important home page elements" | "hoover__List Your Property __ hoover__NRI Special* __ hoover__Housing Select"                                                         |
      | "important home page elements" | "labl__Featured Developer labl__Featured Projects __ labl__Top Cities In India btn__All Cities"                                        |
      | "important home page elements" | "labl__Land & Plot Projects __ lnk__Invest in Land __ lnk__Invest in Plots"                                                            |
      | "pop up"                       | "no_popup __ no_screenshot"                                                                                                                    |
      | "home button"                  | "img__HOUSING"                                                                                                                         |
      | "sign up"                      | "sign up link"                                                                                                                         |
      | "sign in"                      | "sign in link"                                                                                                                         |
      | "social plugin facebook"       | "social_plugin__ facebook"                                                                                                             |
      | "social plugin twitter"        | "social_plugin__ twitter"                                                                                                              |
      | "social plugin googleplus"     | "social_plugin__ googleplus"                                                                                                           |
      | "social plugin instagram"      | "social_plugin__ instagram"                                                                                                            |
      | "social plugin youtube"        | "social_plugin__ youtube"                                                                                                              |
      | "home page web elements"       | "all elements __ all frames"                                                                                                           |
      | "download app check"           | "ios __ android"                                                                                                                       |

  #==================================================================================
  Scenario Outline: HOUSING Property searching GUI options validation
    When HOUSING User validates property searching GUI options from <GUI options list> with <expected GUI options value>
    Then HOUSING Test result should be successful or log the error meessage
    And HOUSING Quit the test scenario

    Examples: 
      | GUI options list                          | expected GUI options value                                                                                   |
      | "BUY_section__ auto suggest"              | "LOCATION LANDMARK_optional DEVELOPER PROJECT"                                                               |
      | "RENT_section__ auto suggest"             | "LOCATION LANDMARK BUILDING_optional"                                                                        |
      | "PG & HOSTELS_section__ auto suggest"     | "LOCATION LANDMARK_optional"                                                                                 |
      | "HOME LOANS_section__ auto suggest"       | "LOCATION LANDMARK_optional"                                                                                 |
      | "BUY_section__ other items"               | "tick_box__Under Construction __ tick_box__Ready To Move __ drp_dwn__Room Count __ drp_dwn__Budget Range"    |
      | "RENT_section__ other items"              | "drp_dwn__Room Count __ drp_dwn__Budget Range"                                                               |
      | "PG & HOSTELS_section__ other items"      | "drp_dwn__Gender __ drp_dwn__Rent Range"                                                                     |
      | "HOME LOANS_section__ other items"        | "drp_dwn__Property Value Range __ drp_dwn__Property Type __ drp_dwn__Property City __ lnk__Get Pre-approved" |
      | "RENTAL AGREEMENTS_section__ other items" | "drp_dwn__City of Property Location __ lnk__existing agreements"                                             |
      | "BUY_section__ search history"            | "LOCATION LANDMARK DEVELOPER PROJECT"                                                                        |
      | "RENT_section__ search history"           | "LOCATION LANDMARK BUILDING"                                                                                 |
      | "PG & HOSTELS_section__ search history"   | "LOCATION LANDMARK"                                                                                          |

  #==================================================================================
  Scenario Outline: HOUSING Property searching scenarions combination validation
    When HOUSING User validates search scenario for <section type> and <search text> with <expected search scenario result>
    Then HOUSING Test result should be successful or log the error meessage
    And HOUSING Quit the test scenario

    Examples: 
      | section type             | search text         | expected search scenario result              |
      | "BUY__LOCATION"          | "valid location"    | "valid results"                              |
      | "BUY__LANDMARK"          | "valid landmark"    | "valid results"                              |
      | "BUY__BUILDING"          | "valid building"    | "valid results"                              |
      | "BUY__DEVELOPER"         | "valid developer"   | "valid results"                              |
      | "BUY__"                  | "invalid text"      | "error_message__Oops! No suggestions found." |
      | "RENT__LOCATION"         | "valid location"    | "valid results"                              |
      | "RENT__LANDMARK"         | "valid landmark"    | "valid results"                              |
      | "RENT__BUILDING"         | "valid building"    | "valid results"                              |
      | "RENT__"                 | "invalid text"      | "error_message__Oops! No suggestions found." |
      | "PG & HOSTELS__LOCATION" | "valid location"    | "valid results"                              |
      | "PG & HOSTELS__LANDMARK" | "valid landmark"    | "valid results"                              |
      | "PG & HOSTELS__"         | "invalid text"      | "error_message__Oops! No suggestions found." |
      | "HOME LOANS__"           | "all valid options" | "valid offers"                               |
      | "RENTAL AGREEMENTS"      | "valid city"        | "agreement details"                          |

  #==================================================================================
  Scenario Outline: HOUSING Property searching result information validation - Buy property
    When HOUSING User performs valid search to buy a property with default parameters
    Then HOUSING Search result information from <search result information item check list for buy property> should be shown for type buy property
    And HOUSING Quit the test scenario

    Examples: 
      | search result information item check list for buy property                                                                                                              |
      | "drpdwn_highlight__Buy txt_box__Text entered"                                                                                                                           |
      | "tab__Filters __ labl__Budget __ labl__BHK __ chk_box__Under Construction __ chk_box__Ready to Move tab__More __ labl__Reset"                                           |
      | "General_options_tab_Filters_Budget__ labl__Available property price range __ txt_box__Min __ txt_box__Max"                                                             |
      | "General_options_tab_Filters_BHK__ tick_box__1 RK __ tick_box__1 BHK __ tick_box__2 BHK __ tick_box__3 BHK __ tick_box__3+ BHK"                                         |
      | "General_options_tab_Filters_Possession__ btn_radio__In 1 Year __ btn_radio__In 2 Years __ btn_radio__In 3 Years __ btn_radio__Beyond 3 Years"                          |
      | "General_options_tab_Filters_Age__ btn_radio__1 Year __ btn_radio__2 Years __ btn_radio__5 Years __ btn_radio__10 Years __ btn_radio__More than 10 Years"               |
      | "General_options_tab_More_Check_all_suboptions_items__ Property Type __ Amenities __ Bathrooms __ Listed By"                                                            |
      | "btn__Save Search labl__Quick Links lnk__Flats for Sale in __ General_options_NEARBY_LOCALITIES_Check_options_extsts_optional General_options_Promoted_properties"      |
      | "General_options_Sort_by_Check_options_extsts__ btn__Relevance __ btn__Price Low __ btn__Price High __ btn__Price sqft Low __ btn__Price sqft High __ btn__Newly Added" |
      | "General_options_matching_result_count_details__ labl__total results count btn__previous page btn__current page btn__next page"                                         |
      | "Property_options__ img__Thumbnail __ labl__Title __ labl__by group name __ labl__Short Address __ labl__Flat details __ btn__Shortlist icon __ btn__Contact person"    |
      | "Property_options__ labl___Property price __ lnk__EMI details __ btn__Sqft price __ btn__Possession details btn__Room bathroom details __ btn__Price age details"       |
      | "Property_preview_options__ img__Short pictures __ labl__Added on date __ labl__Title __ btn__Shortlist icon __ btn__Contact person __ labl__Short Address"             |
      | "Property_preview_options__ labl___Property price __ lnk__EMI details __ labl__BUILT UP AREA __ labl__AGE OF PROPERTY __ labl__Direction __ labl__FLOOR"                |
      | "Property_preview_options__ labl___Basic __ labl___Details __ labl___Amenities __ labl___Location __ labl___Contact Person __ btn__Close preview"                       |

  #==================================================================================
  Scenario Outline: HOUSING Property searching result information validation - Rent property
    When HOUSING User performs valid search to rent a property with default parameters
    Then HOUSING Search result information from <search result information item check list for rent property> should be shown for type rent property
    And HOUSING Quit the test scenario

    Examples: 
      | search result information item check list for rent property                                                                                                                                        |
      | "drpdwn_highlight__Rent txt_box__Text entered"                                                                                                                                                     |
      | "labl__Filters __ drp_dwn__Room count __ drp_dwn__Price range __ drp_dwn__Listed By __ drp_dwn__Restrictions __ drp_dwn__More __ labl__Reset __ btn__Save Search"                                  |
      | "btn__Map __ btn__List __ chk_box__Include nearby homes __ lnk__Found home count notification __ labl__Rent your property __ btn__Rent property"                                                   |
      | "General_options_tab_Filters_BHK__ tick_box__1 RK __ tick_box__1 BHK __ tick_box__2 BHK __ tick_box__3 BHK __ tick_box__3+ BHK"                                                                    |
      | "General_options_tab_Filters_Budget__ labl__Available property price range __ txt_box__Min __ txt_box__Max"                                                                                        |
      | "General_options_tab_Filters_Listed_By__ tick_box__Agents __ tick_box__Landlords"                                                                                                                  |
      | "General_options_tab_More_Check_all_suboptions_items__ Furnishing __ Property Type __ Amenities __  Date Added __ Availability __ Society Facilities __ Bathrooms __ Flat Facilities __ btn__Done" |
      | "General_options__ lnk__Area name Know more about Map icon __ tab__Result count tab__Shortlist icon __ drp_down__Sort By"                                                                          |
      | "General_options__ labl__total results count btn__previous page btn__current page btn__next page __ labl__Nearby localities"                                                                       |
      | "Map_options_check__ Main area highlight __ Found property pointers __ Property pointer hoover details __ Zoom in button __ Zoom out button"                                                       |
      | "Property_options__ img__Thumbnail __ labl__Title __ labl__Locality name __ labl__Short Address __ btn__Shortlist icon __ labl___Property rent price"                                              |
      | "Property_preview_options__ img__Short pictures __ labl__Verified property and subinfo __ tab__DETAILS and subinfo"                                                                                |
      | "Property_preview_options__ tab__AMENITIES and subinfo __ tab__COMMUTE and subinfo __ tab__LOCALITY and subinfo"                                                                                   |
      | "Property_preview_options__ btn__Contact Person __ btn__Add to Shortlist __ btn__Close preview"                                                                                                    |

  #==================================================================================
  Scenario Outline: HOUSING Property searching result information validation - PG and Hostels
    When HOUSING User performs valid search for PG and hostels with default parameters
    Then HOUSING Search result information from <search result information item check list for PG and Hostels> should be shown for type rent property
    And HOUSING Quit the test scenario

    Examples: 
      | search result information item check list for rent property                                                                                       |
      | "drpdwn_highlight__PG & Hostels txt_box__Text entered"                                                                                            |
      | "labl__Filters __ drp_dwn__Gender __ drp_dwn__Available for __ drp_dwn__Occupancy __ drp_dwn__More __ labl__Reset"                                |
      | "btn__Map __ btn__List __ lnk__Found PG count notification"                                                                                       |
      | "General_options_tab_Filters_Gender__ tick_box__Boys __ tick_box__Girls"                                                                          |
      | "General_options_tab_Filters_Budget__ labl__Available property price range __ txt_box__Min __ txt_box__Max"                                       |
      | "General_options_tab_Filters_Available_For__ tick_box__Students __ tick_box__Working Professional"                                                |
      | "General_options_tab_More_Check_all_suboptions_items__ Listed By __ Accommodation __ Food __ Facilities Available __ Meals Included __ btn__Done" |

  #==================================================================================
  Scenario Outline: HOUSING Property search End-To-End search scenario validation type first
    When HOUSING User performs valid search from <search type> and search case from <search case details type first> and validates result
    Then HOUSING Test result should be successful or log the error meessage
    And HOUSING Quit the test scenario

    Examples: 
      | search type    | search case details type first                                                                |
      | "BUY"          | "type_first_01 Select first search result and browse photos and contact person"               |
      | "RENT"         | "type_first_02 Select first search result and browse photos and contact person"               |
      | "PG & Hostels" | "type_first_03 Select first search result and browse photos and contact person"               |
      | "RENT"         | "type_first_04 Select first search result and browse photos and navigate back to home page"   |
      | "RENT"         | "type_first_05 Select first search result and browse photos and shortlist and contact person" |

  #==================================================================================
  Scenario Outline: HOUSING Property search End-To-End search scenario validation type second
    When HOUSING User performs valid search from <search type> and search case from <search case details type second> and validates result
    Then HOUSING Test result should be successful or log the error meessage
    And HOUSING Quit the test scenario

    Examples: 
      | search type    | search case details type second                                                                                               |
      | "BUY"          | "type_second_01 Filter search result by second budget range and addition of 2 BHK and select first result and contact person" |
      | "RENT"         | "type_second_02 Filter search result by second budget range and listed by all and select first result and contact person"     |
      | "PG & Hostels" | "type_second_03 Filter search result by all gender and all occupancy and select first result and contact person"              |
      | "RENT"         | "type_second_04 Filter search result by any argument confirm search results and clear the filter list"                        |

  #==================================================================================
  Scenario Outline: HOUSING Property search End-To-End search scenario validation type third
    When HOUSING User performs valid search from <search type> and search case from <search case details type third> and validates result
    Then HOUSING Test result should be successful or log the error meessage
    And HOUSING Quit the test scenario

    Examples: 
      | search type    | search case details type third                                                                                        |
      | "BUY"          | "type_third_01 Without any filter sort results by Low Price and select first result and contact person"               |
      | "BUY"          | "type_third_02 Without any filter sort results by Newely Added and select first result and contact person"            |
      | "RENT"         | "type_third_03 Without any filter sort results by Date Added and select first result and contact person"              |
      | "RENT"         | "type_third_04 Without any filter sort results by Date Price(high to low) and select first result and contact person" |
      | "PG & Hostels" | "type_third_03 Without any filter sort results by Date Added and select first result and contact person"              |
      | "PG & Hostels" | "type_third_04 Without any filter sort results by Date Price(high to low) and select first result and contact person" |

  #==================================================================================
  Scenario Outline: HOUSING User profile and user managemennt validation
    When HOUSING User validates user management case from <user management case list>
    Then HOUSING Test result should be successful or log the error meessage
    And HOUSING Quit the test scenario

    Examples: 
      | user management case list                                           |
      | "Sign_up__ with dummy users and dummy details"                      |
      | "Sign_in__ with pre registered user and sign out"                   |
      | "Edit_profile__ update few details and conform __ forget password " |

  #==================================================================================
  Scenario Outline: HOUSING Specific other items validation
    When HOUSING User validates specific other items from <HOUSING specific other items list>
    Then HOUSING Test result should be successful or log the error meessage
    And HOUSING Quit the test scenario

    Examples: 
      | HOUSING specific other items list  |
      | "See all shortlisted properties"   |
      | "LIST YOUR PROPERTY Rent"          |
      | "LIST YOUR PROPERTY Sell"          |
      | "LIST YOUR PROPERTY Paying Guests" |
      | "Give us your feedback"            |

  #==================================================================================
  Scenario Outline: HOUSING Consistancy of elements across pages validation
    When HOUSING User navigates between different pages by selecting different options from <HOUSING navigation case list>
    And HOUSING User validates consistancy of common web elements "btn__Home __  lnk__DOWNLOAD APP __ lnk__LIST YOUR PROPERTY"
    And HOUSING User validates consistancy of common web elements "lnk__BLOG img__Shortlisted property __ lnk__LOGIN __ lnk__MENU"
    Then HOUSING Test result should be successful or log the error meessage
    And HOUSING Quit the test scenario

    Examples: 
      | HOUSING navigation case list |
      | "navigate_01 Buy property"  |
      | "navigate_02 Rent property" |
      | "navigate_03 PG & Hostels"  |

  #==================================================================================
  @homepageother
  Scenario Outline: HOUSING Home page functionality other items validation
    When HOUSING User validates home page other attribute from <home page other attribute list> with <expected other attribute value list>
    Then HOUSING Test result should be successful or log the error meessage
    And HOUSING Quit the test scenario

    Examples: 
      | home page other attribute list | expected other attribute value list |
      | "Careers"                      | "url__Careers"                      |
      | "About Us"                     | "url__About Us"                     |
      | "Contact Us"                   | "url__Contact Us"                   |
      | "Blog"                         | "url__Blog"                         |
      | "Blog"                         | "url__Data Sciences"                |
