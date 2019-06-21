#property装饰器，把方法当成属性调用
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return  self._width*self._height

s = Screen()
s.width = 1024
print(s.width)
s.height = 768
print(s.height)
print(s.resolution)
