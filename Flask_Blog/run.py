from flaskblog import create_app

app = create_app()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if __name__ == '__main__':
    app.run(debug=True)



