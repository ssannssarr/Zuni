import requests 
import os
import json 

def api_key():
	api_key = os.getenv('OPENROUTER_API_KEY')
	if not api_key:
		print('ERROR: OPENROUTER_API_KEY not found in envioroment!\nhint: export OPENROUTER_API_KEY="<API-KEY>"\nhint: Get API key from https://openroter.ai')
		exit()
	return api_key

def build_payload(query: str, model: str = None):
	if not query:
		raise ValueError('Argument "query" cant be empty!')
	if model is None:
		model = 'openroter/free'

	payload = {
		'model':model,
		'messages':[{
			'role':'user',
			'content':query
		}],
		'tools':tools
	}

def to_api(msg):
	key = api_key()
	headers = {
		'Authorization':f'Bearer {key}', 
		'Content-Type':'application/json'
	}
