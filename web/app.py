from flask import Flask, render_template, request
from functions.crawl import rain_predict
from models.model import model_pred

app = Flask(__name__, static_folder='static')

# ============================ 首頁start =========================


@app.route('/')
def homepage():
    return render_template('index.html')
# ============================ 首頁end   =========================

# ============================ 統計圖表start =========================


@app.route('/index1')
def statistics_plot():
    return render_template('index1.html', page_header="page_header")
# ============================ 統計圖表end   =========================

# ============================ 模型預測start =========================


@app.route('/index2')
def crawl():
    # 調用爬蟲函數並得到返回的文字，用來判斷是否會下雨
    result = rain_predict()
    if result == 'T':
        result = "可能下雨"
    else:
        result = "可能不下雨"
    return render_template('index2.html', result=result)

# 表單接收值


@app.route('/submit_form', methods=['POST'])
def submit_form():
    # 從表單中獲取數據，接收dict型態的值，並添加是否下雨的資訊
    data = request.form.to_dict()
    result = rain_predict()
    data['rain'] = result

    # 呼叫模型預測
    pre_result = model_pred(data)
    pre_result = "預估今日均價為："+str(pre_result)+"元。"
    return pre_result
# ============================ 模型預測end   =========================


if __name__ == '__main__':
    app.run(debug=True)
