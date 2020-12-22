import uiautomator2 as u2

d = u2.connect()

#修改延迟为操作前延迟 2S 操作后延迟 0S
d.settings['operation_delay'] = (2,0)
#修改延迟生效方法
d.settings['operation_delay_methods'] = ['click','press','send_keys']
# 修改默认等待
d.settings['wait_timeout'] = 10
# 输出全局设置信息
print(d.settings)

# a = d(description=" 会议").exists
# b = True
# print(a)
# if a == True:
#     print(b)

# d(description=" 会议").click()
# d(description=" ").click()
# d(description=" 知识库").click()
# d(description=" 我的").click()

def xwTest():
    # 首页推荐下滑
    d.swipe(32, 1233, 32, 379)
    # 点击新闻链接再返回列表
    d(description="全国人大常委会全票通过香港特别行政区维护国家安全法").click()
    d.xpath('//*[@content-desc="光明人大"]/android.view.View[1]/android.view.View[1]').wait(3)
    d.xpath('//*[@content-desc="光明人大"]/android.view.View[1]/android.view.View[1]').click()
    print('首页新闻跳转正常')
    d(description="人大要闻").click()
    d.click(335, 296)
    d.xpath('//*[@content-desc="光明人大"]/android.view.View[1]/android.view.View[1]').wait(3)
    d.xpath('//*[@content-desc="光明人大"]/android.view.View[1]/android.view.View[1]').click()
    print('人大要闻tab新闻跳转正常')
    d(description="工作动态").click()
    d(description="省十三届人大三次会议主席团举行第一次会议").click()
    d.xpath('//*[@content-desc="光明人大"]/android.view.View[1]/android.view.View[1]').wait(3)
    d.xpath('//*[@content-desc="光明人大"]/android.view.View[1]/android.view.View[1]').click()
    print('工作动态tab新闻跳转正常')
    d(description="通知公告").click()
    d(description="深圳市光明区第一届人民代表大会公告").click()
    d.xpath('//*[@content-desc="光明人大"]/android.view.View[1]/android.view.View[1]').wait(3)
    d.xpath('//*[@content-desc="光明人大"]/android.view.View[1]/android.view.View[1]').click()
    print('通知公告tab新闻跳转正常')
    d(description="人大会议").click()
    d(description="聚焦光明两会 | 光明区第一届人民代表大会第三次会议胜利闭幕").click()
    d.xpath('//*[@content-desc="光明人大"]/android.view.View[1]/android.view.View[1]').wait(3)
    d.xpath('//*[@content-desc="光明人大"]/android.view.View[1]/android.view.View[1]').click()
    print('人大会议tab新闻跳转正常')

def RdlzTest():
    d(description=" 人大履职").click()  # 点击人大履职
    d.click(673, 456) # 点击发布动态
    d(text="这一刻的想法……").send_keys("简单的测试，发布一条新动态") # 输入动态文字
    d.click(155, 496)   # 点击上传
    d.click(375, 148)   # 点击图片
    d.click(763, 80)    # 确定上传
    d.click(725, 95)    # 点击发布
    d(description=" ").click()  # 点击中心

def HyTest():
    d.click(487, 1147) # 点击第一个会议
    d(description="签到").click() # 点击进入签到页面
    d.xpath('//*[@content-desc="光明人大"]/android.view.View[6]/android.view.View[1]').click()  # 点击签到

def loginTest():
    d(description=" 会议").click()
    d(text="输入手机号").send_keys("15766471748")
    d(text="请输入验证码").send_keys("gmrd2019")
    d.click(155, 1038)
    d(description="登录").click()




loginTest()
#HyTest()
#RdlzTest()
#xwTest()