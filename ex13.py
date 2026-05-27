emails = ["teste@gmail.com", "admin@escola.br", "prof@escola.br","bob@gmail.com","bob2@outlook.com"]
print("E-mails:",emails)
print("E-mails escolares:")
for email in emails:
    if email.endswith("@escola.br"):
        print(email)
