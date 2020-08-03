from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # todo: add new book
    # todo: remove book
    # todo: display books table with paging, search and sort
    # todo: export books into file
    # todo: import books from file

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
