import os

cmd = [  # 执行monkey 注入1000事件
        'adb shell monkey 1000',
        # 查看应用包名
        'adb shell dumpsys window w |findstr \/ |findstr name=',
        # 人大APP执行monkey测试，注入1000事件
        'adb shell monkey -p com.guopeiyu.rmo 1000',
        # 人大APP执行mokey测试，注入1000时间并下载日志
       ' adb shell monkey -p com.guopeiyu.rmo -v-v-v 10000 >d:\RDAPP.txt ',
       ]

os.system(cmd[3])