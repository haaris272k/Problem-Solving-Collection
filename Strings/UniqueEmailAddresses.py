# Unique Email Addresses
# 929 LC
# https://leetcode.com/problems/unique-email-addresses/

emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]

# all dots before @ will be removed/ignored
# anything after + and before @ will be removed

processedmail = []

for i in range(len(emails)):

    mail = emails[i]

    for j in range(len(mail)):

        if mail[j] == "@":

            localname = mail[:j]
            domainname = mail[j:]

            # removing . in localnames
            localname = localname.replace(".", "")

            # removing everything after + char
            localname = localname.split("+")[0]

            # finally processing the email
            processedmail.append(localname + domainname)

print(processedmail)

print(len(set(processedmail)))
