Tweets to MongoDB

Esse projeto foi feito baseado no exercício do capitulo 2 do Livro Big Data - Técnicas e tecnologias para extração de valor dos dados da autora Rosangela Marquesone.
Originalmente o projeto deveria ser feita em linguagem Java, porem decidi fazer em Python para praticar a linguagem.

O objetivo era coletar os tweets com uma palavra chave e armazená-los no MongoDB. 
São coletado o tweet_ID, usuario e texto do tweet que contenha a palavra "Pudim", colocado num dict e armazenado numa collection do MongoDB.

Para a execução foram utilizados containeres com MongoDB e MongoExpress. Dessa forma, toda a execução do script fica melhor protegida de erros e problemas de compatibilidade, por exemplo. Durante a execução, também é criado um ambiente virtual Python e são baixadas todas as dependências necessárias para a execução.

Para executar, basta chamar o comando abaixo:

sh install.sh

O resultado pode ser visto na collection tweets dentro da base tweets_db criada no MongoDB em:
http://localhost:8081/db/tweets_db/tweets