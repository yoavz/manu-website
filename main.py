from flask import Flask, render_template, redirect, request
app = Flask(__name__)

michael_score = 0
antonio_score = 0
wayne_score = 0

@app.route('/')
def hello():
	global michael_score
	return render_template('index.html', votesm=michael_score, votesa=antonio_score, votesw=wayne_score)

@app.route('/like', methods=['POST'])
def like():
	global michael_score
	global antonio_score
	global wayne_score

	for r in request.form.getlist('name'):
		if r == "michael":
			michael_score += 1
		if r == "wayne":
			wayne_score += 1
		if r == "antonio":
			antonio_score += 1


	return redirect('/')

@app.route('/unlike', methods=['POST'])
def unlike():
	global michael_score
	global antonio_score
	global wayne_score

	for r in request.form.getlist('name'):
		if r == "michael":
			if michael_score > 0:
				michael_score -= 1
		if r == "wayne":
			if wayne_score > 0:
				wayne_score -= 1
		if r == "antonio":
			if antonio_score > 0:
				antonio_score -= 1


	return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
