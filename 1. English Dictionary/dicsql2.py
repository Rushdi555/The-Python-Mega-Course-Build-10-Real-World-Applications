import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()


def translate(keyword):
    try:    
        new_str = ''
        lower = keyword.lower() 
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % lower)
        results = cursor.fetchall()
        n = 1
        if results:
            for result in results:
                line_break = '%s. ' %n + result[1] + '\n'
                new_str += line_break
                n += 1
        elif len(results) == 0:
            query = cursor.execute(
            "SELECT * FROM Dictionary WHERE (Expression LIKE '{0}' OR Expression LIKE '{1}%' OR Expression LIKE '%{2}') AND (length(Expression) < {3} AND length(Expression) > {4})".format(lower, (lower[0]+lower[1]), (lower[-2]+lower[-1]), len(lower)+3, len(lower)-3)
            )
            results = cursor.fetchall()
            if len(results) == 0:
                query2 = cursor.execute(
                "SELECT * FROM Dictionary WHERE (Expression LIKE '{0}' OR Expression LIKE '{1}%' OR Expression LIKE '%{2}') AND (length(Expression) < {3} AND length(Expression) > {4})".format(lower, (lower[0]), (lower[-1]), len(lower)+3, len(lower)-3)
                )
                results = cursor.fetchall()
            best_word = get_close_matches(lower, (result[0] for result in results),cutoff=0.6)[0]
            cor = input('Did you mean %s? (Y/N)'  % best_word)
            if cor == 'Y':
                query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % best_word)
                results = cursor.fetchall() 
                for result in results:
                    line_break = '%s. ' %n + result[1] + '\n'
                    new_str += line_break
                    n += 1
            else:
                return 'error' 
        else:
            new_str += 'error'

        return new_str

    except IndexError:
        return 'error'



def start():
    stop = True
    while stop:
        word = input('Enter word: ')
        output = translate(word)
        if output == 'error':
            print('Word not found, please try again')
        else:
            print('Here is the translation:\n' + output + '\n Thank you!')
            stop = False
        

start()
