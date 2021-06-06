## CovidPlot
An easy way to plot COVID-19 info.

### Sofware (for developers)

[Get the last version of this software here](https://github.com/PythonForChange/CovidPlot).


### Installation
#### Option 1: Use pip (recommended, last stable version)
1. Install pyforchange
```
pip install pyforchange
```
2. Import pfcf in your python file
```python
import pyforchange.pfcf
```
3. Enjoy!

#### Option 2: Download the source (unstable pre-realise version)
1. Download [PFCF](pfcf.py) into your proyect folder
2. Import pfcf in your python file
```python
import pfcf
```
3. Enjoy!
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
