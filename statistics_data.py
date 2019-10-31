import math
import statistics as st
data=[]
def heikin(command):
    try:

        data = command.split()
        data.remove('平均値')
        data=list(map(int,data))
        heikin_figure = st.mean(data)
        response='平均値は{}です'.format(heikin_figure)
        return response

    except:
        response='予期せぬエラーが発生しました。正しい形で入力してください'
        return response

def chuo_ti(command):
    try:

        data=command.split()
        data.remove('中央値')
        data=list(map(int,data))
        chuo=st.mean(data)
        response='中央値は{}です'.format(chuo)
        return response

    except:
        response='予期せぬエラーが発生しました。正しい形で入力してください'
        return response













