from covidPlot import *
chile=CovidData()
usa=CovidData('United States')
chile.plot('new_vaccinations_smoothed_per_million')
usa.plot("new_cases")