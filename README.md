![](http://ForTheBadge.com/images/badges/made-with-python.svg)

# Hawqal

```
Python package that contains the data of countries, states
and their cities. Now it's easy for the end-user to get all
the data by just calling the relevant functions
```

## Functions

- getCountries( )
- getStates( )
- getCities( )

## Installation Guide

- windows

  ```
  pip install hawqal

  ```

- Unix/macOS

  ```
  python3 -m pip install hawqal
  ```

- Latest Version

  ```
  pip install --upgrade hawqal

  ```

## Usage/Examples

- Returns countries
  ```python
  from hawqal.country import Country
  Country.getCountries()
  ```
- Returns cities
  ```python
  from hawqal.cities import City
  City.getCities()
  ```
- Returns cities by country
  ```python
  from hawqal.cities import City
  City.getCities("countries name")
  ```
- Returns cities by state
  ```python
  from hawqal.cities import City
  City.getCities("", "state")
  ```
- Returns states
  ```python
  from hawqal.states import StatesByCountry
  StatesByCountry.getStates()
  ```
- Returns states by country
  ```python
  from hawqal.states import StatesByCountry
  StatesByCountry.getStates("country name")
  ```

## Success Response

- ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', . . . ]
- ['Alabama', 'Alaska', 'American Samoa', 'Arizona', . . . ]

## Error Response

- [ ]

## Tech Stack

**Language:** Python 3.10.9

## Authors

- [Capregsoft](https://www.github.com/capregsoft)
- [Husnain Khurshid](https://www.github.com/husnain9)
