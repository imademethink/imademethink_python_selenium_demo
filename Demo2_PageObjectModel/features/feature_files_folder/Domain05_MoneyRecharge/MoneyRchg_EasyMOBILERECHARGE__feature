@moneyrecharge @desktop @easymoneyrecharge
Feature: Money recharge website validation - EASYMOBILERECHARGE

  Background: EASYMOBILERECHARGE.com functionality validation
    Given Init "firefox" browser
    Given EASYMOBILERECHARGE website under test "http://www.easymobilerecharge.com" and short name is "EMR"

  #==================================================================================
  @homepage
  Scenario Outline: EASYMOBILERECHARGE Home page functionality, look-n-feel validation
    When EASYMOBILERECHARGE User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then EASYMOBILERECHARGE Test result should be successful or log the error meessage
    And EASYMOBILERECHARGE Quit the test scenario

    Examples: 
      | home page attribute list       | expected attribute value list                 |
      | "home page URL"                | "http://www.easymobilerecharge.com"           |
      | "home page title"              | "Online Mobile Recharge"                      |
      | "home page logo"               | "default home page logo"                      |
      | "home page loading time"       | "general home page loading time"              |
      | "important home page elements" | "RechargeIt RECHARGENOW RECHAEGE (top right)" |
      | "pop up"                       | "no_popup __ no_screenshot"               |
      | "home button"                  | "home button image or link"                   |
      | "sign up"                      | "sign up link"                                |
      | "sign in"                      | "sign in link"                                |
      | "social plugin googleplus"     | "social plugin googleplus"                    |
      | "home page web elements"       | "all elements __ all frames"                  |
      | "home page other"              | "NA"                                          |

  #==================================================================================
  Scenario Outline: EASYMOBILERECHARGE all individual mobile operator direct recharge
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User selects <mobile service provider> from service providers list
    And EASYMOBILERECHARGE User enters mobile number of <circle mobile number>
    And EASYMOBILERECHARGE User selects <mobile circle name> from mobile circle list
    And EASYMOBILERECHARGE User selects "default" payment method
    And EASYMOBILERECHARGE User enter direct amount "100" for <circle mobile number> to recharge and continue as guest
    Then EASYMOBILERECHARGE Corresponding payment method "default" home page to be shown

    Examples: 
      | mobile service provider | circle mobile number | mobile circle name              |
      | "Idea"                  | "9822012345"         | "Maharashtra & Goa"             |
      | "MTNL Mumbai"           | "9869012345"         | "Mumbai"                        |
      | "Tata Walky"            | "9212121272"         | "Delhi & NCR"                   |
      | "Videocon Mobile"       | "9074056789"         | "MP & Chattisgarh"              |
      | "AirCel"                | "9716012345"         | "Delhi & NCR"                   |
      | "BSNL"                  | "9434024365"         | "West Bengal & Andaman Nicobar" |
      | "Reliance GSM"          | "7305008999"         | "Tamil Nadu"                    |
      | "Vodafone"              | "9609060092"         | "West Bengal & Andaman Nicobar" |

  #==================================================================================
  Scenario Outline: EASYMOBILERECHARGE all individual mobile operator recharge from plan
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User selects <mobile service provider> from service providers list
    And EASYMOBILERECHARGE User enters mobile number of <circle mobile number>
    And EASYMOBILERECHARGE User selects <mobile circle name> from mobile circle list
    And EASYMOBILERECHARGE User selects "default" payment method
    And EASYMOBILERECHARGE User choose to select first option from <plan type> from available plans for <circle mobile number> and continue as guest
    Then EASYMOBILERECHARGE Corresponding payment method "default" home page to be shown

    Examples: 
      | mobile service provider | circle mobile number | mobile circle name              | plan type  |
      | "Idea"                  | "9822012345"         | "Maharashtra & Goa"             | "Talktime" |
      | "MTNL Mumbai"           | "9869012345"         | "Mumbai"                        | "SMS"      |
      | "Videocon Mobile"       | "9074056789"         | "MP & Chattisgarh"              | "Local"    |
      | "AirCel"                | "9716012345"         | "Delhi & NCR"                   | "STD"      |
      | "BSNL"                  | "9434024365"         | "West Bengal & Andaman Nicobar" | "ISD"      |
      | "Reliance GSM"          | "7305008999"         | "Tamil Nadu"                    | "Talktime" |
      | "Vodafone"              | "9609060092"         | "West Bengal & Andaman Nicobar" | "ISD"      |

  #==================================================================================
  Scenario Outline: EASYMOBILERECHARGE all individual mobile data recharge from plan or direct
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User opens sub home page for "data" on "EMR" portal
    And EASYMOBILERECHARGE User selects <mobile service provider> from service providers list
    And EASYMOBILERECHARGE User enters mobile number of <circle mobile number>
    And EASYMOBILERECHARGE User selects <mobile circle name> from mobile circle list
    And EASYMOBILERECHARGE User choose to select first data recharge option from available plans for <circle mobile number>
    And EASYMOBILERECHARGE User selects "default" payment method
    Then EASYMOBILERECHARGE Corresponding payment method "default" home page to be shown

    Examples: 
      | mobile service provider | circle mobile number | mobile circle name |
      | "- MTNL -"              | "9869012345"         | "Mumbai"           |
      | "Reliance 2G/3G"        | "7305008999"         | "Tamil Nadu"       |
      | "MTS M Blaze"           | "9136155155"         | "Delhi & NCR"      |

  #==================================================================================
  Scenario Outline: EASYMOBILERECHARGE all individual dth service provider direct recharge
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User opens sub home page for "dth" on "EMR" portal
    And EASYMOBILERECHARGE User selects <dth service provider> from dth service providers list
    And EASYMOBILERECHARGE User enters dth <subscriber number> from subscriber number list
    And EASYMOBILERECHARGE User enter direct amount "1000" for <subscriber number> to recharge dth and continue as guest
    And EASYMOBILERECHARGE User selects "default" payment method
    Then EASYMOBILERECHARGE Corresponding payment method "default" home page to be shown

    Examples: 
      | dth service provider | subscriber number |
      | "Videocon D2H"       | "107777977"       |
      | "Airtel Digital TV"  | "3096325874"      |
      | "Tata Sky"           | "1098765432"      |
      | "Big TV"             | "207894556123"    |

  #==================================================================================
  Scenario Outline: EASYMOBILERECHARGE all payment method validation
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE From home page user selects any quick recharge case
    And EASYMOBILERECHARGE User selects <main payment method> and later <sub payment method> from list
    Then EASYMOBILERECHARGE Corresponding <main payment method> and <sub payment method> home page to be shown

    Examples: 
      | main payment method | sub payment method                         |
      | "Payumoney"         | "NA"                                       |
      | "Net Banking"       | "Axis Bank"                                |
      | "Net Banking"       | "State Bank of India"                      |
      | "Net Banking"       | "HDFC Bank"                                |
      | "Net Banking"       | "ICICI Bank"                               |
      | "Net Banking"       | "AXIS Bank"                                |
      | "Net Banking"       | "State Bank of Hyderabad"                  |
      | "Net Banking"       | "Union Bank of India"                      |
      | "Net Banking"       | "Andhra Bank"                              |
      | "Net Banking"       | "Bank of Bahrain & Kuwait"                 |
      | "Net Banking"       | "Bank of Baroda Corporate Accounts"        |
      | "Net Banking"       | "Bank of Baroda Retail Accounts"           |
      | "Net Banking"       | "Bank of India"                            |
      | "Net Banking"       | "Bank of Maharashtra"                      |
      | "Net Banking"       | "Canara Bank"                              |
      | "Net Banking"       | "Catholic Syrian Bank"                     |
      | "Net Banking"       | "Central Bank of India"                    |
      | "Net Banking"       | "Citibank Bank Account Online"             |
      | "Net Banking"       | "City Union Bank"                          |
      | "Net Banking"       | "Corporation Bank"                         |
      | "Net Banking"       | "DBS Bank"                                 |
      | "Net Banking"       | "Deutsche Bank"                            |
      | "Net Banking"       | "Development Credit Bank"                  |
      | "Net Banking"       | "Dhanlaxmi Bank"                           |
      | "Net Banking"       | "Federal Bank"                             |
      | "Net Banking"       | "Indian Bank"                              |
      | "Net Banking"       | "Indian Overseas Bank"                     |
      | "Net Banking"       | "IndusInd Bank"                            |
      | "Net Banking"       | "ING Vysya Bank"                           |
      | "Net Banking"       | "Jammu & Kashmir Bank"                     |
      | "Net Banking"       | "Karnataka Bank"                           |
      | "Net Banking"       | "Karur Vysya Bank"                         |
      | "Net Banking"       | "Kotak Mahindra Bank"                      |
      | "Net Banking"       | "Lakshmi Vilas Bank NetBanking"            |
      | "Net Banking"       | "Oriental Bank of Commerce"                |
      | "Net Banking"       | "Punjab National Bank Corporate Accounts"  |
      | "Net Banking"       | "Royal Bank of Scotland N.V."              |
      | "Net Banking"       | "Saraswat Bank"                            |
      | "Net Banking"       | "Shamrao Vithal Bank"                      |
      | "Net Banking"       | "South Indian Bank"                        |
      | "Net Banking"       | "Standard Chartered Bank"                  |
      | "Net Banking"       | "State Bank of Bikaner and Jaipur"         |
      | "Net Banking"       | "State Bank of Mysore"                     |
      | "Net Banking"       | "State Bank of Patiala"                    |
      | "Net Banking"       | "State Bank of Travancore"                 |
      | "Net Banking"       | "Syndicate Bank"                           |
      | "Net Banking"       | "Tamilnad Mercantile Bank"                 |
      | "Net Banking"       | "United bank of India"                     |
      | "Net Banking"       | "Vijaya Bank"                              |
      | "Net Banking"       | "YES Bank"                                 |
      | "Debit Card"        | "Andhra Bank Debit Card (ATM PIN)"         |
      | "Debit Card"        | "State Bank of India Debit Card (SBI)"     |
      | "Debit Card"        | "Canara Bank Debit Card (ATM PIN)"         |
      | "Debit Card"        | "Citibank Debit Card"                      |
      | "Debit Card"        | "Indian Overseas Bank Debit Card"          |
      | "Debit Card"        | "Union Bank of India Debit Card (ATM PIN)" |
      | "Debit Card"        | "Visa Debit Card of all other banks"       |
      | "Credit Card"       | "Visa Credit Card"                         |
      | "Credit Card"       | "Master Credit Card"                       |

  #==================================================================================
  Scenario Outline: EASYMOBILERECHARGE mobile recharge using home page hyperlink
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User clicks on <mobile service provider hyperlink> from mobile service providers hyperlink list for "EMR"
    Then EASYMOBILERECHARGE URL of resulting page should contain <mobile service provider hyperlink> text

    Examples: 
      | mobile service provider hyperlink |
      | "AirCel"                          |
      | "Hutch"                           |
      | "Idea"                            |
      | "TataIndicom"                     |
      | "Idea"                            |
      | "TataIndicom"                     |
      | "Reliance"                        |
      | "BSNL"                            |
      | "Loop"                            |
      | "Virgin-mobile"                   |
      | "Tata-Docomo"                     |
      | "Stel"                            |
      | "MTS"                             |
      | "Uninor"                          |
      | "Videocon"                        |

  #==================================================================================
  Scenario Outline: EASYMOBILERECHARGE home page other attraction page validation
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User clicks on <other attraction page link> from home page for "EMR"
    And EASYMOBILERECHARGE User validates <particular attribute> on resulting other attraction page
    Then EASYMOBILERECHARGE User logs result for EMR home page in common format

    Examples: 
      | other attraction page link   | particular attribute                              |
      | "Free Recharge"              | "First company offer view details"                |
      | "Free Coupons and Discounts" | "First cash back offer"                           |
      | "DTH Free Recharge"          | "Image, Terms & Condition, View All winners list" |

  #==================================================================================
  Scenario Outline: EASYMOBILERECHARGE home page other items validation
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User clicks on <home page other item link> from non home page list for "EMR"
    And EASYMOBILERECHARGE User validates <home page other item url> with <particular attribute> on resulting non home page for "EMR"
    Then EASYMOBILERECHARGE User logs result for EMR home page other item in html format

    Examples: 
      | home page other item link | home page other item url | particular attribute                                                                    |
      | "Order Status"            | "order-status"           | "9822012345, 500, Check status"                                                         |
      | "Win Free Recharge"       | "dth-free-recharge"      | "Image, Terms & Condition, View All winners list"                                       |
      | "About Us"                | "about_us"               | "About EasyMobileRecharge.com, email"                                                   |
      | "Contact Us"              | "contact_us"             | "Open Recharge Not Done ticket"                                                         |
      | "Terms of Usage"          | "term_condition"         | "Terms of Usage section"                                                                |
      | "Privacy Policy"          | "privacy_policy"         | "Privacy Policy section"                                                                |
      | "Disclaimer"              | "disclaimer"             | "Disclaimer section"                                                                    |
      | "Refund Policy"           | "refund-policy"          | "Refund Policy section"                                                                 |
      | "Blog"                    | "blog"                   | "Popup, Categories, Verify first blog,Poll section, Whats Hot section and put comments" |

  #==================================================================================
  Scenario: EASYMOBILERECHARGE user profile management validation - Sign Up
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User click on register hyperlink and enters sample details without captcha and submits the form for "EMR"
    Then EASYMOBILERECHARGE Following confirmation message to be shown "Your account is created. You can now login to use the recharge service." during signup for "EMR"

  #==================================================================================
  Scenario: EASYMOBILERECHARGE user profile management validation - Sign In
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User click on login hyperlink and enters sample details to login for "EMR"
    Then EASYMOBILERECHARGE User should be logged in with user name shown on home page for "EMR"
    When EASYMOBILERECHARGE User click on sign out hyperlink for "EMR"
    Then EASYMOBILERECHARGE User should be logged out and no user name should be shown on home page for "EMR"

  #==================================================================================
  Scenario: EASYMOBILERECHARGE user profile management validation - My Account
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User click on my account button and enters sample details to login for "EMR"
    And EASYMOBILERECHARGE User changes profile paramaters and saves it for "EMR"
    Then EASYMOBILERECHARGE Changes saved should reflect in user profile for "EMR"

  #==================================================================================
  Scenario Outline: EASYMOBILERECHARGE Sign In using Social plugin
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User click on <social plugin> and login using sample credential
    Then EASYMOBILERECHARGE User validates username shown on home page for <social plugin>

    Examples: 
      | social plugin |
      | "googleplus"  |

  #================================================================
  Scenario: EASYMOBILERECHARGE user profile management validation - Forget Password
    Given EASYMOBILERECHARGE User opens home page for "EMR home page"
    When EASYMOBILERECHARGE User click on forget password hyperlink and enters sample details without captcha
    Then EASYMOBILERECHARGE Following error to be shown "Sorry Your Email address or username is not registered with us." on EMR
