#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import click
# import logging


#TODO - CHECKLIST
# python 2.7 - done
# https://developer.oxforddictionaries.com/
# API - https://od-api.oxforddictionaries.com/api/v1 - DONE
# requires authentication (apiKey or OAuth) - DONE (apiKey)
# responds with JSON or XML - DONE (json)
# supports GET or POST request type. - DONE (get)
# format of the program - :$ python script_name.py arg1 arg2 kwarg1=value1 (arguments are just an example).
# use click for this !!! (should be cooler) - NOT OK - use argparse, don't have external dependency
# allows user to write results to specific file .csv
# provides support for arguments and keyworded arguments
# use logging as logger!!! (should be better, and maybe easier to implement the debug flag)

# EXAMPLE:
# Script would be called like:

# $ python forge_api_script.py output.csv pairs=EURUSD --debug , where:

#     output.csv - output filename
#     pairs=EURUSD - currency pair to be returned by API
#     --debug turns debug mode of the script i.e.: more detailed log messages

# Running above command would result in sending request to the following endpoint https://forex.1forge.com/1.0.3/quotes?pairs=EURUSD with pairs=EURUSD as query argument and saving output data to output.csv file.


#TODO - add error checking

"""
app_id, app_key

app_id and app_key are required authentication parameters. An incorrect or missing app_id or app_key will result in 403 Authentication failed error. Authentication parameters are generated when you create your account and are visible in the API Credentials page after you login.

    app_id is a unique identifier for your application. It is generated automatically when you create your account.

    app_key is a key for your application. You can generate up to 5 unique keys and manage them in your app description page.
"""

"status codes: https://developer.oxforddictionaries.com/documentation/response-codes"


#TODO example from site

'''
# for more information on how to install requests# http://docs.python-requests.org/en/master/user/install/#install
import  requests
import json
# TODO: replace with your own app_id and app_key
# app_id = '<my app_id>'
# app_key = '<my app_key>'
# language = 'en'
# word_id = 'Ace'
# url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()
# #url Normalized frequencyurl
# FR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()
# r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
# print("code {}\n".format(r.status_code))
# print("text \n" + r.text)
# print("json \n" + json.dumps(r.json()))				
'''

class define_word(object):
    def __init__(self, word):
        if isinstance(word, (int,float)):
            raise ValueError
        try:
            self.word = str(word)
        except (NameError, SyntaxError) as err:
            raise err
    def get_definition(self):
        my_id = 'b9dba52d'
        my_key = '5c6ef63eaa447fc38ec4e0e1c34f8f97'
        language_id = 'en'
        word_id = self.word
        # url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()
        # url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/%s/%s' % (language_id, word_id.lower())
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/{lang}/{word}'.format(lang=language_id, word=word_id.lower())
        print url
        r = requests.get(url, headers = {'app_id' : my_id, 'app_key' : my_key})
        print "code {}\n".format(r.status_code)
        print "text \n" + r.text
        print "json \n" + json.dumps(r.json())




@click.group()
@click.option("--debug", is_flag=True, help="print debug messages")

def cli(debug):
    if debug:
        # click.echo('Debug mode is %s' % ('on' if debug else 'off'))
        click.echo('Debug mode is on')

@cli.command()
@click.option("--word", type=click.STRING, default=None, help="Word to fetch definition for.")
@click.option("--language", type=click.STRING, default=None, help="Language to be used.")
def get_definition(word, language):
    """Get word definition from Oxford Dictionary """
    cat_definition = define_word('cat')
    cat_definition.get_definition()
@cli.command()
def fake_command():
    pass
if __name__ == '__main__':
    # my_id = 'b9dba52d'
    # my_key = '5c6ef63eaa447fc38ec4e0e1c34f8f97'
    # language_id = 'en'
    # word_id = 'cat'
    # # url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()
    # # url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/%s/%s' % (language_id, word_id.lower())
    # url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/{lang}/{word}'.format(lang=language_id, word=word_id.lower())
    # print url
    # r = requests.get(url, headers = {'app_id' : my_id, 'app_key' : my_key})
    # print "code {}\n".format(r.status_code)
    # print "text \n" + r.text
    # print "json \n" + json.dumps(r.json())
    cli()