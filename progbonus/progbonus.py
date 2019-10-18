import requests
import sys


class ProgBonusCredentials:
    def __init__(self, url, market_id, api_key, store_id):
        self.api_url = url
        self.market_id = market_id
        self.api_key = api_key
        self.store_id = store_id


class ProgBonusResult:
    def __init__(self, success, error=None, data=None):
        self.success = success and error is None
        self.error = error
        self.data = data

    def __str__(self):
        if self.error:
            return str(self.success) + ": " + self.error
        else:
            return str(self.success) + ": " + str(self.data)

    @staticmethod
    def get_result(response):
        if response.ok:
            return ProgBonusResult.ok(response.json())
        else:
            try:
                err = response.json()
                return ProgBonusResult.fail(err["error"])
            except:
                return ProgBonusResult.fail(response.reason)

    @staticmethod
    def ok(data=None):
        return ProgBonusResult(True, data=data)

    @staticmethod
    def fail(reason):
        return ProgBonusResult(False, error=reason)

    @staticmethod
    def exception(ex):
        return ProgBonusResult(False, error=ex)


class ProgBonus:
    def __init__(self, credentials: ProgBonusCredentials):
        self.base_url = credentials.api_url
        self.market_id = credentials.market_id
        self.api_key = credentials.api_key
        self.store_id = credentials.market_id

    # def get_customers(self):
    #     url = self.base_url + "/api/v1/customers"
    #     r = requests.get(url, headers={"Authorization": self.api_key})
    #     data = r.json()
    #     print(data)
    #     return data.items

    def find_by_phone(self, phone_number):
        url = (
            "/api/v1/customer/by/phone/"
            + phone_number
            + "/?include=bonusInfo,discountLevel"
        )
        return self.get_result(url)

    def send_registration_code(self, phone_number):
        url = (
            "/api/shortcodes/registration/?phoneNumber="
            + phone_number
            + "&storeId="
            + str(self.store_id)
        )
        return self.get_result(url, data=None)

    def save_customer(self, phone_number, full_name, short_code):
        url = "/api/v1/customers?include=bonusInfo,discountLevel"
        data = {
            "phoneNumber": phone_number,
            "fullName": full_name,
            "shortCode": short_code,
            "storeId": self.store_id,
        }
        return self.get_result(url, post=True, json=data)

    def get_result(self, url, post=False, data=None, json=None):
        u = self.base_url + url
        try:
            if post:
                r = requests.post(
                    u, data=data, json=json, headers={"Authorization": self.api_key}
                )
            else:
                r = requests.get(u, headers={"Authorization": self.api_key})
            return ProgBonusResult.get_result(r)
        except:
            ex = sys.exc_info()[0]
            print("Oops!", ex, "occured.")
            return ProgBonusResult.exception(ex)
