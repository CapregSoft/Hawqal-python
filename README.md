![](http://ForTheBadge.com/images/badges/made-with-python.svg)

# Hawqal

Python package that contains the data of world's countries,states and their cities name

## Functions

- Get Countries
- Get Cities By State
- Get State By Country
- Get Cities By Country

## Installation Guide

- windows

```python
pip install hawqal

```

- Unix/macOS

```
python3 -m pip install hawqal
```

## Usage/Examples

```python
from hawqal.country import Country
Country.getCountries()

from hawqal.cities import City
City.getCities("countries name", "state")

from hawqal.states import StatesByCountry
StatesByCountry.getStates()

from hawqal.citiesbycountry import CitiesByCountry
CitiesByCountry.getCities("country name")

```

## Success Response

- ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', . . . ]
- ['Alabama', 'Alaska', 'American Samoa', 'Arizona', . . . ]

## Error Response

- [ ]

## Tech Stack

**Client:** Python 3.10.9

## Authors

- [Capregsoft](https://www.github.com/capregsoft)
- [Husnain Khurshid](https://www.github.com/husnain9)
