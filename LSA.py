'''
This is Version 1.0 of Alfred Simpson's Lyrics Sentiment Analysis program. 

It relies on the user to input .txt files of lyrics from an artist. Future versions plan to crawl the internet based upon user input of artist name and album names or song names.
'''
import string

def lyrics(inFile):
	wordDict = {}
	otherSum = 0
	selfSum = 0
	jointSum =0
	formattedLyrics = []
	inFile = open(inFile, 'r')
	songs = inFile.readlines()
	inFile.close()
	for line in songs:
		for word in lines:
			word = word.strip(string.punctuation)
			formattedLyrics += word
			formattedLyrics += ''
	formattedLyrics = formattedLyrics.split()


	# Establishing words flagged for sentiment
self = ['me', 'my', 'mine', 'i', 'im', 'ill', 'id', 'ive']