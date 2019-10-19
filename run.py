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
print("Customer result is " + str(customerResult))

customer = customerResult.data

# if customer:
#     purchaseCodeResult = progbonus.send_purchase_code(customer["customerId"], 10)
#     print("Purchase code result is " + str(purchaseCodeResult))
# else:
#     regCodeResult = progbonus.send_registration_code(os.getenv("TEST_PHONE"))
#     print("Registration code result is " + str(regCodeResult))

# purchaseCodeResult = progbonus.send_purchase_code(customer["customerId"], 10)
# print("Purchase code result is " + str(purchaseCodeResult))

# CHECK REGISTRATION CODE
# res = progbonus.is_registration_code_valid("2557", os.getenv("TEST_PHONE"))
# print("Result is " + str(res))

# SAVE CUSTOMER
res = progbonus.save_customer(os.getenv("TEST_PHONE"), os.getenv("TEST_NAME"), "2557")
print("Result is " + str(res))

# CHECK PURCHASE CODE
# res = progbonus.is_purchase_code_valid("1232", customer["customerId"])
# print("Result is " + str(res))

# SAVE PURCHASE
# res = progbonus.save_purchase(customer["customerId"], 10, 0, "1234")
# print("Result is " + str(res))

