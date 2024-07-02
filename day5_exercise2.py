''''
    The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    Sort the list and find the min and max age
    Add the min age and the max age again to the list
    Find the median age (one middle item or two middle items divided by two)
    Find the average age (sum of all items divided by their number )
    Find the range of the ages (max minus min)
    Compare the value of (min - average) and (max - average), use abs() method

    Find the middle country(ies) in the countries list
    Divide the countries list into two equal lists if it is even if not one more country for the first half.
    ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
'''
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print('Min age is ', min(ages))
print('Max age is ', max(ages))
import statistics
print('Median age is ', statistics.median(ages))
average_age = sum(ages) / len(ages)
print('Average age is ' , average_age)
range_age = max(ages) - min(ages)
print('The range of the ages is ' , range_age)
min_average = ages[0:6]
max_average = ages[5:]
min_average = sum(min_average) / 5
max_average = sum(max_average) /5
print('The absolute min avg is ' , abs(min_average))
print('The absolute max avg is ' , abs(max_average))
print()
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch,ru,us,fin,*rest, ev=countries
print('Middle country is ' , countries[3])
first_half = countries[:4]
second_half = countries[4:]
print(f'List split in to two first half is {first_half}, the other is {second_half}')
print(ch)
print(ev)
print(rest) ## doesn't retur the last one