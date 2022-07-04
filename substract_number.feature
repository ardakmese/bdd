Feature: Calculator Test Subtraction

Scenario:Subtraction
 Given Calculator app is run for subtraction
 When I subtract "6" and "3" using calculator
 Then I get from subtraction "3"

Scenario:Subtracting Negative
 Given Calculator app is run for subtraction
 When I subtract "2" and "-3" using calculator
 Then I get from subtraction "5"

Scenario:Subtracting Two Negatives
 Given Calculator app is run for subtraction
 When I subtract "-2" and "-3" using calculator
 Then I get from subtraction "1"


