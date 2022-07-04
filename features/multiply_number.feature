Feature: Calculator Test Multiplying

Scenario:Multiplying
 Given Calculator app is run for multiplying
 When I multiply "6" and "3" using calculator
 Then I get from multiplying "18"

Scenario:Multiplying Negative
 Given Calculator app is run for multiplying
 When I multiply "2" and "-3" using calculator
 Then I get from multiplying "-6"

Scenario:Multiplying Two Negatives
 Given Calculator app is run for multiplying
 When I multiply "-2" and "-3" using calculator
 Then I get from multiplying "6"


