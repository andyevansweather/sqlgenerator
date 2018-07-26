"""logic for creating the SQL files"""

#!/usr/bin/python'
from datetime import datetime, timedelta
from random import randint


def random_with_N_digits(n):
    """
    how many days after now you want to set to start
    :param n:
    :return:
    """
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def warning_generator(start_day, end_day):
    """
    :param start_day: how many days after now you want to set to start
    :param end_day: how many days after now you want to set to end
    :return: SQL string
    """
    N = start_day

    date_N_days_ago = datetime.now() + timedelta(days=N)
    date_N_days_ahead = datetime.now() + timedelta(days=end_day)

    valid_from = date_N_days_ago
    valid_to = date_N_days_ahead

    warning_string = "Insert into mo_aws.WARNINGS (ID,ISSUE_DATE_TIME,ISSUE_TYPE,ISSUED_BY,ISSUE_SERVICE,FORECASTING_REGION,SSPAID,ICAO,AERODROME,WARNING_CATEGORY,WARNING_TYPE,WARNING_TEXT,VALID_FROM,VALID_TO,SITE_WARNING_NO,NIL_WARNING,CANCELLED) values ({},'{}','New','AW-4 Scenario 3 Forecaster','BASIC','AW-4 Scenario 3 Region',1,'EGMC','SOUTHEND AIRPORT','AW-4 Scenario 3 Category','AW-4 Scenario 3 Warning Type','AW-4 Scenario 3 Default Text','{}','{}','01/001','N','N');\n".format(random_with_N_digits(4), datetime.now(), valid_from, valid_to)
    return warning_string