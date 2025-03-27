Feature: Coordinate-based velocity calculation
    As a navigation system user, 
    I want to calculate the velocity between two coordinates
    So that I can determine the velocity of the spacecraft

Scenario Outline: Calculate Velocity Between Two Coordinates
    Given two 3D coordinates "<Coordinate1>" and "<Coordinate2>"
    When I request the velocity calculation
    Then the system returns the correct speed "<CorrectSpeed>" in meters per second

    Examples:
      | Coordinate1 | Coordinate2 | CorrectSpeed |
      | 0,0,0       | 3,4,5       | 1.414        |
      | 1,2,3       | 4,6,8       | 1.581        |