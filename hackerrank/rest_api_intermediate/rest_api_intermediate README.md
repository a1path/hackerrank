# https://www.hackerrank.com/skills-verification/rest_api_intermediate
# Rest API (Intermediate)

API endpoint: 
https://jsonmock.hackerrank.com/api/football_matches?year=<year>&page=<page>

For Question2, if you try to compare team1goals and team2goals to find match game, your program will exceed 10s runtime limit. so you need to query the endpoint as below

https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team1goals=1&team2goals=1

which will return the total matched game counts directly when goal=1. you just loop through goals=0 to goals=10 and add them up. 
