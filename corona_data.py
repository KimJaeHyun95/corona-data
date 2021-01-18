import requests
import xmltodict
import json
from pprint import pprint

def get_corona_data(startCreateDt, endCreateDt):
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
    params = {
        'serviceKey':'VTUeqd1slg4TKcsHOuAFbWpG6rAHz1rkW96QWrNb/tIOAYcPj2ZjQVl7xltLhsblFBUX1iv7peyTxj0dWiuLBg==',
        'pageNo':'1',
        'numOfRows':30,
        'startCreateDt': startCreateDt ,
        'endCreateDt':  endCreateDt , 
    }

    res = requests.get(url, params=params)
 

    # xml to dict
    dict_data = xmltodict.parse(res.text)

    # dict to json
    json_data = json.dumps(dict_data)
    # print(json_data, type(json_data))

    # json to dict
    dict_data = json.loads(json_data)

    # totalCount로 제대로 데이터가 가져와졌는지 확인하기
    totalCount = dict_data['response']['body']['totalCount']
    # print(totalCount)
    if totalCount == "0" :
        return False

    # 지역 정보를 담은 리스트
    area_data = dict_data['response']['body']['items']['item']
    area_data.reverse()

    return area_data

if __name__ == "__main__":
    data = get_corona_data('20200630','20200630')
    print(data)