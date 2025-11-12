from extract_bikepoint import extract
from load import load
print('loading functions')

url = 'https://api.tfl.gov.uk/BikePoint'

print('running extract')
extract(url)
print('extract done')

print('running load')
load()
print('load done')

print('script finished')
