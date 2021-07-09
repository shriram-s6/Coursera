punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(string):
    return ''.join([s.replace(s, '') if s in punctuation_chars else s for s in string])


def get_pos(string):
    positive_words_count = {}
    string = strip_punctuation(string)
    for each_string in string.split():
        positive_words_count[each_string] = 0
        if each_string.lower() in positive_words:
            positive_words_count[each_string] = positive_words_count[each_string] + 1

    return sum(positive_words_count.values())


def get_neg(string):
    negative_words_count = {}
    string = strip_punctuation(string)
    for each_string in string.split():
        negative_words_count[each_string] = 0
        if each_string.lower() in negative_words:
            negative_words_count[each_string] = negative_words_count[each_string] + 1
    return sum(negative_words_count.values())


resulting_data_file = open('resulting_data.csv', 'w')
with open('project_twitter_data.csv', 'r') as proj_twitter_file:
    resulting_data_file.write('Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score')
    resulting_data_file.write('\n')
    proj_twitter_reader = proj_twitter_file.readlines()[1:]
    for line in proj_twitter_reader:
        tweet, retweet_count, reply_count = line.strip().split(',')
        positive_score = get_pos(tweet)
        negative_score = get_neg(tweet)
        net_score = positive_score - negative_score

        resulting_data_file.write(
            '{},{},{},{},{}'.format(retweet_count, reply_count, positive_score, negative_score, net_score))
        resulting_data_file.write('\n')

