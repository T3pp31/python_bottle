#utf-8
from eto import eto_command
from len_moji import len_moji
from gengo_calculater import gengo_calculater
from pybot_random import choice_command,dice_command
from date_time import today_command,now_command,weekday_command
from heisei_calculater import heisei_calculater
from reiwa_calculater import reiwa_calculater
from showa_calculater import showa_calculater
from pybot_weather import weather_command
from pybot_wikipedia import wikipedia_command


open_file = open("teikei.txt", encoding="utf-8")
raw_data = open_file.read()
open_file.close()
lines = raw_data.splitlines()


print("「さようなら」と入力されると、終了します。\n長さ　長さを調べたい文字列と入れると文字列の長さを測定できます。\n干支　生まれた年で入力するとあなたの干支が表示されます。")
print("元号　西暦(2000など）と入れると元号〇〇年と表示されます。\nさいころと入力するとサイコロがふられます。\n選ぶ　ラーメン　うどん　そばのように入力すると３つのうちどれかが選ばれます（何個でも可能）")
print("今日、現在などと入力すると現在の日付、日時がわかります\n曜日　2000 05 10　のように入力するとその日の曜日が取得できます。")
print("天気と入力すると、東京の天気が求められます。\n意味 調べたいワード　とすると調べたい言葉がwikipediaからひかれます")


bot_dict = {}
for line in lines:
    word_list = line.split(":")
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

def bot(command):
    #command = input("pybot> ")
    response = ""
    try:
        for key in bot_dict:
            if key in command:
                response = bot_dict[key]
                break

            if "意味" in command:
                response = wikipedia_command(command)
            if "長さ" in command:
                response = len_moji(command)
    
            if "干支" in command:
                response = eto_command(command)
    
            if "元号" in command:
                response = gengo_calculater(command)

            if "heisei" in command:
                response = heisei_calculater(command)
            if "平成" in command:
                response = heisei_calculater(command)
    
            if "reiwa" in command:
                response = reiwa_calculater(command)
            if "令和" in command:
                response = reiwa_calculater(command)
    
            if "昭和" in command:
                response = showa_calculater(command)
            if "showa" in command:
                response = showa_calculater(command)


            if "サイコロ" in command:
                response = dice_command()
            if "さいころ" in command:
                response = dice_command()
            if "dice" in command:
                response = dice_command()

            if "選ぶ" in command:
                response = choice_command(command)
    
            if "今日" in command:
                response = today_command()
            if "today" in command:
                response = today.command()

            if "現在" in command:
                response = now_command()
            if "now" in command:
                response = now_command()

            if "曜日" in command:
                response = weekday_command(command)
            if "weekday" in command:
                response = weekday_command(command)

            if "天気" in command:
                response = weather_command()
            if "weather" in command:
                response = weather_command()

  

        if not response:
            response = "何言ってるかわからん＼(^o^)／ｵﾜﾀ\nこれから勉強します(^^♪"
            output_file = open("new_word.txt","a", encoding="utf-8")
            output_file.write("{}\n".format(command))
            output_file.close()
        return response


    except Exception as e:
        print("予期せぬエラーが発生しました。")
        print("* 種類:",type(e))
        print("* 内容:",e)
        error_file = open("error.txt","a",encoding="utf-8")
        error_file.write("種類：{} 内容{}\n".format(type(e),e))
        error_file.close()
