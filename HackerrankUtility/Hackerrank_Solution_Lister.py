'''
Title     : Hackerrank Solution Lister
Subdomain : None
Domain    : None
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2017
'''
import re,os,sys

info_file_name = 'python_info.txt'

def get_valid_name(given_name):
    return re.sub(r'[^\w]','',given_name)

problem_list = ''
subdomain_name = ''
extension = '.py'

info_file = open(info_file_name,"r")
info_file_lines = info_file.readlines()
info_file.close()
output_file_name = 'solution_list.html'
f = open(output_file_name,'w')
f.write('<ul>\n')
for line in info_file_lines:
    line = line.strip()
    if line == '':
        continue
    elif line[0] == '[':
        problem_list = line
    else:
        subdomain_name = line        
    if subdomain_name != '' and problem_list != '':
        folder_name = get_valid_name(subdomain_name)
        title_ar = re.findall(r'("[^"]*")',problem_list)
        title_ar_len = len(title_ar)
        f.write('  <li>'+subdomain_name+'\n')
        f.write('    <ul>\n')
        for title in title_ar:
            filename = get_valid_name(title[1:-1])
            filepath = folder_name + '\\' + filename+extension
            f.write('      <li>['+title[1:-1]+']('+filepath+')</li>\n')
        f.write('    </ul>\n')
        f.write('  </li>\n')
        subdomain_name = ''
        problem_list = ''
f.write('</ul>\n')
f.close()
print('List generated successfully. Open '+output_file_name+' to view.')
