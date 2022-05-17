```python
# 연습을 위한 nltk 책 리스트 다운로드
import nltk
nltk.download("book", quiet=True)
from nltk.book import * 
```

    *** Introductory Examples for the NLTK Book ***
    Loading text1, ..., text9 and sent1, ..., sent9
    Type the name of the text or sentence to view it.
    Type: 'texts()' or 'sents()' to list the materials.
    text1: Moby Dick by Herman Melville 1851
    text2: Sense and Sensibility by Jane Austen 1811
    text3: The Book of Genesis
    text4: Inaugural Address Corpus
    text5: Chat Corpus
    text6: Monty Python and the Holy Grail
    text7: Wall Street Journal
    text8: Personals Corpus
    text9: The Man Who Was Thursday by G . K . Chesterton 1908
    


```python
# 책 리스트 확인
nltk.corpus.gutenberg.fileids()
```




    ['austen-emma.txt',
     'austen-persuasion.txt',
     'austen-sense.txt',
     'bible-kjv.txt',
     'blake-poems.txt',
     'bryant-stories.txt',
     'burgess-busterbrown.txt',
     'carroll-alice.txt',
     'chesterton-ball.txt',
     'chesterton-brown.txt',
     'chesterton-thursday.txt',
     'edgeworth-parents.txt',
     'melville-moby_dick.txt',
     'milton-paradise.txt',
     'shakespeare-caesar.txt',
     'shakespeare-hamlet.txt',
     'shakespeare-macbeth.txt',
     'whitman-leaves.txt']




```python
# 이상한나라의 앨리스 데이터 가져오기
alice = nltk.corpus.gutenberg.raw("carroll-alice.txt")
print(alice[:1000])
```

    [Alice's Adventures in Wonderland by Lewis Carroll 1865]
    
    CHAPTER I. Down the Rabbit-Hole
    
    Alice was beginning to get very tired of sitting by her sister on the
    bank, and of having nothing to do: once or twice she had peeped into the
    book her sister was reading, but it had no pictures or conversations in
    it, 'and what is the use of a book,' thought Alice 'without pictures or
    conversation?'
    
    So she was considering in her own mind (as well as she could, for the
    hot day made her feel very sleepy and stupid), whether the pleasure
    of making a daisy-chain would be worth the trouble of getting up and
    picking the daisies, when suddenly a White Rabbit with pink eyes ran
    close by her.
    
    There was nothing so VERY remarkable in that; nor did Alice think it so
    VERY much out of the way to hear the Rabbit say to itself, 'Oh dear!
    Oh dear! I shall be late!' (when she thought it over afterwards, it
    occurred to her that she ought to have wondered at this, but at the time
    it all seemed quite natural); but
    


```python
# 토큰화
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# 3글자 이상, 알파벳 및 숫자만 가져옴
tokenizer = RegexpTokenizer("[\w']{3,}")
# 소문자로 변환
tokens = tokenizer.tokenize(alice.lower())
# 불용어 사전에 있는 단어들 제외
english_stops = set(stopwords.words('english'))
result = [word for word in tokens if word not in english_stops]
```


```python
result[10000:10010]
```




    ['work',
     'shaking',
     'punching',
     'back',
     'last',
     'mock',
     'turtle',
     'recovered',
     'voice',
     'tears']




```python
# 어간추출

# 포터 스테머
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
porter = [stemmer.stem(token) for token in result]
```


```python
porter[10000:10010]
```




    ['work',
     'shake',
     'punch',
     'back',
     'last',
     'mock',
     'turtl',
     'recov',
     'voic',
     'tear']




```python
from nltk.stem import LancasterStemmer
stemmer = LancasterStemmer()
lancaster = [stemmer.stem(token) for token in result]
```


```python
lancaster[10000:10010]
```




    ['work',
     'shak',
     'punch',
     'back',
     'last',
     'mock',
     'turtl',
     'recov',
     'voic',
     'tear']




```python
# 표제어 추출

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
lemma = [lemmatizer.lemmatize(token) for token in result]
```


```python
lemma[10000:10010]
```




    ['work',
     'shaking',
     'punching',
     'back',
     'last',
     'mock',
     'turtle',
     'recovered',
     'voice',
     'tear']




```python
# NLTK를 활용한 품사 태깅
import nltk
from nltk.tokenize import word_tokenize

# 추출한 표제어에 품사를 태깅한다
tagging = nltk.pos_tag(lemma)
```


```python
tagging[10000:10010]
```




    [('work', 'NN'),
     ('shaking', 'VBG'),
     ('punching', 'VBG'),
     ('back', 'RB'),
     ('last', 'JJ'),
     ('mock', 'NN'),
     ('turtle', 'NN'),
     ('recovered', 'VBD'),
     ('voice', 'JJ'),
     ('tear', 'IN')]




```python
nltk.help.upenn_tagset("NNP")
```

    NNP: noun, proper, singular
        Motown Venneboerger Czestochwa Ranzer Conchita Trumplane Christos
        Oceanside Escobar Kreisler Sawyer Cougar Yvette Ervin ODI Darryl CTCA
        Shannon A.K.C. Meltex Liverpool ...
    


```python
# 명사, 동사 리스트 만들기
noun_list = [a[0] for a in tagging if a[1]=="NN"]
verb_list = [a[0] for a in tagging if a[1]=="VBG"]
```


```python
# Scikit-Learn 자연어 분석 시 같은 토큰이라도 품사가 다르면 다른 토큰으로 처리해야 함
# 원래의 토큰과 품사를 붙여서 새로운 토큰이름을 만들면, 철자가 같고 품사가 다른 단어를 구분할 수 있다.

def tokenizer(doc):
    return ["/".join(p) for p in tagging]

b = tokenizer(tagging) 
b[10000:10010]
```




    ['work/NN',
     'shaking/VBG',
     'punching/VBG',
     'back/RB',
     'last/JJ',
     'mock/NN',
     'turtle/NN',
     'recovered/VBD',
     'voice/JJ',
     'tear/IN']




```python
# 각 단어의 사용빈도를 보여줌

from nltk import Text
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt 

retokenize = RegexpTokenizer("[\w]+")

text = Text(retokenize.tokenize(alice.lower))
text.plot(20)
plt.show()
```


    
![output_16_0](https://user-images.githubusercontent.com/52664532/168908653-fbe0a1b9-c5b0-47b6-a8a0-42b53d08d365.png)

    



```python
text = Text(noun_list)
text.plot(20)
plt.show()
```


    
![output_17_0](https://user-images.githubusercontent.com/52664532/168908763-4341774d-3bce-4514-908e-cf27e5b14efe.png)

    



```python
text = Text(verb_list)
text.plot(20)
plt.show()
```


    
![output_18_0](https://user-images.githubusercontent.com/52664532/168908792-4b833d5e-99e1-4ac3-878f-62be5e6a9f62.png)

    



```python
text = Text(b)
text.plot(20)
plt.show()
```


![output_19_0](https://user-images.githubusercontent.com/52664532/168908831-d43bf55f-b6f3-410c-96c3-3c88a2e5fa74.png)




```python
# 등장인물이 스토리의 어디에 등장하는지 시각적으로 확인할 수 있다.

text = Text(retokenize.tokenize(alice.lower()))
text.dispersion_plot(["alice", "rabbit", "queen", "turtle", "mouse","gryphon", "caterpillar", "hatter"])
```


    
![output_20_0](https://user-images.githubusercontent.com/52664532/168908854-c195ecc8-bd55-4f02-9237-5dffc901f239.png)




```python
text.concordance("queen")
```

    Displaying 25 of 75 matches:
    r the duchess an invitation from the queen to play croquet the frog footman rep
    order of the words a little from the queen an invitation for the duchess to pla
    d get ready to play croquet with the queen and she hurried out of the room the 
    the cat do you play croquet with the queen to day i should like it very much sa
    as at the great concert given by the queen of hearts and i had to sing twinkle 
    first verse said the hatter when the queen jumped up and bawled out he s murder
     the cool fountains chapter viii the queen s croquet ground a large rose tree s
    etter not talk said five i heard the queen say only yesterday you deserved to b
    a white one in by mistake and if the queen was to find it out we should all hav
    ing across the garden called out the queen the queen and the three gardeners in
     the garden called out the queen the queen and the three gardeners instantly th
     alice looked round eager to see the queen first came ten soldiers carrying clu
    s grand procession came the king and queen of hearts alice was rather doubtful 
    ll stopped and looked at her and the queen said severely who is this she said i
    d and smiled in reply idiot said the queen tossing her head impatiently and tur
    d of them and who are these said the queen pointing to the three gardeners who 
    courage it s no business of mine the queen turned crimson with fury and after g
    ce very loudly and decidedly and the queen was silent the king laid his hand up
    ider my dear she is only a child the queen turned angrily away from him and sai
    efully with one foot get up said the queen in a shrill loud voice and the three
     up and began bowing to the king the queen the royal children and everybody els
    ody else leave off that screamed the queen you make me giddy and then turning t
     spoke we were trying i see said the queen who had meanwhile been examining the
    hers are their heads off shouted the queen their heads are gone if it please yo
    ed in reply that s right shouted the queen can you play croquet the soldiers we
    


```python
# 주어진 단어 대신 사용된 횟수가 높은 단어를 찾음
text.similar("queen")
```

    king duchess gryphon hatter mouse dormouse way cook rabbit cat other
    dodo jury caterpillar pigeon baby sea knave first house
    


```python
# 두 단어의 공통 문맥
text.common_contexts(["king", "queen"])
```

    the_and the_said the_the the_s the_say the_was the_put the_it the_i
    the_in the_who the_turned the_had the_added
    


```python
# 단어(토큰)의 사용빈도 확인
fd = text.vocab()
print(type(fd))

from nltk import FreqDist
from nltk.tag import pos_tag
stopwords = ["Mr.", "Mrs.", "Miss", "Mr", "Mrs", "Dear"]
alice_tokens = pos_tag(retokenize.tokenize(alice))

# 고유대명사
names_list = [t[0] for t in alice_tokens if t[1] == "NNP" and t[0] not in stopwords]
fd_names = FreqDist(names_list)
```

    <class 'nltk.probability.FreqDist'>
    


```python
fd_names.N(), fd_names["Alice"], fd_names.freq("Alice")
```




    (1981, 0, 0.0)




```python
fd_names
```




    FreqDist({'Alice': 391, 'Queen': 73, 'King': 60, 'Turtle': 58, 'Mock': 56, 'Hatter': 55, 'Gryphon': 55, 'Duchess': 42, 'Dormouse': 40, 'Rabbit': 38, ...})




```python
fd_names.most_common(5)
```




    [('Alice', 391), ('Queen', 73), ('King', 60), ('Turtle', 58), ('Mock', 56)]




```python
# 워드클라우드
from wordcloud import WordCloud

wc = WordCloud(width=1000, height=600, background_color="white", random_state=0)
plt.imshow(wc.generate_from_frequencies(fd_names))
plt.axis("off")
plt.show()
```


![output_28_0](https://user-images.githubusercontent.com/52664532/168908881-e9726063-2219-49b6-8c6e-c929409e2ac1.png)


