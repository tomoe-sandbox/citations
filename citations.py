
# Accept a citation and save it as a dictionary as such:

# McGill: <PARTY NAME>, <YEAR> <COURT> <CASE>. e.g. Radonna Investments Ltd v Rubin, 2012 ONCA 321.                                                                                                                                                                                                                                         
# OSCOLA: <PARTY NAME> <[YEAR]> <COURT> <CASE>. e.g. Corr v IBC Vehicles Ltd [2008] UKHL 13; Attorney-General v Ting Choon Meng [2017] SGCA 6 

# # We've created a dictionary called "citation" for you.
# citation = {
#     "party": "",
#     "year": "",
#     "court":"",
#     "case_no": ""
# }

# # Create list for recording users' citations 
# citations = []


# # Accept user input
# is_active = True

# while is_active:
#     user_cite = input("Enter your citation here in the format PARTY YEAR COURT CASE e.g. Corr v IBC Vehicles Ltd 2008 UKHL 13: ")
#     # We want to get everything before the year.
#     index = 0 
#     # Get party name 
#     for char in user_cite:
#         if char.isdigit():
#             index = user_cite.index(char)
#             party = user_cite[0:index]
#             citation["party"] = party
#             print(citation)
#             break
print("Hello!")

