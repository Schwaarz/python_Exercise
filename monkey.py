import os

cmd = ['adb shell monkey 1000', # 执行monkey 注入1000事件
      'adb shell dumpsys window w |findstr \/ |findstr name=', # 查看应用包名
        'adb shell monkey -p com.guopeiyu.rmo 1000', # 人大APP执行monkey测试，注入1000事件
       'adb shell monkey -p com.guopeiyu.rmo -v-v-v 10000 >d:\RDAPP.txt ', # 人大APP执行mokey测试，注入1000时间并下载日志
       ]

os.system(cmd[3])