class StateFilter:
    def __init__(self, state_id=True, state_name=True, country_name=True, longitude=True, latitude=True):
        self.state_id = state_id
        self.state_name = state_name
        self.country_name = country_name
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        fields = ""
        for field in ['state_id', 'state_name', 'country_name', 'longitude', 'latitude']:
            if getattr(self, field):
                fields = fields + field + ','
        return fields[:-1]
