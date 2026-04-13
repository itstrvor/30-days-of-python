from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis = None
    if request.method == 'POST':
        text = request.form['text_to_analyze']
        
        # --- Python Logic ---
        words = text.split()
        char_count = len(text)
        word_count = len(words)
        
        # Word Variety (Lexical Density)
        # Formula: (Unique Words / Total Words) * 100
        if word_count > 0:
            unique_words = set(words)
            variety = (len(unique_words) / word_count) * 100
        else:
            variety = 0

        analysis = {
            "word_count": word_count,
            "char_count": char_count,
            "variety": round(variety, 2)
        }

    return render_template('index.html', analysis=analysis)

if __name__ == '__main__':
    app.run(debug=True)