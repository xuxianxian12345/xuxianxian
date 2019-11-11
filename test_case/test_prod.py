from tools import pub_data
from tools.api import request_tool
from tools.security.md5_tool import md5_passwd

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
def test_prod_json(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '新增产品接口'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers={"token": pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
   {
  "brand": "华为",
  "colors": [
    "土豪金"
  ],
  "price": 5000,
  "productCode": "自动生成 字符串 3,10 数字字母",
  "productName": "华为给op",
  "sizes": [
    "6寸"
  ],
  "type": "手机"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_psth=[{"productCode":'$.data[0].productCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r=request_tool.request(json_psth=json_psth,headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    pub_data["skuCode"]=r.json()["data"][0]["skuCode"]


def test_change_prince(pub_data):

    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '锁定用户'  # allure报告中二级分类
    title = "字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"SKU":pub_data['skuCode'],"price":1589}
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)




def test_post_product(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "编码批量修改模块"  # allure报告中一级分类
    story = '编码批量修改价格用户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"prodCode":'p3099313',"price":5000}
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

def test_post_productsoldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品改为下架"  # allure报告中一级分类
    story = '锁定用户'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"productCode":'YSL008'}
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


def test_post_fullSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "全量调整整个库存"  # allure报告中一级分类
    story = '全量调整商品库存'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/fullSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode":'ljujj_土豪金_6寸',"qty":5}
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


def test_post_ordeerPrice(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '无签名无加密下单'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrder"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None

    json_data = {
        "ordeerPrice":5000,
        "orderLineList": [
            {
                "qty": 1,
                "skuCode": "ljujj_土豪金_6寸"
            }
        ],
        "receiver": "15295292396",
        "receiverPhone": "15295292396",
        "receivingAddress": "闵行区",
        "sign": "",
        "userName": "xuepl8811"
    }
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

def test_post_recharge(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "充值模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = {
        "accountName": "xuepl8811",
        "changeMoney": 100000
    }
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


def test_post_ordeerPrice(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '签名下单接口'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrderSignBody"  # 接口地址
    #headers = {"token": pub_data["token"]}
    s="receiver=15295292396&ordeerPrice=5000&receiverPhone=15295292396&key=guoya"
    sign=md5_passwd(s,"")
    pub_data["sign"]=sign
    # post请求json数据，注意数据格式为字典或者为json串 为空写None

    json_data = {
        "ordeerPrice":5000,
        "orderLineList": [
            {
                "qty": 1,
                "skuCode": "ljujj_土豪金_6寸"
            }
        ],
        "receiver": "15295292396",
        "receiverPhone": "15295292396",
        "receivingAddress": "闵行区",
        "sign": "${sign}",
        "userName": "xuepl8811"
    }
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
