import re
import datetime as dt

delimiter = "(\.|_| |-|\s)"
patterns_list = [{"pattern": "([1-9]|0[1-9]|1[\d]|2[\d]|3[0-1])"+delimiter+"([1-9]|0[1-9]|1[0-2])"+delimiter+"(19[\d][\d]|20[\d][\d])",
                  "strp_format": "%d/%m/%Y"},
                 {"pattern":"(19[\d][\d]|20[\d][\d])"+delimiter+"([1-9]|0[1-9]|1[0-2])"+delimiter+"([1-9]|0[1-9]|1[\d]|2[\d]|3[0-1])",
                  "strp_format": "%Y/%m/%d"},
                 {"pattern": "(19[\d][\d]|20[\d][\d])(0[1-9]|1[0-2])(0[1-9]|1[\d]|2[\d]|3[0-1])",
                  "strp_format": "%Y%m%d"},
                 {"pattern": "(0[1-9]|1[\d]|2[\d]|3[0-1])(0[1-9]|1[0-2])(19[\d][\d]|20[\d][\d])",
                  "strp_format": "%d%m%Y"}
                 ]

def extract_date_from_str(patterns_list, string):
    """
    This function extracts a date from a string using a list of regex patterns
    :param patterns_list: list of pattern dictionaries [{pattern 1: regex, strp_format: datetime format}]
    :param string: str
    :return: datetime.date
    """
    for pt in patterns_list:
        match = re.search(pt["pattern"], string)
        if match:
            match = match[0]
            delim = re.search(delimiter, match)
            if delim:
                match = match.replace(delim[0], "/")
            return dt.datetime.strptime(match, pt["strp_format"]).date()
    return None

if __name__ == '__main__':
    string = 'letter_of_resignation_09012011.xlsx'
    date = extract_date_from_str(patterns_list=patterns_list, string=string)