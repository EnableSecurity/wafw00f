#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

from dataclasses import dataclass
from random import randint

from wafw00f import __version__


@dataclass
class Color:
    """ANSI colors."""
    W: str = '\033[1;97m'
    Y: str = '\033[1;93m'
    G: str = '\033[1;92m'
    R: str = '\033[1;91m'
    B: str = '\033[1;94m'
    C: str = '\033[1;96m'
    E: str = '\033[0m'

    @classmethod
    def disable(cls):
        """Disables all colors."""
        cls.W = ''
        cls.Y = ''
        cls.G = ''
        cls.R = ''
        cls.B = ''
        cls.C = ''
        cls.E = ''

    @classmethod
    def unpack(cls):
        """Unpacks and returns the color values.
        Useful for brevity, e.g.:
        (W,Y,G,R,B,C,E) = Color.unpack()
        """
        return (
            cls.W,
            cls.Y,
            cls.G,
            cls.R,
            cls.B,
            cls.C,
            cls.E
        )


def randomArt():
    # Colors for terminal

    (W,Y,G,R,B,C,E) = Color.unpack()

    woof = '''
                   '''+W+'''______
                  '''+W+'''/      \\
                 '''+W+'''(  Woof! )
                  '''+W+r'''\  ____/                      '''+R+''')
                  '''+W+''',,                           '''+R+''') ('''+Y+'''_
             '''+Y+'''.-. '''+W+'''-    '''+G+'''_______                 '''+R+'''( '''+Y+'''|__|
            '''+Y+'''()``; '''+G+'''|==|_______)                '''+R+'''.)'''+Y+'''|__|
            '''+Y+'''/ ('        '''+G+r'''/|\                  '''+R+'''(  '''+Y+'''|__|
        '''+Y+'''(  /  )       '''+G+r''' / | \                  '''+R+'''. '''+Y+'''|__|
         '''+Y+r'''\(_)_))      '''+G+r'''/  |  \                   '''+Y+'''|__|'''+E+'''

                    '''+C+'~ WAFW00F : '+B+'v'+__version__+''' ~'''+W+'''
    The Web Application Firewall Fingerprinting Toolkit
    '''+E

    w00f = '''
                '''+W+'''______
               '''+W+'''/      \\
              '''+W+'''(  W00f! )
               '''+W+r'''\  ____/
               '''+W+''',,    '''+G+'''__            '''+Y+'''404 Hack Not Found
           '''+C+'''|`-.__   '''+G+'''/ /                     '''+R+''' __     __
           '''+C+'''/"  _/  '''+G+'''/_/                       '''+R+r'''\ \   / /
          '''+B+'''*===*    '''+G+'''/                          '''+R+r'''\ \_/ /  '''+Y+'''405 Not Allowed
         '''+C+'''/     )__//                           '''+R+r'''\   /
    '''+C+'''/|  /     /---`                        '''+Y+'''403 Forbidden
    '''+C+r'''\\/`   \ |                                 '''+R+'''/ _ \\
    '''+C+r'''`\    /_\\_              '''+Y+'''502 Bad Gateway  '''+R+r'''/ / \ \  '''+Y+'''500 Internal Error
      '''+C+'''`_____``-`                             '''+R+r'''/_/   \_\\

                        '''+C+'~ WAFW00F : '+B+'v'+__version__+''' ~'''+W+'''
        The Web Application Firewall Fingerprinting Toolkit
    '''+E

    wo0f = r'''
                 ?              ,.   (   .      )        .      "
         __        ??          ("     )  )'     ,'        )  . (`     '`
    (___()'`;   ???          .; )  ' (( (" )    ;(,     ((  (  ;)  "  )")
    /,___ /`                 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( ' )
    \\   \\                 |____|____|____|____|____|____|____|____|____|

                                ~ WAFW00F : v'''+__version__+''' ~
                    ~ Sniffing Web Application Firewalls since 2014 ~
'''

    arts = [woof, w00f, wo0f]
    return arts[randint(0, len(arts)-1)]
