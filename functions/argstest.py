def concatenate_args(*fruits):
    fruits2=" "
    for f in fruits:
        fruits2+=f
    return fruits2     

def concatenate_kwargs(**kwargs):
    into_string=" "
    for key,value in kwargs.items():
        into_string+=str((f"{key}:{value}"))
    return into_string
    

        
      
      



