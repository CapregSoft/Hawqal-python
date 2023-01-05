class CountryFilter:
    def __init__(self, country_name=True, iso_code=True, phone_code=True, capital=True, currency=True, currency_name=True, currency_symbol=True, country_domain=True, region=True, subregion=-True, timezone=True, zone_city=True, UTC=True, latitude=True, longitude=True):
        self.country_name = country_name
        self.longitude = longitude
        self.latitude = latitude
        self.iso_code = iso_code
        self.phone_code = phone_code
        self.capital = capital
        self.currency = currency
        self.currency_name = currency_name
        self.currency_symbol = currency_symbol
        self.country_domain = country_domain
        self.region = region
        self.subregion = subregion
        self.timezone = timezone
        self.zone_city = zone_city
        self.UTC = UTC

    def __str__(self):
        fields = ""
        for field in ['country_name', 'iso_code', 'phone_code', 'capital', 'currency', 'currency_name', 'currency_symbol', 'country_domain', 'region', 'subregion', 'timezone', 'zone_city', 'UTC', 'longitude', 'latitude']:
            if getattr(self, field):
                fields = fields + field + ','
        return fields[:-1]
