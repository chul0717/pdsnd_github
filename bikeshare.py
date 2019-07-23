import time
import pandas as pd
import numpy as np
import json

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('\nWould you like to see data for Chicago, New York City, or Washington?\n').lower().strip()
            if city in CITY_DATA.keys():
                break
            else:
                print('\nInput Error: Please choose between Chicago, New York City, or Washington.\n')
        except:
            print('\nInput Error: Please choose between Chicago, New York City, or Washington.\n')

    while True:
        try:
            filter = input('\nWould you like to filter the data by month, day, or not at all? Enter "none" for no filter.\n').lower().strip()
            if filter == 'month':
                # TO DO: get user input for month (all, january, february, ... , june)
                day = 'none'
                while True:
                    try:
                        month = input('\nWhich month? January, February, March, April, May or June.\n').lower().strip()
                        if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                            break
                        else:
                            print('\nInput Error: Please choose between January, February, March, April, May or June.\n')
                    except:
                        print('\nInput Error: Please choose between January, February, March, April, May or June.\n')
                break
            elif filter == 'day':
                month = 'none'
                # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                while True:
                    try:
                        day = input('\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday\n').lower().strip()
                        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                            break
                        else:
                            print('\nInput Error: Please choose between Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday\n')
                    except:
                        print('\nInput Error: Please choose between Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday\n')
                break
            elif filter == 'none':
                month = 'none'
                day = 'none'
                break
            else:
                print('\nInput Error: Please choose between month, day, or none\n')
        except:
            print('\nInput Error: Please choose between month, day, or none\n')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "None" to apply no month filter
        (str) day - name of the day of week to filter by, or "None" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(f'{city}.csv')
    df.rename({'Unnamed: 0': 'id'}, axis=1, inplace=True) # change awkard column label
    df['Start Time'] = pd.to_datetime(df['Start Time']) # convert to datetime
    df['End Time'] = pd.to_datetime(df['End Time']) # convert to datetime
    df['Month'] = df['Start Time'].dt.month # get month as integer
    df['Day'] = df['Start Time'].dt.dayofweek # get day of week as integer

    # get index of input month/day from list to get month/day as integer
    # filter rows according to month/day integer
    if month is not 'none':
        df = df[df['Month'] == ['january', 'february', 'march', 'april', 'may', 'june'].index(month)]
    if day is not 'none':
        df = df[df['Day'] == ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'].index(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    month = ['january', 'february', 'march', 'april', 'may', 'june']
    i = df['Month'].mode()[0]
    print('Most common month: ', month[i-1])

    # TO DO: display the most common day of week

    day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    i = df['Day'].mode()[0]
    print('Most common day of the week: ', day[i])

    # TO DO: display the most common start hour

    print('most common hour: ', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station: ', df['Start Station'].value_counts().index[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station: ', df['End Station'].value_counts().index[0])

    # TO DO: display most frequent combination of start station and end station trip
    print()
    print('Most frequent combindation of start station and end station trip:')
    print(df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: ', (df['End Time'] - df['Start Time']).sum())

    # TO DO: display mean travel time
    print('Average travel time: ', (df['End Time'] - df['Start Time']).mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        print('Counts of user types:')
        print(df['User Type'].value_counts())
        print()
        # TO DO: Display counts of gender
        print('Counts of gender:')
        print(df['Gender'].value_counts())
        print()

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest year of birth:', int(df['Birth Year'].sort_values(ascending=True).iloc[0]))
        print('Most recent year of birth:', int(df['Birth Year'].sort_values(ascending=False).iloc[0]))
        print('Most common year of birth:', int(df['Birth Year'].mode()))
    except:
        print('Data does not exist.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    while True:
        try:
            show_data = input("\nWould you like to see the raw data? Enter 'yes' or 'no' \n").lower().strip()
            if show_data != 'yes':
                return

            for i in range(0, len(df), 5):
                list_of_rows = df.iloc[i:i+5].to_json(orient='records', lines=True).split('\n') # create list of rows(strings)
                for row in list_of_rows:
                    row_dictionary = json.loads(row) # convert into dictionary
                    display_row = json.dumps(row_dictionary, indent=2) # convert back into string with format
                    print(display_row)

                next = input("\nWould you like to see more? Enter 'yes' or 'no'\n").lower().strip()
                if next != 'yes':
                    return
        except:
            print("Error: invalid input please try again.\n ")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower().strip() != 'yes':
            print('\nGood bye.')
            break


if __name__ == "__main__":
	main()
