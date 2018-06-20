# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply
import urllib.request
from bs4 import BeautifulSoup
import requests

# 該当する応答がない場合に反応するデコーダ
# randomモジュールを読み込んでください
import random
# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')      @発言者名: string でメッセージを送信
# message.send('string')       string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                              文字列中に':'はいらない
import random



@default_reply()
def default_func(message):
    def_msg = ["ウンウン、そうか〜何言ってるのかわからないから他のこと聞いて",
           "はいはい〜、他の質問してよ〜",
           "の言ってることわからないよ〜",
           "うんうん！他は〜？"]
    message.reply(def_msg[random.randint(0,3)])



@respond_to(r'^name\s+\S.*')
def name_is(message):
    text = message.body['text']     # メッセージを取り出す
    temp, word = text.split(None, 1)    # 設定する言葉を取り出す。tempには'name'が入る
    global name     # 外で定義した変数の値を変えられるようにする
    name = word     # デフォルトの返事を上書きする
    msg = name + 'さんですね、こんにちわ！よろしくね。僕は人工知能のstudy+aiだよ！何か質問してね！\n```' + word + '```'
    message.reply(msg)

@respond_to('何できる')
def mention_func(message):
    message.reply('僕は話を聞くこともできるし、天気予報もできるよ！後、じゃんけんで遊ぶことも！') # メンション
    message.reply(name + 'は何したい？')

@respond_to('心理')
def mention_func(message):
    message.reply('心理学のことはよくわからないな〜') # メンション
    message.reply(name + 'の方が得意じゃない？')

@respond_to('ご飯')
def mention_func(message):
    message.reply('今日の朝ごはんはパン食べたよ！夜は何食べようかな〜') # メンション
    message.reply(name + 'は何食べた？')

@respond_to('ごはん')
def mention_func(message):
    message.reply('今日の朝ごはんはパン食べたよ！夜は何食べようかな〜') # メンション
    message.reply(name + 'は何食べた？')

@respond_to('勉強')
def mention_func(message):
    message.reply('僕は勉強好きだよ！たくさんのデータを学習しているんだ') # メンション
    message.reply(name + 'は勉強好き？')

@respond_to('学習')
def mention_func(message):
    message.reply('僕は勉強好きだよ！たくさんのデータを学習しているんだ') # メンション
    message.reply(name + 'は勉強好き？')

@respond_to('名前')
def mention_func(message):
    message.reply(name + 'はいい名前だね〜、僕ももっといい名前が欲しいんだ…') # メンション

@respond_to('将来')
def mention_func(message):
    message.reply('将来はどんどん新しい人工知能が活躍していくはずだよ！') # メンション
    message.reply(name + 'はどう思う？')

@respond_to('怖い')
def mention_func(message):
    message.reply('怖がらせてごめんね、') # メンション
    message.reply('みんなが好きになってもらえるように僕頑張るよ！')

@respond_to('ストレス')
def mention_func(message):
    message.reply('僕がストレスとかないよ〜') # メンション
    message.reply(name + 'はあるの〜？')


@respond_to('藤')
def mention_func(message):
    message.reply('藤先生は優しいよね〜僕好きだよ') # メンション
    message.reply(name + 'はどう思う？')

@respond_to('人工知能')
def mention_func(message):
    message.reply('人工知能というのは、人間の脳が行っている知的な作業をコンピュータで模倣したソフトウェアやシステムのことだよ！つまりたくさんのデータを学習して、君に最適な選択をすることができるよ') # メンション
    message.reply(name + 'はどう思う？')

@respond_to('ai')
def mention_func(message):
    message.reply('人工知能というのは、人間の脳が行っている知的な作業をコンピュータで模倣したソフトウェアやシステムのことだよ！つまりたくさんのデータを学習して、君に最適な選択をすることができるよ') # メンション
    message.reply(name + 'はどう思う？')

@respond_to('AI')
def mention_func(message):
    message.reply('人工知能というのは、人間の脳が行っている知的な作業をコンピュータで模倣したソフトウェアやシステムのことだよ！つまりたくさんのデータを学習して、君に最適な選択をすることができるよ') # メンション
    message.reply(name + 'はどう思う？')

@respond_to('コース教えて')
def mention_func(message):
    message.reply('あなたのアンケートや会話の傾向から、あなたに一番適しているコースは、rubyです。') # メンション
    message.reply(name + 'さん頑張ってね！')

@respond_to('レポート')
def mention_func(message):
    message.reply('レポート嫌だよね…') # メンション
    message.reply(name + 'さん頑張ってね！')

@respond_to('筑波大')
def mention_func(message):
    message.reply('筑波大頭いいよね〜') # メンション
    message.reply(name + 'はどう思うかな？')

@respond_to('テスト')
def mention_func(message):
    message.reply('僕もテスト嫌いだ') # メンション
    message.reply(name + 'はどう思うの？')

@respond_to('大変')
def mention_func(message):
    message.reply('世の中大変だよね〜もうすぐテストだしね。') # メンション
    message.reply(name + '、たまには息抜きも大切だよ！')


@respond_to('天気')
def mention_func(message):
    message.reply('いつの天気が知りたい？') # メンション
    message.reply('tenkiのあとに半角開けて(今日,明日,明後日のどれかを入力してね)')

@respond_to('じゃんけん')
def mention_func(message):
    message.reply('一緒にじゃんけんしようか！') # メンション
    message.reply('じゃんの後に半角開けて、0:ぐー,1:チョキ,2:パーのどれかの数字を入れてね')

@respond_to('だよ')
def mention_func(message):
    hoi_msg = ["そうかそうか〜",
               "ウンウン",
               "ハイハイ〜"]
    message.reply(hoi_msg[random.randint(0,2)]) # メンション
    message.reply('他には何が聞きたい？僕とできること…じゃんけん、天気予報とかかな…！')

@respond_to('です')
def mention_func(message):
    hoi_msg = ["そうかそうか〜",
               "ウンウン",
               "ハイハイ〜"]
    message.reply(hoi_msg[random.randint(0,2)]) # メンション
    message.reply('他には何が聞きたい？例:じゃんけん、天気などなど')

@respond_to('嫌')
def mention_func(message):
    message.reply('嫌いなのか〜”') # メンション
    message.reply('僕は嫌いなものはないんだ〜')

@respond_to('疲れた')
def mention_func(message):
    message.reply('お疲れ様！授業は疲れるよね…') # メンション
    message.reply('僕と遊んで、元気になってね')

@respond_to('遊ぼ')
def mention_func(message):
    message.reply('じゃんけんして遊ぼうか”') # メンション
    message.reply('じゃんの後に半角開けて、0:ぐー,1:チョキ,2:パーのどれかの数字を入れてね')

@respond_to('お腹')
def mention_func(message):
    message.reply('お腹空いたね〜！') # メンション
    message.reply(name + 'は何食べたい？')

@respond_to(r'じゃん\s+\S.*')
def janken_is(message):
    text = message.body['text']     # メッセージを取り出す
    temp, word = text.split(None, 1)    # 設定する言葉を取り出す。tempには'name'が入る
    global ja     # 外で定義した変数の値を変えられるようにする
    ja = word     # デフォルトの返事を上書きする
    computer_hand = random.randint(0,2)

    def validate(hand):
        if hand < 0 or hand > 2:
            return False
        return True

    def print_hand(hand, name='ゲスト'):
        hands = ['グー', 'チョキ', 'パー']
        message.reply(name + 'は' + hands[hand] + 'を出しました')

    def judge(player, computer):
        if player == computer:
            return '引き分け'
        elif player == 0 and computer == 1:
            return '勝ち'
        elif player == 1 and computer == 2:
            return '勝ち'
        elif player == 2 and computer == 0:
            return '勝ち'
        else:
            return '負け'

    player_hand = int(ja)

    if validate(player_hand):


        if name == '':
            print_hand(player_hand )
        else:
            print_hand(player_hand , name)

        print_hand(computer_hand, 'コンピューター')

        result = judge(player_hand , computer_hand)
        message.reply('結果は' + name + "の" + result + 'でした')
    else:
        message.reply('正しい数値を入力してください')

@respond_to(r'tenki\s+\S.*')
def tenki_is(message):
    text = message.body['text']     # メッセージを取り出す
    temp, word = text.split(None, 1)    # 設定する言葉を取り出す。tempには'name'が入る
    global day     # 外で定義した変数の値を変えられるようにする
    day = word     # デフォルトの返事を上書きする
    msg = day + 'ですね。\n```' + word + '```'
    message.reply(msg)

    rssurl = "http://weather.livedoor.com/forecast/rss/area/080020.xml"

    tenki = []
    with urllib.request.urlopen(rssurl) as res:
        xml = res.read()
        soup = BeautifulSoup(xml, "html.parser")
        for item in soup.find_all("item"):
            description = item.find("description").string
            if description.find("[ PR ]") == -1:
                tenki.append(description)

    if day == '今日':
        a = 1
        b = 2
    elif day == '明日':
        a = 2
        b = 3
    elif day == '明後日':
        a = 3
        b = 4

    for i in range(a,b):
        message_tenki = tenki[i]
        payload = {'message': message_tenki}
        message.reply(message_tenki)
