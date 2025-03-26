Feature: Star Identification
  As an astronomer
  I want to identify stars
  So that I can catalog celestial objects

  Scenario: Check if an object is a star
    Given an object named "Sirius"
    When it emits its own light
    Then it should be classified as a star

  Scenario: Check whether light is reflected
    Given emission spectra that is not sun-like
    When compared to the sun's spectra
    Then it should not be equal