from matplotlib.patches import Arc
import matplotlib.pyplot as plt
import pandas as pd


def fit_coords(df, xpos, ypos, newxpos='xc', newypos='yc', width=68, length=105):
    df = df.copy()  # Avoid modifying original DataFrame
    
    df[newxpos] = df[xpos].apply(lambda coord: coord * length if coord != 0 else None)
    df[newypos] = df[ypos].apply(lambda coord: coord * width if coord != 0 else None)

    return df


def createPitch():
    
    #Create figure
    fig=plt.figure(figsize=(10,8))
    ax=fig.add_subplot(1,1,1)

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,90], color="black")
    plt.plot([0,130],[90,90], color="black")
    plt.plot([130,130],[90,0], color="black")
    plt.plot([130,0],[0,0], color="black")
    plt.plot([65,65],[0,90], color="black")
    
    #Left Penalty Area
    plt.plot([16.5,16.5],[65,25],color="black")
    plt.plot([0,16.5],[65,65],color="black")
    plt.plot([16.5,0],[25,25],color="black")
    
    #Right Penalty Area
    plt.plot([130,113.5],[65,65],color="black")
    plt.plot([113.5,113.5],[65,25],color="black")
    plt.plot([113.5,130],[25,25],color="black")
    
    #Left 6-yard Box
    plt.plot([0,5.5],[54,54],color="black")
    plt.plot([5.5,5.5],[54,36],color="black")
    plt.plot([5.5,0.5],[36,36],color="black")
    
    #Right 6-yard Box
    plt.plot([130,124.5],[54,54],color="black")
    plt.plot([124.5,124.5],[54,36],color="black")
    plt.plot([124.5,130],[36,36],color="black")
    
    #Prepare Circles
    centreCircle = plt.Circle((65,45),9.15,color="black",fill=False)
    centreSpot = plt.Circle((65,45),0.8,color="black")
    leftPenSpot = plt.Circle((11,45),0.8,color="black")
    rightPenSpot = plt.Circle((119,45),0.8,color="black")
    
    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)
    
    #Prepare Arcs
    leftArc = Arc((11,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="black")
    rightArc = Arc((119,45),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="black")

    #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)
    
    #Tidy Axes
    plt.axis('off')
    
    #Display Pitch
    plt.show()
    
    return fig,ax


# values for clock need to be changed to integers so we can account for additional time intervals
def clock_obj_int(clock):
    if '+' in clock:  
        base, extra = clock.replace("'", "").split('+')
        return int(base) + int(extra) /10
    else:
        return int(clock.replace("'", ""))  
    

# def sorting_plays(event):
#     words = event.lower().split(' ')
#     if any(word in words for word in ['shot', 'goal']):
#         return 1
#     else:
#         return 0


def sorting_plays(event, word1='shot', word2='goal', word3='scored'):
    words = event.lower().split(' ')
    if word1 in words or word2 in words or word3 in words:
        return 1
    else:
        return 0