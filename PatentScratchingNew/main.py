from bs4 import BeautifulSoup
from urllib import parse, request, response
from baseClass import base
import json
import xlwt
from xlrd import open_workbook

"""
    table -> tr -> a
"""


class Scratching(base):

    def __init__(self, param_wanted, bank_wanted):
        super().__init__()
        self.param_wanted = param_wanted
        self.bank_wanted = bank_wanted
        self.count = 0
        self.dic = {}
        self.page_index = 0

    def cpc_extract(self, urlGet):
        self.count += 1
        url_record = self.url2 + urlGet
        req_record = request.Request(method="GET", url=url_record, headers=self.headers)
        respond_record = request.urlopen(req_record, timeout=600).read()
        res_record = respond_record.decode('utf-8')
        soup = BeautifulSoup(res_record, 'html.parser')
        peas = soup.find_all('p')
        dic_new = {}
        print(soup.title.string)
        for pea in peas:
            if pea.find("table"):
                target_list = pea.find_all('td')
                for target in target_list:
                    if not target.find('b'):
                        CPC_list = str(target.text).split(";")
                        for CPC_raw in CPC_list:
                            CPC = CPC_raw.split("/")[0].replace(" ", "")
                            if CPC not in dic_new and CPC.count(self.param_wanted):
                                dic_new[CPC] = 1
                            elif CPC in dic_new:
                                dic_new[CPC] += 1
                        print(self.count)
                        return dic_new

    def page_find(self):
        self.page_index += 1
        Base = base()
        if self.page_index > 1:
            self.params2['p'] = str(self.page_index)
            self.params2['RS'] = Base.params2['RS'].format(label=self.param_wanted, bank_name=self.bank_wanted)
            self.params2['OS'] = Base.params2['OS'].format(label=self.param_wanted, bank_name=self.bank_wanted)
            self.params2['S1'] = Base.params2['S1'].format(label=self.param_wanted, bank_name=self.bank_wanted)
            urlQuery = self.url + '?' + parse.urlencode(self.params2)
        else:
            self.params['RS'] = Base.params['RS'].format(label=self.param_wanted, bank_name=self.bank_wanted)
            self.params['Query'] = Base.params['Query'].format(label=self.param_wanted, bank_name=self.bank_wanted)
            urlQuery = self.url + '?' + parse.urlencode(self.params)
        req = request.Request(method="GET", url=urlQuery, headers=self.headers)
        respond = request.urlopen(req, timeout=600).read()
        respond = respond.decode('utf-8')

        soup = BeautifulSoup(respond, 'html.parser')
        tables = soup.find_all('table')
        url_set = set()
        url_next_page = ""

        for table in tables:
            records = table.find_all("tr")
            for record in records:
                a_records = record.find_all("a")
                for a_record in a_records:
                    if 'href' in a_record.attrs and str(a_record['href']).startswith("/netacgi/nph-Parser"):
                        if a_record.find("img") and a_record.find("img")['alt'] == "[NEXT_LIST]":
                            url_next_page = a_record['href']
                        else:
                            url_set.add(a_record['href'])

        while len(url_set):
            dic_new = self.cpc_extract(url_set.pop())
            for CPC, CPC_count in dic_new.items():
                if CPC in self.dic:
                    self.dic[CPC] = self.dic[CPC] + CPC_count
                else:
                    self.dic[CPC] = CPC_count
            print(self.dic)

        if url_next_page != "":
            print("new page index is " + str(self.page_index + 1))
            self.page_find()


# bank_wanted_list = ["Wells Fargo"] param_wanted_list = ["B08B", "B42D", "B65D", "E04B", "G02B", "G03B", "G06F",
# "G06K", "G06N", "G06Q", "G06T", "G07B", "G07C", "G07D", "G07F", "G08B", "H04L", "H04M", "H04N", "H04W", "Y10S"]

bank_wanted_list = []
param_wanted_list = []
wanted_list: [(str, str)] = []
book1 = open_workbook("1.xlsx")
bank_wanted_sheet = book1.sheet_by_index(0)
book2 = open_workbook("2.xlsx")
param_wanted_sheet = book2.sheet_by_index(0)

for bank_num in range(0, bank_wanted_sheet.nrows):
    bank_wanted_list.append(bank_wanted_sheet.row_values(bank_num)[0])

for param_num in range(0, param_wanted_sheet.nrows):
    param_wanted_list.append(param_wanted_sheet.row_values(param_num)[0])

# for bank_wanted in range(0, bank_wanted_sheet.nrows): for param_wanted in range(0, param_wanted_sheet.nrows):
# wanted_list.append((bank_wanted_sheet.row_values(bank_wanted)[0], param_wanted_sheet.row_values(param_wanted)[0]))


book_write = xlwt.Workbook()
sheet_write = book_write.add_sheet("sheet0")
dic_CPC_Number = {}
row_count = 1

for bank_name in bank_wanted_list:
    list_to_append = [0 for i in range(0, len(dic_CPC_Number) + 1)]
    list_to_append[0] = bank_name
    for param_name in param_wanted_list:
        search = Scratching(bank_wanted=bank_name, param_wanted=param_name)
        search.page_find()
        for CPC_name, CPC_count in search.dic.items():
            if CPC_name in dic_CPC_Number:
                list_to_append[dic_CPC_Number[CPC_name]] = CPC_count
                continue
            len_of_dic = len(dic_CPC_Number)
            dic_CPC_Number[CPC_name] = len_of_dic + 1
            list_to_append.append(CPC_count)
    for i in range(0, len(list_to_append)):
        sheet_write.write(row_count, i, list_to_append[i])
    row_count += 1

list_to_append = [""]
for a in range(0, len(dic_CPC_Number)):
    list_to_append.append(a)
for i in range(0, len(list_to_append)):
    sheet_write.write(0, i, list_to_append[i])
book_write.save("saved.xlsx")

# for bank_name, param_name in wanted_list:
#     search = Scratching(bank_wanted=bank_name, param_wanted=param_name)
#     search.page_find()
#     list_to_append = [0 for i in range(0, len(dic_CPC_Number) + 1)]
#     for CPC_name, CPC_count in search.dic.items():
#         if CPC_name in dic_CPC_Number:
#             list_to_append[dic_CPC_Number[CPC_name]] = CPC_count
#             continue
#         len_of_dic = len(dic_CPC_Number)
#         dic_CPC_Number[CPC_name] = len_of_dic + 1
#         list_to_append.append(CPC_count)
#     list_to_append[0] = bank_name


# with open("{label} {bank_name}.json".format(label=search.param_wanted, bank_name=search.bank_wanted),
#           'w') as json_file:
#     json_file.write(json.dumps(search.dic, indent=2))

# for bank_name in bank_wanted_list:
#     for bank_param in param_wanted_list:
#         search = Scratching(bank_wanted=bank_name, param_wanted=bank_param)
#         search.page_find()
#
