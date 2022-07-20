import toml
import tweepy
import pymongo

def configuraCredenciais():
    # abrir o arquivo com as credenciais de acesso
    with open('config.toml') as config:
    # ler o arquivo e salvar as chaves nas variáveis
        config = toml.loads(config.read())
        bearer_token = config['BEARERTOKEN']
    
    return bearer_token

def capturaTweets(bearer_token, query):
    client = tweepy.Client(bearer_token)
    response = client.search_recent_tweets(query=query,
                                       max_results = 100,
                                       expansions=["attachments.media_keys", "author_id"])

    tweets = response.data

    includes = response.includes
    users = includes["users"]

    users = {user["id"]: user for user in users}
    for tweet in tweets:
        tweet_data = { 
            "tweet_ID":  tweet.id, 
            "usuario": users[tweet.author_id].username,
            "tweet": tweet.text
            }
        
        conectaMongoDB(tweet_data)
    
def conectaMongoDB(mydict):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                                    username='root',
                                    password='123456')
    mydb = myclient["tweets_db"]
    mycol = mydb["tweets"]

    mycol.insert_one(mydict)
    
## implementation
bearer_token = configuraCredenciais()
query = "pudim"
capturaTweets(bearer_token, query)

