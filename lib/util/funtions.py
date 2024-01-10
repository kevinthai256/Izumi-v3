
import json
import requests
import re
from replit import db
import random
import os


def update_tree(newtree): 
  if "trees" in db.keys(): 
    trees = db["trees"]
    trees.append(newtree) 
    db["trees"] = trees
  else: 
    db["trees"] = [newtree] 

def update_muted(newmute): 
  if "muted" in db.keys(): 
    muted = db["muted"]
    muted.append(newmute) 
    db["muted"] = muted
  else: 
    db["muted"] = [newmute] 

def remove_muted(id): 
  if "muted" in db.keys(): 
    muted = db["muted"]
    muted.remove(id) 
    db["muted"] = muted
  else: 
    return

def update_xp(new): 
  if "xp" in db.keys(): 
    xp = db["xp"]
    xp.append(new) 
    db["xp"] = xp
  else: 
    db["xp"] = [new] 


def update_user(new): 
  if "users" in db.keys(): 
    users = db["users"]
    users.append(new) 
    db["users"] = users
  else: 
    db["users"] = [new] 

def ntinder(uid,age,bio): 
  new = {}
  new['id'] = uid
  new['id']['age'] = age
  new['id']['bio'] = bio
  print(new)
  if "tidict" in db.keys(): 
    tdict = db["tdict"]
    tdict.append(new) 
    db["tdict"] = tdict
  else: 
    db["tdict"] = [new] 


#string to list
def makelist(string):
	  li = list(string.split(";"))
	  return (li)

#finds images
def sortimg(string):
  gimg = random.choice(string)
  while 'png' not in gimg:
    print(gimg)
    ging = random.choice(string)
  else:
    return gimg
   

#makes sure its 'media', random
def RandomGif(string):
	RGif = random.choice(string)
	while 'media' not in RGif:
		RGif = random.choice(string)
	else:
		return RGif


#string to list, random
def RandomChoice(string):
	li = list(string.split(":"))
	return random.choice(li)

#string to list, random
def RandomChoice2(string):
  if ',' in string:
	  li = list(string.split(","))
	  return random.choice(li)
  if 'or' in string:
    li = list(string.split(" or "))
    return random.choice(li)

def boldText(text):
	return ('**' + text + '**')


def action(search):
  lmt = 30
  search_term = search

  r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&limit=%s&media_filter=%s" % (search_term, os.environ['apikey'], lmt, 'gif'))
  
  if r.status_code == 200:
    gif_results = json.loads(r.content)
  else:
    gif_results = "Not Working"
  urls = re.findall(
	    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str(gif_results))
    
  return (urls)

def image(search):
  lmt = 1
  search_term = search
  r = requests.get(
	    "https://tenor.googleapis.com/v2/search?q=%s&key=%s&limit=%s&media_filter=%s" %
	    (search_term, os.environ['apikey'], lmt, 'gif'))
  
  if r.status_code == 200:
    gif_results = json.loads(r.content)
  else:
    gif_results = "Not Working"
  urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(gif_results))
  return (urls)