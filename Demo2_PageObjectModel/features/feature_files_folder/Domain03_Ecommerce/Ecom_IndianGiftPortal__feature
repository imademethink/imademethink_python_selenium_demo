@ecommerce @desktop @igp
Feature: Ecommerce website validation - IndianGiftPortal

  Background: IndianGiftPortal.com website functionality validation
    Given Init "firefox" browser
    Given IndianGiftPortal website under test "http://www.indiangiftportal.com" and short name is "igp"

  #==================================================================================
  Scenario Outline: IndianGiftPortal Gift purchase End-To-End scenario validation type first
    Given IndianGiftPortal Item to search is <item name> as available from excel or db
    When IndianGiftPortal User validates end to end item purchase case type first from <case list type first>
    Then IndianGiftPortal Test result should be successful or log the error meessage
    And igp Quit the test scenari8o

    Examples: 
      | item name           | case list type first                                                                                                     |
      | "Handpicked Gifts"  | "type_first_01 Select first search result with non out of stock item and and enter user details and continue to payment" |
      | "Cakes"             | "type_first_02 Select first search result and select item and add to cart and remove the same"                           |
      | "Educational Games" | "type_first_03 Select item from search history and and enter user details and continue to payment"                       |

  #==================================================================================
  # IndianGiftPortal Gift purchase End-To-End scenario validation type second - NA
  #==================================================================================
  Scenario Outline: IndianGiftPortal Gift purchase End-To-End scenario validation type third
    Given IndianGiftPortal Item to search is <item name> as available from excel or db
    When IndianGiftPortal User validates end to end item purchase case type third from <case list type third>
    Then IndianGiftPortal Test result should be successful or log the error meessage
    And igp Quit the test scenari8o

    Examples: 
      | item name          | case list type third                                                                                           |
      | "Cool Gifts"       | "type_third_01 Without any filter sort results by Popularity and purchase first item until payment section"    |
      | "Cool Accessories" | "type_third_02 Without any filter sort results by Discounts and purchase first item until payment section"     |
      | "Nautical Gifts"   | "type_third_03 Without any filter sort results by Price Low to High purchase first item until payment section" |
      | "Photo Frames"     | "type_third_04 Without any filter sort results by Price High to Low purchase first item until payment section" |

  #==================================================================================
  Scenario Outline: IndianGiftPortal Gift purchase End-To-End scenario validation type fourth
    Given IndianGiftPortal Item to search is <item name> as available from excel or db
    When IndianGiftPortal User validates end to end item purchase case type fourth from <case list type fourth>
    Then IndianGiftPortal Test result should be successful or log the error meessage
    And igp Quit the test scenari8o

    Examples: 
      | item name           | case list type fourth                                                                                                            |
      | "Gifts For Husband" | "type_fourth_03 Select first search result and select any seat and try to purchase the item after timeout period of ten minutes" |
      | "Gift Vouchers"     | "type_fourth_04 Sign in and select any search result and book any item with any combination until payment section"               |

  #==================================================================================
  Scenario Outline: IndianGiftPortal Generic item search menu navigation scenario validation
    When IndianGiftPortal User invokes to <category_1>
    When IndianGiftPortal User invokes to <category_2>
    When IndianGiftPortal User validates if available products are non empty
    When IndianGiftPortal User searches for sample products from <sample product>
    Then IndianGiftPortal Test result should be successful or log the error meessage
    And igp Quit the test scenari8o

    Examples: 
      | category_1           | category_2        | sample product                            |
      | "Flowers"            | "Bunches"         | "Lovely Red Roses"                        |
      | "Jewelery"           | "Rings"           | "Diamond Ring"                            |
      | "Electronics"        | "Car Accesseries" | "Univesal Car Mount Holder"               |
      | "Birtday"            | "Cakes"           | "Round Chocolate Cake"                    |
      | "Anniversary"        | "Perfumes"        | "Body Women"                              |
      | "Wedding"            | "Jewelery Boxes"  | "Multi Tiered Multipurpose Jewellery Box" |
      | "Gifts For Him"      | "Shirts"          | "Van Heusen Gentleman"                    |
      | "Gifts for Her"      | "Pearl"           | "Oval Blue Choker"                        |
      | "Gifts For Kids"     | "Dolls"           | "Robin Hood"                              |
      | "Personalised Gifts" | "Laptop Skins"    | "Friends For Lifetime"                    |

  #==================================================================================
  Scenario Outline: IndianGiftPortal Generic item search from search text box scenario validation
    Given IndianGiftPortal User searches for popular item from <item name>
    When IndianGiftPortal User searches for popular item with exact name from <exact item name>
    When IndianGiftPortal User searches for popular item with relative matching name from <relative item names>
    When IndianGiftPortal User searches for popular item with relative matching name from <relative item names> using auto suggest NA
    When IndianGiftPortal User searches for popular item with exact matching name from <exact item name> using auto suggest NA
    When IndianGiftPortal User searches for popular item with relative matching name from <relative item names> using search history
    When IndianGiftPortal User searches for popular item with exact matching name from <exact item name> using search history
    Then IndianGiftPortal Test result should be successful or log the error meessage
    And igp Quit the test scenari8o

    Examples: 
      | item name                       | exact item name                          | relative item names                                                     |
      | "Anniversary __ Greeting Cards" | "A New Life Togethereness Card"          | "anniversary gift card __ anniversary card __ wedding annivarsary card" |
      | "Wedding __ Flowers"            | "Assorted Rose Bunch"                    | "rose bunch __ rose bookey __ bookey with rose __ red rose bookey"      |
      | "Birthday __ Cakes"             | "Black Forest Gateau"                    | "black forest cake __ forest cakes __ black cake"                       |
      | "Gifts For Him __ Cool Gifts"   | "Surprise Pillow"                        | "Indian pillow __ his pillow __ fantacy pillow"                         |
      | "Gifts For Her __ Handbag"      | "Animal Printed Side Bag"                | "side bag __ ethenic bag __ multicolour ide bag"                        |
      | "Gifts For Kids __ Planes"      | "Super Jumbo -747"                       | "jumbo jet __ jet plane __ airplenes"                                   |
      | "Personalised Gifts __ Crystal" | "Personalized Heart Shape Laser Crystal" | "crystal heart __ love crystal __ awesome crystal"                      |

  #==================================================================================
  Scenario Outline: IndianGiftPortal Generic item search result scenario validation
    Given IndianGiftPortal User searches for popular item from <item name>
    When IndianGiftPortal User scrables <item name> and validates empty search result
    When IndianGiftPortal User searches for <item name> and validates search result for short product details
    When IndianGiftPortal User searches for <item name> and validates search result for full product details using individual navigation
    When IndianGiftPortal User searches for <item name> and validates similar products are shown
    When IndianGiftPortal User searches for <item name> and validates recommended products are shown
    Then IndianGiftPortal Test result should be successful or log the error meessage
    And igp Quit the test scenari8o

    Examples: 
      | item name                       |
      | "Anniversary __ Greeting Cards" |
      | "Wedding __ Flowers"            |
      | "Birthday __ Cakes"             |
      | "Gifts For Him __ Cool Gifts"   |
      | "Gifts For Her __ Handbag"      |
      | "Gifts For Kids __ Planes"      |
      | "Personalised Gifts __ Crystal" |

  #==================================================================================
  Scenario Outline: IndianGiftPortal Generic shopping cart scenario validation
    When IndianGiftPortal User performs action_1 <action1__item name__quantity>
    When IndianGiftPortal User performs action_2 <action1__item name__quantity>
    When IndianGiftPortal User searches for <item name> and validates search result for full product details using individual navigation
    When IndianGiftPortal User searches for <item name> and validates similar products are shown
    When IndianGiftPortal User searches for <item name> and validates recommended products are shown
    Then IndianGiftPortal Test result should be successful or log the error meessage
    And igp Quit the test scenari8o

    Examples: 
      | action1__item name__quantity             | action2__item name__quantity                | action3__item name__quantity        |
      | "add __ Anniversary Greeting Cards __ 1" | "NA"                                        | "NA"                                |
      | "add __ Anniversary Greeting Cards __ 5" | "remove __ Anniversary Greeting Cards __ 3" | "add __ Wedding Flowers __ 2"       |
      | "add __ Anniversary Greeting Cards __ 5" | "remove __ Anniversary Greeting Cards __ 3" | "remove all"                        |
      | "add __ Birthday Cakes __ exceed"        | "NA"                                        | "NA"                                |
      | "add __ Gifts For Kids Planes __ 1"      | "remove all"                                | "add __ Gifts For Kids Planes __ 1" |
      | "add __ Personalised Gifts Crystal __ 1" | "add __ Gifts For Her Handbag __ 1"         | "check details"                     |
      | "add __ Laptop Skins __ 5"               | "add __ Laptop Skins __ 2"                  | "NA"                                |
