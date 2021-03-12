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
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }

