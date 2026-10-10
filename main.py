
from flask import Flask

app = Flask(__name__)

@app.route("/")
def birthday():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Happy Birthday Abdullah</title>
<style>
body {
  background: linear-gradient(135deg,#141e30,#653a80,#c850c0);
  color: white;
  font-family: Arial;
  text-align: center;
  padding: 25px 12px;
}
.card {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background: #ffffff20;
  border-radius: 25px;
}
h1 { color: #ffe58a; }
p { line-height: 1.8; font-size: 17px; }
button {
  padding: 14px 20px;
  border: 0;
  border-radius: 25px;
  background: #ffe58a;
  font-size: 17px;
}
#message { display: none; }
.stickers { font-size: 35px; }
</style>
</head>
<body>
<div class="card">
<div class="stickers">🎂🎉🎈🥳</div>
<h1>HAPPY BIRTHDAY ABDULLAH! 👑</h1>
<p>OYYYY BIRTHDAY BOYYYY! 😂😭</p>
<p>Aaj tumhara special day hai! Cake tumhara,
lekin sabse bara piece humara! 🍰🤣</p>

<button onclick="
document.getElementById('message').style.display='block';
this.style.display='none';
">OPEN YOUR SURPRISE 🎁</button>

<div id="message">
<h2>Dear Abdullah 💙</h2>
<p>
Happy Birthday, bhai! 🎂❤️
May Allah bless you with happiness, good health,
success, peace and endless barakah.
May every good dua of yours be accepted.
May Allah protect you from evil and guide you
towards what is best. Ameen! 🤲🌙
</p>
<p>
Allah tumhare parents ko tumhari kamyabi par
fakhr karne ka mauqa de, tumhari mushkilein
aasaan kare aur tumhari zindagi ko khushiyon
se bhar de. InshaAllah! 💖
</p>
<div class="stickers">🤲🌙🧿💙</div>
<h2>AB THORI BEIZZATI 😂</h2>
<p>
Age barh rahi hai, lekin harkatein abhi bhi
nursery wali hain! 🤡💀
Candles phoonkne se pehle dua karna,
warna cake bhi bolega: "Mera piece kidhar hai?" 😂🍰
</p>
<p>
May you become so successful that your problems
need an appointment to meet you! 💸😎
</p>
<div class="stickers">🐸🦖🍕😂</div>
<h2>A HEARTFELT WISH 🫂</h2>
<p>
Keep smiling, never give up on your dreams,
always respect your loved ones and trust Allah.
May every new year make you wiser, stronger
and happier. You deserve beautiful things
and countless reasons to smile. ✨
</p>
<p>
Stay blessed in this world and the Hereafter.
May Allah always protect you. Ameen! 🤲❤️
</p>
<h1>HAPPY BIRTHDAY ONCE AGAIN! 🎉</h1>
<div class="stickers">🎁🎂💙👑🥳</div>
</div>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
