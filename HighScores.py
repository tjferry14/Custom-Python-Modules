import pickle

class HighScores(object):
    def __init__(self, in_file_name = 'highscores'):
        self.file_name = in_file_name
        if not self.file_name.endswith('.pkl'):
            self.file_name += '.pkl'
        self.high_scores = self.__load_scores()

    def __load_scores(self):  # private function
        try:
            with open(self.file_name, 'rb') as in_file:
                return pickle.load(in_file)
        except IOError:
            return {}

    def __save_scores(self):  # private function
        with open(self.file_name, 'wb') as out_file:
            pickle.dump(self.high_scores, out_file)

    def is_high_score(self, name, score):
        try:
            curr_high_score = self.high_scores.get(name, score-1)
        except TypeError:
            raise TypeError('The score arguement must be a number.')
        is_new_high_score = score > curr_high_score
        if is_new_high_score:
            self.high_scores[name] = score
            self.__save_scores()
        return is_new_high_score

    def print_scores(self):
        score_line = '{{name:>{col_width}}} | {{score}}'.format(col_width=(80-3)//2)
        scores_sorted = sorted(zip(self.high_scores.values(),
                                   self.high_scores.keys()), reverse=True)
        for score, name in scores_sorted:
            print(score_line.format(name=name, score=score))

if __name__ == '__main__':  # this is run on run only
    high_scores = HighScores('testing')
    # raw_input used only for testing, normally use variables or values instead
    if high_scores.is_high_score(raw_input('Name: ').title(),
                                 int(raw_input('Score: '))):
        print('Congratulations on your new high score!')
    high_scores.print_scores()
