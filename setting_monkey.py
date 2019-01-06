# -*- coding:utf-8 -*-  
# __auth__ = mocobk
# email: mailmzb@qq.com
import configparser
from adk import print_color_font

event_parameter = """
--pct-touch     0：触摸事件百分比
--pct-motion    1：滑动事件百分比
--pct-pinchzoom 2：缩放事件百分比
--pct-trackball 3：轨迹球事件百分比
--pct-rotation  4：屏幕旋转事件百分比
--pct-nav       5：基本导航事件百分比
--pct-majornav  6：主要导航事件百分比
--pct-syskeys   7：系统事件百分比
--pct-appswitch 8：Activity启动事件百分比
--pct-flip      9：键盘翻转事件百分比
--pct-anyevent  10：其他事件百分比
example:--pct-touch 40 --pct-motion 30 --pct-rotation 20 --pct-appswitch 10
"""


def select_event():
    print(u'1 触摸优先  2 滑动优先  3 屏幕旋转优先  4 Activity切换优先  5 自定义事件')
    event = None
    pattern_num = input('\n请选择事件：')
    if pattern_num == '1':
        event = '--pct-touch 50'  # 触摸事件优先
    elif pattern_num == '2':
        event = '--pct-motion 50'  # 滑动事件优先
    elif pattern_num == '3':
        event = '--pct-rotation 50'  # 屏幕旋转优先
    elif pattern_num == '4':
        event = '--pct-appswitch 50'  # Activity启动事件优先
    elif pattern_num == '5':
        print_color_font(event_parameter, 0x0b)
        # print(event_parameter)
        event = input('输入自定义参数：\n')  # 自定义事件
    else:
        event = ''  # 无优先事件
    return event


def set_parameter(pck_name):
    event = select_event()
    seed = input('请输入种子数(1-10000)：')
    throttle_time = input('请输入事件间隔时间(ms)：')
    count = input('请输入事件运行次数：')
    monkey_cmd = 'monkey -p {pck_name} {event} -s {seed} --throttle {throttle_time} --ignore-timeouts ' \
                 '--ignore-crashes --monitor-native-crashes -v -v -v {count} >'.format(pck_name=pck_name,
                                                                                       event=event, seed=seed,
                                                                                       throttle_time=throttle_time,
                                                                                       count=count)
    print_color_font('\n您设置的命令参数如下(执行大约%s秒)：\n\n%s' % (str((float(throttle_time)/1000)*int(count)/3), monkey_cmd), 0x0b)

    cf = configparser.ConfigParser()
    cf.set('DEFAULT', 'cmd', value=monkey_cmd)
    cf.set('DEFAULT', 'package_name', value=pck_name)
    cf.set('DEFAULT', 'net', value='wifi')
    fp = open('monkey.ini', 'w+')
    cf.write(fp)
    fp.close()
    print_color_font('\n按回车开始测试！', 0x0e)
    t = input()


if __name__ == '__main__':
    set_parameter('com.mpr.mprepubreader')
