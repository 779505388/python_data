import time as t
class Mytime():
    
    def start(self):
        """开始计时…………"""
        self.start=t.localtime
        print('计时开始……')
    def stop(self):
        """停止计时…………"""
        self.stop=t.localtime
        print('停止计时……')
    def __calu__(self):
        """计算运行时间"""
        