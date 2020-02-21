#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

from sys import platform
from random import randint
from wafw00f import __version__

# Colors for terminal
W = '\033[1;97m'
Y = '\033[1;93m'
G = '\033[1;92m'
R = '\033[1;91m'
B = '\033[1;94m'
C = '\033[1;96m'
E = '\033[0m'

# Windows based systems do not support ANSI sequences,
# hence not displaying them.
if 'win' in platform:
    W = Y = G = R = B = C = E = ''

def randomArt():

    woof = '''
                   '''+W+'''______
                  '''+W+'''/      \\
                 '''+W+'''(  Woof! )
                  '''+W+r'''\  ____/                      '''+R+''')
                  '''+W+''',,                           '''+R+''') ('''+Y+'''_
             '''+Y+'''.-. '''+W+'''-    '''+G+'''_______                 '''+R+'''( '''+Y+'''|__|
            '''+Y+'''()``; '''+G+'''|==|_______)                '''+R+'''.)'''+Y+'''|__|
            '''+Y+'''/ ('        '''+G+'''/|\                  '''+R+'''(  '''+Y+'''|__|
        '''+Y+'''(  /  )       '''+G+''' / | \                  '''+R+'''. '''+Y+'''|__|
         '''+Y+r'''\(_)_))      '''+G+'''/  |  \                   '''+Y+'''|__|'''+E+'''

                    '''+C+'~ WAFW00F : '+B+'v'+__version__+''' ~'''+W+'''
    The Web Application Firewall Fingerprinting Toolkit
    '''+E

    w00f = '''
                '''+W+'''______
               '''+W+'''/      \\
              '''+W+'''(  W00f! )
               '''+W+'''\  ____/
               '''+W+''',,    '''+G+'''__            '''+Y+'''404 Hack Not Found
           '''+C+'''|`-.__   '''+G+'''/ /                     '''+R+''' __     __
           '''+C+'''/"  _/  '''+G+'''/_/                       '''+R+'''\ \   / /
          '''+B+'''*===*    '''+G+'''/                          '''+R+'''\ \_/ /  '''+Y+'''405 Not Allowed
         '''+C+'''/     )__//                           '''+R+'''\   /
    '''+C+'''/|  /     /---`                        '''+Y+'''403 Forbidden
    '''+C+r'''\\/`   \ |                                 '''+R+'''/ _ \\
    '''+C+r'''`\    /_\\_              '''+Y+'''502 Bad Gateway  '''+R+'''/ / \ \  '''+Y+'''500 Internal Error
      '''+C+'''`_____``-`                             '''+R+'''/_/   \_\\

                        '''+C+'~ WAFW00F : '+B+'v'+__version__+''' ~'''+W+'''
        The Web Application Firewall Fingerprinting Toolkit
    '''+E

    arts = [woof, w00f]
    return arts[randint(0,1)]