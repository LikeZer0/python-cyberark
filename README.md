# Python CyberArk module

The module, forked from iamtrump/python-cyberark, implements few CyberArk API functions. The only difference is that in this version we skip certificate validation. This fork is meant to be used in lab environments; I suggest using the original python-cyberark module for production.

## Requirements
* CyberArk 9.3+
## Installation
```
pip install git+https://github.com/LikeZer0/python-cyberark.git
```
## Code example

```
import cyberark

ca = cyberark.CyberArk("https://cyberark.local", "my_login", "password")
# List safes:
print(ca.list_safes())
# Print account details
print(ca.get_account_details("Safe", "Account_name"))
ca.logoff()
```
