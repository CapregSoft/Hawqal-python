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
        if self.country_name:
            fields = fields+'country_name,'
        if self.longitude:
            fields = fields+' longitude,'
        if self.latitude:
            fields = fields + 'latitude,'
        if self.iso_code:
            fields = fields + 'iso_code,'
        if self.phone_code:
            fields = fields + 'phone_code,'
        if self.capital:
            fields = fields+'capital,'
        if self.currency:
            fields = fields+' currency,'
        if self.currency_name:
            fields = fields + 'currency_name,'
        if self.currency_symbol:
            fields = fields + 'currency_symbol,'
        if self.country_domain:
            fields = fields + 'country_domain,'
        if self.region:
            fields = fields + 'region,'
        if self.subregion:
            fields = fields + 'subregion,'
        if self.timezone:
            fields = fields + 'timezone,'
        if self.zone_city:
            fields = fields + 'zone_city,'
        if self.UTC:
            fields = fields + 'UTC,'

        return fields[:-1]+' '
