import praw
from praw.models import MoreComments
import pickle

def savedata(data):
	with open('reddit.pickle', 'wb') as file:
		pickle.dump(data, file,protocol=pickle.HIGHEST_PROTOCOL)
		print("Success")

def getcomments(chain):
	chain.replace_more(limit=0)
	for top_comment in chain:
		return top_comment.body

def readdata(data):
	with open(data, 'rb') as file:
		extracted=pickle.load(file)
		print(extracted)

def buildresult(reddit):
	data=[]
	for submission in reddit.subreddit('machinelearning').hot(limit=10):
		submission = {'title' : submission.title,
		'text' : submission.selftext,
        'score' : submission.score,
        'url' : submission.url,
        'comments' : getcomments(submission.comments)
		}
		data.append(submission)
		return data



if __name__ == '__main__':
	reddit=praw.Reddit(client_id='',client_secret='',user_agent='Witbot',username='',password='')
	data=buildresult(reddit)
	savedata(data)


