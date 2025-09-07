#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

def getTotalGoals(team, year):
    # Write your code here
    # https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team1=<team>&page=<page>
    page=1
    URL="https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&team1=" + team +"&page=" + str(page)
    # print(URL)
    Response=requests.get(URL).json()
    # print(Response)
    total_pages=Response['total_pages']
    # print(Response['data'])
    
    team_total_goal=0
    for page in range(1,total_pages+1): # from page 1 to page {total_pages}
        for home_visit in ['team1','team2']: # team1 is hometeam and team2 is visiting team.
            URL="https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&" + home_visit +"=" + team +"&page=" + str(page)
            # print (URL)
            Response=requests.get(URL).json()
            # print(Response)
            teamdata=Response['data']
            # print(teamdata)
            teamgoals=home_visit+"goals"
            for game in teamdata:
                team_total_goal += int(game[teamgoals])
            # print(team_total_goal)
    
    return(team_total_goal)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
