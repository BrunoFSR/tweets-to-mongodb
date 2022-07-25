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

def conectaMongoDB(mydict):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                                    username='root',
                                    password='123456')
    mydb = myclient["tweets_db"]
    mycol = mydb["tweets"]

    mycol.insert_one(mydict)
    
class CapturaTweets(tweepy.StreamingClient):
    
    def on_response(self, tweet):
        data = tweet.data
        
        includes = tweet.includes
        users = includes["users"]
        users = {user["id"]: user for user in users}
            
        tweet_data = { 
            "tweet_ID":  data.id, 
            "usuario": users[data.author_id].username,
            "tweet": data.text
            }
        
        print(tweet_data)
            
        conectaMongoDB(tweet_data)
        
    
## implementation
bearer_token = configuraCredenciais()
query = "Pudim"

tweeter_stream = CapturaTweets(bearer_token)

## Limpando as rules, se existirem
rules = tweeter_stream.get_rules()

if rules.data != None: 
    rules_id = []
    for rule in rules.data:
        rules_id.append(rule[2])
        
    tweeter_stream.delete_rules(rules_id)

tweeter_stream.add_rules(tweepy.StreamRule(query))
tweeter_stream.add_rules(tweepy.StreamRule("-is:retweet"))

tweeter_stream.filter(expansions=["author_id"])
