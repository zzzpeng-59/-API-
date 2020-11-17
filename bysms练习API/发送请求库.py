
import requests
class APIMGR:
    """打印相关的响应消息"""
    def printResponse(self,response):
        print('\n\n--------HTTP RESPONSE * BEGIN-------- ')
        print(response.status_code)
        for k,v in response.headers.items():
            print(f'{k},{v}')

        print(response.content.decode('utf8'))

        print('-------------HTTP RESPONSE * END----------')

    """登录"""
    def mgr_login(self,username='byhy',password='88888888'):
        self.s = requests.Session()
        response = self.s.post('http://127.0.0.1/api/mgr/signin',
                               data={
                                   "username":username,
                                   "password":password
                               })
        self.printResponse(response)
        return response

    """列出所有客户"""
    def custmoer_list(self,pagesize=10,pagenum=1,keywords=''):
        response = self.s.get('http://127.0.0.1/api/mgr/customers',
                              params={
                                  "action":"list_customer",
                                  "pagesize": pagesize,
                                  "pagenum":pagenum,
                                  "keywords":keywords
                              })
        self.printResponse(response)
        return response

    """添加客户"""
    def customer_add(self,name,phonenumber,address):
        # if 2<len(name)<20 & 8<len(phonenumber)<15 & 2<len(address)<100:
        response = self.s.post('http://127.0.0.1/api/mgr/customers',
                               json={
                                   "action":"add_customer",
                                   "data":{
                                       "name":name,
                                       "phonenumber":phonenumber,
                                       "address":address
                                   }
                               })

        # else:
        #     print('字段长度范围不符合规范')
        self.printResponse(response)
        return response



    """修改客户信息"""
    def customer_mod(self,cid,name,phonenumber,address):
        # if 2 < len(name) < 20 & 8 < len(phonenumber) < 15 & 2 < len(address) < 100:
        response = self.s.put('http://127.0.0.1/api/mgr/customers',
                              json={
                                  "action":"modify_customer",
                                  "id":cid,
                                  "newdata":{
                                      "name":name,
                                      "phonenumber":phonenumber,
                                      "address":address
                                  }
                              })
        # else:
        #     print('字段长度不符合规范')

        self.printResponse(response)
        return response

    """删除客户信息"""
    def customer_delete(self,cid):
        response = self.s.delete('http://127.0.0.1/api/mgr/customers',
                                 json={
                                     "action":"del_customer",
                                     "id":cid
                                 })
        self.printResponse(response)
        return response

    """删除所有客户信息"""
    def customer_delete_all(self):
        response = self.custmoer_list(100,1)
        theList = response.json()["retlist"]
        for one in theList:
            self.customer_delete(one["id"])

    """列出药品"""
    def medicine_list(self,pagesize=10,pagenum=1,keywords=''):
        response = self.s.get('http://127.0.0.1/api/mgr/medicines',
                              params={
                                  "action":"list_medicine",
                                  "pagesize":pagesize,
                                  "pagenum":pagenum,
                                  "keywords":keywords
                              })
        self.printResponse(response)
        return response

    """添加药品"""
    def medicine_add(self,name,desc,sn):
        # if 2<len(name)<20 & 2<len(desc)<500 & 8<len(sn)<20:
        response = self.s.post('http://127.0.0.1/api/mgr/medicines',
                               json={
                                   "action":"add_medicine",
                                   "data":{
                                       "name":name,
                                       "desc":desc,
                                       "sn":sn
                                   }
                               })
        # else:
        #     print('字段长度不符合规范')

        self.printResponse(response)
        return response

    """修改药品"""
    def medicine_mod(self,mid,name,desc,sn):
        # if 2 < len(name) < 20 & 2 < len(desc) < 500 & 8 < len(sn) < 20:
        response = self.s.put('http://127.0.0.1/api/mgr/medicines',
                              json={
                                  "action":"modify_medicine",
                                  "id":mid,
                                  "newdata":{
                                      "name":name,
                                      "desc":desc,
                                      "sn":sn
                                  }
                              })
        # else:
        #     print('字段长度不符合规范')

        self.printResponse(response)
        return response

    """删除药品"""
    def medicine_delete(self,mid):
        response = self.s.delete('http://127.0.0.1/api/mgr/medicines',
                                 json={
                                     "action":"del_medicine",
                                     "id":mid
                                 })

        self.printResponse(response)
        return response

    """删除所有药品"""
    def medicine_delete_all(self):
        response = self.medicine_list(100,1)
        theList = response.json()["retlist"]
        for one in theList:
            self.medicine_delete(one["id"])
    """列出所有订单"""
    def order_list(self,pagesize=10,pagenum=1,keywords=''):
        response = self.s.get('http://127.0.0.1/api/mgr/orders',
                              params={
                                  "action":"list_order",
                                  "pagesize":pagesize,
                                  "pagenum":pagenum,
                                  "keywords":keywords
                              })

        self.printResponse(response)
        return response

    """添加订单"""
    def order_add(self,name,customerid,medicineid,amount,medicinename):
        # if 2<len(name)<100:
        response = self.s.post('http://127.0.0.1/api/mgr/orders',
                               json={
                                   "action":"add_order",
                                   "data":{
                                       "name":name,
                                       "customerid":customerid,
                                       "medicinelist":[
                                           {"id":medicineid,"amount":amount,"name":medicinename},
                                           {"id":medicineid,"amount":amount,"name":medicinename}
                                       ]
                                   }
                               })
        # else:
        #     print('字段不符合长度')

        self.printResponse(response)
        return response

    """删除订单"""
    def order_delete(self,oid):
        response = self.s.delete('http://127.0.0.1/api/mgr/orders',
                                 json={
                                     "action":"delete_order",
                                     "id":oid
                                 })

        self.printResponse(response)
        return response

    """删除所有订单"""
    def order_delete_all(self):
        response = self.order_list(100,1)
        theList = response.json()["retlist"]
        for one in theList:
            self.order_delete(one["id"])

apimgr = APIMGR()