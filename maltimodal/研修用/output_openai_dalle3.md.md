# OpenAI Images APIを使った画像生成

## はじめに
OpenAI Images APIを使うと、テキストプロンプトから画像を生成したり、既存の画像を編集・変換したりすることができます。このAPIは、DALL·E 3とDALL·E 2の2つのモデルをサポートしています。

## クイックスタート
以下は、DALL·E 3を使って画像を生成する最も簡単な例です。

```python
from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
```

このコードでは、"a white siamese cat"というプロンプトから1024x1024ピクセルの画像を1枚生成しています。生成された画像のURLは`image_url`変数に格納されます。

## プログラムを実行してみよう

### 例1: 複数の画像を生成する
以下のコードは、プロンプトから複数の画像を生成する例です。

```python
from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-2",
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=4,
  size="512x512"
)

for i, image in enumerate(response.data):
    print(f"Image {i+1} URL: {image.url}")
```

このコードでは、DALL·E 2を使って512x512ピクセルの画像を4枚生成しています。生成された各画像のURLが出力されます。

### 例2: 画像を編集する
以下のコードは、既存の画像の一部を編集する例です。

```python
from openai import OpenAI
client = OpenAI()

response = client.images.edit((
  model="dall-e-2",
  image=open("sunlit_lounge.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url = response.data[0].url
```

このコードでは、`sunlit_lounge.png`という画像の一部を`mask.png`で指定された領域だけ編集しています。編集後の画像は1024x1024ピクセルで生成され、そのURLが`image_url`変数に格納されます。

## 問題

<details>
<summary>1. DALL·E 3で生成できる画像の最大サイズは？</summary>

- [ ] 512x512ピクセル
- [ ] 1024x1024ピクセル
- [x] 1792x1024ピクセル
- [ ] 2048x2048ピクセル

DALL·E 3では、1024x1024、1024x1792、1792x1024ピクセルの画像を生成できます。
</details>

<details>
<summary>2. 画像編集（inpainting）で使用する画像とマスクのファイル形式は？</summary>

- [ ] JPEG
- [x] PNG
- [ ] GIF
- [ ] BMP

画像編集では、アップロードする画像とマスクは両方ともPNG形式である必要があります。
</details>

<details>
<summary>3. DALL·E 2を使って一度に生成できる画像の最大枚数は？</summary>

- [ ] 1枚
- [x] 10枚
- [ ] 20枚
- [ ] 50枚

DALL·E 2では、`n`パラメータを使って一度に最大10枚の画像を生成できます。
</details>