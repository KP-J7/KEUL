'''KE Universal Library - KEUL Version 2.0'''
import platform
global s
from math import*
def pp(i):
   return i+1
def mm(i):
   return i-1
def revd(a,b):
   return b/a
def fl(a):
   return float(a)
def unit(a):
   return int(a)
def line(a):
   return str(a)
def sym(a):
   return char(a)
def s(a):
   return str(a)
def f(a):
   return float(a)
def p(n):
   print(n)
def typing(n):
   print(n)
def pr(n):
   print(n)
def tp(n):
   print(n)
def typ(n):
   print(n)
def m(a,b):
   return a*b
def d(a,b):
   return a/b
def stick(s,a):
   a.append(s)
def st(a,b):
   return a**b
def circlesqr(r):
   return pi*r*r
def circlelnth(r):
   return 2*pi*r
def sqrsqr(a):
   return a*a
def sqrp(a):
   return 4*a
def sqrprgtrg(a,b):
   return (a*b)/2
def systsch(num,i):
   result = ''
   while num:
      result += str(num %i)
      num //= i
   return result[::-1]
def step(s):
   return s.clear()
def md(n):
   return abs(s)
def ln(n):
   return log(n)
def lg(n):
   return log10(n)
def binn(n):
   return bin(n)[2:]
def hexn(n):
   return hex(n)[2:]
def octn(n):
   return oct(n)[2:]
def symb(n):
   return chr(n)
def codsymb(n):
   return ord(n)
def fact(n):
   return factorial(n)
def root(n,k):
   return n**(1/k)
def rootst(n,k,m):
   return n**(m/k)
def simpleexpeq(x,z):
   return log(z,x)
def tg(x):
   return tan(x)
def ctg(x):
   return 1/(tan(x))
def sin2a(x):
   return 2*sin(x)*cos(x)
def nok(a,b):
   return lcm(a,b)
def nod(a,b):
   return gcd(a,b)
def bitesinbits(n):
   return n*8
def bitsinbites(n):
   return n/8
def kbinbites(n):
   return n*1024
def bitesinkb(n):
   return n/1024
def mbinkb(n):
   return n*1024
def kbinmb(n):
   return n/1024
def gbinmb(n):
   return n*1024
def mbingb(n):
   return n/1024
def tbingb(n):
   return n*1024 
def pbingb(n):
   return n*1024
def gbinpb(n):
   return n/1024
def bitsinkb(n):
   return n/(1024*8)
def imp(a,b):
   return a<=b
def equ(a,b):
   return a==b
def cl():
   return list()
def l(s):
   return len(a)
def srt(n):
   return sorted(n)
def revsrt(n):
   return sorted(n,reverse=True)
def bck(n):
   return n.pop()
def frc(n):
   return float(n)
def i(n):
   return int(n)
def squaresurfsphere(r):
   return 4*pi*r**2
def squaresurfcube(a):
   return 6*(a**2)
def spherevol(r):
   return (4/3)*pi*(r**3)
def osversion():   
   try:     
      version = {
            'platform': platform.platform(),
            'version': platform.version(),
            'release': platform.release(),
            'system': platform.system(),
            'arch': platform.architecture(),
            'machine': platform.machine(),
            'node': platform.node(),
            'processor': platform.processor()
        }
      return version
   except Exception as e:
      return {'error': str(e)}
def winver():   
   version_info = osversion()    
   if 'error' in version_info:
      print(f"Error while getting OS informat: {version_info['ошибка']}")
   else:
      print("OS info:")
      print(f"System: {version_info['system']}") 
      print(f"Release: {version_info['release']}") 
      print(f"Version: {version_info['version']}")
      print(f"Platform: {version_info['platform']}")              
      print(f"Architecture: {version_info['arch']}")      
      print(f"Machine: {version_info['machine']}")
      print(f"Node: {version_info['node']}")
      print(f"Processor: {version_info['processor']}") 
      if platform.system()=='Windows':
         print(f"Edition:{platform.win32_edition()}")    
if __name__ == '__main__':
   winver()