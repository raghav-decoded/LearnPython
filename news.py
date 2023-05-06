from newsapi import NewsApiClient
# import requests

# url = ('https://newsapi.org/v2/everything?'
#        'q=Apple&'
#        'from=2022-11-07&'
#        'sortBy=popularity&'
#        'apiKey=1b06170a85924114831bd80864b6c7fb')

# response = requests.get(url)

# print (response.text)

# Init
newsapi = NewsApiClient(api_key='1b06170a85924114831bd80864b6c7fb')

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(from_param='2017-12-01',to='2017-12-12')
#, sources='abc-news', category='business', language='en', country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',sources='bbc-news,the-verge',domains='bbc.co.uk,techcrunch.com',from_param='2022-11-07',to='2022-11-07',language='en',sort_by='relevancy',page=2)
print(all_articles)


# /v2/top-headlines/sources
sources = newsapi.get_sources()
