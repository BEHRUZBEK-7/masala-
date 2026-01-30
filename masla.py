# class Hayvon :
#     def __init__(self, name):
#         self.name = name
#
#     def ovoz_chiqar(self):
#         return f"hayvon ovoz chiqarmaoqda"
# class it(Hayvon) :
#     def ovoz_chiqar(self):
#         return f"Vov - vov!"
# it = It("Bobik")
# print(it.name)
# print(it.ovoz_chiqar())

# class shakl :
#     def __init__(self, rang):
#         self.rang = rang
#
# class kvadirat(shakl) :
#     def __init__(self, rang):
#         shakl.__init__(self, rang)
#
#
#
#
# k = kvadirat("qizil"  )
# print(k.rang)
# print(5 * 5)

# class Xodim :
#     def __init__(self, ism, mosh):
#         self.ism = ism
#         self.mosh = mosh
#
# class Manager(Xodim):
#     def __init__(self, ism, mosh):
#         Xodim.__init__(self, ism, mosh)
#
#     Manager = Xodim("Farhod",12000 )
# print(Manager.ism)
# print(Manager.mosh)

# class Trik :
#     def __init__(self, name, turi, qanday_boqiladi, ovozi):
#         self.name = name
#         self.turi = turi
#         self.qanday_boqiladi = qanday_boqiladi
#         self.ovozi = ovozi
# class Mushuk(Trik) :
#     def __init__(self, name, turi, qanday_boqiladi, ovozi ) :
#         Trik.__init__(self, name, turi, qanday_boqiladi, ovozi)
# m = Mushuk("Mushuk", "sut emuzuvchi", "uy hayvoni", "miyov!" )
# print(m.name)
# print(m.turi)
# print(m.qanday_boqiladi)
# print(m.ovozi)

# class Transport :
#     def __init__(self,name):
#         self.name = name
# class Avtomabil(Transport) :
#     def __init__(self, name, price, service_fee ) :
#         Transport.__init__(self, name)
# class Velasapet(Transport) :
#     def __init__(self, name, price, service_fee ) :
#         Transport.__init__(self, name)
# a = Avtomabil("bu aftomabil")
# b = Velasapet("bu velasapet")
# print(a)
# print(b)
