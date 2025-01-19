1、安装必须得库 ：
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install requests beautifulsoup4 lxml pyjwt
2、
修改token.txt文件
F12获取token -- application -- flutter.user_access_token
格式为：
eyJ....
eyJ....
每行一个，支持多账户签到！
