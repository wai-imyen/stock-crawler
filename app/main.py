import requests
from bs4 import BeautifulSoup

def fetch_stock_offering_data():
    max_count = 10
    stock_info_list = []
    url = 'https://histock.tw/stock/public.aspx'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr')
        for row in rows:
            stock_info = {}

            # 限制取得前 n 筆資料
            if (max_count < len(stock_info_list)):
                break

            row_data = row.find_all('td')
            if len(row_data) == 0:
                continue

            # 抽籤日期
            stock_info['date'] = row_data[0].text.strip()
            # 股票代號 + 名稱
            stock_mix_element = row_data[1].find('a')
            if stock_mix_element is not None:
                mix_str = stock_mix_element.text.strip()
            else:
                mix_str = row_data[1].text.strip()
            mix_str_arr = mix_str.split()
            stock_info['stock_code'] = mix_str_arr[0].strip()
            stock_info['stock_name'] = mix_str_arr[1].strip()
            # 發行市場
            stock_info['market'] = row_data[2].text.strip()
            # 申購期間
            stock_info['period'] = row_data[3].text.strip()
            # 撥券日期
            stock_info['issue_date'] = row_data[4].text.strip()
            # 承銷張數
            stock_info['volume'] = row_data[5].text.strip()
            # 承銷價
            stock_info['price'] = row_data[6].text.strip()
            # 市價
            stock_info['market_price'] = row_data[7].text.strip()
            # 獲利
            stock_info['profit'] = row_data[8].text.strip()
            # 報酬率(%)
            stock_info['reward_rate'] = row_data[9].text.strip()
            # 申購張數
            stock_info['offering_volume'] = row_data[10].text.strip()
            # 總合格件
            stock_info['total_volume'] = row_data[11].text.strip()
            # 中籤率(%)
            stock_info['issue_rate'] = row_data[12].text.strip()
            # 備註
            stock_info['note'] = row_data[13].text.strip()

            stock_info_list.append(stock_info)

            print("日期:", stock_info['date'])
            print("股票代號:", stock_info['stock_code'])
            print("股票名稱:", stock_info['stock_name'])
            print("發行市場:", stock_info['market'])
            print("申購期間:", stock_info['period'])
            print("撥券日期:", stock_info['issue_date'])
            print("承銷張數:", stock_info['volume'])
            print("承銷價:", stock_info['price'])
            print("市價:", stock_info['market_price'])
            print("獲利:", stock_info['profit'])
            print("報酬率(%):", stock_info['reward_rate'])
            print("申購張數:", stock_info['offering_volume'])
            print("總合格件:", stock_info['total_volume'])
            print("中籤率(%):", stock_info['issue_rate'])
            print("備註:", stock_info['note'])
            print('---' * 10)
    else:
        print('爬取資料失敗')

if __name__ == '__main__':
    fetch_stock_offering_data()