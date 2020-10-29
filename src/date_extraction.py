import re
from dateutil.parser import parse

delimiter = "(\.| |-||/)"
patterns_list = [#14-digit delimited sequence in the following order (4-2-2 2:2:2.6)
                 #The first two digit sequence is recognised automatically as a month
                 "\d{4}"+delimiter+"\d{2}"+delimiter+"\d{2} (\d\d:){2}\d{2}.\d{6}",
                 #14-digit delimited sequence in the following order (2-2-4 2:2:2.6)
                 #The first two digits are recognised automatically as a month
                 "\d{2}"+delimiter+"\d{2}"+delimiter+"\d{4} (\d\d:){2}\d{2}.\d{6}",
                 #8-digit delimited (4-2-2) sequence
                 "\d{4}"+delimiter+"\d{2}"+delimiter+"\d{2}",
                 #8-digit delimited (4-2-2) sequence
                 "\d{2}"+delimiter+"\d{2}"+delimiter+"\d{4}",
                 ]

def extract_date_from_str(patterns_list, string):
    """
    This function extracts a date from a string using a list of regex patterns
    For the patterns extracted from string look at the patterns_list variable
    For strings recognized as dates in the dateutil.parser module, take a look at https://stackabuse.com/converting-strings-to-datetime-in-python/
    :param patterns_list: list of regex date patterns
    :param string: str
    :return: datetime.date or False
    """
    for pt in patterns_list:
        match = re.search(pt, string)
        if match:
            match = match[0]
            try:
                return parse(match)
            except:
                print(f"String {match} was not recognised as date. Check date patterns")
                return None