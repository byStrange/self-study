import sqlite3

con = sqlite3.connect('vote.db')

cur = con.cursor()


#creating table
#cur.execute(
#    'CREATE TABLE IF NOT EXISTS votes(Russia TEXT, Ukraine TEXT, America, ID)'
#)


def vote(to, who):
    _is = {
        'russia': to.count('ru') > 0,
        'english': to.count('en') > 0,
        'ukraine': to.count('uk') > 0
    }
    for i in cur.execute('SELECT ID FROM votes'):
        if i[0] == who:
            return
    
    if _is['russia']:
        cur.execute(f'INSERT INTO votes VALUES("1", "0", "0", "{who}")')
        con.commit()
    elif _is['english']:
        cur.execute(f'INSERT INTO votes VALUES("0", "0", "1", "{who}")')
        con.commit()
    elif _is['ukraine']:
        cur.execute(f'INSERT INTO votes VALUES("0", "1", "0", "{who}")')
        con.commit()

#voted('ukraine')

def most_voted():
    most = 0
    _all = {
        "ru": 0,
        "en": 0,
        'uk': 0,
    }
    for i in cur.execute('SELECT * FROM votes'):
        _all['ru'] += int(i[0])
        _all['uk'] += int(i[1])
        _all['en'] += int(i[2])
    for i in _all:
        if int(_all[i]) > int(most):
            most = _all[i]
            most_char = i
    return {
        "most": [most_char, most],
        "all": _all
    }