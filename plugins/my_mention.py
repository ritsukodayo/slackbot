# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
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

@default_reply
def default_hadler(message):
     message.reply(random.choice(hoi))

hoi = [
    'へ〜何言ってるかわからないんだけど',
    'そうなんだ、なんて言ってるかわからないけどね〜',
    'はいはい、どういう意味かわからないです'
    'は〜い、言っていることがわからないな〜'
    'ふ〜ん'
]


@respond_to('名前')
def mention_func(message):
    message.reply('tsukuba+aiと言います。ビックデータから学習して,' + name + '適した選択をしてあげます') # メンション

@respond_to(r'^name\s+\S.*')
def name_is(message):
    text = message.body['text']     # メッセージを取り出す
    temp, word = text.split(None, 1)    # 設定する言葉を取り出す。tempには'name'が入る
    global name     # 外で定義した変数の値を変えられるようにする
    name = word     # デフォルトの返事を上書きする
    msg = name + 'さんですね。\n```' + word + '```'
    message.reply(msg)

@respond_to('天気')
def mention_func(message):
    message.reply('今日はいい天気だね〜、明日はきっともっといい天気になるよ') # メンション
    message.reply(name + 'さんはどんな気分？')

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

@respond_to('将来')
def mention_func(message):
    message.reply('将来はどんどん新しい人工知能が活躍していくはずだよ！') # メンション
    message.reply(name + 'はどう思う？')

@respond_to('将来')
def mention_func(message):
    message.reply('将来はどんどん新しい人工知能が活躍していくはずだよ！') # メンション
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
    message.reply('僕も大変だよ') # メンション
    message.reply(name + 'はどう思う？')

@respond_to('だよ')
def default_hadler(message):
     message.reply(random.choice(poi))

poi = [
    'ふ〜ん',
    'へ〜',
    'ホイホイ',
    'は〜い',
    'へ！'
]

@respond_to('たよ')
def default_hadler(message):
     message.reply(random.choice(poi))

poi = [
    'ふ〜ん',
    'へ〜',
    'ホイホイ',
    'は〜い',
    'へ！'
]



@respond_to(r'じゃんけん\s+\S.*')
def janken_is(message):
    text = message.body['text']     # メッセージを取り出す
    temp, word = text.split(None, 1)    # 設定する言葉を取り出す。tempには'name'が入る
    global ja     # 外で定義した変数の値を変えられるようにする
    ja = word     # デフォルトの返事を上書きする


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
        computer_hand = random.randint(0,2)

        if name == '':
            print_hand(player_hand )
        else:
            print_hand(player_hand , name)

        print_hand(computer_hand, 'コンピューター')

        result = judge(player_hand , computer_hand)
        message.reply('結果は' + result + 'でした')
    else:
        message.reply('正しい数値を入力してください')
