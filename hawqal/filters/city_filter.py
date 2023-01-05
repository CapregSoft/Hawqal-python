class CityFilter:
    def __init__(self, city_id=True, city_name=True, state_name=True, state_id=True, country_name=True, latitude=True,
                 longitude=True):
        self.country_name = country_name
        self.longitude = longitude
        self.latitude = latitude
        self.city_id = city_id
        self.city_name = city_name
        self.state_name = state_name
        self.state_id = state_id

    def __str__(self):
        fields = ""
        for field in ['country_name', 'city_id', 'city_name', 'state_id', 'state_name', 'latitude', 'longitude']:
            if getattr(self, field):
                fields = fields + field + ","
        return fields[:-1]
