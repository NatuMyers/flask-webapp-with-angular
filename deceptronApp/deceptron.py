from flask import Flask, render_template, request
from flask import Blueprint,  abort
import string

deceptron = Blueprint('deceptron', __name__, template_folder='templates')

@deceptron.route('/deceptron')
def start_here():
	return render_template("pirate_greet.html")

@deceptron.route('/deceptron/play')
def game():
	return render_template("pirate_game.html")

@deceptron.route('/deceptron/translate')
def translate():
	# takes input from pirate_game.html page (inputted on /play)
	input_sentence = request.args.get("input_sentence")
	print input_sentence

	pirate_dict = {"sir": "matey", "hotel" : "fleabag inn", "student" : "swabbie", "boy" : "matey", "madam" : "proud beauty", "professor": "foul blaggart", "restaurant" : "galley", "your" : "yer", "excuse" : "arr", "students" : "swabbies", "are" : "be", "lawyer" : "foul blaggart", "the" : "th'", "restroom" : "head", "my" : "me", "hello": "avast", "is" : "be", "man" : "matey"}

	#FIXME, can currently only accept words with spaces
	split_sentence = input_sentence.split()

	result_list = []
	for word in split_sentence:
		if word in pirate_dict:
			value = pirate_dict[word]
			result_list.deceptronend(value)
		else:
			result_list.deceptronend(word)
	
	result_sentence = string.join(result_list)

	return render_template("pirate_translate.html", input_sentence=input_sentence, result_sentence= result_sentence)

@deceptron.route('/deceptron/playagain')
def game_again():
	response = request.args.get("game")

	if response == "yes":
		return render_template("pirate_game.html")
	if response == "no":
		return render_template("pirate_bye.html")

