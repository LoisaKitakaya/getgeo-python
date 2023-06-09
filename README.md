# getgeo-python

getgeo-python is a python wrapper for the API provided by [getgeoapi.com](https://getgeoapi.com).

This API allows the one to access a wide range of information to better understand ones customers.

#### Information provided by [getgeoapi.com](https://getgeoapi.com) includes:

- City data | Find out where your customers are from
- Country data | Customize your application based on your user's country
- Security data | Check if your user appeared in any security blacklist and could be a threat to your business
- Currency data | Find out the preferred currency of your visitors and display prices in their preferred currency
- Time zone data | Retrieve the time zone of your visitors to customize your offers and promotions
- ASN data | Access information about the internet provided by your users

#### Why use [getgeoapi.com](https://getgeoapi.com):

- IPv4 and IPv6 | Access location and security data whether you have an IPv4 or IPv6 address
- Reliable | Scalable infrastructure with 99.99% up time
- Secure | 256-bit SSL encryption to ensure your data is transmitted safely
- Fast | Average response time is 66ms

## Usage

#### Requirements

For you to be able to use this package you must have `Python 3` installed in your system.

You must also have an api_key provided by [getgeoapi.com](https://getgeoapi.com). To get an api_key for your application, simply create an account, and click the 'Generate API Key' button.

Copy your api_key to a secure location.

#### Installation

To use getgeo-python, you need to first install it as follows:

```
# upgrade pip
pip install --upgrade pip

# install getgeo-python
pip install getgeo-python
```

Once installation is complete, you can now start using getgeo-python.

#### Usage

Import `GetGeoData` class, and create a new instance of it by providing your api key.

```
# import GetGeoData
from getgeo.geodata import GetGeoData

# setup api key
your_api_key = "exampleofapikey"

# create a new instance of GetGeoData
ip_data = GetGeoData("your_api_key")
```

Don't forget to replace `"exampleofapikey"` with your actual api_key.

The class `GetGeoData` has two instance methods, i.e.:

- `get_my_geo_data`
- `get_geo_data`

The `get_my_geo_data` method returns information based on your IP address. While the `get_geo_data` method, takes one argument (any IP address\_\_IPV4 or IPV6), and returns information based on the IP address.

The response of both methods in in json format.

Example:

```
# get my own geo data
my_geo_data = ip_data.get_my_geo_data()

print(my_geo_data)

# get geo data of given IP address
# Google's IPv6 address
# 2001:4860:4860::8888
geo_data = ip_data.get_geo_data("2001:4860:4860::8888")

print(geo_data)
```

For more information visit [getgeoapi.com](https://getgeoapi.com).
