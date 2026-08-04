from pathlib import Path

readme_path = Path("README-pt-BR.md")
contributing_path = Path("CONTRIBUTING-pt-BR.md")

readme = readme_path.read_text(encoding="utf-8")
contributing = contributing_path.read_text(encoding="utf-8")

additional_anchor = '<a id="outras-perguntas-de-entrevista-de-design-de-sistemas"></a>'
architectures_anchor = '<a id="arquiteturas-do-mundo-real"></a>'
company_anchor = '<a id="arquiteturas-de-empresas"></a>'
blogs_anchor = '<a id="blogs-de-engenharia-de-empresas"></a>'

if any(anchor in readme for anchor in (additional_anchor, architectures_anchor, company_anchor, blogs_anchor)):
    raise RuntimeError("As seções de perguntas adicionais e arquiteturas já foram adicionadas")

replacements = {
    "README.md#additional-system-design-interview-questions": "#outras-perguntas-de-entrevista-de-design-de-sistemas",
    "README.md#real-world-architectures": "#arquiteturas-do-mundo-real",
    "README.md#company-architectures": "#arquiteturas-de-empresas",
    "README.md#company-engineering-blogs": "#blogs-de-engenharia-de-empresas",
}
for old, new in replacements.items():
    readme = readme.replace(old, new)

marker = "\n## Status da tradução\n"
if marker not in readme:
    raise RuntimeError("Marcador de status não encontrado")

translated = r'''
<a id="outras-perguntas-de-entrevista-de-design-de-sistemas"></a>
### Outras perguntas de entrevista de design de sistemas

> Perguntas comuns de entrevista de design de sistemas, com links para recursos que ajudam a resolver cada uma delas.

| Pergunta | Referência(s) |
|---|---|
| Projete um serviço de sincronização de arquivos como o Dropbox | [youtube.com](https://www.youtube.com/watch?v=PE4gwstWhmc) |
| Projete um mecanismo de busca como o Google | [queue.acm.org](http://queue.acm.org/detail.cfm?id=988407)<br/>[stackexchange.com](http://programmers.stackexchange.com/questions/38324/interview-question-how-would-you-implement-google-search)<br/>[ardendertat.com](http://www.ardendertat.com/2012/01/11/implementing-search-engines/)<br/>[stanford.edu](http://infolab.stanford.edu/~backrub/google.html) |
| Projete um rastreador web escalável como o Google | [quora.com](https://www.quora.com/How-can-I-build-a-web-crawler-from-scratch) |
| Projete o Google Docs | [code.google.com](https://code.google.com/p/google-mobwrite/)<br/>[neil.fraser.name](https://neil.fraser.name/writing/sync/) |
| Projete um armazenamento chave-valor como o Redis | [codecapsule.com](http://codecapsule.com/2012/11/07/ikvs-implementing-a-key-value-store-table-of-contents/)<br/>[allthingsdistributed.com](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) |
| Projete um sistema de cache como o Memcached | [slideshare.net](http://www.slideshare.net/oemebamo/introduction-to-memcached) |
| Projete um sistema de recomendação como o da Amazon | [hulu.com](https://web.archive.org/web/20170406065247/http://tech.hulu.com/blog/2011/09/19/recommendation-system.html)<br/>[ijcai13.org](http://ijcai13.org/files/tutorial_slides/td3.pdf) |
| Projete um sistema de URLs curtas como o Bitly | [n00tc0d3r.blogspot.com](http://n00tc0d3r.blogspot.com/) |
| Projete um aplicativo de chat como o WhatsApp | [highscalability.com](http://highscalability.com/blog/2014/2/26/the-whatsapp-architecture-facebook-bought-for-19-billion.html) |
| Projete um sistema de compartilhamento de imagens como o Instagram | [highscalability.com](http://highscalability.com/flickr-architecture)<br/>[highscalability.com](http://highscalability.com/blog/2011/12/6/instagram-architecture-14-million-users-terabytes-of-photos.html) |
| Projete a funcionalidade de feed de notícias do Facebook | [quora.com](http://www.quora.com/What-are-best-practices-for-building-something-like-a-News-Feed)<br/>[quora.com](http://www.quora.com/Activity-Streams/What-are-the-scaling-issues-to-keep-in-mind-while-developing-a-social-network-feed)<br/>[slideshare.net](http://www.slideshare.net/danmckinley/etsy-activity-feeds-architecture) |
| Projete a funcionalidade de timeline do Facebook | [facebook.com](https://www.facebook.com/note.php?note_id=10150468255628920)<br/>[highscalability.com](http://highscalability.com/blog/2012/1/23/facebook-timeline-brought-to-you-by-the-power-of-denormaliza.html) |
| Projete a funcionalidade de chat do Facebook | [erlang-factory.com](http://www.erlang-factory.com/upload/presentations/31/EugeneLetuchy-ErlangatFacebook.pdf)<br/>[facebook.com](https://www.facebook.com/note.php?note_id=14218138919&id=9445547199&index=0) |
| Projete uma funcionalidade de busca em grafos como a do Facebook | [facebook.com](https://www.facebook.com/notes/facebook-engineering/under-the-hood-building-out-the-infrastructure-for-graph-search/10151347573598920)<br/>[facebook.com](https://www.facebook.com/notes/facebook-engineering/under-the-hood-indexing-and-ranking-in-graph-search/10151361720763920)<br/>[facebook.com](https://www.facebook.com/notes/facebook-engineering/under-the-hood-the-natural-language-interface-of-graph-search/10151432733048920) |
| Projete uma rede de distribuição de conteúdo como a Cloudflare | [figshare.com](https://figshare.com/articles/Globally_distributed_content_delivery/6605972) |
| Projete um sistema de tópicos em alta como o do Twitter | [michael-noll.com](http://www.michael-noll.com/blog/2013/01/18/implementing-real-time-trending-topics-in-storm/)<br/>[snikolov.wordpress.com](http://snikolov.wordpress.com/2012/11/14/early-detection-of-twitter-trends/) |
| Projete um sistema de geração de identificadores aleatórios | [blog.twitter.com](https://blog.twitter.com/2010/announcing-snowflake)<br/>[github.com](https://github.com/twitter/snowflake/) |
| Retorne as k requisições mais frequentes durante um intervalo de tempo | [cs.ucsb.edu](https://www.cs.ucsb.edu/sites/default/files/documents/2005-23.pdf)<br/>[wpi.edu](http://davis.wpi.edu/xmdv/docs/EDBT11-diyang.pdf) |
| Projete um sistema que forneça dados a partir de vários data centers | [highscalability.com](http://highscalability.com/blog/2009/8/24/how-google-serves-data-from-multiple-datacenters.html) |
| Projete um jogo de cartas multiplayer on-line | [indieflashblog.com](https://web.archive.org/web/20180929181117/http://www.indieflashblog.com/how-to-create-an-asynchronous-multiplayer-game.html)<br/>[buildnewgames.com](http://buildnewgames.com/real-time-multiplayer/) |
| Projete um sistema de coleta de lixo | [stuffwithstuff.com](http://journal.stuffwithstuff.com/2013/12/08/babys-first-garbage-collector/)<br/>[washington.edu](http://courses.cs.washington.edu/courses/csep521/07wi/prj/rick.pdf) |
| Projete um limitador de taxa para APIs | [stripe.com](https://stripe.com/blog/rate-limiters) |
| Projete uma bolsa de valores, como NASDAQ ou Binance | [Jane Street](https://youtu.be/b1e4t2k2KJY)<br/>[Golang Implementation](https://around25.com/blog/building-a-trading-engine-for-a-crypto-exchange/)<br/>[Go Implementation](http://bhomnick.net/building-a-simple-limit-order-in-go/) |
| Adicione uma pergunta de design de sistemas | [Contribua](#como-contribuir) |

<a id="arquiteturas-do-mundo-real"></a>
### Arquiteturas do mundo real

> Artigos sobre como sistemas do mundo real são projetados.

<p align="center">
  <img src="images/TcUo2fw.png">
  <br/>
  <i><a href="https://www.infoq.com/presentations/Twitter-Timeline-Scalability">Fonte: Twitter timelines at scale</a></i>
</p>

**Não se concentre nos detalhes minuciosos dos artigos a seguir. Em vez disso:**

* identifique princípios compartilhados, tecnologias comuns e padrões presentes nos artigos;
* estude quais problemas cada componente resolve, onde funciona e onde não funciona;
* revise as lições aprendidas.

| Tipo | Sistema | Referência(s) |
|---|---|---|
| Processamento de dados | **MapReduce** — processamento distribuído de dados do Google | [research.google.com](http://static.googleusercontent.com/media/research.google.com/zh-CN/us/archive/mapreduce-osdi04.pdf) |
| Processamento de dados | **Spark** — processamento distribuído de dados da Databricks | [slideshare.net](http://www.slideshare.net/AGrishchenko/apache-spark-architecture) |
| Processamento de dados | **Storm** — processamento distribuído de dados do Twitter | [slideshare.net](http://www.slideshare.net/previa/storm-16094009) |
| | | |
| Armazenamento de dados | **Bigtable** — banco de dados distribuído orientado a colunas do Google | [harvard.edu](http://www.read.seas.harvard.edu/~kohler/class/cs239-w08/chang06bigtable.pdf) |
| Armazenamento de dados | **HBase** — implementação open source do Bigtable | [slideshare.net](http://www.slideshare.net/alexbaranau/intro-to-hbase) |
| Armazenamento de dados | **Cassandra** — banco de dados distribuído orientado a colunas do Facebook | [slideshare.net](http://www.slideshare.net/planetcassandra/cassandra-introduction-features-30103666) |
| Armazenamento de dados | **DynamoDB** — banco de dados orientado a documentos da Amazon | [harvard.edu](http://www.read.seas.harvard.edu/~kohler/class/cs239-w08/decandia07dynamo.pdf) |
| Armazenamento de dados | **MongoDB** — banco de dados orientado a documentos | [slideshare.net](http://www.slideshare.net/mdirolf/introduction-to-mongodb) |
| Armazenamento de dados | **Spanner** — banco de dados globalmente distribuído do Google | [research.google.com](http://research.google.com/archive/spanner-osdi2012.pdf) |
| Armazenamento de dados | **Memcached** — sistema distribuído de cache em memória | [slideshare.net](http://www.slideshare.net/oemebamo/introduction-to-memcached) |
| Armazenamento de dados | **Redis** — sistema distribuído de cache em memória com persistência e tipos de valores | [slideshare.net](http://www.slideshare.net/dvirsky/introduction-to-redis) |
| | | |
| Sistema de arquivos | **Google File System — GFS** — sistema de arquivos distribuído | [research.google.com](http://static.googleusercontent.com/media/research.google.com/zh-CN/us/archive/gfs-sosp2003.pdf) |
| Sistema de arquivos | **Hadoop File System — HDFS** — implementação open source do GFS | [apache.org](http://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html) |
| | | |
| Diversos | **Chubby** — serviço de bloqueio para sistemas distribuídos fracamente acoplados do Google | [research.google.com](http://static.googleusercontent.com/external_content/untrusted_dlcp/research.google.com/en/us/archive/chubby-osdi06.pdf) |
| Diversos | **Dapper** — infraestrutura de rastreamento de sistemas distribuídos | [research.google.com](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36356.pdf) |
| Diversos | **Kafka** — fila de mensagens publish/subscribe do LinkedIn | [slideshare.net](http://www.slideshare.net/mumrah/kafka-talk-tri-hug) |
| Diversos | **ZooKeeper** — infraestrutura e serviços centralizados que permitem sincronização | [slideshare.net](http://www.slideshare.net/sauravhaloi/introduction-to-apache-zookeeper) |
| | Adicione uma arquitetura | [Contribua](#como-contribuir) |

<a id="arquiteturas-de-empresas"></a>
### Arquiteturas de empresas

| Empresa | Referência(s) |
|---|---|
| Amazon | [Amazon architecture](http://highscalability.com/amazon-architecture) |
| Cinchcast | [Producing 1,500 hours of audio every day](http://highscalability.com/blog/2012/7/16/cinchcast-architecture-producing-1500-hours-of-audio-every-d.html) |
| DataSift | [Realtime datamining At 120,000 tweets per second](http://highscalability.com/blog/2011/11/29/datasift-architecture-realtime-datamining-at-120000-tweets-p.html) |
| Dropbox | [How we've scaled Dropbox](https://www.youtube.com/watch?v=PE4gwstWhmc) |
| ESPN | [Operating At 100,000 duh nuh nuhs per second](http://highscalability.com/blog/2013/11/4/espns-architecture-at-scale-operating-at-100000-duh-nuh-nuhs.html) |
| Google | [Google architecture](http://highscalability.com/google-architecture) |
| Instagram | [14 million users, terabytes of photos](http://highscalability.com/blog/2011/12/6/instagram-architecture-14-million-users-terabytes-of-photos.html)<br/>[What powers Instagram](http://instagram-engineering.tumblr.com/post/13649370142/what-powers-instagram-hundreds-of-instances) |
| Justin.tv | [Justin.Tv's live video broadcasting architecture](http://highscalability.com/blog/2010/3/16/justintvs-live-video-broadcasting-architecture.html) |
| Facebook | [Scaling memcached at Facebook](https://cs.uwaterloo.ca/~brecht/courses/854-Emerging-2014/readings/key-value/fb-memcached-nsdi-2013.pdf)<br/>[TAO: Facebook’s distributed data store for the social graph](https://cs.uwaterloo.ca/~brecht/courses/854-Emerging-2014/readings/data-store/tao-facebook-distributed-datastore-atc-2013.pdf)<br/>[Facebook’s photo storage](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Beaver.pdf)<br/>[How Facebook Live Streams To 800,000 Simultaneous Viewers](http://highscalability.com/blog/2016/6/27/how-facebook-live-streams-to-800000-simultaneous-viewers.html) |
| Flickr | [Flickr architecture](http://highscalability.com/flickr-architecture) |
| Mailbox | [From 0 to one million users in 6 weeks](http://highscalability.com/blog/2013/6/18/scaling-mailbox-from-0-to-one-million-users-in-6-weeks-and-1.html) |
| Netflix | [A 360 Degree View Of The Entire Netflix Stack](http://highscalability.com/blog/2015/11/9/a-360-degree-view-of-the-entire-netflix-stack.html)<br/>[Netflix: What Happens When You Press Play?](http://highscalability.com/blog/2017/12/11/netflix-what-happens-when-you-press-play.html) |
| Pinterest | [From 0 To 10s of billions of page views a month](http://highscalability.com/blog/2013/4/15/scaling-pinterest-from-0-to-10s-of-billions-of-page-views-a.html)<br/>[18 million visitors, 10x growth, 12 employees](http://highscalability.com/blog/2012/5/21/pinterest-architecture-update-18-million-visitors-10x-growth.html) |
| Playfish | [50 million monthly users and growing](http://highscalability.com/blog/2010/9/21/playfishs-social-gaming-architecture-50-million-monthly-user.html) |
| PlentyOfFish | [PlentyOfFish architecture](http://highscalability.com/plentyoffish-architecture) |
| Salesforce | [How they handle 1.3 billion transactions a day](http://highscalability.com/blog/2013/9/23/salesforce-architecture-how-they-handle-13-billion-transacti.html) |
| Stack Overflow | [Stack Overflow architecture](http://highscalability.com/blog/2009/8/5/stack-overflow-architecture.html) |
| TripAdvisor | [40M visitors, 200M dynamic page views, 30TB data](http://highscalability.com/blog/2011/6/27/tripadvisor-architecture-40m-visitors-200m-dynamic-page-view.html) |
| Tumblr | [15 billion page views a month](http://highscalability.com/blog/2012/2/13/tumblr-architecture-15-billion-page-views-a-month-and-harder.html) |
| Twitter | [Making Twitter 10000 percent faster](http://highscalability.com/scaling-twitter-making-twitter-10000-percent-faster)<br/>[Storing 250 million tweets a day using MySQL](http://highscalability.com/blog/2011/12/19/how-twitter-stores-250-million-tweets-a-day-using-mysql.html)<br/>[150M active users, 300K QPS, a 22 MB/S firehose](http://highscalability.com/blog/2013/7/8/the-architecture-twitter-uses-to-deal-with-150m-active-users.html)<br/>[Timelines at scale](https://www.infoq.com/presentations/Twitter-Timeline-Scalability)<br/>[Big and small data at Twitter](https://www.youtube.com/watch?v=5cKTP36HVgI)<br/>[Operations at Twitter: scaling beyond 100 million users](https://www.youtube.com/watch?v=z8LU0Cj6BOU)<br/>[How Twitter Handles 3,000 Images Per Second](http://highscalability.com/blog/2016/4/20/how-twitter-handles-3000-images-per-second.html) |
| Uber | [How Uber scales their real-time market platform](http://highscalability.com/blog/2015/9/14/how-uber-scales-their-real-time-market-platform.html)<br/>[Lessons Learned From Scaling Uber To 2000 Engineers, 1000 Services, And 8000 Git Repositories](http://highscalability.com/blog/2016/10/12/lessons-learned-from-scaling-uber-to-2000-engineers-1000-ser.html) |
| WhatsApp | [The WhatsApp architecture Facebook bought for $19 billion](http://highscalability.com/blog/2014/2/26/the-whatsapp-architecture-facebook-bought-for-19-billion.html) |
| YouTube | [YouTube scalability](https://www.youtube.com/watch?v=w5WVu624fY8)<br/>[YouTube architecture](http://highscalability.com/youtube-architecture) |

<a id="blogs-de-engenharia-de-empresas"></a>
### Blogs de engenharia de empresas

> Arquiteturas das empresas nas quais você está participando de processos seletivos.
>
> As perguntas encontradas podem pertencer ao mesmo domínio de negócio.

* [Airbnb Engineering](http://nerds.airbnb.com/)
* [Atlassian Developers](https://developer.atlassian.com/blog/)
* [AWS Blog](https://aws.amazon.com/blogs/aws/)
* [Bitly Engineering Blog](http://word.bitly.com/)
* [Box Blogs](https://blog.box.com/blog/category/engineering)
* [Cloudera Developer Blog](http://blog.cloudera.com/)
* [Dropbox Tech Blog](https://tech.dropbox.com/)
* [Engineering at Quora](https://www.quora.com/q/quoraengineering)
* [Ebay Tech Blog](http://www.ebaytechblog.com/)
* [Evernote Tech Blog](https://blog.evernote.com/tech/)
* [Etsy Code as Craft](http://codeascraft.com/)
* [Facebook Engineering](https://www.facebook.com/Engineering)
* [Flickr Code](http://code.flickr.net/)
* [Foursquare Engineering Blog](http://engineering.foursquare.com/)
* [GitHub Engineering Blog](https://github.blog/category/engineering)
* [Google Research Blog](http://googleresearch.blogspot.com/)
* [Groupon Engineering Blog](https://engineering.groupon.com/)
* [Heroku Engineering Blog](https://engineering.heroku.com/)
* [Hubspot Engineering Blog](http://product.hubspot.com/blog/topic/engineering)
* [High Scalability](http://highscalability.com/)
* [Instagram Engineering](http://instagram-engineering.tumblr.com/)
* [Intel Software Blog](https://software.intel.com/en-us/blogs/)
* [Jane Street Tech Blog](https://blogs.janestreet.com/category/ocaml/)
* [LinkedIn Engineering](http://engineering.linkedin.com/blog)
* [Microsoft Engineering](https://engineering.microsoft.com/)
* [Microsoft Python Engineering](https://blogs.msdn.microsoft.com/pythonengineering/)
* [Netflix Tech Blog](http://techblog.netflix.com/)
* [Paypal Developer Blog](https://developer.paypal.com/community/blog/)
* [Pinterest Engineering Blog](https://medium.com/@Pinterest_Engineering)
* [Reddit Blog](http://www.redditblog.com/)
* [Salesforce Engineering Blog](https://developer.salesforce.com/blogs/engineering/)
* [Slack Engineering Blog](https://slack.engineering/)
* [Spotify Labs](https://labs.spotify.com/)
* [Stripe Engineering Blog](https://stripe.com/blog/engineering)
* [Twilio Engineering Blog](http://www.twilio.com/engineering)
* [Twitter Engineering](https://blog.twitter.com/engineering/)
* [Uber Engineering Blog](http://eng.uber.com/)
* [Yahoo Engineering Blog](http://yahooeng.tumblr.com/)
* [Yelp Engineering Blog](http://engineeringblog.yelp.com/)
* [Zynga Engineering Blog](https://www.zynga.com/blogs/engineering)

#### Fontes e leituras complementares

Deseja adicionar um blog? Para evitar duplicação de trabalho, considere adicionar o blog da sua empresa ao repositório abaixo:

* [kilimchoi/engineering-blogs](https://github.com/kilimchoi/engineering-blogs)
'''

readme = readme.replace(marker, "\n" + translated.strip() + "\n" + marker, 1)

old_status = "- [ ] perguntas adicionais, arquiteturas e blogs de engenharia;"
new_status = "- [x] perguntas adicionais, arquiteturas e blogs de engenharia;"
if old_status not in readme:
    raise RuntimeError("Linha de status esperada não encontrada")
readme = readme.replace(old_status, new_status, 1)

glossary_marker = "| call center | central de atendimento |"
glossary_addition = """| call center | central de atendimento |
| file sync service | serviço de sincronização de arquivos |
| recommendation system | sistema de recomendação |
| rate limiter | limitador de taxa |
| real-world architecture | arquitetura do mundo real |
| data processing | processamento de dados |
| data store | armazenamento de dados |
| file system | sistema de arquivos |
| company engineering blog | blog de engenharia de empresa |"""
if glossary_marker not in contributing:
    raise RuntimeError("Marcador do glossário não encontrado")
contributing = contributing.replace(glossary_marker, glossary_addition, 1)

readme_path.write_text(readme.rstrip() + "\n", encoding="utf-8")
contributing_path.write_text(contributing.rstrip() + "\n", encoding="utf-8")
