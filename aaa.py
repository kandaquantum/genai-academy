from graphviz import Digraph

dot = Digraph(comment='AI Content Creation Roadmap', graph_attr={'rankdir': 'LR', 'splines': 'ortho', 'nodesep': '0.2'})

# 基礎編
dot.node('基礎編', '基礎編', shape='box')

with dot.subgraph(name='cluster_基礎編') as c:
    c.attr(color='green')
    c.node('1.2', '1.2 ドキュメントプログラム基礎講座', shape='box', width='4', style='filled', fillcolor='lightblue')
    c.node('1.1', '1.1 プロンプトプログラム基礎講座', shape='box', width='4', style='filled', fillcolor='lightblue')
    
    # ノードを左揃えにするために同じランクに設定
    c.attr(rank='same')
    c.edge('基礎編', '1.2')
    c.edge('基礎編', '1.1')

# 中級編
with dot.subgraph(name='cluster_中級編') as c:
    c.attr(color='orange')
    c.node('中級編', '中級編', shape='box')
    c.node('2.7', '2.7 RAG講座', shape='box', width='4', style='filled', fillcolor='lightblue')  # RAG講座を追加🆕
    c.node('2.6', '2.6 デプロイ関連講座', shape='box', width='4', style='filled', fillcolor='lightblue') 
    c.node('2.5', '2.5 バックエンド開発講座', shape='box', width='4', style='filled', fillcolor='lightblue')  
    c.node('2.4', '2.4 フロントエンド開発講座', shape='box', width='4', style='filled', fillcolor='lightblue') 
    c.node('2.3', '2.3 GAS講座', shape='box', width='4', style='filled', fillcolor='lightblue')
    c.node('2.2', '2.2 マルチモーダル生成AI API基礎講座', shape='box', width='4', style='filled', fillcolor='lightblue')
    c.node('2.1', '2.1 Cursor/ Open Interpreter講座', shape='box', width='4', style='filled', fillcolor='lightblue')
    c.edge('中級編', '2.7')  # RAG講座へのエッジを追加🌈
    c.edge('中級編', '2.6')
    c.edge('中級編', '2.5')
    c.edge('中級編', '2.4')
    c.edge('中級編', '2.3')
    c.edge('中級編', '2.2')
    c.edge('中級編', '2.1')

# 応用編
dot.node('応用編', '応用編', shape='box')

# 3.1 テキストベースのコンテンツ制作
with dot.subgraph(name='cluster_3.1') as c:
    c.attr(rank='same', color='blue')
    c.node('3.1', '3.1 テキストベースのコンテンツ制作', shape='box', width='4')
    c.node('3.1.2', '3.1.2 ブログ記事の自動生成講座', shape='box', width='4')
    c.node('3.1.1', '3.1.1 20分で書籍1冊（20万文字）執筆講座', shape='box', width='4', style='filled', fillcolor='lightblue')
    c.edge('3.1', '3.1.2')
    c.edge('3.1', '3.1.1')

# 3.2 画像コンテンツ制作
with dot.subgraph(name='cluster_3.2') as c:
    c.attr(rank='same', color='blue')
    c.node('3.2', '3.2 画像コンテンツ制作', shape='box', width='4')
    c.node('3.2.1', '3.2.1 画像バナー自動生成講座', shape='box', width='4', style='filled', fillcolor='lightblue')
    c.edge('3.2', '3.2.1')

# 3.3 データ分析とインタープリター
dot.node('3.3', '3.3 データ分析とインタープリター', shape='box', width='4')
with dot.subgraph(name='cluster_3.3') as c:
    c.attr(rank='same', color='blue')
    c.node('3.3.2', '3.3.2 データ可視化講座', shape='box', width='4')
    c.node('3.3.1', '3.3.1 Data Interpreter講座', shape='box', width='4')
    c.edge('3.3', '3.3.2')
    c.edge('3.3', '3.3.1')

# 3.4 動画コンテンツ制作
with dot.subgraph(name='cluster_3.4') as c:
    c.attr(rank='same', color='blue')
    c.node('3.4', '3.4 動画コンテンツ制作', shape='box', width='4')
    c.node('3.4.3', '3.4.3 Gemini 1ミリオン！ 動画解釈AI講座', shape='box', width='4', style='filled', fillcolor='lightblue')
    c.node('3.4.2', '3.4.2 動画バナー制作講座', shape='box', width='4')
    c.node('3.4.1', '3.4.1 Manim動画教材制作講座', shape='box', width='4', style='filled', fillcolor='lightblue')
    c.edge('3.4', '3.4.3')
    c.edge('3.4', '3.4.2')
    c.edge('3.4', '3.4.1')

# 3.5 ロボット
dot.node('3.5', '3.5 ロボット', shape='box', width='4')
with dot.subgraph(name='cluster_3.5') as c:
    c.attr(rank='same', color='blue')
    c.node('3.5.1', '3.5.1 ロボット講座', shape='box', width='4')
    c.edge('3.5', '3.5.1')

# 3.6 バーチャルアバター
dot.node('3.6', '3.6 バーチャルアバター', shape='box', width='4')  # バーチャルアバターのカテゴリーを追加🎭✨
with dot.subgraph(name='cluster_3.6') as c:
    c.attr(rank='same', color='blue')
    c.node('3.6.1', '3.6.1 バーチャルアバター制作講座', shape='box', width='4')
    c.edge('3.6', '3.6.1')

# 3.7 生成AI活用営業講座
dot.node('3.7', '3.7 生成AI活用営業講座', shape='box', width='4', rank='sink')
with dot.subgraph(name='cluster_3.7') as c:
    c.attr(rank='sink', color='blue')
    c.node('3.7.1', '3.7.1 商談議事録作成術', shape='box', width='4')
    c.node('3.7.2', '3.7.2 顧客整理術', shape='box', width='4')
    c.node('3.7.3', '3.7.3 見積もり作成術', shape='box', width='4')
    c.node('3.7.4', '3.7.4 提案資料作成術', shape='box', width='4')
    c.edge('3.7', '3.7.1')
    c.edge('3.7', '3.7.2')
    c.edge('3.7', '3.7.3')
    c.edge('3.7', '3.7.4')


# カテゴリー間の矢印
dot.edge('基礎編', '中級編', style='dashed')
dot.edge('中級編', '応用編', style='dashed')
dot.edge('応用編', '3.1', style='dashed')
dot.edge('応用編', '3.2', style='dashed')
dot.edge('応用編', '3.3', style='dashed')
dot.edge('応用編', '3.4', style='dashed')
dot.edge('応用編', '3.5', style='dashed')
dot.edge('応用編', '3.6', style='dashed')  # バーチャルアバターのカテゴリーへの矢印を追加🏹✨

# グラフの出力
dot.render('ai_content_creation_roadmap_horizontal_ortho_aligned', view=True)