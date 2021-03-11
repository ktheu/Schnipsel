## NLP

Mit den Paketen *spaCy* und *nltk*

### Spacy

Im Jupyter Notebook:

```
import spacy
!python -m spacy validate
!python -m spacy download en
!python -m spacy download de

```

pos = part-of-speech  = Sprachkomponente

Liste mit den pos-tags [hier](https://spacy.io/api/annotation#pos-tagging)


```
nlp = spacy.load(r"C:\Users\khthe\\.conda\envs\nlp\lib\site-packages\de_core_news_sm\de_core_news_sm-2.0.0")
```

```
id2word.token2id
id2word.id2token     # not filled until used
id2word.cfs          # dict id -> frequency of tokens
id2word.dfs          # dict id -> how many documents contain token
id2word.num_docs     # number of documents processed
id2word.num_nnz      # sum of the number of unique words per document over the entire corpus
```

```
model.get_document_topics(corpus[0])
model.get_term_topics(3)               # bringt nichts ?
model.get_topic_terms(0,topn=15)       # ids of most significant words for this topic
model.get_topics().shape                # topic-term matrix of shape num_topics, vocabulary_size
model.print_topic(0)
model.print_topics()
model.show_topic(0)
model.show_topics(formatted = False)
model.top_topics(corpus)
```