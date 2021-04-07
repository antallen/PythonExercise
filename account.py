passwords = {"Peter" : "Aa123456", "Jame" : "qweasdxzc"}
print(f'{"Success" if passwords["Peter"] == "Bb123qweasd" else "Login Error"}')

passwords.update({"Rose" : "Hello123"})
print(passwords)