## CovidPlot
An easy way to plot COVID-19 info.

[View](exampleOfUsage.ipynb)

### Install


### Usage
```python
chile=CovidData()
usa=CovidData('United States')
```

```python
chile.plot('new_vaccinations_smoothed_per_million')

chile.plot("casos")

usa.plot("new_cases")

chile.plot("vacunas")

usa.plot("total_cases")
```
