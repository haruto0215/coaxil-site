# 自己紹介ページ（OneDrive の原本）から、公開用の index.html を作る
# 実行：python3 build.py
import re, os
SRC = os.path.expanduser('~/Library/CloudStorage/OneDrive-個人用/営業資料作成/自己紹介ページ/はると_自己紹介.html')
s = open(SRC, encoding='utf-8').read()
s = re.sub(r'<title>[^<]*</title>\s*', '', s, count=1)
s = re.sub(r'<meta name="claude:[^>]*>\s*', '', s)
s = re.sub(r'/\*[\s\S]*?\*/', '', s)                 # 制作メモを公開しない（CSS）
s = re.sub(r'(?m)^\s*//[^\n]*\n', '', s)             # 制作メモを公開しない（JS）
d = '中小企業のための、AI業務効率化。御社の仕事を伺い、御社のやり方に合わせた専用のAIの仕組みをつくります。初回のヒアリングは無料です。'
head = f'''<!doctype html>
<html lang="ja"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>コアシル｜中小企業のAI活用</title>
<meta name="description" content="{d}">
<link rel="canonical" href="https://coaxil.jp/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="コアシル">
<meta property="og:title" content="コアシル｜中小企業のAI活用">
<meta property="og:description" content="{d}">
<meta property="og:url" content="https://coaxil.jp/">
<meta property="og:image" content="https://coaxil.jp/logo-512.png">
<meta name="twitter:card" content="summary">
<link rel="icon" type="image/png" sizes="48x48" href="/icon-48.png">
<link rel="apple-touch-icon" href="/icon-192.png">
<style>body{{margin:0;padding:0}}</style>
'''
i = s.index('</style>') + len('</style>')
s = s[:i] + '\n</head>\n<body>' + s[i:]
out = head + s + '\n</body>\n</html>\n'
open('docs/index.html', 'w', encoding='utf-8').write(out)
open('docs/CNAME', 'w').write('coaxil.jp\n')
open('docs/.nojekyll', 'w').write('')
os.makedirs('docs/privacy', exist_ok=True)
PV = os.path.expanduser('~/Library/CloudStorage/OneDrive-個人用/営業資料作成/templates/コアシル_プライバシーポリシー_案.html')
open('docs/privacy/index.html', 'w', encoding='utf-8').write(open(PV, encoding='utf-8').read())
print(len(out))
