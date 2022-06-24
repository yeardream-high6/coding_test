import heapq

def solution(genres, plays):
    genre_counters = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genre_counters:
            genre_counters[genre][i] = play
        else:
            genre_counters[genre] = {i: play}

    sorted_genre_counters = sorted(genre_counters.items(),
                                   key=lambda pair: sum(pair[1].values()),
                                   reverse=True)

    answer = []

    for genre, counter in sorted_genre_counters:
        tops = heapq.nlargest(2, counter.items(), key=lambda x: (x[1], -x[0]))
        answer += [index for index, count in tops]

    return answer
