class StateFilter:
    def __init__(self, state_id=True, state_name=True, country_name=True, longitude=True, latitude=True):
        print("Param")
        print(state_id)
        self.state_id = state_id
        self.state_name = state_name
        self.country_name = country_name
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        fields = ""
        if self.state_id:
            fields = fields+'state_id,'
        if self.state_name:
            fields = fields+' state_name,'
        if self.country_name:
            fields = fields + 'country_name,'
        if self.longitude:
            fields = fields + 'longitude,'
        if self.latitude:
            fields = fields + 'latitude,'

        return fields[:-1]+' '
