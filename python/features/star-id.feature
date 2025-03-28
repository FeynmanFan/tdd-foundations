Feature: Star Identification
  As an astronomer
  I want to identify stars
  So that I can catalog celestial objects

  Scenario: Check if an object is a star
    Given a Celestial object with a spectrum
    When it emits its own light
    Then it should be classified as a star

  Scenario: Check whether light is reflected
    Given emission spectra that is not sun-like
    When compared to the sun's spectra
    Then it should not be equal

  Scenario: Check whether an object has a gas signature
    Given an emission spectra 
    When the first element should be less than the second
    And the third element should be less than the second
    Then the spectra should be classified as having a gas signature