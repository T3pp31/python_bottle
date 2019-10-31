<html>
<link rel="stylesheet" type="text/css" href="../css/style.css">
<body>
<h1>chat_bot</h1>
<form method="post" action="/">
メッセージを入力してください: <input type="text" name="input_text">
<input type="submit" value="送信">
</form>
<ul>
<li>入力されたメッセージ: {{input_text}}</li>
<li>応答メッセージ: {{output_text}}</li>
</ul>
<h2>使い方</h2>
<ul>
<li>長さ　長さを調べたい文字列と入れると文字列の長さを測定できます。</li>
<li>干支　生まれた年で入力するとあなたの干支が表示されます。</li>
<li>元号　西暦(2000など）と入れると元号〇〇年と表示されます。</li>
<li>さいころと入力するとサイコロがふられます。</li>
<li>選ぶ　ラーメン　うどん　そばのように入力すると３つのうちどれかが選ばれます（何個でも可能）</li>
<li>今日、現在などと入力すると現在の日付、日時がわかります</li>
<li>曜日　2000 05 10　のように入力するとその日の曜日が取得できます。</li>
<li>天気と入力すると、東京の天気が求められます。</li>
<li>意味 調べたいワード　とすると調べたい言葉がwikipediaからひかれます</li>
<li>平均値：数値①　数値②　数値③と入力すると数値の平均値を求められます。</li>
<li>中央値：数値①　数値②　数値③と入力すると数値の中央値を求められます。</li>
</ul>
</body>
</html>
