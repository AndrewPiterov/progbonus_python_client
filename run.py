from dotenv import load_dotenv
import os
from progbonus import ProgBonusCredentials, ProgBonus

load_dotenv()

PROGBONUS_API_URL = os.getenv("PROGBONUS_API_URL")
print("ProgBonus on " + PROGBONUS_API_URL)
print("Test phone is " + os.getenv("TEST_PHONE"))

cred = ProgBonusCredentials(
    os.getenv("PROGBONUS_API_URL"),
    os.getenv("PROGBONUS_MARKET_ID"),
    os.getenv("PROGBONUS_API_KEY"),
    os.getenv("PROGBONUS_STORE_ID"),
)

progbonus = ProgBonus(cred)

customerResult = progbonus.find_by_phone(os.getenv("TEST_PHONE"))
print("Result is " + str(customerResult))

# ProgBonus().send_registration_code(test_phone)
# res = ProgBonus().save_customer(test_phone, test_name, "3288")
# print("Result is " + str(res))
