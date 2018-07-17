p = 7901324502264899236349230781143813838831920474669364339844939631481665770635584819958931021644265960578585153616742963330195946431321644921572803658406281
q = 12802918451444044622583757703752066118180068668479378778928741088302355425977192996799623998720429594346778865275391307730988819243843851683079000293815051
dp = 5540655028622021934429306287937775291955623308965208384582009857376053583575510784169616065113641391169613969813652523507421157045377898542386933198269451
dq = 9066897320308834206952359399737747311983309062764178906269475847173966073567988170415839954996322314157438770225952491560052871464136163421892050057498651
c = 62078086677416686867183857957350338314446280912673392448065026850212685326551183962056495964579782325302082054393933682265772802750887293602432512967994805549965020916953644635965916607925335639027579187435180607475963322465417758959002385451863122106487834784688029167720175128082066670945625067803812970871

def decodeWithAllValues(p, q, dp, dq, c):

    def egcd(a, b):
         if a == 0:
             return (b, 0, 1)
         else:
             g, y, x = egcd(b % a, a)
             return (g, x - (b // a) * y, y)
    def modinv(a, m):
         g, x, y = egcd(a, m)
         if g != 1:
             raise Exception('modular inverse does not exist')
         else:
             return x % m

    qinv = modinv(q, p)
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    h = (qinv * (m1 - m2)) % p
    m = m2 + h * q
    return hex(m)

print decodeWithAllValues(p, q, dp, dq, c)
