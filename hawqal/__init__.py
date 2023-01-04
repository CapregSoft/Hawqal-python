from hawqal.cities import City
from hawqal.country import Country
from hawqal.states import States
from .filters.state_filter import StateFilter

getCities = City.getCities
getCountries = Country.getCountries
getStates = States.getStates
getState = States.getState

# filters = [StateFilter]
# functions = [getCities, getCountries, getStates, getState]
__all__ = [getCities, getCountries, getStates, getState]
