import edison

from flask import render_template


app = edison.app
db = edison.db

# Creates all tables defined in the database models and the only ones that are not created yet.
# If there's any change in the database models you should perform a migration to apply this change in the database itself.
# More about database migrations can be found in /edison/migrations/README.
db.create_all()

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
