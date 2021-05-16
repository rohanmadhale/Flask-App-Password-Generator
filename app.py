from flask import Flask, render_template
import random
import pandas as pd

app = Flask(__name__)


@app.route('/')
def get_num():
    words = pd.read_csv('pass_phrase_words.txt',header=None)
    words[0] = words[0].astype(str)
    words = words[0].to_list()
    password = [i.capitalize() for i in random.sample(
        [i for i in words if len(i) == random.randint(2, 9)], k=3)] 
    password.append(str(random.randint(1, 9)))
    password[0:4] = ['-'.join(password[0:4])]
    password = str(password[0])
    pass_len = len(password)

    return (render_template('app.html', phrase = password, len = pass_len))
if __name__=='__main__':
    app.run()  
    
    
