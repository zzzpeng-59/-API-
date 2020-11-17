from lib.白月黑羽练习API.发送请求库 import apimgr
import pytest

class Test_客户:

    def test_001(self):
        print('列出客户')
        r = apimgr.custmoer_list()
        listRet = r.json()
        customerlist = listRet['total']
        assert customerlist == 0

    def test_002(self):
        print('添加客户')
        r = apimgr.customer_add('武汉市桥东医院','13666666636','武汉市桥东北路')
        addRet = r.json()
        self.add_cus_id = addRet['id']
        assert addRet['ret'] == 0

    # def customerId(self):
    #     cid = self.customerId()
    def test_003(self):
        print('修改客户')
        self.test_002()
        cid = self.add_cus_id
        r = apimgr.customer_mod(cid,'武汉市东桥医院','15625483254','武汉市东桥北路')
        modRet = r.json()
        assert modRet['ret'] == 0

    def test_004(self):
        print('删除客户')
        self.test_002()
        cid = self.add_cus_id
        r = apimgr.customer_delete(cid)
        deleteRet = r.json()
        assert deleteRet['ret'] == 0

class Test_药品:

    def test_011(self):
        print('列出所有药品')
        r = apimgr.medicine_list()
        listRet = r.json()
        medicineList = listRet['total']
        assert medicineList == 0

    def test_012(self):
        print('添加一个药品')
        r = apimgr.medicine_add('阿莫西林','阿莫西林 国字号','09981235470')
        addRet = r.json()
        self.add_med_id = addRet['id']
        assert addRet['ret'] == 0

    def test_013(self):
        print('修改药品信息')
        self.test_012()
        mid = self.add_med_id
        r = apimgr.medicine_mod(mid,'阿莫西林口服液','口服液 国字号','01112345618')
        modRet = r.json()
        assert modRet['ret'] == 0

    def test_014(self):
        print('删除药品')
        self.test_012()
        mid = self.add_med_id
        r = apimgr.medicine_delete(mid)
        deleteRet = r.json()
        assert deleteRet['ret'] == 0

class Test_订单:

    def test_111(self):
        print('列出订单')
        r = apimgr.order_list()
        listRet = r.json()
        assert listRet['total'] == 0

    def test_112(self):
        print('添加一个订单')
        """先创建一个客户"""
        cr = apimgr.customer_add('杭州人民医院','16542385164','杭州市江干区北路')
        cus_addRet = cr.json()
        #保存客户ID
        customerId = cus_addRet['id']
        """添加药品"""
        meidicinename = '新康泰克' #保存药品名字
        mr = apimgr.medicine_add('新康泰克','新康泰克 国字号','0564225463')
        med_addRet = mr.json()
        #保存药品ID
        medicineid = med_addRet['id']
        """添加订单"""
        r = apimgr.order_add('杭州人民医院订单001',customerId,medicineid,'5',meidicinename)
        addRet = r.json()
        self.add_order_id = addRet['id']
        assert addRet['ret'] == 0

    def test_113(self):
        print("删除订单")
        self.test_112()
        oid = self.add_order_id
        r = apimgr.order_delete(oid)
        deleteRet = r.json()
        assert deleteRet['ret'] == 0













