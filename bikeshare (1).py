import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    cities=['chicago', 'new york city', 'washington']
    months=['January', 'February', 'March', 'April', 'May','June']
    days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday']
    
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    While True:
        City = input("\n Which city do you want to see? \n Please select one of the following cities: chicago, new york city, washington. \n").lower()
        if City not in (chicago, new york city, washington)

        
    # TO DO: get user input for month (all, january, february, ... , june)
    While True:
        month = input("\n What month would you like to filter ?: january, february, march, april, may, june, all? \n").lower()
        if month not in ('January', 'February', 'March', 'April', 'May','June', all)
        
   
       
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhat day do you want to analyze?: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, all? \n").lower()
        if day not in (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, all)


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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
   
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print ('\n The month most common is.'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\n The day most common is: ', most_common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('\n The hour most common is.\n'.format(most_common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station =df['Start Station'].value_counts().idxmax()
    print('\n Most commonly used start station ', Start_Station)
    
    # TO DO: display most commonly used end station
    End_Station =df['End Station'].value_counts().idxmax()
    print('\n Most commonly used end station ', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    more_frequent_trip = df['route'].mode()[0]
    print('\n Most frequent combination of start station and end station trip ', more_frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= sum(df['Trip Duration'])
    print('\n Total travel time is.\n'.format(round((total_travel_time/86400), 1)))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('\n Mean travel time in minute is.\n'.format(round((mean_travel_time/60), 1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('User Type:\n', user_types)

    # TO DO: Display counts of gender
    try:
          gender_=df['Gender'].value_counts()
          print('\n Total Gender Types:\n', gender_)
    

    # TO DO: Display earliest, most recent, and most common year of birth
try:
        by_earliest=df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()