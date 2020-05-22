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