@recruitment @mobile @android @ios @iimjobsmobile
Feature: Recruitment mobile app validation - iimjobs

  Background: iimjobs mobile app functionality validation
    Given Init "selendroid" browser
    Given iimjobs mobapp under test is "iimjobs"

  #==================================================================================
  @homescreen
  Scenario Outline: iimjobs mobapp Home screen functionality, look-n-feel validation
    When iimjobs mobapp User validates home screen attribute from <home screen attribute list> with <expected attribute value list>
    Then iimjobs mobapp Test result should be successful or log the error meessage
    And iimjobs mobapp Quit the test scenario

    Examples: 
      | home screen attribute list       | expected attribute value list                                                                                                          |
      | "home screen title"              | "iimjobs"                                                                                                      |
      | "home screen logo"               | "default iimjobs logo at starting of app"                                                                                                                 |
      | "home screen loading time"       | "general home screen loading time"                                                                                                       |
      | "important home screen elements" | "icon__iimjobs __ txtbox__Email __ txtbox__Password __ btn__Login __ lnk__Forget Password" |
      | "pop up"                         | "no_popup __ no_screenshot"                                                                                                                    |
      | "home button"                    | "NA"                                                                                                                         |
      | "sign up"                        | "sign up link"                                                                                                                         |
      | "sign in"                        | "sign in link"                                                                                                                         |

  #==================================================================================
  Scenario Outline: iimjobs mobapp Recruitment searching GUI options validation
    When iimjobs mobapp User validates recruitment searching GUI options from <GUI options list> using Browse Jobs option
    Then iimjobs mobapp Test result should be successful or log the error meessage
    And iimjobs mobapp Quit the test scenario

    Examples: 
      | GUI options list                          |
	  | "icon__iimjobs __ txtbox__Search __ btn__Filter"|
      | "btn__Sign In / Sign Up __ btn__Job Feed __ btn__Applied Jobs __ btn__Saved Jobs" |
	  | "lnk__Banking & Finance Jobs __ lnk__Sales & Marketing __ lnk__Consulting __ lnk__HR & IR" |
	  | "lnk__IT & Systems __ lnk__SCM & Operations __ lnk__Legal __ lnk__BPO" |
	  | "btn__Home __ btn__Profile __ btn__Settings" |
	  
  #==================================================================================
  Scenario Outline: iimjobs mobapp Job search scenarions combination validation
    When iimjobs mobapp User initiates search scenario combination with <main category> and <sub category>
    And iimjobs mobapp User validates <result screen title>
    Then iimjobs mobapp Test result should be successful or log the error meessage
    And iimjobs mobapp Quit the test scenari8o

    Examples: 
      | main category            | sub category                              | result screen title                       |
      | "Finance Jobs"           | "Finance and Accounts Jobs"               | "Finance and Accounts Jobs"               |
      | "Finance Jobs"           | "Equity Research Jobs"                    | "Equity Research Jobs"                    |
      | "Sales & Marketing Jobs" | "Sales Jobs"                              | "Sales Jobs"                              |
      | "Sales & Marketing Jobs" | "Market Research Jobs"                    | "Market Research Jobs"                    |
      | "Consulting Jobs"        | "Strategy Consulting"                     | "Strategy Consulting Jobs"                |
      | "Consulting Jobs"        | "Consulting - Consumer Goods Jobs"        | "Consulting - Consumer Goods Jobs"        |
      | "HR Jobs"                | "HR Generalist Jobs"                      | "HR Generalist Jobs"                      |
      | "HR Jobs"                | "Compensation & Benefits Jobs"            | "Compensation & Benefits Jobs"            |
      | "IT & Systems Jobs"      | "IT Project Management Jobs"              | "IT Project Management Jobs"              |
      | "IT & Systems Jobs"      | "IT Business Analyst Jobs"                | "IT Business Analyst Jobs"                |
      | "Operations Jobs"        | "Plant Operations Jobs"                   | "Plant Operations Jobs"                   |
      | "Operations Jobs"        | "Demand Planning Jobs"                    | "Demand Planning Jobs"                    |
      | "Legal Jobs"             | "Legal Jobs"                              | "Legal Jobs"                              |
      | "Legal Jobs"             | "Legal Jobs in BFSI"                      | "Legal Jobs in BFSI"                      |
      | "BPO Jobs"               | "BPO Presales Jobs"                       | "BPO Presales Jobs"                       |
      | "BPO Jobs"               | "BPO Sales Jobs"                          | "BPO Sales Jobs"                          |

  #==================================================================================
  Scenario Outline: iimjobs mobapp Individual main and sub category screen element validation
    When iimjobs mobapp User initiates search scenario from <main and sub category details list>
    And iimjobs mobapp User validates resulting screen elements from <resulting screen element list>
    Then iimjobs mobapp Test result should be successful or log the error meessage
    And iimjobs mobapp Quit the test scenari8o

    Examples: 
      | main and sub category details list       | resulting screen element list                                |
      | "Operations Jobs__Supply Chain Jobs"     | "btn__Filter"                                                 |
      | " IT & Systems Jobs__IT Sales Jobs"      | "icon__Location __ labl__Location name or names"            |
      | " Operations Jobs__Demand Planning Jobs" | "lnk__Job short description __  __ labl__Job posting date __ labl__Exp range"    |

  #==================================================================================
  Scenario Outline: iimjobs mobapp Individual job search details screen information validation
    When iimjobs mobapp User initiates search valid job search and navigates to any individual job details screen
    And iimjobs mobapp User validates job details screen information items from <job details screen information item list>
    Then iimjobs mobapp Test result should be successful or log the error meessage
    And iimjobs mobapp Quit the test scenari8o

    Examples: 
      | job details screen information item list                                           |
	  | "labl__Job Detail __ btn__Save" |
	  | "img__Recruiter image __ labl__Recruiter name __ labl__Recruiter job title" |
	  | "labl__Views count __ labl__Applications count __ labl__Recruiter Actions count" |
	  | "labl__Job title __ labl__Exp range __ labl__Location names __ labl__Job Code" |
	  | "labl__Relevant hash tags labl__Job description detailed" |
      | "btn__Apply __ btn__Follow up __ btn__Share __ btn__Similar jobs" |

  #==================================================================================
  Scenario Outline: iimjobs mobapp Job search and apply End-To-End scenario validation type first
    Given iimjobs mobapp User initiates job search actions from <job search action list>
    Then iimjobs mobapp Test result should be successful or log the error meessage
    And iimjobs mobapp Quit the test scenari8o

    Examples: 
      | job search action list                                                                                 |
      | "type_first_01 Without login and valid job search and select first job listing and click on Apply"    |
      | "type_first_02 Without login and valid job search and select second job listing and click on Save"     |
      | "type_first_03 Without login and valid job search and select last job listing and click on Share" |
      | "type_first_04 Without login and valid job search and select second last job listing and click on Follow up" |
      | "type_first_05 Without login and valid job search and select any job listing and click on Similar Jobs" |
	  | "type_first_06 With login and valid job search and select third job listing and click on Apply"       |
      | "type_first_07 With login and valid job search and select first job listing and click on Save"        |
      | "type_first_08 With login and valid job search and select first job listing and click on Share"    |
      | "type_first_09 With login and valid job search and select first job listing and click on Follow up"    |
      | "type_first_10 With login and valid job search and select last job listing and click on Similar Jobs"    |

  #==================================================================================
  Scenario Outline: iimjobs mobapp Ticket booking End-To-End scenario validation type second
    Given iimjobs mobapp User initiates job search actions from <job search action list second>
    Then iimjobs mobapp Test result should be successful or log the error meessage
    And iimjobs mobapp Quit the test scenari8o

    Examples: 
      | job search action list second                                                                                                |
      | "type_second_01 With login and valid job search and filter search result by second experiance range and apply for first job"              |
      | "type_second_02 With login and valid job search and filter search result by single location and save first job"              |
      | "type_second_03 With login and valid job search and filter search result by multiple location and apply for first job"       |
      | "type_second_04 With login and valid job search and filter search result by second experiance and single location and apply for first job" |

  #==================================================================================
  #==================== Search case list type third and fourth is NA for iimjobs mobapp
  #==================================================================================
  Scenario Outline: iimjobs mobapp User profile and user managemennt validation
    When iimjobs mobapp User validates user management case from <user management case list>
    Then iimjobs mobapp Test result should be successful or log the error meessage
    And iimjobs mobapp Quit the test scenari8o

    Examples: 
      | user management case list                                                     |
      | "Sign_up_job_seeker__ with dummy details"                                     |
      | "Sign_up_recruiter__ with dummy details"                                      |
      | "Sign_in_job_seeker__ with pre registered user and sign out"                  |
      | "Sign_in_recruiter__ with pre registered user and sign out"                   |
      | "Edit_profile_job_seeker__ update few details and conform __ forget password" |
      | "Edit_profile_recruiter__ update few details and conform __ forget password"  |
      | "Edit_profile_job_seeker__ resume update"                                     |
