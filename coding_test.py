from collections import OrderedDict
import fileinput
import sys
from sys import argv

def organize_data(*args):
    
    """a function that takes in a file, or stdin, reads each line,
       splits up the teams, and their wins, losses or draws, and assigns a dictionary with them"""
    
    print("Please enter the game outcome")
    team_scores = {}
    #read each line in the argument given
    for line in fileinput.input(*args):
        #strip the new line character
        if line.rstrip('\n') == "":
            #if the next line is empty break loop signalling input is complete
            break
        line = line.rstrip('\n')
        line = line.split(", ")
        first_half = line[0].split(" ")
        second_half = line[1].split(" ")
        team_1 = first_half[0]
        team_2 = second_half[0]
        
        score_team1 = int(first_half[1])
        score_team2 = int(second_half[1])

        #assigning a dictionary for teams with their individual results
        if score_team1 > score_team2:
            #if the key doesnt exist in the dictionary assign it, else append if it does exit
            if team_1 not in team_scores:
                team_scores[team_1] = ["win"]
            else:
                team_scores[team_1].append("win")
            if team_2 not in team_scores:
                team_scores[team_2] = ["lose"]
            else:
                team_scores[team_2].append("lose")
                
        elif score_team2 > score_team1:
            if team_2 not in team_scores:
                team_scores[team_2] = ["win"]
            else:
                team_scores[team_2].append("win")
            if team_1 not in team_scores:
                team_scores[team_1] = ["lose"]
            else:
                team_scores[team_1].append("lose")
                
        elif score_team1 == score_team2:
            if team_1 not in team_scores:
                team_scores[team_1] = ["draw"]
            else:
                team_scores[team_1].append("draw")
            if team_2 not in team_scores:
                team_scores[team_2] = ["draw"]
            else:
                team_scores[team_2].append("draw")
    #close the file input stream else it will fail on the next iteration 
    fileinput.close()
    #return back team_scores dictionary so we can pass it into our next function
    return team_scores

def get_points(team_scores):
    
    """ a function that takes the dictionary from the previous function, counts up the wins, draws, and losses and converts them to points
        appropriately, assigning and returning a dictionary with teams as keys and points as values"""
    
    team_points = {}

    #loop through the keys
    for key in team_scores:
        #count the wins, losses, or draws
        wins = team_scores[key].count("win")
        draws = team_scores[key].count("draw")
        losses = team_scores[key].count("lose")
        #multiply them based on the game rules
        Wpoint = wins * 3
        Dpoint = draws * 1
        Lpoint = losses * 0
        #assign to a dictionary
        points_total = Wpoint + Dpoint + Lpoint
        team_points[key] = points_total

    #return dictionary so we can pass it into our next function
    return team_points

def output_sorted_points(team_points):
    """ function that takes a dictionary with teams as keys and points as values, sorts it alphabetically, and orders the values from largest to smallest
        displaying them in the desired output """

    #order the keys alphabetically
    ordered_team = OrderedDict(sorted(team_points.items()))
    #order the values from largest to smallest
    sorted_val = sorted(team_points.values(), reverse = True)
    #create our dictionary to store
    sorted_dict = {}

    #for each value in sorted_val and for each key in ordered_team if the value and key match up in team_points assign it to our sorted dictionary
    for i in sorted_val:
        for k in ordered_team:
            if team_points[k] == i:
                #this ensures that if any two teams have the same points, they will be displayed alphabetically
                sorted_dict[k] = team_points[k]
    count = 1


    for key in sorted_dict:
        if sorted_dict[key] <= 0 or sorted_dict[key] > 1:
            print("{}. {}, {} pts".format(count,key, sorted_dict[key]))
        else:
            print("{}. {}, {} pt".format(count,key, sorted_dict[key]))
        count +=1
    return sorted_dict


if __name__ == "__main__":
    
    start = organize_data(*argv[1:])
    middle = get_points(start)
    end = output_sorted_points(middle)


