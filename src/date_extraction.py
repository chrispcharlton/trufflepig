import re

delimiter = "(\.|_| |-|\s)"
#pattern_1 finds day-month-year with delimiters
pattern_1 = "([1-9]|0[1-9]|1[\d]|2[\d]|3[0-1])"+delimiter+"([1-9]|0[1-9]|1[0-2])"+delimiter+"([\d][\d]|19[\d][\d]|20[\d][\d])"
#pattern_2 finds year-month-day patterns with delimiters
pattern_2 = "([\d][\d]|19[\d][\d]|20[\d][\d])"+delimiter+"([1-9]|0[1-9]|1[0-2])"+delimiter+"([1-9]|0[1-9]|1[\d]|2[\d]|3[0-1])"
#pattern 3 finds strings of eight consecutive digits that match a year-month-day format
pattern_3 = "(19[\d][\d]|20[\d][\d])(0[1-9]|1[0-2])(0[1-9]|1[\d]|2[\d]|3[0-1])"
#pattern 4 finds strings of eight consecutive digits that match a day-month-year format
pattern_4 = "(0[1-9]|1[\d]|2[\d]|3[0-1])(0[1-9]|1[0-2])(19[\d][\d]|20[\d][\d])"
dates_regex_list  = [pattern_1, pattern_2, pattern_3, pattern_4]

for pattern in dates_regex_list:
    match = re.search(pattern, 'letter_of_resignation_20201031.xlsx')
    if match: break

