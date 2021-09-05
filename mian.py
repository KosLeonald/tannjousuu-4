import json
import random
#import time , datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

option_1 = "【誕生数４】\nあなたは余りにも一人ぼっちだと思い込み過ぎていませんか？もしくはあなたの方から人を遠ざけていますか？あなたに手を貸したい人や、あなたに付いていきたい人は何人もいるのに、あなたは心を開かずに頑なな様子が浮かびます。あなたはちゃんと自立していて、誰の力を借りなくても前に進める人ですが、今は人の声に耳を傾け、受容モードになる事を勧められていますよ。"
option_2 = "【誕生数４】\n今この時期は、緊急性があるという想像に基づいて行動を取るときではありません。感情があなたと共に流れ出るのを止めてください。あなたの理性の力をしっかりと持ち、目の前のドラマやこの瞬間の激しさから遠ざかりたいという気持ちを信頼しましょう。あなたのハイヤー・セルフが、あなたを正しい結論へ誘導してくれるのに任せましょう。その結論を心に抱いて眠りにつき、さらには、その結論を心に抱いて三夜眠り、ハイヤー・セルフのメッセージを心に留めましょう。\n\n「今は、ハイヤー・セルフにそれを任せてください」\n（ハイヤー・セルフとは、あなたの中に在る本当のあなた、なにが真実かを知っているあなたのことです）"
option_3 = "【誕生数４】\nあなたの心の声に耳を傾けてください。誰かの迷惑や噂や評価、顔色などを全く気にしなくてよい状況ならあなたはどんな答えを出すか、その声を聴いてみてください。本当はきっとあなたには分かっているのではないでしょうか。自分が何をしたいか、どう動きたいか。もしもそれが実行出来ていないとしたら、周りの環境のせいではなく、あなた自身への信頼不足なだけでしょう。今は、自分の心の声に素直になること、自分を信じてそれに飛び込んで行くことです。"
#option_4 = "確率分散 1"
#option_5 = "確率分散 2"
#option_6 = "確率分散 3"

def main():
    USER_ID = info['USER_ID']
    mylist = [ option_1,option_2,option_3]    
    messages1= TextSendMessage(random.choice(mylist))
    #messages = TextSendMessage(text=random.choice(mylist))
    #messages2= TextSendMessage(text = "今日も1日頑張りましょう♪")
    # today = datetime.datetime.fromtimestamp(time.time())
    #time  = today.strftime('%H')      
 
     #   if int(time) > 20 :
    line_bot_api.broadcast(messages1)
     #   else :
    #line_bot_api.broadcast(messages2)  
    
if __name__ == "__main__" :
    main()
