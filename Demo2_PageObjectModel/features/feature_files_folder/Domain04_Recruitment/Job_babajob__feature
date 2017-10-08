@recruitment @desktop @babajob
Feature: Recruitment website validation - babajob

  Background: babajob.com website functionality validation
    Given Init "firefox" browser
    Given babajob website under test "http://www.babajob.com" and short name is "babajob"

  #==================================================================================
  @homepage
  Scenario Outline: babajob Home page functionality, look-n-feel validation
    When babajob User validates home page attribute from <home page attribute list> with <expected attribute value list>
    Then babajob Test result should be successful or log the error meessage
    And babajob Quit the test scenari8o

    Examples: 
      | home page attribute list       | expected attribute value list                                                                                                              |
      | "home page URL"                | "http://www.babajob.com"                                                                                                                   |
      | "home page title"              | "Job Search Online - Free Job Alerts for Delivery Boys, Sales Jobs, BPO, Drivers, Receptionist Jobs, Beautician Jobs, Data Entry Jobs Etc" |
      | "home page logo"               | "default babajob logo"                                                                                                                     |
      | "home page loading time"       | "general home page loading time"                                                                                                           |
      | "important home page elements" | "btn__REGISTER NOW lnk__Are you and employer? labl__Pick your desired job in drpdwn__City"                                                 |
      | "important home page elements" | "lnk__babajob btn__HOME btn__SEARCH JOBS btn__FOR EMPLOYERS labl__Better Jobs for Everyone"                                                |
      | "important home page elements" | "lnk__Sales lnk__BPO lnk__DataEntry lnk__Cashier"                                                                                          |
      | "important home page elements" | "lnk__Receptionist lnk__Beautician lnk__Helper lnk__Delivery lnk__Steward"                                                                 |
      | "important home page elements" | "lnk__Driver lnk__Security lnk__Machinist lnk__Maid"                                                                                       |
      | "important home page elements" | "lnk__Cook lnk__Aayah lnk__Nurse lnk__Management"                                                                                          |
      | "important home page elements" | "lnk__Finance lnk__Engineer lnk__ITPro lnk__Teacher"                                                                                       |
      | "important home page elements" | "labl__Give a Missed Call 0 888 000 4444 for Jobs"                                                                                         |
      | "important home page elements" | "labl__JOBS BY CITY labl__JOBS BY CATEGORY labl__HIRE BY CITY"                                                                             |
      | "important home page elements" | "labl__HIRE BY CATEGORY labl__COMPANY labl__ADDITIONAL LINKS"                                                                              |
      | "important home page elements" | "lnk__mailto:support@babajob.com labl__Call +91 888-0006-666 img__babajob small image"                                                     |
      | "important home page elements" | "lnk__Jobs in Bangalore __ lnk__Jobs in Mumbai __ lnk__Jobs in Delhi"                                                                      |
      | "important home page elements" | "lnk__Marketing Jobs __ lnk__Data Entry Jobs __ lnk__Call Center Jobs"                                                                     |
      | "important home page elements" | "lnk__Hire in Bangalore __ lnk__Hire in Mumbai __ lnk__Hire in Chennai"                                                                    |
      | "important home page elements" | "lnk__Hire Marketing __ lnk__Hire Data Entry __ lnk__Hire Call Center __ lnk__Hire Logistics"                                              |
      | "important home page elements" | "lnk__Employer Resources __ lnk__Search Jobs __ lnk__Search Candidates"                                                                    |
      | "pop up"                       | "no_popup __ no_screenshot"                                                                                                                        |
      | "home button"                  | "img__babajob"                                                                                                                             |
      | "sign up"                      | "sign up link"                                                                                                                             |
      | "sign in"                      | "sign in link"                                                                                                                             |
      | "social plugin facebook"       | "social_plugin__ facebook"                                                                                                                 |
      | "social plugin twitter"        | "social_plugin__ twiter"                                                                                                                   |
      | "social plugin linkedin"       | "social_plugin__ linkedin"                                                                                                                 |
      | "home page web elements"       | "all elements __ all frames"                                                                                                               |
      | "download app check"           | "NA"                                                                                                                                       |

  #==================================================================================
  Scenario Outline: babajob Job search GUI options validation
    When babajob User navigates to SEARCH JOBS page
    And babajob User validates job search page elements from <GUI options list> with <expected GUI options value>
    Then babajob Test result should be successful or log the error meessage
    And babajob Quit the test scenari8o

    Examples: 
      | GUI options list                                                                                                                      | expected GUI options value                                                                                                |
      | "txtbox__Job search keyword"                                                                                                          | "Default text"                                                                                                            |
      | "drpdwn__Job search keyword"                                                                                                          | "As available from DB or excel file"                                                                                      |
      | "labl_Job search heading"                                                                                                             | "check__Search Jobs in city name"                                                                                         |
      | "drpdwn__Job location name"                                                                                                           | "As available from DB or excel file"                                                                                      |
      | "btn__SEARCH"                                                                                                                         | "check__SEARCH"                                                                                                           |
      | "labl__Sort By"                                                                                                                       | "check__Sort By"                                                                                                          |
      | "labl__Filter Results"                                                                                                                | "check__Filter Results"                                                                                                   |
      | "labl__ACTIVE OPENINGS FOUND IN"                                                                                                      | "check__ACTIVE OPENINGS FOUND IN"                                                                                         |
      | "lnk__Best Match lnk__Freshness  lnk__Highest Salary  lnk__Lowest Salary lnk__Delivery Executive"                                     | "check__if exists"                                                                                                        |
      | "lnk__SALARY RANGE lnk__GENDER  lnk__PINCODE  lnk__TIMINGS lnk__EXPERIENCE lnk__JOBS POSTED WITHIN"                                   | "check__if exists"                                                                                                        |
      | "lnk__SALARY RANGE arrow lnk__GENDER arrow lnk__PINCODE arrow lnk__TIMINGS arrow lnk__EXPERIENCE arrow lnk__JOBS POSTED WITHIN arrow" | "check__if exists"                                                                                                        |
      | "lnk__SALARY RANGE sub options"                                                                                                       | "check__< Rs 3999 __ Rs 4000 - Rs 7999 __ Rs 8000 - Rs 11999 __ Rs 12000 - Rs 15999 __ Rs 16000 - Rs 19999 __ > Rs 20000" |
      | "lnk__GENDER sub options"                                                                                                             | "check__Male Female"                                                                                                      |
      | "lnk__PINCODE sub options"                                                                                                            | "check__Any"                                                                                                              |
      | "lnk__TIMINGS sub options"                                                                                                            | "check__Part Time - Mornings __ Part Time - Afternoons __ Day Shift __ Night Shift __ Accommodation/Live In"              |
      | "lnk__EXPERIENCE sub options"                                                                                                         | "check__None/Fresher __ 1 - 4 Yrs __ 5 - 7 Yrs __ 8 - 10 Yrs __ > 10 Yrs"                                                 |
      | "lnk__JOBS POSTED WITHIN sub options"                                                                                                 | "check__Last 30 days __ Last 60 days __ Last 90 days __ Last 120 days"                                                    |
      | "lnk__Best Match lnk__Freshness  lnk__Highest Salary  lnk__Lowest Salary"                                                             | "check__if exists"                                                                                                        |
      | "lnk__Best Match lnk__Freshness  lnk__Highest Salary  lnk__Lowest Salary"                                                             | "check__if exists"                                                                                                        |

  #==================================================================================
  Scenario Outline: babajob Job search result information validation
    When babajob User navigates to SEARCH JOBS page and performs valid job search
    And babajob Basic search result information from <job search result information item check list> should be shown.
    Then babajob Test result should be successful or log the error meessage
    And babajob Quit the test scenari8o

    Examples: 
      | job search result information item check list                                                                     |
      | "drp_dwn__Search text box keyword list"                                                                           |
      | "drp_dwn__Search text box arrow all job type and count"                                                           |
      | "btn__Search all job type text box arrow"                                                                         |
      | "drp_dwn__City name text box selected city name"                                                                  |
      | "drp_dwn__City name text box arrow all city names"                                                                |
      | "btn__City name text box arrow"                                                                                   |
      | "btn__SEARCH"                                                                                                     |
      | "Job_priority_posting__ Highlight with special color __ labl__Sponsored by"                                       |
      | "General_info__ labl__Job Location __ labl__Pin code __ labl__City name"                                          |
      | "General_info__ labl__Salary labl__Experience  labl__Short job description lnk__More or detailed job description" |
      | "General_info__ labl__Applicants count labl__Posted on date time details img__Recruiter image optional"           |
      | "General_options__ btn__APPLY"                                                                                    |
      | "invalid job search"                                                                                              |

  #==================================================================================
  Scenario Outline: babajob Posting jobs page information validation
    When babajob User navigates to HIRE page
    And babajob User validates posting job page elements from <post job page GUI options list> with <post job page expected GUI options value>
    Then babajob Test result should be successful or log the error meessage
    And babajob Quit the test scenari8o

    Examples: 
      | post job page GUI options list | post job page expected GUI options value |
      | "Heading text"                 | "labl__Hire Smart. Hire Fast."           |
      | "lnk__Post a job"              | "url__Post a job"                        |
      | "lnk__Preview Candidates"      | "url__Preview Candidates"                |
      | "lnk__Hiring Solutions"        | "url__Hiring Solutions"                  |
      | "btn__START HIRING"            | "heck__pop up"                           |
      | "Testimonials heading"         | "Testimonials"                           |

  #==================================================================================
  Scenario Outline: babajob Actual job posting page information validation
    When babajob User navigates to HIRE page and initiates action to post a job requirement
    And babajob User selects user type from <user type list>
    And babajob User enters sample job requrement details and proceed to submit or register
    Then babajob Test result should be successful or log the error meessage
    And babajob Quit the test scenari8o

    Examples: 
      | user type list   |
      | "HOUSEHOLD"      |
      | "AGENCY"         |
      | "SMALL BUSINESS" |
      | "LARGE BUSINESS" |

  #==================================================================================
  Scenario Outline: babajob Individual job search details page information validation
    When babajob User initiates valid job search and navigates to any individual job details page
    And babajob User validates job details page information items from <job details page information item list>
    Then babajob Test result should be successful or log the error meessage
    And babajob Quit the test scenari8o

    Examples: 
      | job details page information item list                                                                         |
      | "lnk__Job category type __ labl__Posted on date time details __ labl__Short job description"                   |
      | "labl__EMPLOYER __ labl__Valid employer name"                                                                  |
      | "labl__SALARY __ labl__Salary details"                                                                         |
      | "labl__LOCATION __ labl__Location details"                                                                     |
      | "labl__CONTACT __ labl__Mandatory information"                                                                 |
      | "labl__GENDER __ labl__Preferred gender of employee"                                                           |
      | "labl__LANGUAGES_optional __ labl__Preferred language details optional"                                        |
      | "labl__EXPERIENCE optional __ labl__Experience level expected optional"                                        |
      | "labl__DESCRIPTION __ labl__Long job description __ lnk__More Jobs with"                                       |
      | "txtbox__Applicant name __ txtbox__Mobile or email __ txtbox__Password tickbox__Send SMS alerts __ btn__APPLY" |

  #==================================================================================
  Scenario Outline: babajob Job search and apply End-To-End scenario validation type first
    Given babajob User initiates job search actions from <job search action list>
    Then babajob Test result should be successful or log the error meessage
    And babajob Quit the test scenari8o

    Examples: 
      | job search action list                                                                             |
      | "type_first_01 Without login and valid job search and select first job listing and click on Apply" |
      | "type_first_02 With login and valid job search and select first job listing and click on Apply"    |

  #==================================================================================
  Scenario Outline: babajob Ticket booking End-To-End scenario validation type second
    Given babajob User initiates job search actions from <job search action list second>
    Then babajob Test result should be successful or log the error meessage
    And babajob Quit the test scenari8o

    Examples: 
      | job search action list second                                                                                                           |
      | "type_second_01 With login and valid job search and filter search result by salary and apply for first job"                             |
      | "type_second_02 With login and valid job search and filter search result by any two categories and apply for first job"                 |
      | "type_second_03 With login and valid job search and filter search result by any category then clear the filter and apply for first job" |

  #==================================================================================
  #==================== Search case list type third and fourth is NA for babajob
  #==================================================================================
  Scenario Outline: babajob Job search functionality scenario validation
    Given babajob User navigates to job search page
    When babajob User performs search using <job search keyword list>
    Then babajob Test result should be successful or log the error meessage
    And babajob Quit the test scenari8o

    Examples: 
      | job search keyword list |
      | "Marketing"             |
      | "Driver"                |
      | "Receptionist"          |
      | "DataEntry"             |

  #==================================================================================
  Scenario Outline: babajob User profile and user managemennt validation
    When babajob User validates user management case from <user management case list>
    Then babajob Test result should be successful or log the error meessage
    And babajob Quit the test scenari8o

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
  Scenario Outline: babajob Home page functionality other items validation
    When babajob User validates home page other attribute from <home page other attribute list> with <expected other attribute value list>
    Then babajob Test result should be successful or log the error meessage
    And babajob Quit the test scenari8o

    Examples: 
      | home page other attribute list | expected other attribute value list |
      | "Contact us"                   | "lnk__Contact us"                   |
      | "Privacy Policy"               | "url__Privacy Policy"               |
      | "Terms and Conditions"         | "url__Terms and Conditions"         |
      | "Search Candidates"            | "url__Search Candidates"            |
