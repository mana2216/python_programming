interpreter = ['Python', 'Perl', 'Ruby']
compiler = ['C#', 'C++', 'Java']
language = 'Python'

if language in interpreter:
    print('インタプリター言語')
elif language in compiler:
    print('コンパイル言語')
else:
    print('不可')