from bibro import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    # books = db.execute(
    #     'SELECT id, title, author, publisher, publish_year FROM books'
    # ).fetchall()
    books = [
        {'title': 'The Collapsing Empire', 'author': 'John Scalzi', 'publisher': 'a', 'published': '2017'},
        {'title': "Mote in God's Eye", 'author': 'Larry Niven', 'publisher': 'b', 'published': '1998'},
        {'title': 'Red Moon', 'author': 'Kim Stanley Robinson', 'publisher': 'c', 'published': '2018'},
        {'title': 'The Consuming Fire', 'author': 'John Scalzi', 'publisher': 'd', 'published': '2018'}
    ]

    user = {'username': 'Eliad'}
    return render_template('index.html', title='Bibro', user=user, books=books)
