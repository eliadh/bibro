from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, g
)
from werkzeug.security import generate_password_hash
from bibro.auth import login_required
from bibro.db import get_db

bp = Blueprint('books', __name__)


@bp.route('/')
def index():
    """Show all the posts, most recent first."""
    db = get_db()
    books = db.execute(
        'SELECT id, title, author, publisher, publish_year FROM books'
    ).fetchall()
    # books = [
    #     {'title': 'The Collapsing Empire', 'author': 'John Scalzi', 'published': '2017'},
    #     {'title': "Mote in God's Eye", 'author': 'Larry Niven', 'published': '1998'},
    #     {'title': 'Red Moon', 'author': 'Kim Stanley Robinson', 'published': '2018'},
    #     {'title': 'The Consuming Fire', 'author': 'John Scalzi', 'published': '2018'}
    # ]

    return render_template('books/index.html', books=books)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publish_year = request.form['publish_year']
        error = None

        if not title:
            error = 'Title is required.'

        if not author:
            error = 'Author is required.'

        if not publish_year:
            error = 'Publish Year is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO books (title, author, publish_year)'
                ' VALUES (?, ?, ?)',
                (title, author, publish_year)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

