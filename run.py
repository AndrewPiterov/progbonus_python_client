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
# purchaseCodeResult = progbonus.send_purchase_code(customer["customerId"], 10)
# print("Purchase code result is " + str(purchaseCodeResult))

# CHECK PURCHASE CODE
res = progbonus.is_purchase_code_valid("1232", customer["customerId"])
print("Result is " + str(res))

# SAVE PURCHASE
res = progbonus.save_purchase(customer["customerId"], 10, 0, "1234")
print("Result is " + str(res))

# res = ProgBonus().save_customer(test_phone, test_name, "3288")
# print("Result is " + str(res))
