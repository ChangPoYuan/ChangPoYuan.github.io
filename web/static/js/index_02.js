// 今天日期/星期 start
// 獲取當前日期
var today = new Date();
var day = today.getDate();
var month = today.getMonth() + 1; // 月份從0開始計算所以要加1
var year = today.getFullYear();

// 獲取當前星期
var daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
var dayOfWeekIndex = today.getDay(); // 星期日為0
var dayOfWeek = daysOfWeek[dayOfWeekIndex];
// 建立字串
var currentDateStr = "國曆：" + year + "-" + month + "-" + day + "，星期：" + dayOfWeek;
// 將字串填入指定元素id裡
document.getElementById("currentDate").innerText = currentDateStr;
document.getElementById("month").value = month;
document.getElementById("week").value = dayOfWeek;

//農曆
var currentLuDateStr = "農曆：" + calendar.solar2lunar(year, month, day).lunarDate;
document.getElementById("lu_currentDate").innerText = currentLuDateStr;

//是否為農曆
if (calendar.solar2lunar(year, month, day).lDay == 1 | calendar.solar2lunar(year, month, day).lDay == 15) {
    document.getElementById("lu_festival").value = "YES";
} else {
    document.getElementById("lu_festival").value = "NO";
}

//判斷重量
function validweightForm() {
    var weight = parseFloat(document.getElementById('weight').value);
    var totalWeight = parseFloat(document.getElementById('total_weight').value);

    if (weight > totalWeight) {
        alert('該果種到貨重量不能比全場到貨重量大');
        return false;
    }
    return true;
}

//在接收前端數值後直接將後端模型算出的值呈現出來不跳轉頁面
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('predictionForm');
    const resultDiv = document.getElementById('starresult');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // 防止表單提交刷新頁面

        const formData = new FormData(form);

        fetch('/submit_form', {
            method: 'POST',
            body: formData
        })
            .then(response => response.text()) // 假設伺服器回傳文本
            .then(data => {
                resultDiv.innerHTML = data; // 將伺服器回傳的結果設定為<div id="result"></div>的內容
            })
            .catch(error => {
                console.error('發生錯誤：', error);
            });
    });
});
// 今天日期/星期 end