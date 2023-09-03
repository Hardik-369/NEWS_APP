from flask import Flask, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)

# Initialize NewsApiClient with your API Key
newsapi = NewsApiClient(api_key='1c130d1fae9c482ea447c08c2df21daf')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_query = request.form['query']
        
        # Get top headlines based on user query
        top_headlines = newsapi.get_top_headlines(q=user_query,
                                                  language='en',
                                                  country='us')
        top_headlines = top_headlines['articles'][:10]

        # Get all articles based on user query
        all_articles = newsapi.get_everything(q=user_query,
                                              language='en',
                                              sort_by='relevancy')
        
        all_articles = all_articles['articles'][:10]

        return render_template('index.html', user_query=user_query, top_headlines=top_headlines, all_articles=all_articles)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
