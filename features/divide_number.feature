Feature: Calculator Test Dividing

Scenario:Dividing
 Given Calculator app is run for dividing
 When I divide "6" and "3" using calculator
 Then I get from dividing "2"

Scenario:Dividing Negative
 Given Calculator app is run for dividing
 When I divide "6" and "-3" using calculator
 Then I get from dividing "-2"

Scenario:Dividing Two Negatives
 Given Calculator app is run for dividing
 When I divide "-6" and "-6" using calculator
 Then I get from dividing "1"

Scenario:Dividing by Zero
 Given Calculator app is run for dividing
 When I divide "6" and "0" using calculator
 Then I get from dividing "0"