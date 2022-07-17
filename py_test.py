# 2 Table Methods
# ---------------
import prettytable

sample_dict = {'Abba':[ 'Abba Greatest Hits Vol.1','Abba Greatest Hits Vol.2','Waterloo' ],
'ABC':[ 'The Lexicon Of Love', "ABC Greatest Hits" ],
'AC/DC':[ 'Back In Black' , 'Highway to Hell' ],
'All About Eve':[ 'All About Eve' ]}
 
# Table from PrettyTable - produces a table with no rows
# url: https://pypi.org/project/prettytable/
 
pt = PrettyTable(['Artist', 'Album'])
for key, value in sample_dict.items():
    pt.add_row([key, "\n".join(value)])
    # tt.add_row([key, ",\n".join(value)])
 
pt.max_width["Artist"] = 20
pt.max_width["Album"] = 30
pt.padding_width = 2
pt.align["Artist"] = "r"
pt.align["Album"] = "l"
print(pt)
 
# Table from TextTable - produces a table with cells
# url: https://pypi.org/project/texttable/
 
from texttable import Texttable
t = Texttable()
for key, value in sample_dict.items():
    artist = key
    album = ("\n".join(value))
    t.add_rows([['Name', 'Age'], [artist, album]])

    print(t.draw())


# 2 Table Methods
# ---------------

sample_dict = {'Abba':[ 'Abba Greatest Hits Vol.1','Abba Greatest Hits Vol.2','Waterloo' ],
'ABC':[ 'The Lexicon Of Love', "ABC Greatest Hits" ],
'AC/DC':[ 'Back In Black' , 'Highway to Hell' ],
'All About Eve':[ 'All About Eve' ]}

# Table from PrettyTable - produces a table with no rows
# url: https://pypi.org/project/prettytable/

pt = PrettyTable(['Artist', 'Album'])
for key, value in sample_dict.items():
    pt.add_row([key, "\n".join(value)])
    # tt.add_row([key, ",\n".join(value)])

pt.max_width["Artist"] = 20
pt.max_width["Album"] = 30
pt.padding_width = 2
pt.align["Artist"] = "r"
pt.align["Album"] = "l"
print(pt)

# Table from TextTable - produces a table with cells
# url: https://pypi.org/project/texttable/

from texttable import Texttable
t = Texttable()
for key, value in sample_dict.items():
    artist = key
    album = ("\n".join(value))
    t.add_rows([['Name', 'Age'], [artist, album]])
print(t.draw())
