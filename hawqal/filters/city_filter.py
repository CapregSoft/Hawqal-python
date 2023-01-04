class CityFilter:
    def __init__(self, city_id=True, city_name=True, state_name=True, state_id=True, country_name=True, latitude=True, longitude=True):
        self.country_name = country_name
        self.longitude = longitude
        self.latitude = latitude
        self.city_id = city_id
        self.city_name = city_name
        self.state_name = state_name
        self.state_id = state_id

    def __str__(self):
        fields = ""
        if self.country_name:
            fields = fields+'country_name,'
        if self.longitude:
            fields = fields+' longitude,'
        if self.latitude:
            fields = fields + 'latitude,'
        if self.city_id:
            fields = fields+'city_id,'
        if self.city_name:
            fields = fields+' city_name,'
        if self.state_name:
            fields = fields + 'state_name,'
        if self.state_id:
            fields = fields + 'state_id,'

        return fields[:-1]+' '
