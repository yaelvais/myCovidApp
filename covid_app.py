#This script fetches Covid-19 data from disease.sh API, according to the requested query.
from flask import Flask, jsonify, request
import urllib3
import json

app = Flask(__name__)
base_url = 'https://disease.sh'
https = urllib3.PoolManager()  # need a PoolManager instance to make requests.


# @app.route('/')
# def index():
#     return "Getting COVID-19 data from corona.lmao.ninja API"


# error handling
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({})

# Returns a value of success / fail to contact the backend API


@app.route('/status')
def status():
    r = https.request('GET', base_url)
    if (r.status) != 200:
        return jsonify({'status': 'fail'})
    else:
        return jsonify({'status': 'success'})

# helper function to get the relevent highest peak
# info is cases/recoverd/deths according to the endpoint

def get_highest_peak(json_data, info):
    dic = json_data['timeline'][info]
    prev=0
    max_peak=0
    for i,(date,value) in enumerate(dic.items()):
        if i==0:
	        prev=value
        curr_peak=value-prev
        if curr_peak>=max_peak:
                max_peak=curr_peak
                curr_date=date
        prev=value
    return curr_date,max_peak


# Returns the date (and value) of the highest peak of new/recovered/deths
# Covid-19 cases in the last 30 days for a required country.


@ app.route('/newCasesPeak', endpoint='newCasesPeak')
@ app.route('/recoveredPeak', endpoint='recoveredPeak')
@ app.route('/deathsPeak', endpoint='deathsPeak')
def highest_peak():
    if request.endpoint == 'newCasesPeak':
        method = 'newCasesPeak'
        info = 'cases'
    elif request.endpoint == 'recoveredPeak':
        method = 'recoveredPeak'
        info = 'recovered'
    elif request.endpoint == 'deathsPeak':
        method = 'deathsPeak'
        info = 'deaths'
    # Check if a country was provided as part of the URL as a paramater after '?'
    if 'country' in request.args:
        country = str(request.args.get('country'))
        url = 'https://disease.sh/v3/covid-19/historical/'+country+'?lastdays=30'
        r = https.request('GET', url)
        if (r.status) != 200:  # country does not hava any info on the api
            return jsonify({})
        else:
            data = json.loads(r.data.decode('utf-8'))
            date, value = get_highest_peak(data, info)
            return json.dumps({'country': country, 'method': method, 'date': date, 'value': value}, sort_keys=False)
    else:
        return jsonify({})


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
