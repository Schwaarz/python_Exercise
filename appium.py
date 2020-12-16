import uiautomator2 as u2

d = u2.connect()

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
    d.click(246, 1380)
    d(description="发布动态 ").click()
    d(text="这一刻的想法……").click()
    d.send_keys("简单的测试", clear=True)
    d.click(364, 771)
    d(description="确定 ").click()



#RdlzTest()
xwTest()