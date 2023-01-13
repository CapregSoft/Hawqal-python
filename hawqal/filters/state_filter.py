class StateFilter:
    def __init__(self, state_id=False, state_name=False, country_name=False, longitude=False, latitude=False):
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
