## Python Flask for Covid-19 statistics

The script fetches Covid-19 data from disease.sh API.


## Usage via jenkinsfile

Please add the parameters as a choice parameter, with the name "country".
The jenkins file clones the git repo, starts the script and then query the script, using the provided parameters.
Please note that the file runs the commands as 'sh' (linux).

## Usage via shell

You might need to install flask first:

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask.

```bash
pip install flask
```

```python
python3 covid_app.py
```
Then you can query the service:

```
curl localhost:5000/status
curl localhost:5000/newCasesPeak?country=israel
curl localhost:5000/recoveredPeak?country=israel
curl localhost:5000/deathsPeak?country=France
```

