# bikehub-api

This project connects to the Transport for London (TfL) BikePoint API to retrieve live availability information for Santander Cycle Hire docking stations across London.

What is BikePoint?

BikePoint is the name TfL uses for their cycle docking stations.
Each BikePoint site has an ID (e.g. BikePoints_1) and contains live data such as:

total docks

number of bikes available

number of empty docks

geolocation (lat/lon)

station name

API Endpoint

Base endpoint:

https://api.tfl.gov.uk/BikePoint

Common endpoints:

Purpose Endpoint
Get all BikePoints GET https://api.tfl.gov.uk/BikePoint
Get a specific BikePoint by ID GET https://api.tfl.gov.uk/BikePoint/{id}
Search BikePoints by name GET https://api.tfl.gov.uk/BikePoint/Search?query={text}
Example: Get all BikePoints
GET https://api.tfl.gov.uk/BikePoint

This returns an array of all docking stations in London, with their IDs and status.

API Keys (optional but recommended)

You can call BikePoint endpoints without an API key — but TfL supports key-based requests and rate limits are more generous when you authenticate.

Append app_id and app_key:

https://api.tfl.gov.uk/BikePoint?app_id=YOUR_ID&app_key=YOUR_KEY

You can register for free keys at:
https://api-portal.tfl.gov.uk/

Example JSON snippet
{
"id": "BikePoints_1",
"commonName": "River Street , Clerkenwell",
"lat": 51.52916347,
"lon": -0.109970527,
"additionalProperties": [
{
"key": "NbBikes",
"value": "7"
},
{
"key": "NbDocks",
"value": "30"
}
]
}

Basic workflow

GET the BikePoint endpoint

parse JSON

extract dock + bike counts from additionalProperties array

(optional) join with geospatial data for mapping / BI tools
