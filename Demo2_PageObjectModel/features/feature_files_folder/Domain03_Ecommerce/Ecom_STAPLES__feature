@ecommerce @desktop @STAPLES
Feature: Ecommerce website validation - STAPLES

  Background: STAPLES.com website functionality validation
    Given Init "firefox" browser
    Given STAPLES website under test "http://www.staples.com" and short name is "STAPLES"

  #==================================================================================
  Scenario Outline: STAPLES Stationary purchase End-To-End scenario validation type first
    Given STAPLES Item to search is <item name> as available from excel or db
    When STAPLES User validates end to end item purchase case type first from <case list type first>
    Then STAPLES Test result should be successful or log the error meessage
    And STAPLES Quit the test scenari8o

    Examples: 
      | item name               | case list type first                                                                                                 |
      | "Multipurpose Paper"    | "type_first_01 Select first search result with non out of stock item and enter user details and continue to payment" |
      | "Scrapbooking Scissors" | "type_first_02 Select first search result and select item and add to cart and remove the same"                       |
      | "Lamps & Lighting"      | "type_first_03 Select item from search history and and enter user details and continue to payment"                   |

  #==================================================================================
  Scenario Outline: STAPLES Stationary purchase End-To-End scenario validation type second
    Given STAPLES Item to search is <item name> as available from excel or db
    When STAPLES User validates end to end purchase item case type second from <case list type second>
    Then STAPLES Test result should be successful or log the error meessage
    And STAPLES Quit the test scenari8o

    Examples: 
      | item name              | case list type second                                                                                                                                  |
      | "Accent Lighting"      | "type_second_01 Filter search result by first brand name among the list and select first result and purchase item until payment section"               |
      | "Condiments"           | "type_second_02 Filter search result by rating option and brand option and select first result among the list and purchase item until payment section" |
      | "Home & Office Tables" | "type_second_03 Filter search result by any argument confirm search results and clear the filter list"                                                 |

  #==================================================================================
  Scenario Outline: STAPLES Gift purchase End-To-End scenario validation type third
    Given STAPLES Item to search is <item name> as available from excel or db
    When STAPLES User validates end to end purchase item case type third from <case list type third>
    Then STAPLES Test result should be successful or log the error meessage
    And STAPLES Quit the test scenari8o

    Examples: 
      | item name            | case list type third                                                                                                              |
      | "Optra S 1255"       | "type_third_01 Without any filter sort results by Name in ascending order and purchase item until payment section"                |
      | "HR & Medical Forms" | "type_third_02 Without any filter sort results by Name in decending order and purchase first purchase item until payment section" |
      | "Binders"            | "type_third_03 Without any filter sort results by Top Rating and purchase item until payment section"                             |
      | "Back Pillow"        | "type_third_04 Without any filter sort results by Best Matches and purchase first purchase item until payment section"            |
      | "Stapler"            | "type_third_05 Without any filter sort results by Price Low to High and purchase item until payment section"                      |
      | "Card Readers"       | "type_third_06 Without any filter sort results by Price High to Low and purchase item until payment section"                      |

  #==================================================================================
  Scenario Outline: STAPLES Gift purchase End-To-End scenario validation type fourth
    Given STAPLES Item to search is <item name> as available from excel or db
    When STAPLES User validates end to end purchase item case type fourth from <case list type fourth>
    Then STAPLES Test result should be successful or log the error meessage
    And STAPLES Quit the test scenari8o

    Examples: 
      | item name           | case list type fourth                                                                                                        |
      | "Binders"           | "type_fourth_03 Select first search result and select any seat and try to purchase item after timeout period of ten minutes" |
      | "Cameras & Sensors" | "type_fourth_04 Sign in and select any search result and purchase item with any combination until payment section"           |

  #==================================================================================
  Scenario Outline: STAPLES Generic item search menu navigation scenario validation
    When STAPLES User invokes to <category_1>
    When STAPLES User invokes to <category_2>
    When STAPLES User validates if available products are non empty
    When STAPLES User searches for sample products from <sample product>
    Then STAPLES Test result should be successful or log the error meessage
    And STAPLES Quit the test scenari8o

    Examples: 
      | category_1                      | category_2                          | sample product       |
      | "Shop By Catogery__Products"    | "Homewares and Appliances__Kitchen" | "Disposable Cutlery" |
      | "Shop By Catogery__Products"    | "Office Supplies__Lables"           | "Self-Adhesive"      |
      | "Shop By Catogery__Electronics" | "Software__Tax Sofware"             | "Turbo Tax"          |

  #==================================================================================
  Scenario Outline: STAPLES Generic item search from search text box scenario validation
    Given STAPLES User searches for popular item from <item name>
    When STAPLES User searches for popular item with exact name from <exact item name>
    When STAPLES User searches for popular item with relative matching name from <relative item names>
    When STAPLES User searches for popular item with relative matching name from <relative item names> using auto suggest
    When STAPLES User searches for popular item with exact matching name from <exact item name> using auto suggest
    When STAPLES User searches for popular item with relative matching name from <relative item names> using search history NA
    When STAPLES User searches for popular item with exact matching name from <exact item name> using search history NA
    Then STAPLES Test result should be successful or log the error meessage
    And STAPLES Quit the test scenari8o

    Examples: 
      | item name     | exact item name    | relative item names                                    |
      | "White Board" | "Dry-Erase Board"  | "white board __ meeting room board __ marker and bord" |
      | "Binder Clip" | "Mini Binder Clip" | "mini binder __ binder clip __ small clip"             |
      | "Trash Bag"   | "Trash bag"        | "trash bag __ dustbin bag __ plastic trash bag"        |
      | "Hand Gloves" | "Hand Gloves"      | "hand gloves __ exam gloves __ surgery gloves"         |
      | "Desks"       | "Desks"            | "office desk __ L shape school desk __ computer desk"  |

  #==================================================================================
  Scenario Outline: STAPLES Generic item search result scenario validation
    Given STAPLES User searches for popular item from <item name>
    When STAPLES User scrables <item name> and validates empty search result
    When STAPLES User searches for <item name> and validates search result for short product details
    When STAPLES User searches for <item name> and validates search result for full product details using individual navigation
    When STAPLES User searches for <item name> and validates similar products are shown
    When STAPLES User searches for <item name> and validates recommended products are shown
    Then STAPLES Test result should be successful or log the error meessage
    And STAPLES Quit the test scenari8o

    Examples: 
      | item name                                                                    |
      | "Techni Mobili Modern Computer Workstation"                                  |
      | "Parker Sonnet GT Fountain Pen, Medium Nib, Black"                           |
      | "Stalwart Plastic 41-Compartment Hardware Storage Box, Black"                |
      | "SafetyClean™ Disposable Lens Cleaning Station Wipe Pre-Moistened Towelette" |
      | "Xerox Black Toner Cartridge (6R244), 2/Pack"                                |
      | "Duracell DL2032 3 Volt Lithium Battery, 2/Pk"                               |

  #==================================================================================
  Scenario Outline: STAPLES Generic shopping cart scenario validation
    When STAPLES User performs action_1 <action1__item name__quantity>
    When STAPLES User performs action_2 <action1__item name__quantity>
    When STAPLES User searches for <item name> and validates search result for full product details using individual navigation
    When STAPLES User searches for <item name> and validates similar products are shown
    When STAPLES User searches for <item name> and validates recommended products are shown
    Then STAPLES Test result should be successful or log the error meessage
    And STAPLES Quit the test scenari8o

    Examples: 
      | action1__item name__quantity                                                                    | action2__item name__quantity                                                                     | action3__item name__quantity                                           |
      | "add __ Gift Shop __ Edible Gifts __ 1"                                                         | "NA"                                                                                             | "NA"                                                                   |
      | "add __ Paper & Stationery __ Novelty Paper Items __ 5"                                         | "remove __ Paper & Stationery __ Novelty Paper Items __ 3"                                       | "add __ Coffee, Water & Snacks __ Coffee __ 2"                         |
      | "add __ Coffee, Water & Snacks __ Disposable Cutlery __ 5"                                      | "remove __ Coffee, Water & Snacks __ Disposable Cutlery __ 3"                                    | "remove all"                                                           |
      | "add __ Shipping, Packing & Mailing Supplies __ Mailroom Equipment __ Utility Knives __ exceed" | "NA"                                                                                             | "NA"                                                                   |
      | "add __ Cleaning Supplies & Facilities Maintenance __ Trash Bags __ 1"                          | "remove all"                                                                                     | "add __ Cleaning Supplies & Facilities Maintenance __ Trash Bags __ 1" |
      | "add __ Arts & Crafts __ Arts & Crafts __ Crafts Storage __ 1"                                  | "add __ Arts & Crafts __ Arts & Crafts __ Lighting & Magnifiers __ 1"                            | "check details"                                                        |
      | "add __ Gift Shop __ Gift Sets, Photo & Custom Gifts __ Photo Gifts __ Custom Laptop Skins__ 5" | "add __ Gift Shop __ Gift Sets, Photo & Custom Gifts __ Photo Gifts __ Custom Laptop Skins __ 2" | "NA"                                                                   |
