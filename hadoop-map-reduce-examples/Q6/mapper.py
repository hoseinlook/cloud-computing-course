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

    created_at, tweet_id, tweet, likes, retweet_count, source, user_id, username, user_screen_name, user_description, user_join_date, user_followers_count, user_location, lat, lon, city, country, continent, state, state_code, collected_at = cols
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
    lat, lon = float(lat), float(lon)
    if -79.7624 < lon < -71.7517 and 40.4772 < lat < 45.0153:
        state_inferred_from_lat_and_long = 'New York'
    elif -124.6509 < lon < -114.1315 and 32.5121 < lat < 42.0126:
        state_inferred_from_lat_and_long = "Texas"
    else:
        return None
    result = f'{kind}{SEPARATOR}{state_inferred_from_lat_and_long}'
    return result


for row in csv.reader(sys.stdin):
    try:
        result = mapper(row)
        if result is not None:
            print(result)
    except:
        pass
