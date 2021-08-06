#!/usr/bin/env python
# coding: utf-8

# In[51]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv', 
             'dc': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York, or DC? ').lower()
    while city not in ['chicago', 'new york', 'dc']:
        print("{} is not a valid input.".format(city))
        city = input('Would you like to see data for Chicago, New York, or DC? ').lower()

    # get user input for month (all, january, february, ... , june)
    month = input('Which month? Jan, Feb, Mar, Apr, May, Jun or all? ').lower()
    while month not in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']:
        print("{} is not a valid input.".format(month))
        month = input('Which month? Jan, Feb, Mar, Apr, May, Jun or all? ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day? Mo, Tu, We, Th, Fr, Sa, Su or all? ').lower()
    while day not in ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su', 'all']:
        print("{} is not a valid input.".format(day))
        day = input('Which day? Mo, Tu, We, Th, Fr, Sa, Su or all? ').lower()

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
    df['day_of_week'] = df['Start Time'].dt.weekday


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month] 
    # filter by day of week if applicable
    if day != 'all':
        # Convert day name to day number
        days = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
        day = days.index(day)
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day] 
    print('\n Here is a sample of the data:\n', df.head())
    print('-'*40)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Frequent Month: ', common_month)
    
    # display the most common day of week
    common_weekday = df['day_of_week'].mode()[0]
    print('Most Frequent Day of Week (0=Monday): ', common_weekday)
    
    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    print('Most Frequent Start Station: ', common_sstation)

    # display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    print('Most Frequent End Station: ', common_estation)

    # display most frequent combination of start station and end station trip
    #combine station column into new column, with space in between 
    df['Start and End Station'] = df['Start Station'] + '\n\t' + df['End Station']
    common_esstation = df['Start and End Station'].mode()[0]
    print('Most Frequent Start and End Station:\n\t', common_esstation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time: {} seconds'.format(total_time))
    
    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean Travel Time: {} seconds'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print('\nGender:\n', gender)

    # Display earliest, most recent, and most common year of birth
    min_year = df['Birth Year'].min()
    print('\nEarliest Birth Year: ', min_year)
    max_year = df['Birth Year'].max()
    print('Most Recent Birth Year: ', max_year)
    mode_year = df['Birth Year'].mode()
    print('Most Common Birth Year: ', mode_year)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    raw_data = input('\nWould you like to see the raw data? Enter yes or no.\n')
    if raw_data.lower() == 'yes':
        i = 0
        while raw_data.lower() == 'yes':
            print(df.iloc[i:i+5, :])
            i += 5  
            raw_data = input('\nWould you like to see more raw data? Enter yes or no.\n')
            
def main():
    while True:
        df = load_data(*get_filters())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()


# In[ ]:




