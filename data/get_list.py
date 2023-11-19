from geopy.geocoders import Nominatim
import random

import pandas as pd

listofcountries1 = ['India', 'China', 'Nigeria', 'Pakistan', 'Indonesia', 'United States', 'Democratic Republic of the Congo', 'Ethiopia', 'Bangladesh', 'Brazil', 'Egypt', 'Tanzania', 'Philippines', 'Mexico', 'Uganda', 'Russia', 'Kenya', 'Vietnam', 'Sudan', 'Iran', 'Angola', 'Turkey', 'Afghanistan', 'Mozambique', 'Niger', 'Iraq', 'South Africa', 'Ivory Coast', 'Cameroon', 'Algeria', 'Myanmar', 'Madagascar', 'Ghana', 'Yemen', 'Japan', 'Mali', 'Burkina Faso', 'Germany', 'United Kingdom', 'Argentina', 'France', 'Colombia', 'Chad', 'Somalia', 'Zambia', 'Malawi', 'Thailand', 'Morocco', 'Uzbekistan', 'Senegal', 'Peru', 'Saudi Arabia', 'Nepal', 'Malaysia', 'Venezuela', 'Guinea', 'Burundi', 'Benin', 'Syria', 'Guatemala', 'Zimbabwe', 'Italy', 'Rwanda', 'South Sudan', 'Canada', 'Ukraine', 'Spain', 'Cambodia', 'North Korea', 'South Korea', 'Poland', 'Kazakhstan', 'Ecuador', 'Australia', 'Sri Lanka', 'Togo', 'Tajikistan', 'Haiti', 'Sierra Leone', 'Bolivia', 'Papua New Guinea', 'Chile', 'Jordan', 'Honduras', 'Taiwan', 'Dominican Republic', 'Tunisia', 'Republic of the Congo', 'Romania', 'Netherlands', 'Central African Republic', 'Israel', 'Liberia', 'Laos', 'Mauritania', 'Palestine', 'Kyrgyzstan', 'Azerbaijan', 'Paraguay', 'Turkmenistan', 'Nicaragua', 'Belgium', 'Sweden', 'Libya', 'El Salvador', 'Lebanon', 'Cuba', 'Eritrea', 'Czech Republic', 'Belarus', 'United Arab Emirates', 'Gambia', 'Austria', 'Hungary', 'Switzerland', 'Oman', 'Hong Kong', 'Panama', 'Serbia', 'Portugal', 'Greece', 'Namibia', 'Mongolia', 'Guinea-Bissau', 'Gabon', 'Costa Rica', 'Denmark', 'Norway', 'New Zealand', 'Bulgaria', 'Ireland', 'Botswana', 'Lesotho', 'Slovakia', 'Kuwait', 'Singapore', 'Georgia', 'Finland', 'Equatorial Guinea', 'Uruguay', 'Jamaica', 'Timor-Leste', 'Moldova', 'Armenia', 'Croatia', 'Albania', 'Eswatini', 'Comoros', 'Qatar', 'Lithuania', 'Bosnia and Herzegovina', 'Bahrain', 'Solomon Islands', 'North Macedonia', 'Djibouti', 'Puerto Rico', 'Slovenia', 'Latvia', 'Fiji', 'Trinidad and Tobago', 'Guyana', 'Estonia', 'Reunion', 'Mauritius', 'Bhutan', 'Western Sahara', 'Cyprus', 'Suriname', 'Cape Verde', 'Vanuatu', 'Belize', 'Mayotte', 'French Guiana', 'Montenegro', 'Sao Tome and Principe', 'Macau', 'Luxembourg', 'Maldives', 'Brunei', 'Bahamas', 'Samoa', 'Guadeloupe', 'Malta', 'Iceland', 'New Caledonia', 'French Polynesia', 'Martinique', 'Kiribati', 'Barbados', 'Guam', 'Federated States of Micronesia', 'Tonga', 'Saint Lucia', 'Curacao', 'Channel Islands', 'Grenada', 'Saint Vincent and the Grenadines', 'Seychelles', 'Antigua and Barbuda', 'Aruba', 'United States Virgin Islands']

geolocator = Nominatim(user_agent="CountryLatLon")

location = geolocator.geocode("Bajestan", country_codes="IR")

print("The latitude of the location is: ", location.latitude)
print("The longitude of the location is: ", location.longitude)

import pycountry

countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_2

codes = [countries.get(country, 'Unknown code') for country in listofcountries1]

df = pd.read_csv('full_population_by_country_2020.csv')

df['country'] = pd.Categorical(df['Country (or dependency)'], categories=listofcountries1, ordered=True)

# Sort the DataFrame by the 'id' column
df_sorted = df.sort_values(by='country')

list_of_area = df_sorted['Land Area'].tolist()

list_of_zoom = []
for i in range(len(list_of_area)):
    if list_of_area[i] > 1000000:
        zoom = 5
    if list_of_area[i] > 500000 and list_of_area[i] < 1000000:
        zoom = 6
    if list_of_area[i] > 100000 and list_of_area[i] < 500000:
        zoom = 6
    if list_of_area[i] > 50000 and list_of_area[i] < 100000:
        zoom = 7
    if list_of_area[i] > 10000 and list_of_area[i] < 50000:
        zoom = 8
    if list_of_area[i] < 10000:
        zoom = 10

    list_of_zoom.append(zoom)
