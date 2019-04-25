import smartsheet

"""
Token = 'c07p10drrej00l1ylcm904uq2w'
"""

token = 'c07p10drrej00l1ylcm904uq2w'
ss_client = smartsheet.Smartsheet(token)
user_profile = ss_client.Users.get_current_user()
print(user_profile.email)
sheets_response = ss_client.Sheets.list_sheets(include_all=True)
sheets = sheets_response.data
for i in range(len(sheets)):
    print('%s, %s' % (i, sheets[i].name))
