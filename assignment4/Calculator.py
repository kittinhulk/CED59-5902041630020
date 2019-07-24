class Calculator():
  def __init__(self,input_x,input_y):
    self.x = input_x
    self.y = input_y

  def multiply(self):
    result = self.x * self.y
    print('result of',self.x ,'x',self.y ,'=' ,result)

  def plus(self):
    result = self.x + self.y
    print('result of',self.x ,'+',self.y ,'=' ,result)

  def minus(self):
    result = self.x - self.y
    print('result of',self.x ,'-',self.y ,'=' ,result)

  def divide(self):
    result = self.x / self.y
    print('result of',self.x ,'/',self.y ,'=' ,result)

print('Ex: var1 symbols var2 = result')
x = int(input('input var1(number) : '))
y = int(input('input var2(number) : '))
symbols = input("symbols(+,-,*,/) : ")
cal = Calculator(x,y)

if symbols=='+':
  cal.plus()
if symbols=='-':
  cal.minus()
if symbols=='*':
  cal.multiply()
if symbols=='/':
  cal.divide()
