# import requests_with_caching
import requests
import json


def get_movies_from_tastedive(movie_name):

    # payload = {}
    # payload['q'] = movie_name
    # payload['type'] = 'movies'
    # payload['limit'] = 5
    # movie_details = requests_with_caching.get('https://tastedive.com/api/similar', params=payload)

    payload = {'q': movie_name, 'type': 'movies', 'limit': 5}
    movie_details = requests.get('https://tastedive.com/api/similar', params=payload)
    movie_details = json.loads(movie_details.text)
    return movie_details


def extract_movie_titles(movie_details):
    movie_titles = [title['Name'] for title in movie_details['Similar']['Results']]
    return movie_titles


def get_related_titles(movie_titles):
    movies_title_list = []
    [movies_title_list.append(title) for movie in movie_titles
     for title in extract_movie_titles(get_movies_from_tastedive(movie)) if title not in movies_title_list]
    return movies_title_list


def get_movie_data(title):

    # payload = {}
    # payload['t'] = title
    # payload['r'] = 'json'
    # movie_data = requests_with_caching.get('http://www.omdbapi.com/', params=payload)

    payload = {'t': title, 'r': 'json'}
    movie_data = requests.get('http://www.omdbapi.com/', params=payload)
    movie_data = json.loads(movie_data.text)
    return movie_data


def get_movie_rating(movie_data):
    rot_tom_rating = 0
    movie_rating = movie_data['Ratings']
    for rating in movie_rating:
        if rating['Source'] == 'Rotten Tomatoes':
            rot_tom_rating = int(rating['Value'][:-1])

    return rot_tom_rating


def get_sorted_recommendations(movie_titles):
    rel_mov_list = get_related_titles(movie_titles)
    movie_rating_lst = []
    for title in rel_mov_list:
        movie_dict = {'title': title, 'rating': get_movie_rating(get_movie_data(title))}
        movie_rating_lst.append(movie_dict)
    movie_rating_lst = [each_movie['title'] for each_movie in
                        sorted(movie_rating_lst, key=lambda x: (x['rating'], x['title']), reverse=True)]
    return movie_rating_lst
