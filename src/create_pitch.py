from matplotlib.patches import Arc
import matplotlib.pyplot as plt

def createpitch():
    
    #Create figure
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,1], color="black")
    plt.plot([0,2],[1,1], color="black")
    plt.plot([2,2],[1,0], color="black")
    plt.plot([2,0],[0,0], color="black")
    plt.plot([1,1],[0,1], color="black")
    
    # #Left Penalty Area
    plt.plot([0.2538,0.2538],[0.7222,0.2777],color="black")
    plt.plot([0,0.2538],[0.7222,0.7222],color="black")
    plt.plot([0.2538,0],[0.2777,0.2777],color="black")
    

    
    #Left 6-yard Box
    plt.plot([0,0.0846],[0.6,0.6],color="black")
    plt.plot([0.0846,0.0846],[0.6,0.4],color="black")
    plt.plot([0.0846,0.0077],[0.4,0.4],color="black")
    

    
    #Prepare Circles
    centreCircle = plt.Circle((1,0.5),0.1017,color="black",fill=False)
    centreSpot = plt.Circle((1,0.5),0.0099,color="black")
    leftPenSpot = plt.Circle((0.1692,0.5),0.0099,color="black")
    
    # #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    
    # #Prepare Arcs
    leftArc = Arc((0.1811,0.5),height=0.2033,width=0.2815,angle=0,theta1=310,theta2=50,color="black")



    # #Draw Arcs
    ax.add_patch(leftArc)

    ax.set_aspect('equal')

    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)

    #Tidy Axes
    # plt.axis('off')
    
    #Display Pitch
    return fig,ax

createpitch()