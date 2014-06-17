import pickle
import os
global high_scores, file_name

def setup_scores():
	global high_scores, file_name
	high_scores = {}
	file_name = 'highscores.pkl'

	if os.path.isfile(file_name):
		with open(file_name,"r") as h:
				high_scores = pickle.load(h)
	else:
		pass

def save_score(name, score):
	if name in high_scores:
		if score > high_scores[name]:
			high_scores[name] = score
    else:
        high_scores[name] = score

	with open(file_name,"w") as out:
		pickle.dump(high_scores, out)

def print_scores():
	score_line = "{{name:>{col_width}}} | {{score}}".format(col_width=(80-3)//2)
	for name, score in high_scores.items():
		print(score_line.format(name=name, score=score))

setup_scores()  # this is ran on import and on run

if __name__ == '__main__':  # this is run on run only
    # raw_input used only for testing, normally use variables or values instead
    save_score(raw_input('Name: ').title(), int(raw_input('Score: ')))
    print_scores()