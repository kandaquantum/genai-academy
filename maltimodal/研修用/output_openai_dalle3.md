# DALL·E 3 による画像生成入門

## はじめに

DALL·E 3 は、テキストプロンプトから画像を生成するための API です。この研修資料では、DALL·E 3 を使用して画像を生成する方法について学びます。

## 画像生成の基本

DALL·E 3 を使用して画像を生成するには、以下のパラメータを指定します：

- `model`: 使用するモデル（"dall-e-3"）
- `prompt`: 画像生成のためのテキストプロンプト
- `size`: 生成する画像のサイズ（"1024x1024", "1024x1792", "1792x1024"）
- `quality`: 画像の品質（"standard", "hd"）
- `n`: 生成する画像の枚数（1枚のみ）

## プログラムを実行させてみよう

### 例1: 白いシャム猫の画像を生成する

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

### 例2: プロンプトを使用して画像生成をコントロールする

```python
from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS: A red apple on a white table",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
```

## 問題

<details>
<summary>問題1: DALL·E 3 で生成できる画像の最大サイズは？</summary>

a. 512x512
b. 1792x1024
c. 1792x1792
d. 2048x2048

<details>
<summary>回答と解説</summary>

回答: b. 1792x1024

DALL·E 3 では、1024x1024, 1024x1792, 1792x1024 の3つのサイズから選択できます。最大サイズは 1792x1024 です。
</details>
</details>

<details>
<summary>問題2: DALL·E 3 で一度に生成できる画像の枚数は？</summary>

a. 1枚
b. 5枚
c. 10枚
d. 制限なし

<details>
<summary>回答と解説</summary>

回答: a. 1枚

DALL·E 3 では、一度のリクエストで生成できる画像は1枚のみです。複数の画像を生成するには、並列リクエストを送信する必要があります。
</details>
</details>

<details>
<summary>問題3: DALL·E 3 のデフォルトのプロンプト処理について正しいのは？</summary>

a. プロンプトは変更されない
b. プロンプトは自動的に書き換えられ、詳細が追加される
c. プロンプトは自動的に書き換えられ、詳細が削除される
d. プロンプトは無視される

<details>
<summary>回答と解説</summary>

回答: b. プロンプトは自動的に書き換えられ、詳細が追加される

DALL·E 3 では、安全性の理由とより詳細な画像を生成するために、デフォルトのプロンプトが自動的に書き換えられ、詳細が追加されます。この機能を無効にすることはできませんが、プロンプトを工夫することで、望む画像に近づけることができます。
</details>
</details>

## まとめ

この研修資料では、DALL·E 3 を使用して画像を生成する方法について学びました。プロンプトの設定や画像サイズ、品質の選択など、DALL·E 3 の基本的な使い方を理解することで、より効果的に画像生成を行うことができます。