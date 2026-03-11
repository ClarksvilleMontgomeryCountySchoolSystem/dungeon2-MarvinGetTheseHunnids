good = r"""
  .--//-//-//------------/"\
   /  === === ===         j   l
   \  === === ===         l   j
    `--\\-\\-\\------------\_/
"""

bad = r"""
                  /|                        |\
                  ; :                        : :
                  | Y,                      ,P |
                  |  Yb.        __        ,dP  |
                  l\  YMMb,_ _,/  \,_ _,dMMP  /f
                   j;  `YMMP'  `--'  `YMMP'  ;j
                   : \   YP`-._    _.-'YP   / ;
                    \ `\,  _,\_    _/,_  ,/' /
                     `,_,   \`o>   _/      |  Y
                        _\_       ,,T    (   / _ " / /          /  l
                       / l "----""   \    '_/___/^^~~'/"__,,,_,/ ./_
                      l  \            \            7   /          @ )
                       \  \_       _,,-\          \,---~\  __      /
                        ]  \""---"'     '\ /             \"__."  _/
                   ____/  (_`~._       _.-`,            ,___/  (_
               _,-'/,-/,_._ \ `."----""     `,      ___/_/ 7`,-._\__
               \[ {( {(    `_}  `-..          \,   _\[_\({(/     `~_}
"""

drawbridge_raised = True
if drawbridge_raised:
    outcome = "Doom: Find a way to cross bridge."
    print(bad)
else:
    outcome = "thunder: you may cross bridge."
    print(good)

print(outcome)

