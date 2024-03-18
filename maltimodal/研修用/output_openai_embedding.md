# OpenAIの埋め込みモデルを使いこなそう

## はじめに
OpenAIの埋め込みモデルは、テキストを数値ベクトルに変換することで、テキストの意味的な類似性を測定できるようにします。これにより、検索、クラスタリング、推薦システムなど、様々な用途に活用できます。

本研修資料では、OpenAIの埋め込みモデルの基本的な使い方から、具体的なユースケースまでを網羅的に学習します。Pythonのコード例を交えながら、実践的なスキルを身につけましょう。

## クイックスタート
まずは、OpenAIの埋め込みモデルを使って、簡単なテキストの埋め込みベクトルを取得してみましょう。

```python
from openai import OpenAI
client = OpenAI()

response = client.embeddings.create(
    input="OpenAIの埋め込みモデルを使ってみよう。",
    model="text-embedding-3-small"
)

print(response.data[0].embedding)
```

上記のコードでは、`text-embedding-3-small`モデルを使って、"OpenAIの埋め込みモデルを使ってみよう。"という文章の埋め込みベクトルを取得しています。出力結果は、浮動小数点数の配列になります。

## プログラムを実行してみよう
### 例1: 2つの文章の類似度を測定する
2つの文章の埋め込みベクトルを取得し、それらのコサイン類似度を計算することで、文章間の類似度を測定できます。

```python
from openai import OpenAI
from openai.embeddings_utils import cosine_similarity

client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
    return client.embeddings.create(input=[text], model=model).data[0].embedding

sentence1 = "私は犬が好きです。"
sentence2 = "私は猫が好きです。"

embedding1 = get_embedding(sentence1)
embedding2 = get_embedding(sentence2)

similarity = cosine_similarity(embedding1, embedding2)
print(f"類似度: {similarity}")
```

### 例2: 文章の検索
複数の文章の埋め込みベクトルを事前に計算しておき、クエリ文章の埋め込みベクトルとの類似度を計算することで、関連する文章を検索できます。

```python
from openai import OpenAI
from openai.embeddings_utils import cosine_similarity

client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
    return client.embeddings.create(input=[text], model=model).data[0].embedding

documents = [
    "犬は人間の最良の友です。",
    "猫は独立心が強い動物です。",
    "犬は忠実で愛情深い動物です。",
    "猫は狩猟本能を持っています。"
]

document_embeddings = [get_embedding(doc) for doc in documents]

query = "犬の特徴について教えてください。"
query_embedding = get_embedding(query)

similarities = [cosine_similarity(query_embedding, doc_embedding) for doc_embedding in document_embeddings]

most_similar_document_index = similarities.index(max(similarities))
print(f"最も関連する文章: {documents[most_similar_document_index]}")
```

## 問題
<details>
<summary>問題1: OpenAIの埋め込みモデルで使用できるモデルは？</summary>

a. text-embedding-2-small
b. text-embedding-3-small
c. text-embedding-4-small
d. text-embedding-5-small

<details>
<summary>回答と解説</summary>

回答: b. text-embedding-3-small

OpenAIでは現在、text-embedding-3-smallとtext-embedding-3-largeの2つの埋め込みモデルが提供されています。これらは最新かつ高性能なモデルです。

</details>
</details>

<details>
<summary>問題2: 埋め込みベクトルの類似度を測定するのに適した指標は？</summary>

a. ユークリッド距離
b. マンハッタン距離
c. コサイン類似度
d. ジャカード類似度

<details>
<summary>回答と解説</summary>

回答: c. コサイン類似度

埋め込みベクトルの類似度を測定する際は、コサイン類似度が一般的に使用されます。コサイン類似度は、ベクトルの方向の類似性を測定するため、ベクトルの長さに影響されません。

</details>
</details>

<details>
<summary>問題3: 埋め込みベクトルのサイズを減らすために使用できるパラメータは？</summary>

a. size
b. dimensions
c. length
d. reduce

<details>
<summary>回答と解説</summary>

回答: b. dimensions

OpenAIの埋め込みモデルでは、dimensionsパラメータを使用して埋め込みベクトルのサイズを減らすことができます。これにより、計算コストとメモリ使用量を削減できます。

</details>
</details>

以上で、OpenAIの埋め込みモデルの基本的な使い方と応用例を学習しました。これらの知識を活かして、様々なユースケースに埋め込みモデルを活用してみてください。