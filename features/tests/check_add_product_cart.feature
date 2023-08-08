Feature: Adding a product to the cart

  Scenario: open product page and add to cart
    Given Open Amazon Product page
    When Click on add to Cart
    Then Verify the item is added to Cart
