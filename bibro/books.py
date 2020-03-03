from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from bibro.auth import login_required
from bibro.db import get_db

bp = Blueprint('books', __name__)


@bp.route('/')
def index():
    db = get_db()
    books = db.execute(
        'SELECT id, author, published, publisher, title FROM books'
    ).fetchall()
    return render_template('books/index.html', books=books)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        author = request.form['author']
        published = request.form['published']
        publisher = request.form['publisher']
        title = request.form['title']

        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO books (author, published, publisher, title)'
                ' VALUES (?, ?, ?, ?)',
                (author, published, publisher, title)
            )
            db.commit()
            return redirect(url_for('books.index'))

    return render_template('books/create.html')


