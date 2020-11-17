import pytest
from lib.白月黑羽练习API.发送请求库 import apimgr

@pytest.fixture(scope='package',autouse=True)
def st_emptyEnv():
    print('\n**整个目录初始化')
    apimgr.mgr_login()
    apimgr.order_delete_all()
    apimgr.customer_delete_all()
    apimgr.medicine_delete_all()
    yield

    apimgr.order_delete_all()
    apimgr.customer_delete_all()
    apimgr.medicine_delete_all()


