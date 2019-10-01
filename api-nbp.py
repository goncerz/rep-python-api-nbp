import requests

def getUrl(url):
    req = requests.get(url)
    reqCode = req.status_code

    if reqCode == requests.codes.ok:
        reqJson = req.json()

        if type(reqJson) is list:
            reqJson0 = reqJson[0]

            if type(reqJson0) is dict:
                if "rates" in reqJson0.keys():
                    rates = reqJson0["rates"]

                    if type(rates) is list:
                        for rate in rates:
                            if type(rate) is dict:
                                keys = rate.keys()

                                if "currency" in keys:
                                    if "code" in keys:
                                        if "mid" in keys:
                                            print(
                                                rate["currency"].ljust(50),
                                                "1",
                                                rate["code"],
                                                "=",
                                                rate["mid"],
                                                "PLN")


################################################################################


urlNbpA = "http://api.nbp.pl/api/exchangerates/tables/a/?format=json"
urlNbpB = "http://api.nbp.pl/api/exchangerates/tables/b/?format=json"

getUrl(urlNbpA)
getUrl(urlNbpB)
