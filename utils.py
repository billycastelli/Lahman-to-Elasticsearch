def cleanAverage(hits, ab):
    if ab == 0:
        return f"{0:.3f}"
    return f"{hits/ab:.3f}"


def cleanStat(stat):
    if stat == '':
        return 0
    return stat


def careerBattingBase():
    return {
        'games': 0,
        'ab': 0,
        'runs': 0,
        'hits': 0,
        'doubles': 0,
        'triples': 0,
        'homeruns': 0,
        'rbi': 0,
        'sb': 0,
        'cs': 0,
        'bb': 0,
        'so': 0,
        'ibb': 0,
        'hbp': 0,
        'sh': 0,
        'sf': 0,
        'gidp': 0,
    }
