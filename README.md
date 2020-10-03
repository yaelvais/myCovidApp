##Python Flask for Covid-19 statistics

The script fetch Covid-19 data from disease.sh API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask.

```bash
pip install flask
```

## Usage

```python
python covid_app.py
```
Then you can query the localhost:

curl localhost:5000/status
curl localhost:5000/newCasesPeak?country=israel
curl localhost:5000/recoveredPeak?country=israel
curl localhost:5000/deathsPeak?country=France
