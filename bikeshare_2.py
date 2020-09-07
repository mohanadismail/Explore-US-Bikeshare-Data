import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['January', 'February', 'March', 'April', 'May', 'June']

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    vc = False
    city = input('Which city would you like to explore? Chicago, New York City or Washington?\n')
    while vc == False:
        if city.lower() in CITY_DATA.keys():
           vc = True
        else:
            city = input("I didn't quite catch that. Please type the whole city name\n")

    # get user input for month (all, january, february, ... , june)
    vm = False
    month = input('Now, which months would you like to look at? You can choose January to June or type "all"\n')
    while vm == False:
        if month.title() in months or month.lower() == 'all':
            vm = True
        else:
            month = input("I didn't understand :(. Please type the whole month name\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    vd = False
    day = input('Finally, which day would you like to explore? Please type the whole day name or type "all"\n')
    while vd == False:
        if day.title() in days or day.lower() == 'all':
            vd = True
        else:
            day = input("I don't know this day :(. Please type the whole day name\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Start Week Day'] = df['Start Time'].dt.day_name()
    if month != 'all':
        month = months.index(month.title()) + 1
        df = df[df['Start Time'].dt.month == month]
    if day != 'all':
        df = df[df['Start Week Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("\nThe most common month is {}".format(months[df['Start Time'].dt.month.mode()[0] - 1]))

    # display the most common day of week
    print("\nThe most common day of week is {}".format(df['Start Week Day'].mode()[0]))

    # display the most common start hour
    print("\nThe most common start hour is {}".format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most common used start station: {}".format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("Most common used end station: {}".format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    comb = df['Start Station'] + " and " + df['End Station']
    print("Most common frequent combination of start and end stations: {}".format(comb.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is: {} seconds".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("Mean travel time is: {} seconds".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    if (city.lower() != 'washington'):
        # Display counts of gender
        print(df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print("Earliest year of birth is {}".format(df['Birth Year'].min()))
        print("Most recent year of birth is {}".format(df['Birth Year'].max()))
        print("Most common year of birth is {}".format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    raw = input("Would you like to see 5 lines of row data? (y/n)")
    while raw.lower() != 'y' and raw.lower() != 'n':
        raw = input("I didn't quite catch that. Please type 'y' or 'n'\n")
    i = 0
    j = 5
    while raw.lower() == 'y':
        print(df.iloc[i:j])
        raw = input("Would you like to see 5 more rows? (y/n)\n")
        while raw.lower() != 'y' and raw.lower() != 'n':
            raw = input("I didn't quite catch that. Please type 'y' or 'n'\n")
        i += 5
        j += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? (y/n)\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
