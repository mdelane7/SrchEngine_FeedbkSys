import sqlite3
import os
import random
from bs4 import BeautifulSoup
import urllib2
import pickle
import pprint
from random import randint
from json import dumps, loads
from google import google
from flask import Flask, send_from_directory, json, jsonify
from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash

app = Flask(__name__) #create the application instance
app.config.from_object(__name__) #load config from this file

app.config.update(dict(
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":     
        wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
        page = urllib2.urlopen(wiki)
        soup = BeautifulSoup(page) #, "lxml")
        pdata = soup.find('p').getText()

        search_str = [ "sports", "software", "music", "the", "email marketing", "broadband", "online", "insurance", " movie", "tramadol",
        				"weight loss", "chat", "home", "car insurance", "face", "spyware", "youtube", "free tv shows", "downloads",
        				"google maps", "webs biggest", "macromedia flash player", "m nova"];

        for i in range(0, len(search_str)):
            print (search_str[i]);
            # googleData = google.search(search_str[i], 5)
            # file_hndlr = open(search_str[i] + '.pkl', 'w');
            # pickle.dump(googleData, file_hndlr);

        pkl_file = open('file1.pkl', 'rb')
        data1 = pickle.load(pkl_file)

        # for i in range(0, len(data1))
        #     data1[i].google_link.replace('http://www.google.com/url?q=', '')

        return render_template('search.html', data=(data1))
    return render_template('search.html')

app.debug = True
app.run()