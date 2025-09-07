
# Rest API (Intermediate)

```
https://www.hackerrank.com/skills-verification/rest_api_intermediate

```

API endpoint: 
https://jsonmock.hackerrank.com/api/football_matches?year=<year>&page=<page>

For Question2, if you try to compare team1goals and team2goals to find match game, your program will exceed 10s runtime limit. so you need to query the endpoint as below

https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team1goals=1&team2goals=1

which will return the total matched game counts directly when goal=1. you just loop through goals=0 to goals=10 and add them up. 

script run result:

```
$python3 number_of_drawn_matches_sol2.py 
Input match year:2011
total_draw_match_at_each_goal:162 when goal is 0
total_draw_match_at_each_goal:234 when goal is 1
total_draw_match_at_each_goal:99 when goal is 2
total_draw_match_at_each_goal:14 when goal is 3
total_draw_match_at_each_goal:7 when goal is 4
total_draw_match_at_each_goal:0 when goal is 5
total_draw_match_at_each_goal:0 when goal is 6
total_draw_match_at_each_goal:0 when goal is 7
total_draw_match_at_each_goal:0 when goal is 8
total_draw_match_at_each_goal:0 when goal is 9
516
```
