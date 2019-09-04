import wikipedia 

def wikipedia_command(command):
    cmd,keyword = command.split()
    wikipedia.set_lang("ja")
    try:
        page = wikipedia.page(keyword)
        title = page.title
        summary = page.summary
        response = "タイトル：{}\n{}".format(title,summary)
    except wikipedia.exceptions.PageError:
        response = "「{}」の意味がみつかりませんでした。".format(keyword)
    except Exception as e:
        response = "予期せぬエラーが発生しました。"
    return response
























