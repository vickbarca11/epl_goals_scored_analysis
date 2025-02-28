import matplotlib.pyplot as plt
import pandas as pd

# adjusting the x and y positions to fit new pitch based on EPL standard 105m by 68m
def fit_coords(df, xpos, ypos, newxpos='xc', newypos='yc', width=68, length=105):
    df = df.copy()  # Avoid modifying original DataFrame
    
    df[newxpos] = df[xpos].apply(lambda coord: coord * length if coord != 0 else None)
    df[newypos] = df[ypos].apply(lambda coord: coord * width if coord != 0 else None)

    return df


# values for clock need to be changed to integers so we can account for additional time intervals
def clock_obj_int(clock):
    if '+' in clock:  
        base, extra = clock.replace("'", "").split('+')
        return int(base) + int(extra) /10
    else:
        return int(clock.replace("'", ""))  
    

# sorting plays based on common words in the event column. 
# set to sorting for all shots
def sorting_plays(event, word1='shot', word2='goal', word3='scored', word4='header', word5='volley', word6='penalty', word7='free kick'):
    words = event.lower().split(' ')
    if word1 in words or word2 in words or word3 in words or word4 in words or word5 in words or word6 in words or word7 in words:
        return 1
    else:
        return 0
    
    
# sorting playtypes and creating new columns 
def sorting_playtype(event, playtype):
    if event == playtype:
        return 1
    else:
        return 0
    



