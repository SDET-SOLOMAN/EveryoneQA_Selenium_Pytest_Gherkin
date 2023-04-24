Feature: Xpath and Css Selectors for the first homework

  Scenario Outline: User can find items using different selectors
    Given Navigate to Xpath_Examples website
    When Locate <Selector> with given <xpath_or_css>
    Then Verify <search_item> is in there
    Examples:
      |                         Selector                              | xpath_or_css | search_item |
      |                   //*[text() = "Gold"]                        |       x      |     Gold    |
      |               //*[contains(text(), "Gold")]                   |       x      |     Gold    |
      | //div[@style='padding-top: 90px;'] // button[text()='Gold']   |       x      |     Gold    |
      |       //div[contains(@style, 'padd')][2] /button[3]           |       x      |     Gold    |
      |    body.bg-light div:nth-child(2) button:nth-child(3)         |       c      |     Gold    |



#Feature: Test Scenarios for Search functionality
#
#  Scenario: User can search for a product
#    Given Open Google page
#    When Input Car into search field
#    And Click on search icon
#    Then Product results for Car are shown