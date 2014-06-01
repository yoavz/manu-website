from flask import Flask, render_template, redirect, request
app = Flask(__name__)

michael_score = 0
antonio_score = 0
wayne_score = 0

players = [
	{
		"name": "michael",
		"score": 0,
	},
	{
		"name": "antonio",
		"score": 0
	},
	{
		"name": "wayne",
		"score": 0
	},
	{
		"name": "robin",
		"score": 0
	},
	{
		"name": "adnan",
		"score": 0	
	}
]

@app.route('/')
def hello():
	return render_template('index.html', data=players)

@app.route('/like', methods=['POST'])
def like():
	global players

	for r in request.form.getlist('name'):
		for player in players:
			if r == player['name']:
				player['score'] += 1

	return redirect('/')

@app.route('/unlike', methods=['POST'])
def unlike():
	global players

	for r in request.form.getlist('name'):
		for player in players:
			if r == player['name']:
				player['score'] -= 1
				if player['score'] < 0:
					player['score'] = 0


	return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
