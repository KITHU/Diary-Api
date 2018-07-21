"""this will hold our data since am not using database """
import datetime

DIARY_DB = [
    {
        'id': 1,
        'date': '14-07-2018',
        'title': 'a day at andela',
        'data': 'was at andela office in nairobi for developers clinic.. it was awesome'
    },
    {
        'id': 2,
        'date': '15-07-2018',
        'title': 'challange 3',
        'data': 'njiruh@njiruh-HP-EliteBook-8460p:~/Desktop/boot camp wk 1$ source env/bin/activate'
    }
]

"""date getter """
DT = str(datetime.datetime.now().date())
