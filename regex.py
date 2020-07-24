import re

text_to_search = '''ABCFDEF
abcedfed
what'up guys
www.tata.com
943--189-3270
324.545.4443
800-321-2345
900-666-777
Tata Sons,
Bombay House
24, Homi Mody Street
Mumbai 400 001
Phone:+91 (22) 6665 8282
Fax:+91 (22) 6665 8080
Email: info@tata.com
Site: www.tata.com

Ha HaHa
Mr. Jhonson
Mrs. Harry
Ms. Reema
cat
Mr. T
rat
bat

ayushyadav@gmail.com
Ayush32@gmail.com
yadavayush2@gmail.com
corey.sch@unive.edu
corey-r3-r@edep-my.ner
[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|ner)
http://www.goggg.com
https://www.wow.com
http://www.cant.com
https://youtube.com
https://www.nasssss.gov
https?://(w){3}\.?\w+\.(com|gov)
'''
compliling = re.compile(r'''(
''', re.VERBOSE)
subbed_urls = compliling.sub('\1\2', text_to_search)
print(subbed_urls)

# matches = compliling.finditer(text_to_search)


'''with open('regex_match', 'r') as f:
    contents = f.read()
    matches = compliling.finditer(contents)'''
# for match in matches:
#   print(match.group(0))
# print(text_to_search[71:83])
