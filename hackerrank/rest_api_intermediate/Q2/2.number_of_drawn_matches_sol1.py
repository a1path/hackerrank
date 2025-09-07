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
# exceeded Allowed time limit of 10 seconds when looping through 196 pages. so it is not an accepted solution.
#

def getNumDraws(year):
    # Write your code here
    # https://jsonmock.hackerrank.com/api/football_matches?year=<year>&page=<page>
    # json return format: {'page': 1, 'per_page': 10, 'total': 1951, 'total_pages': 196, 'data': [list of dict]}
    # match data format: {'team1': 'Barcelona', 'team2': 'AC Milan', 'team1goals': '2', 'team2goals': '2'}

    # additional parameter to just return team1goals.
    # https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team1goals=1&page=<page>
    # 

    page=1
    URL = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&page=" + str(page)
    
    print(URL)
    response = requests.get(URL).json()
    total_pages=response['total_pages'] #196
    total_games=response['total'] #1951
    print(f"There are {total_games} total games in year {year}")
    
    match_data =[]
    draw_match_per_page=0
    draw_match_total=0
    # total_pages =10
    for page in range(1,total_pages+1):
        URL = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&page=" + str(page)
        # print(URL)
        response = requests.get(URL).json()
        match_data = response['data']
        draw_match_per_page=0
        for match in match_data:
            if match['team1goals'] == match['team2goals'] :
                print(match)
                draw_match_per_page +=1
        print(f"there are {draw_match_per_page} games that matches at page {page}")
        draw_match_total +=  draw_match_per_page
        # print(f"page {page} has {draw_match_count} draw matches")
    print(draw_match_total)
    
    return(draw_match_total)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input("Input game year:").strip())

    result = getNumDraws(year)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
