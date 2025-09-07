#!/bin/python3

import math
import os
import random
import re
import sys
import requests



#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#

def getNumDraws(year):
    # Write your code here

    # additional parameter to just return team1goals. 
    # https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team1goals=1&page=<page>
    # Since there is a run time constraint of 10 seconds, we need to loop through matching goal counts and not comparing goals ourselves. 
    #

    # URL = URL = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&team1goals=" + str(goal) + "&team2goals="+ str(goal)

    total_draw_match_at_each_goal=0
    total_draw_match=0
    for goal in range(0,10):
        URL = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&team1goals=" + str(goal) + "&team2goals="+ str(goal) 
        # print(URL)
        response = requests.get(URL).json()
        # print(response)
        total_draw_match_at_each_goal=response['total'] # ['total'] returns the total counts when team1goal == team2goal == goal
        print(f"total_draw_match_at_each_goal:{total_draw_match_at_each_goal} when goal is {goal}")
        total_draw_match+=int(total_draw_match_at_each_goal)

    # print(total_draw_match)
    return(total_draw_match)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input("Input match year:").strip())

    result = getNumDraws(year)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
