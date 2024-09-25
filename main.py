def get_math_text(a, b, c):
  d=(b**2)-(4*a*c)
  if (d<0):
    return None
  else:
    x1=((b*-1)+(d**0.5))/(2*a)
    x2=((b*-1)-(d**0.5))/(2*a)
    return [x1,x2]
a=input('Введите любой a')
b=input('Введите любой b')
c=input('Введите любой c')
d=get_math_text(a,b,c)
print(d)
def summ(s1, s2):
  s=s1+s2
  return s
f= summ(d, 10)
print(f)
