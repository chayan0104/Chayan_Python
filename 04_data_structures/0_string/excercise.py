email = "chayan.samanta@gmail.com"
phone = 998777666
local, domain = email.split('@')

masked_local = ""

for i in range(len(local)):
    if i == 0 or i == len(local) - 1 or local[i]==".":
        masked_local += local[i]
    else:
        masked_local += "*"

masked_email = masked_local + "@" + domain  
print(masked_email)

# -------------------------------------------------------
phone_str = str(phone)
masked_phone =""
for j in range(len(phone_str)):
    if j == 0 or j == len(phone_str) - 1:
        masked_phone += phone_str[j]
    else:
        masked_phone += "*"

print(masked_phone)