import re
import pandas as pd


def preprocess(data):
    # Preprocess data
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}\s[ap]m\s*-\s*'
    msg = re.split(pattern,data)[1:]
    # extract date and time
    date_time = re.findall(pattern,data)

    cleaned_date_time = [dt.replace('\u202f', '') for dt in date_time]

    df = pd.DataFrame({'user_msg':msg, 'date_time':cleaned_date_time})
    df['date_time'] = pd.to_datetime(df['date_time'], format='%d/%m/%y, %I:%M%p - ')
    df.rename(columns={'date_time': 'datetime'}, inplace=True)

    user_pattern = r'([\w\s]+):|(\+\d{2}\s?\d{5}\s?\d{5}):|(\+\d{3}\s\d{4}\s\d{4}):|(\+\d{2,3}\s?\d{2,5}\s?\d{3,5}\s?\d{4,5}):|(\+1\s\(\d{3}\)\s\d{3}-\d{4}):|(\+\d{3}\s\d{4}\s\d{4}):'

	    # Extract user names and messages
    df['user'] = df['user_msg'].str.extract(user_pattern)[0].fillna(df['user_msg'].str.extract(user_pattern)[1]).fillna(df['user_msg'].str.extract(user_pattern)[2]).fillna(df['user_msg'].str.extract(user_pattern)[3]).fillna(df['user_msg'].str.extract(user_pattern)[4])

    df['message'] = df['user_msg'].str.replace(user_pattern, '', regex=True)

    # Fill NaN user_names with "Viplove Thakran" where applicable
    # viplove_pattern = r'(Viplove Thakran:)'
    # df['user'] = df['user'].fillna(df['message'].str.extract(viplove_pattern)[0])

    # Remove "Viplove Thakran:" from the message column
    # df['message'] = df['message'].str.replace(viplove_pattern, '', regex=True)

    df['user'] = df['user'].fillna('group_notification')

    df['only_date'] = df['datetime'].dt.date
    df['year'] = df['datetime'].dt.year
    df['month_num'] = df['datetime'].dt.month
    df['month'] = df['datetime'].dt.month_name()
    df['day'] = df['datetime'].dt.day
    df['day_name'] = df['datetime'].dt.day_name()
    df['hour'] = df['datetime'].dt.hour
    df['minute'] = df['datetime'].dt.minute
    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    df.drop(columns=['user_msg','datetime'], inplace=True)
    return df