good = r"""  
                  ,$'`$.     ,$'`$.     
                  $'  `$     $'  `$     
                 :$    $;   :$    $;    
                 $$    $$   $$    $$    
                 $$  _.$bqgpd$._  $$    
                 ;$gd$$^$$$$$^$$bg$:    
               .d$P^*'   "*"   `*^T$b.  
              d$$$    ,*"   "*.    $$$b 
             d$$$b._    o   o    _.d$$$b
            *T$$$$$P             T$$$$$P*
              `^T$$    :"---";    $$P^' 
                 `$._   `---'   _.$'    
                .d$$P"**-----**"T$$b.   
               d$$P'             `T$$b  
              d$$P                 T$$b 
             d$P'.'               `.`T$b
             `--:                   ;--'
                |                   |   
                :                   ;   
                 \                 /    
                 .`-.           .-'.    
                /   ."*--+g+--*".   \   
               :   /     $$$     \   ;  
               `--'      $$$      `--'  
                         $$$ [bug]      
                         $$$            
                         :$$;           
                         :$$;           
                          :$$           
                          'T$bg+.____   
                            'T$$$$$  :  
                                "**--'  
"""

bad = r"""

   /
  /
 /____________________
 |________  __________
 /_____  /||   |
|".___."| ||   |
|_______|/ |   |
 || .___."||  /
 ||_______|| /
 |_________|/
"""

escaped = True
if not escaped:
    outcome = "Doom: You have not escaped. FAILURE!"
    print(bad)

else:
    outcome = "Legend: You escaped! You win!"
    print(good)

print(outcome)