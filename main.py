from hawqal.services.country import Country
from hawqal.services.states import State
from hawqal.services.cities import City
from hawqal.services.statesbycountry import StatesByCountry
from hawqal.services.citiesbycountry import CitiesByCountry

if __name__ == "__main__":

    Country.getCountries()
    State.getStates()
    City.getCities()
    StatesByCountry.getStates()
    CitiesByCountry.getCities()
