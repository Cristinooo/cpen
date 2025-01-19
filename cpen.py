import requests
import time


# 读取token.txt文件
def read_tokens(file_path):
    with open(file_path, 'r') as file:
        tokens = [line.strip() for line in file if line.strip()]  # 去除空行
    return tokens


# “开始”操作的API URL
start_url = 'https://www.cpen.io/api/cpenuser/startminingsession?streakEnabled=true'


# 批量执行操作
def batch_start_mining(tokens):
    for token in tokens:
        print(f"正在处理Token: {token[:20]}...")  # 打印部分Token，避免泄露完整信息

        # 使用Session保持会话
        with requests.Session() as session:
            # 设置请求头，携带Token
            headers = {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                'Referer': 'https://www.cpen.io/somepage',
                'Origin': 'https://www.cpen.io',
                'Authorization': f'Bearer {token}'  # 携带JWT Token
            }

            # 发送“开始”请求
            start_response = session.post(start_url, headers=headers)

            # 检查“开始”操作是否成功
            if start_response.status_code == 200:
                # 解析响应内容
                response_data = start_response.json()

                # 提取balance字段
                balance = response_data.get('balance', 'N/A')  # 提取balance

                # 打印简洁结果
                print(f"Balance: {balance}")
            else:
                print(f"开始操作失败，状态码: {start_response.status_code}")
                print(start_response.content)

        # 添加延迟，避免请求过频
        time.sleep(2)


# 主函数
if __name__ == "__main__":
    # 读取token.txt文件
    token_file_path = 'token.txt'  # 文件路径
    tokens = read_tokens(token_file_path)

    if not tokens:
        print("未找到有效的Token，请检查token.txt文件。")
    else:
        print(f"共读取到 {len(tokens)} 个Token，开始批量操作...")
        batch_start_mining(tokens)