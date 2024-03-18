# OpenAI Assistants API入門

## はじめに
OpenAI Assistants APIを使うと、自分のアプリケーション内でAIアシスタントを構築することができます。アシスタントには命令を与えることができ、モデル、ツール、知識を活用してユーザーのクエリに応答します。現在、Assistants APIではCode Interpreter、Retrieval、Function callingの3種類のツールをサポートしています。

## クイックスタート
以下は、Code Interpreterを使用するアシスタントを作成して実行する主要なステップを説明した入門ガイドです。この例では、Code Interpreterツールを有効にした個人的な数学チューターであるアシスタントを作成します。

```python
from openai import OpenAI
from typing_extensions import override

client = OpenAI()

# Step 1: アシスタントの作成  
assistant = client.beta.assistants.create(
  name="Math Tutor",
  instructions="You are a personal math tutor. Write and run code to answer math questions.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4-turbo-preview",
)

# Step 2: スレッドの作成
thread = client.beta.threads.create()

# Step 3: スレッドへのメッセージ追加
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

# Step 4: ランの作成とストリーミング
class EventHandler(AssistantEventHandler):    
  @override
  def on_text_created(self, text) -> None:
    print(f"\nassistant > ", end="", flush=True)
      
  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)
      
  def on_tool_call_created(self, tool_call):
    print(f"\nassistant > {tool_call.type}\n", flush=True)
  
  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)
 
with client.beta.threads.runs.create_and_stream(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account.",
  event_handler=EventHandler(),
) as stream:
  stream.until_done()
```

## プログラムを実行してみよう
上記のコードを実行すると、アシスタントが数式を解くためのコードを書いて実行し、ユーザーに解答を提示します。ユーザーとのやりとりはスレッドに保存され、アシスタントはCode Interpreterツールを使ってユーザーの質問に応答します。

### 例1: 方程式の解法
ユーザー: "I need to solve the equation `2x - 5 = 7`. Can you help me?"

アシスタント: 
```python
# To solve the equation 2x - 5 = 7, we need to isolate the variable x on one side.

# Add 5 to both sides of the equation to get:
# 2x - 5 + 5 = 7 + 5
# 2x = 12

# Now divide both sides by 2 to solve for x:
# 2x / 2 = 12 / 2
# x = 6

# Therefore, the solution to the equation 2x - 5 = 7 is x = 6.
print("The solution to the equation 2x - 5 = 7 is x = 6.")
```

output >
The solution to the equation 2x - 5 = 7 is x = 6.

### 例2: 二次方程式の解法
ユーザー: "Can you help me find the roots of the quadratic equation `x^2 - 5x + 6 = 0`?"

アシスタント:
```python
import math

# The quadratic equation is of the form ax^2 + bx + c = 0
# In this case, a = 1, b = -5, and c = 6

a = 1
b = -5
c = 6

# To find the roots, we use the quadratic formula:
# x = (-b ± √(b^2 - 4ac)) / (2a)

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots are {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The root is {root}")
else:
    print("The equation has no real roots")
```

output >
The roots are 3.0 and 2.0

## 問題
<details>
<summary>問題1: Assistants APIで現在サポートされているツールの種類は？</summary>

a. Code Interpreter, Retrieval, Function calling
b. Code Interpreter, Image Generation, Retrieval  
c. Code Interpreter, Text Generation, Function calling
d. Text Generation, Image Generation, Audio Generation

<details>
<summary>回答と解説</summary>

回答: a. Code Interpreter, Retrieval, Function calling

Assistants APIは現在、Code Interpreter、Retrieval、Function callingの3種類のツールをサポートしています。

> The Assistants API currently supports three types of tools: Code Interpreter, Retrieval, and Function calling.

</details>
</details>

<details>
<summary>問題2: アシスタントを作成する際に指定できるパラメータは？</summary>

a. name, instructions, tools, model
b. name, prompt, max_tokens, model
c. name, instructions, examples, model
d. name, prompt, tools, max_tokens

<details>
<summary>回答と解説</summary>

回答: a. name, instructions, tools, model

アシスタントを作成する際は、name、instructions、tools、modelなどのパラメータを指定できます。

> An Assistant represents an entity that can be configured to respond to a user's messages using several parameters like model, instructions, and tools.

</details>
</details>

<details>
<summary>問題3: スレッドにメッセージを追加する際の制限は？</summary>

a. メッセージの数に制限はない
b. 最大10個のメッセージを追加できる
c. 最大100個のメッセージを追加できる 
d. 最大1000個のメッセージを追加できる

<details>
<summary>回答と解説</summary>

回答: a. メッセージの数に制限はない

スレッドに追加できるメッセージの数に制限はありません。モデルのコンテキストウィンドウに収まらないコンテキストは、スマートに切り捨てられます。

> There is no limit to the number of Messages you can add to Threads — we smartly truncate any context that does not fit into the model's context window.