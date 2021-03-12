class base:

    def __init__(self):
        self.url = "http://patft.uspto.gov/netacgi/nph-Parser"
        self.url2 = "http://patft.uspto.gov"

        self.params = {
            'Sect1': 'PTO2',
            'Sect2': 'HITOFF',
            'u': "/netahtml/PTO/search-adv.htm",
            'r': '0',
            'f': 'S',
            'l': '50',
            'd': 'PTXT',
            'RS': """((CPCL/{label} AND (AN/"{bank_name}" OR AANM/"{bank_name}")) AND ISD/19900101->20200101)""",
            'Refine': 'Refine Search',
            'Query': """CPCL/{label} AND (AN/"{bank_name}" OR AANM/"{bank_name}") AND ISD/19900101->20200101"""
        }
        # p:2
        # S1
        # Page: Next
        # OS:
        # RS:
        # No query now

        self.params2 = {
            'Sect1': 'PTO2',
            'Sect2': 'HITOFF',
            'u': "/netahtml/PTO/search-adv.htm",
            'r': '0',
            'f': 'S',
            'l': '50',
            'd': 'PTXT',
            'p': '{page}',
            'S1': """(({label}.CPCL. AND (("{bank_name}".ASNM.) OR ("{bank_name}".AANM.))) AND @PD>=19900101<=20200101)""",
            'Page': 'Next',
            'OS': """CPCL/{label} AND (AN/"{bank_name}" OR AANM/"{bank_name}") AND ISD/19900101->20200101""",
            'RS': """((CPCL/{label} AND (AN/"{bank_name}" OR AANM/"{bank_name}")) AND ISD/19900101->20200101)"""
        }

        self.headers = {
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
            'Connection': "keep-alive",
            'Host': "patft.uspto.gov",
            'Referer': "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&f=S&l=50&d=PTXT&RS=%28%28CPCL%2FG02B+AND+%28AN%2F%22Wells+Fargo%22+OR+AANM%2F%22Wells+Fargo%22%29%29+AND+ISD%2F19900101-%3E20200101%29&Refine=Refine+Search&Query=CPCL%2FG02B+AND+%28AN%2F%22Wells+Fargo%22+OR+AANM%2F%22Wells+Fargo%22%29+AND+ISD%2F19900101-%3E20200101",
            'Upgrade-Insecure-Requests': "1",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36}"
        }
