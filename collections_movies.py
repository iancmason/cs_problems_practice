def get_movies_by_director(data=movies_csv):
    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
        	try:
        		director = line['director_name']
        		movie = line['movie_title'].replace('\xa0', '')
        		year = int(line['title_year'])
        		score = float(line['imdb_score'])
        	except ValueError:
        		continue

        	m = Movie(title=movie, year=year, score=score)
        	directors[director].append(m)

    return directors
