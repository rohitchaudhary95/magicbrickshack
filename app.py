#!flask/bin/python
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

import nltk, re, pprint
from nltk import word_tokenize
import nltk.corpus
import collections as co
from nltk.text import Text  

#words = co.Counter(nltk.corpus.words.words())
#stopWords =co.Counter( nltk.corpus.stopwords.words() )
stopWords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
words = co.Counter(nltk.corpus.words.words())

app = Flask(__name__)
api = Api(app)

cities = ['delhi','new delhi','faridabad','noida', 'greater noida','gurgaon']

builders = ['puri', 'bptp', 'gaurs']

class TodoSimple(Resource):
	def get(self):
		return {'text':'Hello'}
    	def get(self, text12):
		location=""
		keywords=[]
		p = text12
		text = p.split('/n')
		for data in text:
		    	data=data.lower()
		    	final = data.split()
		    	#final = final.lower()
		    	for x in final:
				if x in stopWords or x == "bhk" or x in words or '.' in x or x.isdigit() :
					continue
				elif x in builders:
					keywords.append(x)
				elif x in cities:
					location=x
				else:
					keywords.append(x)
		#resp = jsonify({'location': location})
        	return {'loc': location,'key':keywords}

class TodoSimple1(Resource):
	def get(self):
		return {'text':'Hello'}
    
api.add_resource(TodoSimple, '/<string:text12>')
api.add_resource(TodoSimple1, '/')

if __name__ == '__main__':
	app.run()
