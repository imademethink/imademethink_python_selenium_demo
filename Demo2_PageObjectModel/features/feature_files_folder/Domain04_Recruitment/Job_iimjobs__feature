@recruitment @desktop @iimjobs
Feature: Recruitment website validation - iimjobs

  Background: iimjobs.com website functionality validation
    Given Init "firefox" browser
    Given iimjobs website under test "http://www.iimjobs.com" and short name is "iimjobs"

  #==================================================================================
  @homepage
  Scenario Outline: iimjobs Home page functionality, look-n-feel validation
    When iimjobs User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then iimjobs Test result should be successful or log the error meessage
    And iimjobs Quit the test scenari8o

    Examples: 
      | home page attribute list       | expected attribute value list                                                                          |
      | "home page URL"                | "http://www.iimjobs.com"                                                                               |
      | "home page title"              | "Jobseekers login - iimjobs.com"                                                                       |
      | "home page logo"               | "NA"                                                                                                   |
      | "home page loading time"       | "general home page loading time"                                                                       |
      | "important home page elements" | "labl__iimjobs labl__.com  btn__Recruiters txt_box__Email txt_box__Password txt_box__Confirm Password" |
      | "important home page elements" | "btn__Register btn__Login"                                                                             |
      | "pop up"                       | "no_popup __ no_screenshot"                                                                                    |
      | "home button"                  | "NA"                                                                                                   |
      | "sign up"                      | "sign up link"                                                                                         |
      | "sign in"                      | "sign in link"                                                                                         |
      | "social plugin facebook"       | "NA"                                                                                                   |
      | "social plugin twitter"        | "NA"                                                                                                   |
      | "home page web elements"       | "all elements __ all frames"                                                                           |
      | "download app check"           | "NA"                                                                                                   |

  #==================================================================================
  #======= iimjobs Recruitment GUI options validation - NA ==========================
  #==================================================================================
  Scenario Outline: iimjobs Job search scenarions combination validation
    When iimjobs User initiates search scenario combination with <main category> and <sub category>
    And iimjobs User validates <URL text> and  highlight on <main menu> and <sub menu>
    Then iimjobs Test result should be successful or log the error meessage
    And iimjobs Quit the test scenari8o

    Examples: 
      | main category            | sub category                              | URL text                          | main menu           | sub menu                                  |
      | "Finance Jobs"           | "NA"                                      | "finance-jobs"                    | "Banking & Finance" | "All Banking & Finance Jobs"              |
      | "Sales & Marketing Jobs" | "NA"                                      | "sales--marketing"                | "Sales & Marketing" | "All Sales & Marketing"                   |
      | "Consulting Jobs"        | "NA"                                      | "consulting-jobs"                 | "Consulting"        | "All Consulting & General Mgmt Jobs"      |
      | "HR Jobs"                | "NA"                                      | "hr-jobs"                         | "HR & IR"           | "All HR & IR Jobs"                        |
      | "IT & Systems Jobs"      | "NA"                                      | "it--systems"                     | "IT & Systems"      | "All IT & Systems Jobs"                   |
      | "Operations Jobs"        | "NA"                                      | "operations-jobs"                 | "SCM & Operarions"  | "All SCM & Operarions Jobs"               |
      | "Legal Jobs"             | "NA"                                      | "legal"                           | "Legal"             | "All Legal Jobs"                          |
      | "BPO Jobs"               | "NA"                                      | "bpo"                             | "BPO"               | "All BPO Jobs"                            |
      | "Finance Jobs"           | "Finance and Accounts Jobs"               | "finance-and-sccounts-jobs"       | "Banking & Finance" | "Finance and Accounts Jobs"               |
      | "Finance Jobs"           | "Banking Jobs"                            | "banking-jobs"                    | "Banking & Finance" | "Banking Jobs"                            |
      | "Finance Jobs"           | "Corporate Banking Jobs"                  | "corporate-banking-jobs"          | "Banking & Finance" | "Corporate Banking Jobs"                  |
      | "Finance Jobs"           | "Investment Banking Jobs"                 | "investment-banking-jobs"         | "Banking & Finance" | "Investment Banking Jobs"                 |
      | "Finance Jobs"           | "Private Equity Jobs"                     | "private-equity-jobs"             | "Banking & Finance" | "Private Equity Jobs"                     |
      | "Finance Jobs"           | "Equity Research Jobs"                    | "equity-research-jobs"            | "Banking & Finance" | "Equity Research Jobs"                    |
      | "Sales & Marketing Jobs" | "Sales Jobs"                              | "sales-jobs"                      | "Sales & Marketing" | "Sales Jobs"                              |
      | "Sales & Marketing Jobs" | "Marketing Jobs"                          | "marketing-jobs"                  | "Sales & Marketing" | "Marketing Jobs"                          |
      | "Sales & Marketing Jobs" | "Brand Management Jobs"                   | "brand-management-jobs"           | "Sales & Marketing" | "Brand Management Jobs"                   |
      | "Sales & Marketing Jobs" | "Online Marketing Jobs "                  | "online-marketing-jobs"           | "Sales & Marketing" | "Online Marketing Jobs"                   |
      | "Sales & Marketing Jobs" | "Marketing Communications Jobs"           | "marketing-communications-jobs"   | "Sales & Marketing" | "Marketing Communications Jobs"           |
      | "Sales & Marketing Jobs" | "Market Research Jobs"                    | "market-research-jobs"            | "Sales & Marketing" | "Market Research Jobs"                    |
      | "Consulting Jobs"        | "Strategy Consulting"                     | "strategy-consulting-jobs"        | "Consulting"        | "Strategy Consulting Jobs"                |
      | "Consulting Jobs"        | "Research Jobs"                           | "research-jobs"                   | "Consulting"        | "Research Jobs"                           |
      | "Consulting Jobs"        | "Analytics Jobs"                          | "analytics-jobs"                  | "Consulting"        | "Analytics Jobs"                          |
      | "Consulting Jobs"        | "Process Excellence Jobs "                | "process-excellence-jobs"         | "Consulting"        | "Process Excellence Jobs"                 |
      | "Consulting Jobs"        | "Consulting - BFSI Jobs"                  | "consulting--bfsi-jobs"           | "Consulting"        | "Consulting - BFSI Jobs"                  |
      | "Consulting Jobs"        | "Consulting - Consumer Goods Jobs"        | "consulting--consumer-goods-jobs" | "Consulting"        | "Consulting - Consumer Goods Jobs"        |
      | "HR Jobs"                | "HR Generalist Jobs"                      | "hr-generalist-jobs"              | "HR Jobs"           | "HR Generalist Jobs"                      |
      | "HR Jobs"                | "HR Business Partner Jobs"                | "ht-business-partner-jobs"        | "HR Jobs"           | "HR Business Partner Jobs"                |
      | "HR Jobs"                | "Talent Acquisition Jobs"                 | "talent-acquisition-jobs"         | "HR Jobs"           | "Talent Acquisition Jobs"                 |
      | "HR Jobs"                | "Organization Development Jobs"           | "organization-development-jobs"   | "HR Jobs"           | "Organization Development Jobs"           |
      | "HR Jobs"                | "Learning and Development Jobs"           | "learning-and-development-jobs"   | "HR Jobs"           | "Learning and Development Jobs"           |
      | "HR Jobs"                | "Compensation & Benefits Jobs"            | "compensation--benefits-jobs"     | "HR Jobs"           | "Compensation & Benefits Jobs"            |
      | "IT & Systems Jobs"      | "IT Project Management Jobs"              | "it-project-management-jobs"      | "IT & Systems Jobs" | "IT Project Management Jobs"              |
      | "IT & Systems Jobs"      | "IT Consulting Jobs"                      | "it-consulting-jobs"              | "IT & Systems Jobs" | "IT Consulting Jobs"                      |
      | "IT & Systems Jobs"      | "Presales Jobs"                           | "presales-jobs"                   | "IT & Systems Jobs" | "Presales Jobs"                           |
      | "IT & Systems Jobs"      | "IT Sales Jobs"                           | "it-sales-jobs"                   | "IT & Systems Jobs" | "IT Sales Jobs"                           |
      | "IT & Systems Jobs"      | "IT Product Management Jobs"              | "it-product-management-jobs"      | "IT & Systems Jobs" | "IT Product Management Jobs"              |
      | "IT & Systems Jobs"      | "IT Business Analyst Jobs"                | "it-business-analyst-jobs"        | "IT & Systems Jobs" | "IT Business Analyst Jobs"                |
      | "Operations Jobs"        | "Supply Chain Jobs"                       | "supply-chain-jobs"               | "Operations Jobs"   | "Supply Chain Jobs"                       |
      | "Operations Jobs"        | "Operations Jobs"                         | "operations-jobs"                 | "Operations Jobs"   | "Operations Jobs"                         |
      | "Operations Jobs"        | "Procurement Jobs"                        | "procurement-jobs"                | "Operations Jobs"   | "Procurement Jobs"                        |
      | "Operations Jobs"        | "Inventory Management Jobs"               | "inventory-management-jobs"       | "Operations Jobs"   | "Inventory Management Jobs"               |
      | "Operations Jobs"        | "Plant Operations Jobs"                   | "plant-operations-jobs"           | "Operations Jobs"   | "Plant Operations Jobs"                   |
      | "Operations Jobs"        | "Demand Planning Jobs"                    | "demand-planning-jobs"            | "Operations Jobs"   | "Demand Planning Jobs"                    |
      | "Legal Jobs"             | "Legal Jobs"                              | "legal-jobs"                      | "Legal Jobs"        | "Legal Jobs"                              |
      | "Legal Jobs"             | "Regulatory Compliance Jobs"              | "regulatory-compliance-jobs"      | "Legal Jobs"        | "Regulatory Compliance Jobs"              |
      | "Legal Jobs"             | "Litigation Jobs"                         | "litigation-jobs"                 | "Legal Jobs"        | "Litigation Jobs"                         |
      | "Legal Jobs"             | "Company Secretary Jobs"                  | "company-secretary-jobs"          | "Legal Jobs"        | "Company Secretary Jobs"                  |
      | "Legal Jobs"             | "Intellectual Property Rights (IPR) Jobs" | "ipr-jobs"                        | "Legal Jobs"        | "Intellectual Property Rights (IPR) Jobs" |
      | "Legal Jobs"             | "Legal Jobs in BFSI"                      | "legal-jobs-in-bfsi"              | "Legal Jobs"        | "Legal Jobs in BFSI"                      |
      | "BPO Jobs"               | "BPO Operations Jobs"                     | "bpo-operations-jobs"             | "BPO Jobs"          | "BPO Operations Jobs"                     |
      | "BPO Jobs"               | "BPO Quality Jobs"                        | "bpo-quality-jobs"                | "BPO Jobs"          | "BPO Quality Jobs"                        |
      | "BPO Jobs"               | "BPO Presales Jobs"                       | "bpo-presales-jobs"               | "BPO Jobs"          | "BPO Presales Jobs"                       |
      | "BPO Jobs"               | "BPO Sales Jobs"                          | "bpo-sales-jobs"                  | "BPO Jobs"          | "BPO Sales Jobs"                          |
      | "BPO Jobs"               | "BPO Training Jobs"                       | "bpo-training-jobs"               | "BPO Jobs"          | "BPO Training Jobs"                       |
      | "BPO Jobs"               | "Customer Service Jobs"                   | "customer-service-jobs"           | "BPO Jobs"          | "Customer Service Jobs"                   |

  #==================================================================================
  Scenario Outline: iimjobs Individual main and sub category page element validation
    When iimjobs User initiates search scenario from <main and sub category details list>
    And iimjobs User validates resulting page elements from <resulting page element list>
    Then iimjobs Test result should be successful or log the error meessage
    And iimjobs Quit the test scenari8o

    Examples: 
      | main and sub category details list       | resulting page element list                                                                         |
      | "Operations Jobs__Supply Chain Jobs"     | "drpdwn__Any Exp. drpdwn__Any Location btn__Filter"                                                 |
      | "Legal Jobs__Regulatory Compliance Jobs" | "labl__Main Category"                                                                               |
      | "BPO Jobs__BPO Sales Jobs"               | "img__Google Ad Click img__Google Ad Click close"                                                   |
      | "Finance Jobs__Banking Jobs"             | "icon_company job icon__premium job"                                                                |
      | "HR Jobs__HR Generalist Jobs"            | "icon__preferred recruiter icon__applied jobs"                                                      |
      | "IT & Systems Jobs__Presales Jobs"       | "icon__save job icon__open house"                                                                   |
      | " HR Jobs__Talent Acquisition Jobs"      | "labl_Featured Employers labl__Learn & Grow labl__Featured Institute"                               |
      | " IT & Systems Jobs__IT Sales Jobs"      | "btn__Menu btn__MenuOption_Jobseekers btn__menuoption_Recruiters btn__menuoption_Advertise with us" |
      | " Operations Jobs__Demand Planning Jobs" | "lnk__Job short description labl__Location name labl__Job posting date"                             |
      | " Legal Jobs__Company Secretary Jobs"    | "lnk__iimjobs.com"                                                                                  |

  #==================================================================================
  Scenario Outline: iimjobs Individual job search details page information validation
    When iimjobs User initiates search valid job search and navigates to any individual job details page
    And iimjobs User validates job details page information items from <job details page information item list>
    Then iimjobs Test result should be successful or log the error meessage
    And iimjobs Quit the test scenari8o

    Examples: 
      | job details page information item list                                           |
      | "labl__Job short description labl__Job experience range lnk__Relevant hash tags" |
      | "Optional_Job full description__Location"                                        |
      | "Optional_Job full description__Company"                                         |
      | "btn__Apply btn__Save btn__Insights btn__Follow-up lnk__Report This Job Posting" |
      | "labl__Similar Jobs btn__Similar Jobs"                                           |
      | "lnk__Posted by person name img__Posted by person photo labl__last login date"   |
      | "lnk__Posted in main category name"                                              |
      | "labl__Job code lnk__Location labl__Posted on date labl__Views count"            |
      | "labl__Applications submit count labl__Recruiter action count"                   |
      | "labl_Featured Employers labl__Learn & Grow labl__Featured Institute"            |
      | "btn__Scroll to top"                                                             |

  #==================================================================================
  Scenario Outline: iimjobs Job search and apply End-To-End scenario validation type first
    Given iimjobs User initiates job search actions from <job search action list>
    Then iimjobs Test result should be successful or log the error meessage
    And iimjobs Quit the test scenari8o

    Examples: 
      | job search action list                                                                                 |
      | "type_first_01 Without login and valid job search and select first job listing  and click on Apply"    |
      | "type_first_02 Without login and valid job search and select first job listing  and click on Save"     |
      | "type_first_03 Without login and valid job search and select first job listing  and click on Insights" |
      | "type_first_04 Without login and valid job search and select first job listing  and click on Followup" |
      | "type_first_05 With login and valid job search and select first job listing  and click on Apply"       |
      | "type_first_06 With login and valid job search and select first job listing  and click on Save"        |
      | "type_first_07 With login and valid job search and select first job listing  and click on Insights"    |
      | "type_first_08 With login and valid job search and select first job listing  and click on Followup"    |
      | "type_first_09 With login and valid job search and select multiple job listing  and click on Apply"    |
      | "type_first_10 With login and valid job search and select multiple job listing  and click on Save"     |

  #==================================================================================
  Scenario Outline: iimjobs Ticket booking End-To-End scenario validation type second
    Given iimjobs User initiates job search actions from <job search action list second>
    Then iimjobs Test result should be successful or log the error meessage
    And iimjobs Quit the test scenari8o

    Examples: 
      | job search action list second                                                                                                |
      | "type_second_01 With login and valid job search and filter search result by experiance and apply for first job"              |
      | "type_second_02 With login and valid job search and filter search result by single location and save first job"              |
      | "type_second_03 With login and valid job search and filter search result by multiple location and apply for first job"       |
      | "type_second_04 With login and valid job search and filter search result by experiance and location and apply for first job" |

  #==================================================================================
  #==================== Search case list type third and fourth is NA for iimjobs
  #==================================================================================
  Scenario Outline: iimjobs Job search functionality scenario validation
    Given iimjobs User navigates to job search page
    When iimjobs User performs search using <job search keyword list>
    Then iimjobs Test result should be successful or log the error meessage
    And iimjobs Quit the test scenari8o

    Examples: 
      | job search keyword list |
      | "Internal audit"        |
      | "Presales"              |
      | "IT consulting"         |

  #==================================================================================
  Scenario Outline: iimjobs User profile and user managemennt validation
    When iimjobs User validates user management case from <user management case list>
    Then iimjobs Test result should be successful or log the error meessage
    And iimjobs Quit the test scenari8o

    Examples: 
      | user management case list                                                     |
      | "Sign_up_job_seeker__ with dummy details"                                     |
      | "Sign_up_recruiter__ with dummy details"                                      |
      | "Sign_in_job_seeker__ with pre registered user and sign out"                  |
      | "Sign_in_recruiter__ with pre registered user and sign out"                   |
      | "Edit_profile_job_seeker__ update few details and conform __ forget password" |
      | "Edit_profile_recruiter__ update few details and conform __ forget password"  |
      | "Edit_profile_job_seeker__ resume update"                                     |

  #==================================================================================
  @homepageother
  Scenario Outline: iimjobs Home page functionality other items validation
    When iimjobs User validates home page other attribute from <home page other attribute list> with <expected other attribute value list>
    Then iimjobs Test result should be successful or log the error meessage
    And iimjobs Quit the test scenari8o

    Examples: 
      | home page other attribute list | expected other attribute value list |
      | "Contact us"                   | "lnk__Contact us"                   |
      | "FAQ"                          | "lnk__FAQ"                          |
      | "Refund"                       | "url__Refund"                       |
      | "Privacy"                      | "url__Privacy"                      |
      | "Terms"                        | "url__Terms"                        |
