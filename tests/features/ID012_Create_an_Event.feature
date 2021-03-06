  Feature: Create an Event
  
  As a user of the "We're Board" app, I would like to create an event in the app 
  so that I can let other users know about my event.
  
  Scenario: Create an event as a normal user (Normal Flow)
    Given I am signed in as a user
     And I am on the create event page
    When I create the event with these informations:
      | Name                        | Game  | Date       | Location                                         | Description | 
      | Friendly poker at my place! | Poker | 07/02/2020 | 3448 Rue Clark, Montréal, Québec H2S 3G5, Canada | blabla      | 
    Then the system should create my event
    And I should see the event in the 'Manage my Events' page under 'hosting'
  
  Scenario: Create an event for an invalid date as a normal user (Error Flow)

    Given I am signed in as a user
     And I am on the create event page
    When I create the event with these informations:
      | Name                        | Game  | Date       | Location                                         | Description | 
      | Friendly poker at my place! | Poker | 07/02/2019 | 3448 Rue Clark, Montréal, Québec H2S 3G5, Canada | blabla      | 

    And I schedule the event for a date prior to the current date
    Then the system display a "Invalid Date" error message
  
  Scenario: Create an event without specifying a game type as a normal user(Error Flow)

    Given I am signed in as a user
    And I am on the create event page
    When I create the event with these informations:
      | Name                        | Game | Date       | Location                                         | Description | 
      | Friendly poker at my place! |      | 07/02/2020 | 3448 Rue Clark, Montréal, Québec H2S 3G5, Canada | blabla      | 

     And I do not specify a game type for the event
    Then the system display a "Invalid Game type" error message
  
  Scenario: Create an event without specifying an event name as a normal user(Error Flow)

    Given I am signed in as a user
    And I am on the create event page
    When I create the event with these informations:
      | Name | Game  | Date       | Location                                         | Description | 
      |      | Poker | 07/02/2020 | 3448 Rue Clark, Montréal, Québec H2S 3G5, Canada | blabla      | 

     And I do not specify a name for the event
    Then the system display a "Invalid event name" error message
  
  
