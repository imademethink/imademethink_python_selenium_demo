@property @mobile @android @ios @HOUSINGmobile
Feature: Property mobile app validation - HOUSING

  Background: HOUSING mobile app functionality validation
    Given Init "selendroid" browser
    Given HOUSING mobapp under test is "HOUSING"

  #==================================================================================
  @homescreen
  Scenario Outline: HOUSING mobapp Home screen functionality, look-n-feel validation
    When HOUSING mobapp User validates home screen attribute from <home screen attribute list> with <expected attribute value list>
    Then HOUSING mobapp Test result should be successful or log the error meessage
    And HOUSING mobapp Quit the test scenario

    Examples: 
      | home screen attribute list       | expected attribute value list                                                                                                          |
      | "home screen title"              | "HOUSING"                                                                                                      |
      | "home screen logo"               | "default HOUSING logo at starting of app"                                                                                                                 |
      | "home screen loading time"       | "general home screen loading time"                                                                                                       |
      | "important home screen elements" | "icon__Home List My Property __ icon__User Account __ btn__My Shortlist __ btn__My Alerts" |
      | "important home screen elements" | "tab__BUY __ txtbox__Search by" |
      | "important home screen elements" | "lnk__Login Now __ lnk__Post My Property __ lnk__Help Us Improve" |
      | "pop up"                         | "no_popup __ no_screenshot"                                                                                                                    |
      | "home button"                    | "labl__HOUSING"                                                                                                                         |
      | "sign up"                        | "sign up link"                                                                                                                         |
      | "sign in"                        | "sign in link"                                                                                                                         |

  #==================================================================================
  Scenario Outline: HOUSING mobapp Property searching GUI options validation
    When HOUSING mobapp User validates property searching GUI options from <GUI options list> with <expected GUI options value>
    Then HOUSING mobapp Test result should be successful or log the error meessage
    And HOUSING mobapp Quit the test scenario

    Examples: 
      | GUI options list                          | expected GUI options value                                                                                   |
      | "BUY_section__ auto suggest"              | "auto suggest matching areas"                                                               |
      | "My Shortlist"                            | "btn__Close __ labl__SHORTLIST __ img__Shortlist __ btn__Facebook_SIGNIN __ btn__Google_SIGNIN" |
      | "My Alerts"                               | "btn__Close __ labl__GET ALERTS __ img__Alerts __ btn__Facebook_SIGNIN __ btn__Google_SIGNIN" |
      | "Login Now"                               | "btn__Close __ labl__YOUR KEYS AWAIT __ btn__Facebook_SIGNIN __ btn__Google_SIGNIN" |
      | "Login Now"                               | "slider_img__Housing __ slider_img__CHAT __ slider_img__GET ALERTS __ slider_img__SHORTLIST" |
      | "Post My Property"                        | "labl__List My Property __ btn_List a property to sell __ img__Property __ btn__Back arrow" |
      | "Post My Property List property to sell"  | "labl__Property Details __ txtbox__Locality Name __ txtbox__Address __ btn__NEXT __ btn__Back arrow" |
      | "Help Us Improve"                         | "labl__Contact us __ txtbox__Feedback __ txtbox__Name __ txtbox__Email __ txtbox__Phone __ btn__SUBMIT __ btn__Back arrow" |

  #==================================================================================
  Scenario Outline: HOUSING mobapp Property searching scenarions combination validation
    When HOUSING mobapp User validates search scenario for <search text> with <expected search scenario result>
    Then HOUSING mobapp Test result should be successful or log the error meessage
    And HOUSING mobapp Quit the test scenario

    Examples: 
	  | search text         | expected search scenario result              |
      | "valid location"    | "valid results"                              |
      | "invalid text"      | "No results"                                 |

  #==================================================================================
  Scenario Outline: HOUSING mobapp Property searching result option validation - Buy property
    When HOUSING mobapp User performs valid search to buy a property with default parameters
    Then HOUSING mobapp Search result option from <search result option item check list for buy property> should be shown for type buy property
    And HOUSING mobapp Quit the test scenario

    Examples: 
      | search result option item check list for buy property                                                                                                              |
      | "General_options__ txtbox__Searched text with auto suggest __ btn__FIND Properties" |
      | "BHKs__ tickbox__1RK __ tickbox__1BHK __ tickbox__2BHK __ tickbox__3BHK __ tickbox__4+BHK" |
      | "Cost__ labl__MIN COST __ labl__MAX COST __ slider_Left __ slider_Right" |
	  
  #==================================================================================
  Scenario Outline: HOUSING mobapp Property searching result information option validation - Buy property
    When HOUSING mobapp User performs valid search to buy a property with default parameters
    And HOUSING mobapp User selects default options among BHKs and price range
    Then HOUSING mobapp Search result information option from <search result information item check list for buy property> should be shown for type buy property
    And HOUSING mobapp Quit the test scenario

    Examples: 
      | search result information item check list for buy property                                                                                                              |
      | "General_options__ txtbox__Searched text with auto suggest __ labl__Search result count __ icon__Favorite" |
	  | "btn__FILTER __ btn__SORT __ btn__NOTIFY" |
	  | "General_options__ img__Property image __ labl__BHK count __ labl__Bedroom count __ labl__Locality name __ labl__Cost" |
	  | "General_options__ labl__Property area sqft __ labl__Lanfrate __labl__Property age __ icon__Individual property favorite" |
	  | "General_options__ labl__Featured Projects __ slider_img__Featured project" |
	  
  #==================================================================================
  Scenario Outline: HOUSING mobapp Property search End-To-End search scenario validation type first
    When HOUSING mobapp User performs valid search from <search type> and search case from <search case details type first> and validates result
    Then HOUSING mobapp Test result should be successful or log the error meessage
    And HOUSING mobapp Quit the test scenario

    Examples: 
      | search type    | search case details type first                                                                |
      | "BUY"          | "type_first_01 Select first search result and browse photos and contact person"               |
      | "BUY"          | "type_first_02 Select last search result and browse photos and contact person"               |
      | "BUY"          | "type_first_03 Select second search result and click on shortlist icon"               |

  #==================================================================================
  Scenario Outline: HOUSING mobapp Property search End-To-End search scenario validation type second
    When HOUSING mobapp User performs valid search from <search type> and search case from <search case details type second> and validates result
    Then HOUSING mobapp Test result should be successful or log the error meessage
    And HOUSING mobapp Quit the test scenario

    Examples: 
      | search type    | search case details type second                                                                                               |
      | "BUY"          | "type_second_01 Filter search result by Basic type and addition of 2 BHK and select first result and select contact person" |
      | "BUY"          | "type_second_02 Filter search result by Property type and select Under Construction all and select first result and contact person"     |
      | "BUY"          | "type_second_03 Filter search result by Developers type and check count of developers available"              |
      | "BUY"          | "type_second_04 Filter search result by Amenities and select all and unselect all"                        |

  #==================================================================================
  Scenario Outline: HOUSING mobapp Property search End-To-End search scenario validation type third
    When HOUSING mobapp User performs valid search from <search type> and search case from <search case details type third> and validates result
    Then HOUSING mobapp Test result should be successful or log the error meessage
    And HOUSING mobapp Quit the test scenario

    Examples: 
      | search type    	| search case details type third                                                                                        |
      | "BUY"          	| "type_third_01 Without any filter sort results by Low to High Price and get price of first property"               |
      | "BUY"          	| "type_third_02 Without any filter sort results by High to Low Price and click on picture of second property" |
      | "BUY"         	| "type_third_03 Without any filter sort results by Date Added and click on shortlist icon" |

  #==================================================================================
  Scenario Outline: HOUSING mobapp User profile and user managemennt validation
    When HOUSING mobapp User validates user management case from <user management case list>
    Then HOUSING mobapp Test result should be successful or log the error meessage
    And HOUSING mobapp Quit the test scenario

    Examples: 
      | user management case list                                           |
      | "Sign_up__ with dummy users and dummy details"                      |
      | "Sign_in__ with pre registered user and sign out"                   |
      | "Edit_profile__ update few details and conform __ forget password " |
