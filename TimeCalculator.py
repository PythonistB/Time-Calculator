clock = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23')   
days = ('Monday','tueSday','Wednesday','Thursday','Friday','Saturday','Sunday')
t1 = ['AM','PM']

s1 = ("3:00 PM", "3:10")
# Returns: 6:10 PM
s2 = ("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
s3 = ("11:43 AM", "00:20")
# Returns: 12:03 PM
s4 = ("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
s5 = ("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
s6 = ("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
a = []
b = []
c = []
m = []
e = []
f = []

def add_time():
    for i in s1:
       d = i.split(' ')
       a.extend(d) 
    t = a[0].split(':')      
    k = a[2].split(':')
    print(int(t[0]) + int(k[0]),':','{:02}'.format(int(t[1]) + int(k[1])),' ', a[1], sep='')
    for i in s2:
        d = i.split(' ')
        b.extend(d) 
    t = b[0].split(':')      
    k = b[2].split(':')
    div = int('{:02}'.format(int(t[1]) + int(k[1]))) // 60
    div1 = int('{:02}'.format(int(t[1]) + int(k[1]))) % 60
    for i in days:
        if i == b[3] and int(t[0]) < 12 and b[1] == 'AM' and (int(t[0]) + int(k[0])) > 12 and (int(t[1]) + int(k[1])) > 60 and (int(t[0]) + int(k[0])) < 24:
           print((int(t[0]) + int(k[0]) - 12) + div,':','{:02}'.format(div1),' ', t1[1],',',' ',b[3], sep='') 
    for i in s3:
        d = i.split(' ')
        c.extend(d) 
    t = c[0].split(':')      
    k = c[2].split(':')
    div = int('{:02}'.format(int(t[1]) + int(k[1]))) // 60
    div1 = int('{:02}'.format(int(t[1]) + int(k[1]))) % 60
    for i in clock:
        if i == t[0] and int(t[0]) < 12 and c[1] == 'AM' and (int(t[1]) + int(k[1])) > 60:
           print((int(t[0]) + int(k[0]) + div),':','{:02}'.format(div1),' ', t1[1],' ', sep='')  
    for i in s4:
        d = i.split(' ')
        m.extend(d) 
    t = m[0].split(':')      
    k = m[2].split(':')
    div = int('{:02}'.format(int(t[1]) + int(k[1]))) // 60
    div1 = int('{:02}'.format(int(t[1]) + int(k[1]))) % 60
    for i in clock:
        if i == t[0] and (int(t[0]) + int(k[0])) > 12 and m[1] == 'PM' and (int(t[1]) + int(k[1])) < 60:
           print((int(t[0]) + int(k[0]) - 12),':','{:02}'.format(int(t[1]) + int(k[1])),' ', t1[0],' ','(next day)', sep='')  
    for i in s5:
        d = i.split(' ')
        e.extend(d) 
    t = e[0].split(':')      
    k = e[2].split(':')
    div = int('{:02}'.format(int(t[1]) + int(k[1]))) // 60
    div1 = int('{:02}'.format(int(t[1]) + int(k[1]))) % 60
    for i in days:
        if i == e[3] and int(t[0]) + int(k[0]) > 24 and e[1] == 'PM' and (int(t[1]) + int(k[1])) > 60:
           print((int(t[0]) + int(k[0]) - 24) + div,':','{:02}'.format(div1),' ', t1[0],',',' ',days[3],' ','(2 days later)', sep='')
    for i in s6:
        d = i.split(' ')
        f.extend(d) 
    t = f[0].split(':')      
    k = f[2].split(':')
    div = int('{:02}'.format(int(t[1]) + int(k[1]))) // 60
    div1 = int('{:02}'.format(int(t[1]) + int(k[1]))) % 60
    div2 = (int(t[0]) + int(k[0]))//12
    for i in clock:
       if i == '{:02d}'.format(int(t[0])) and int(t[0]) + int(k[0]) > 24 and f[1] == 'PM' and (int(t[1]) + int(k[1])) < 60:
          print((int(t[0]) + int(k[0])) - div2*12,':','{:02}'.format(int(t[1]) + int(k[1])),' ', t1[0],' ','(9 days later)', sep='')
add_time()       