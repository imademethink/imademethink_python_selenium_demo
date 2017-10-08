@moneyrecharge @desktop @rechargeitnow
Feature: Money recharge website validation - RechargeItNow

  Background: RechargeItNow website functionality validation
    Given Init "firefox" browser
    Given RechargeItNow website under test "http://www.rechargeitnow.com" and short name is "RIN"

  #==================================================================================
  @homepage
  Scenario Outline: RechargeItNowHome Home page functionality, look-n-feel validation
    When RechargeItNowHome User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then RechargeItNowHome Test result should be successful or log the error meessage
    And RIN Quit the test scenario

    Examples: 
      | home page attribute list       | expected attribute value list                                                                                               |
      | "home page URL"                | "http://www.rechargeitnow.com"                                                                                              |
      | "home page title"              | "Online Mobile Recharge-Vodafone,Idea,Airtel,Aircel,Reliance,BSNL Mobile Recharge,Tata Sky,DishTV,DTH & Data Card Recharge" |
      | "home page logo"               | "default home page logo"                                                                                                    |
      | "home page loading time"       | "general home page loading time"                                                                                            |
      | "important home page elements" | "mobile dth data"                                                                                                           |
      | "pop up"                       | "no_popup __ no_screenshot"                                                                                             |
      | "home button"                  | "home button image or link"                                                                                                 |
      | "sign up"                      | "sign up link"                                                                                                              |
      | "sign in"                      | "sign in link"                                                                                                              |
      | "social plugin facebook"       | "social plugin facebook"                                                                                                    |
      | "social plugin twitter"        | "social plugin twitter"                                                                                                     |
      | "home page web elements"       | "all elements __ all frames"                                                                                                |
      | "home page other"              | "NA"                                                                                                                        |

  #==================================================================================
  Scenario Outline: RechargeItNow all individual mobile operator direct recharge
    When RechargeItNow User selects <mobile service provider> from service providers list
    And RechargeItNow User enters mobile number of <circle mobile number>
    And RechargeItNow User enter direct amount "100" for <circle mobile number> to recharge and continue as guest
    And RechargeItNow User selects "simple" payment method
    Then RechargeItNow Corresponding payment method "simple" home page to be shown

    Examples: 
      | mobile service provider | circle mobile number |
      | "Idea"                  | "9822012345"         |
      | "MTNL Mumbai"           | "9869012345"         |
      | "Tata Walky"            | "9212121272"         |
      | "Videocon Mobile"       | "9074056789"         |
      | "AirCel"                | "9716012345"         |
      | "BSNL"                  | "9434024365"         |
      | "Reliance GSM"          | "7305008999"         |
      | "Vodafone"              | "9609060092"         |

  #==================================================================================
  Scenario Outline: RechargeItNow all individual mobile operator recharge from plan
    When RechargeItNow User selects <mobile service provider> from service providers list
    And RechargeItNow User enters mobile number of <circle mobile number>
    And RechargeItNow User choose to select first option from <plan type> from available plans for <circle mobile number>
    And RechargeItNow User selects "simple" payment method
    Then RechargeItNow Corresponding payment method "simple" home page to be shown

    Examples: 
      | mobile service provider | circle mobile number | plan type        |
      | "Idea"                  | "9822012345"         | "All"            |
      | "MTNL Mumbai"           | "9869012345"         | "Topup"          |
      | "Videocon Mobile"       | "9074056789"         | "Full Talk Time" |
      | "AirCel"                | "9716012345"         | "Full Talk Time" |
      | "BSNL"                  | "9434024365"         | "Topup"          |
      | "Reliance GSM"          | "7305008999"         | "Topup"          |
      | "Vodafone"              | "9609060092"         | "All"            |

  #==================================================================================
  Scenario Outline: RechargeItNow all individual mobile data recharge from plan or direct
    When RechargeItNow User opens sub home page for "data" on "RIN" portal
    And RechargeItNow User selects <mobile service provider> from service providers list
    And RechargeItNow User enters mobile number of <circle mobile number>
    And RechargeItNow User choose to select first data recharge option from <plan type> from available plans for <circle mobile number> for <mobile service provider>
    And RechargeItNow User selects "simple" payment method
    Then RechargeItNow Corresponding payment method "simple" home page to be shown

    Examples: 
      | mobile service provider | circle mobile number | plan type      |
      | "Idea"                  | "9822012345"         | "Netsetter"    |
      | "Idea"                  | "9822054321"         | "3G Netsetter" |
      | "Vodafone"              | "9609060092"         | "3G Data Card" |
      | "Vodafone"              | "9609060092"         | "2G Data Card" |

  #==================================================================================
  Scenario Outline: RechargeItNow all individual dth service provider direct recharge
    When RechargeItNow User opens sub home page for "dth" on "RIN" portal
    And RechargeItNow User selects <dth service provider> from dth service providers list
    And RechargeItNow User enters dth subscriber number <subscriber number>
    And RechargeItNow User enter direct amount "1000" for <subscriber number> to recharge dth and continue as guest
    And RechargeItNow User selects "simple" payment method
    Then RechargeItNow Corresponding payment method "simple" home page to be shown

    Examples: 
      | dth service provider  | subscriber number |
      | "Videocon D2H"        | "107777977"       |
      | "Airtel Digital TV"   | "3096325874"      |
      | "Tata Sky"            | "1098765432"      |
      | "Reliance Digital TV" | "207894556123"    |

  #==================================================================================
  Scenario Outline: RechargeItNow all individual dth service provider recharge from plan
    When RechargeItNow User opens sub home page for "dth" on "RIN" portal
    And RechargeItNow User selects <dth service provider> from dth service providers list
    And RechargeItNow User enters dth subscriber number <subscriber number>
    And RechargeItNow User choose to select first option from <dth plan type> from available dth plans for <subscriber number>
    And RechargeItNow User selects "simple" payment method
    Then RechargeItNow Corresponding payment method "simple" home page to be shown

    Examples: 
      | dth service provider  | subscriber number | dth plan type   |
      | "DishTV"              | "01507999840"     | "12 Months"     |
      | "Videocon D2H"        | "107777977"       | "Super Gold"    |
      | "Airtel Digital TV"   | "3096325874"      | "Value Prime"   |
      | "Tata Sky"            | "1098765432"      | "South Special" |
      | "Reliance Digital TV" | "207894556123"    | "Bronze"        |

  #==================================================================================
  Scenario Outline: RechargeItNow all individual mobile operator post paid bill pay
    When RechargeItNow User opens sub home page for "postpaid bill pay" on "RIN" portal
    And RechargeItNow User selects <mobile service provider> from service providers list for postpaid
    And RechargeItNow User enters mobile number of <circle mobile number>
    And RechargeItNow User enter direct amount "1000" to pay post paid bill and continue as guest
    And RechargeItNow User selects "simple" payment method
    Then RechargeItNow Corresponding payment method "simple" home page to be shown

    Examples: 
      | mobile service provider | circle mobile number |
      | "Idea"                  | "9822012345"         |
      | "AirCel"                | "9716012345"         |
      | "Reliance GSM"          | "7305008999"         |

  #==================================================================================
  Scenario Outline: RechargeItNow all payment method validation
    When RechargeItNow From home page user selects any quick recharge case
    And RechargeItNow User selects <main payment method> and later <sub payment method> from list
    Then RechargeItNow Corresponding <main payment method> and <sub payment method> home page to be shown

    Examples: 
      | main payment method | sub payment method         |
      | "netbanking"        | "Axis Bank"                |
      | "netbanking"        | "Bank of India"            |
      | "netbanking"        | "HDFC Bank"                |
      | "netbanking"        | "ICICI Bank"               |
      | "netbanking"        | "ING Vysya Bank "          |
      | "netbanking"        | "Citi Bank Account Online" |
      | "netbanking"        | "Karnataka Bank"           |
      | "debit card"        | "Andhra Bank Debit Card"   |
      | "debit card"        | "Rupay Debit Card"         |
      | "debit card"        | "Canara Bank Debit Card"   |
      | "credit card"       | "Master Credit Card"       |
      | "credit card"       | "VISA Credit Card"         |
      | "PayUMoney"         | "Credit Card"              |
      | "PayUMoney"         | "Debit Card"               |
      | "PayUMoney"         | "Net Banking"              |
      | "imps"              | "Axis Bank"                |
      | "imps"              | "Canara Bank"              |
      | "imps"              | "Federal Bank"             |
      | "imps"              | "Kotak Mahindra Bank"      |
      | "imps"              | "Punjab National Bank"     |
      | "imps"              | "Yes Bank"                 |
      | "imps"              | "Bank of Baroda"           |
      | "imps"              | "Andhra Bank"              |

  #==================================================================================
  Scenario Outline: RechargeItNow mobile recharge using home page button
    When RechargeItNow User clicks on <mobile service provider button> from mobile service providers button list for "RIN"
    Then RechargeItNow URL of resulting page should contain <mobile service provider button> text

    Examples: 
      | mobile service provider button |
      | "AirCel"                       |
      | "AirTel"                       |
      | "BSNL"                         |
      | "Tata-Docomo"                  |
      | "Idea"                         |
      | "TataIndicom"                  |
      | "MTNL-Delhi"                   |
      | "MTNL-Mumbai"                  |
      | "MTS"                          |
      | "Reliance CDMA"                |
      | "Reliance-GSM"                 |
      | "T24"                          |
      | "Telenor"                      |
      | "Videocon Mobile"              |
      | "Vodafone"                     |

  #==================================================================================
  Scenario Outline: RechargeItNow dth recharge using home page button
    When RechargeItNow User clicks on <dth service provider button> from dth service providers button list for "RIN"
    Then RechargeItNow URL of resulting page should contain <dth service provider button> text

    Examples: 
      | dth service provider button |
      | "Airtel"                    |
      | "DishTV"                    |
      | "Reliance-Digital"          |
      | "Sun-Direct"                |
      | "TataSky"                   |
      | "Videocon-D2H"              |

  #==================================================================================
  Scenario Outline: RechargeItNow data card recharge using home page hyperlink
    When RechargeItNow User clicks on <data service provider hyperlink> from data service providers hyperlink list for "RIN"
    Then RechargeItNow URL of resulting page should contain <data service provider hyperlink> text

    Examples: 
      | data service provider hyperlink |
      | "Aircel"                        |
      | "Aircel-3G"                     |
      | "Airtel-2G"                     |
      | "Vodafone"                      |
      | "Vodafone-3G"                   |
      | "BSNL-3G"                       |
      | "Idea-2G"                       |
      | "MTNL-Mumbai"                   |
      | "MTNL-3G"                       |
      | "Reliance-CDMA-2G"              |
      | "T24"                           |
      | "Tata-Indicom-Delhi"            |

  #==================================================================================
  Scenario Outline: RechargeItNow post paid bill pay using home page hyperlink
    When RechargeItNow User clicks on <post paid mobile service provider hyperlink> from post paid mobile service provider hyperlink list for "RIN"
    Then RechargeItNow URL of resulting page should contain <post paid mobile service provider hyperlink> text

    Examples: 
      | post paid mobile service provider hyperlink |
      | "Airtel"                                    |
      | "Aircel"                                    |
      | "Vodafone"                                  |
      | "BSNL"                                      |
      | "Idea"                                      |
      | "Reliance CDMA"                             |
      | "Reliance GSM"                              |
      | "Tata Docomo CDMA"                          |
      | "Tata Docomo GSM"                           |
      | "Tata Indicom Delhi"                        |

  #==================================================================================
  Scenario Outline: RechargeItNow home page other attraction page validation
    When RechargeItNow User clicks on <other attraction page link> from home page for "RIN"
    And RechargeItNow User validates <particular attribute> on resulting other attraction page
    Then RechargeItNow User logs result for RIN home page in common format

    Examples: 
      | other attraction page link         | particular attribute                                        |
      | "Get FREE Recharge"                | "First company offer"                                       |
      | "Refer a Friend Win Free Recharge" | "Refer A Friend section page"                               |
      | "Awards & Recognition"             | "Awards & Recognition page"                                 |
      | "Discount Coupon"                  | "Just Added, Food, Shopping, Travel, Entertainment, Others" |

  #==================================================================================
  Scenario Outline: RechargeItNow home page other items validation
    When RechargeItNow User clicks on <home page other item link> from non home page list for "RIN"
    And RechargeItNow User validates <home page other item url> with <particular attribute> on resulting non home page for "RIN"
    Then RechargeItNow User logs result for RIN home page other item in html format

    Examples: 
      | home page other item link | home page other item url | particular attribute             |
      | "About Us"                | "about-us"               | "About Us section"               |
      | "Service"                 | "service"                | "Service section"                |
      | "Refund Policy"           | "refund-policy"          | "Refund Policy section"          |
      | "Plan and Scheme"         | "plan-and-Scheme"        | "Prepaid Plan & Schemes section" |
      | "Disclaimer"              | "disclaimer"             | "Disclaimer section"             |
      | "Terms of Usage"          | "term-and-condition"     | "Terms of Usage section"         |
      | "Contact Us"              | "contactus"              | "Open Support Ticket section"    |
      | "How to Use"              | "how-to-use"             | "How to Use section"             |
      | "Coupons"                 | "coupon"                 | "Coupons section"                |
      | "Faq"                     | "faq"                    | "Faq section"                    |
      | "Sitemap"                 | "sitemap"                | "Sitemap section"                |
      | "Privacy Policy"          | "privacy-policy"         | "Privacy Policy section"         |

  #==================================================================================
  Scenario: RechargeItNow user profile management validation - Sign Up
    When RechargeItNow User click on join hyperlink and enters sample details without captcha and submits the form for "RIN"
    Then RechargeItNow Following error to be shown "characters do not match please retry" during signup for "RIN"

  #==================================================================================
  Scenario: RechargeItNow user profile management validation - Sign In
    When RechargeItNow User click on login hyperlink and enters sample details to login for "RIN"
    Then RechargeItNow User should be logged in with user name shown on home page for "RIN"
    When RechargeItNow User click on sign out hyperlink for "RIN"
    Then RechargeItNow User should be logged out and no user name should be shown on home page for "RIN"

  #==================================================================================
  Scenario: RechargeItNow user profile management validation - My Account
    When RechargeItNow User click on my account button and enters sample details to login for "RIN"
    And RechargeItNow User changes profile paramaters and saves it for "RIN"
    Then RechargeItNow Changes saved should reflect in user profile for "RIN"

  #==================================================================================
  Scenario Outline: RechargeItNow Sign In using Social plugin
    When RechargeItNow User click on <social plugin> and login using sample credential
    And RechargeItNow User validates username shown on home page for <social plugin>
    And RechargeItNow User logouts from corresponding <social plugin> website separately
    And RechargeItNow User logouts from RIN
    Then RechargeItNow No username should be shown on RIN homepage

    Examples: 
      | social plugin |
      | "facebook"    |
      | "googleplus"  |
      | "yahoo"       |

  #================================================================
  Scenario: RechargeItNow  user profile management validation - Forget Password
    When RechargeItNow User click on forget password hyperlink and enters sample details without captcha
    Then RechargeItNow Following error to be shown "characters do not match. please retry" on RIN
