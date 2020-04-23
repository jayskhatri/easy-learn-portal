# -*- coding: utf-8 -*-
import sys
from flask import Flask, render_template, url_for, request, redirect
from text_to_speech import mytts
from trans import converthindi
from get_link import video_link # this gives link for iframe
from scrap import get_summary #this gives summary


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
	global topic_name
	global language_convert
	global topic_summary
	global link_1
	topic_name = request.form['topic_name']
	topic_summary = get_summary(topic_name)
	link_1 = str(video_link(topic_name))
	#link_1 = "'" + link_1 + "'"
	language_convert = converthindi(topic_summary.decode('utf-8'))
	return render_template('page1.html', topic_summary = topic_summary, topic_name = topic_name, link_1 = link_1)

@app.route('/report_page_2', methods = ['GET', 'POST'])
def report_page_2():
	language = request.form['language']
	mytts(topic_summary, language)
	return render_template('done.html', language = language, topic_name = topic_name, topic_summary = topic_summary, 
		link_1 = link_1)

@app.route('/text_to_speech', methods = ['GET', 'POST'])
def text_to_speech():
	return render_template('text_to_speech.html')

@app.route('/english_to_hindi', methods = ['GET', 'POST'])
def english_to_hindi():
	language = 'hi'
	mytts(topic_summary.decode('utf-8'), language)
	return render_template('english_to_hindi.html', language_convert = language_convert, language = language)

if __name__ == '__main__':
    app.run(debug = True)
    #app.run(debug = True, host = '2409:4043:2e02:2a22:cdfe:cb12:4ce5:25bb')
