class Filter:
    '''
    Filter function used to pass only TRUE fields to database
    Country function takes 5 optional parameters
    '''
    def CountryFilter(meta):
        fields = ''
        keyArrtibutes = {
            "coordinates": 'latitude,longitude',
            "region": 'region,subregion,country_domain',
            "currency": 'currency,currency_name,currency_symbol',
            "timezone": 'timezone,zone_city,UTC',
            "capital": 'capital,phone_code,iso_code'
        }
        for key, value in meta.items():
            if value:
                fields = fields + keyArrtibutes[key]+','
        return fields[:-1]

    '''
    Filter function used to pass only TRUE fields to database
    State function takes 2 optional parameters
    '''
    def StateFilter(meta):
        fields = ''
        keyArrtibutes = {
            "coordinates": 'latitude,longitude',
            "country": "country_name"
        }
        for key, value in meta.items():
            if value:
                fields = fields + keyArrtibutes[key]+','
        return fields[:-1]

    '''
    Filter function used to pass only TRUE fields to database
    City function takes 3 optional parameters
    '''

    def CityFilters(meta):
        fields = ''
        keyArrtibutes = {
            "coordinates": 'cities.latitude , cities.longitude',
            "country": 'cities.country_name',
            "state": 'cities.state_name',

        }
        for key, value in meta.items():
            if value:
                fields = fields + keyArrtibutes[key]+','
        return fields[:-1]
