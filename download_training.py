import pandas as pd
import boto3

client = boto3.client('s3')

path_user_profile = 's3://capstone-training-data/user_profile.tsv'
path_user_artists = 's3://capstone-training-data/user_artist.tsv'

cols_user_profile = ['user_id', 'gender', 'age', 'country', 'date']
cols_user_artist = ['user_id', 'artist_id', 'artist_name', 'plays']

print('Downloading user_profile')
user_profile = pd.read_csv(path_user_profile,
                        sep = '\t',
                        names = cols_user_profile)

print('Downloading user_artist')
user_artist = pd.read_csv(path_user_artists,
                        sep = '\t',
                        names = cols_user_artist)

user_profile.to_csv('user_profile.csv')
user_artist.to_csv('user_artist.csv')