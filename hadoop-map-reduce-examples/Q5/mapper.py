#!/usr/bin/env python
import datetime
import sys
import csv
from typing import Union

KIND_BIDEN = "Joe_Biden"
KIND_TRUMP = "Donald_Trump"
KIND_BOTH = "Both_Candidates"

biden_keywords = ['#biden', "#jobiden", "biden", "joebiden"]
trump_keywords = ['#trump', "#donaldtrump", "trump", "donaldtrump"]
SEPARATOR = '|---|'


def mapper(cols: list) -> Union[str, None]:
    """
    input example: 2020-10-15 00:00:18	1.31652929349796E+18	@DeeviousDenise @realDonaldTrump @nypost There won’t be many of them.  Unless you all have been voting more than once again.  But God prevails.  BO was the most corrupt President ever.  Dark to light.  Your lies are all coming through.  They wouldn’t last forever. #Trump	0.0	0.0	Twitter for iPhone	9.0076107163143E+17	Stacey Gulledge 🇺🇸 Patriot ♥️ KAG 🙏 👮‍♀️♥️	sm_gulledge	Patriot, Wife, “Shaken not Stirred” Mom of two extraordinary kids & labradoodle lover of “Honey Buns” Trust the Plan! Always Save Our Children!	2017-08-24 16:45:49	766.0	Ohio, USA	40.225356900000000	-82.6881395		United States of America	North America	Ohio	OH	2020-10-21 00:00:02.612515712
    output example: Donald_Trump|---|0.0|---|0.0|---|Twitter for iPhon

    :param text: a row of csv that each column is  separated by \t
    :return: a text as result with this format '{kind}{separator}{likes}{separator}{retweet_count}{separator}{source}'
    """

    created_at, tweet_id, tweet, likes, retweet_count, source, user_id, username, user_screen_name, user_description, user_join_date, user_followers_count, user_location, lat, long, city, country, continent, state, state_code, collected_at = cols
    tweet = tweet.lower()

    trump_condition = any([item in tweet for item in trump_keywords])
    biden_condition = any([item in tweet for item in biden_keywords])

    # Both of them
    if trump_condition and biden_condition:
        kind = KIND_BOTH
    # Donald Trump
    elif trump_condition:
        kind = KIND_TRUMP
    # Joe Biden
    elif biden_condition:
        kind = KIND_BIDEN

    date = datetime.datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
    if date.hour < 9 or 17 <= date.hour:
        return None

    result = f'{kind}{SEPARATOR}{state}'
    return result


for row in csv.reader(sys.stdin):
    try:
        result = mapper(row)
        if result is not None:
            print(result)
    except:
        pass
