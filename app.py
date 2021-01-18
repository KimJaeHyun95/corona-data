from flask import Flask, render_template
import corona_data
from datetime import date, timedelta

# 앱 생성
app = Flask(__name__)

# url 라우터
@app.route('/')
def index():
    now = date.today() # 20200701
    now_str = now.strftime("%Y%m%d")
    print(now_str)
    before30days = now - timedelta(days=30)
    before30days_str = before30days.strftime("%Y%m%d")

    data = corona_data.get_corona_data(before30days_str,now_str)

    #  print(data)
    return render_template('index.html', data=data[1:])

# 메인 영역
if __name__ == "__main__":
    app.run(debug=True)

