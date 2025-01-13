"""
dict use { }
# "year": 1964
# dictionary is a collection which is ordered** and changeable. No duplicate members.

"""

weekdays = {

    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
print(weekdays[1])
print(weekdays.get(1))
weekdays[8] = 'test'
print(weekdays)
weekdays.pop(8)
print(weekdays)

# https://docs.python.org/3.13/tutorial/datastructures.html#dictionaries