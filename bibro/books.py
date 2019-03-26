from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from werkzeug.security import generate_password_hash

from bibro.db import get_db

bp = Blueprint('books', __name__)


@bp.route('/')
def index():
    """Show all the posts, most recent first."""
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    books = [
        {'title': 'The Collapsing Empire', 'author': 'John Scalzi', 'published': '2017'},
        {'title': "Mote in God's Eye", 'author': 'Larry Niven', 'published': '1998'},
        {'title': 'Red Moon', 'author': 'Kim Stanley Robinson', 'published': '2018'},
        {'title': 'The Consuming Fire', 'author': 'John Scalzi', 'published': '2018'}
    ]

    return render_template('books/index.html', books=books)

