import time

import pandas as pd

import numpy as np



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

    print('Welcome! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:

        city = input('Which city would you like to look at? Enter Chicago, New York City or Washington: ')

        city = city.lower()

        if city == 'chicago' or city =='new york city' or city == 'washington':

            break;

        else:

            print('Oops! Please enter a valid response.')



    # TO DO: get user input for month (all, january, february, ... , june)

    while True:

        month = input('Which month would you like to look at? Please choose from January to June, or enter \'all\': ')

        month = month.lower()

        if month == 'january' or month =='february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':

            break;

        else:

            print('Oh no! Please enter a valid response.')



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:

        day = input('Which day of the week would you like to look at? Please choose from Monday to Sunday, or enter \'all\': ')

        day = day.lower()

        if day == 'monday' or day =='tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':

            break;

        else:

            print('Oops! Please enter a valid response.')



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

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name



    # if need to filter by month

    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1



        # filter by month to create the new dataframe

        df = df[df['month'] == month]



    # if need to filter by day

    if day != 'all':

        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]



    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""



    print('\nCalculating The Most Frequent Times of Travel...')

    start_time = time.time()

    # TO DO: display the most common month

    if month == 'all':

        print('The most common month is', df['month'].mode()[0])


    # TO DO: display the most common day of week

    if day == 'all':

        print('\nThe most common day of week is', df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    common_start_hour = df['hour'].mode()[0]

    print('\nThe most common start hour is', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)



def station_stats(df):

    """Displays statistics on the most popular stations and trip."""



    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()


    # TO DO: display most commonly used start station
    # TO DO: display most commonly used end station

    common_start_station = df['Start Station'].mode()[0]

    common_end_station = df['End Station'].mode()[0]

    print('The most common start station is {}, \nThe most common end station is {}'.format(common_start_station, common_end_station))


    # TO DO: display most frequent combination of start station and end station trip

    df['Combined Station'] = df['Start Station'] + ' to ' + df['End Station']

    common_combined_station = df['Combined Station'].mode()[0]

    print('The most common combination of start and end station is', common_combined_station)



    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)



def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""



    print('\nCalculating Trip Duration...\n')

    start_time = time.time()



    # TO DO: display total travel time
    # TO DO: display mean travel time

    total_travel_time = (df['Trip Duration'].sum()/60)

    mean_travel_time = (df['Trip Duration'].mean()/60)

    print('Total travel time is {} minutes and average travel time is {} minutes.'.format(total_travel_time, mean_travel_time))



    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def user_stats(df):

    """Displays statistics on bikeshare users."""



    print('\nCalculating User Stats...\n')

    start_time = time.time()



    # TO DO: Display counts of user types

    print('User Type:\n', df['User Type'].value_counts())



    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth

    if city == 'washington':

        print('There is no information in Washington on users gender or age.')

    else:

        print('\nGender:\n', df['Gender'].value_counts())

        earliest_birth_year = df['Birth Year'].min()

        recent_birth_year = df['Birth Year'].max()

        common_birth_year = df['Birth Year'].mode()[0]

        print('\nThe oldest year of birth is', earliest_birth_year)
        print('\nThe youngest year of birth is', recent_birth_year)
        print('\nThe most common year of birth is', common_birth_year)


def raw_data():

    request = input('Would you like to see five lines of raw data for the city of interest? Enter yes or no.\n')

    x=0

    y=5

    if request == 'yes':

        print(df[x:y])

        request_again = input('Would you like to see five more lines of data? Enter yes or no.\n')

        while request_again == 'yes':

            x += 5

            y += 5

            print(df[x:y])

            request_again = input('Would you like to see five more lines of data? Enter yes or no.\n')

            if request_again == 'no':

                break



while True:

    city, month, day = get_filters()

    df = load_data(city, month, day)



    user_stats(df)

    time_stats(df)

    station_stats(df)

    trip_duration_stats(df)

    raw_data()



    restart = input('\nWould you like to restart? Enter yes or no.\n')

    if restart.lower() != 'yes':

        break
