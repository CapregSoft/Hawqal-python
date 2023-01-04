from hawqal.cities import City
from hawqal.country import Country
from hawqal.states import States

getCities = City.getCities
getCountries = Country.getCountries
getStates = States.getStates
getState = States.getState

__all__ = [getCities, getCountries, getStates, getState]
