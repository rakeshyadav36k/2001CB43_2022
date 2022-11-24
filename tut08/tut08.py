import sys
from platform import python_version
import re
import pandas as pd

from datetime import datetime
start_time = datetime.now()

# here we open the scorecard file in write mode
f = open("Scorecard.txt", 'w')
sys.stdout = f


def scorecard(commentary, tenth_over):
    # this is the list for storing the commentary 
    line = []
    i = 0
    while i < len(commentary):
        line.append(commentary[i].split(','))
        i = i+2

    batsman = []
    bowler = []
    for i in range(len(line)):
        players = line[i][0].split('to')

        batsman.append(players[1])
        if i > tenth_over:
            bowler.append(players[0][4:])
        else:
            bowler.append(players[0][3:])

    batsman = list(dict.fromkeys(batsman))
    bowler = list(dict.fromkeys(bowler))
    # here we create a dataframe 
    myBatsman = pd.DataFrame(
        0, batsman, ['status', 'R', 'B', '4s', '6s', 'SR'])


    myBowler = pd.DataFrame(
        0, bowler, ['O', 'M', 'R', 'W', 'NB', 'WD', 'EC', 'B'])

    myBatsman['status'] = 'not out'

    extra = wide = score = wickets = noBall = penalty = b = lb = 0
    fall = []
    for i in range(len(line)):
        
        players = line[i][0].split('to')
        batsmanName = players[1]
        if i > tenth_over:
            bowlerName = players[0][4:]
            ball_no = line[i][0][:4]
        else:
            bowlerName = players[0][3:]
            ball_no = line[i][0][:3]
        line[i][1] = line[i][1].lower()
        # here we find different ways of getting runs  
        if line[i][1] == ' wide':
            extra = extra+1
            wide = wide+1
            score = score+1
            myBowler.loc[bowlerName, 'WD'] = myBowler.loc[bowlerName, 'WD'] + 1
            myBowler.loc[bowlerName, 'R'] = myBowler.loc[bowlerName, 'R'] + 1


        elif line[i][1] == ' 3 wides':
            wide = wide+3
            extra = extra+3
            score = score+3
            myBowler.loc[bowlerName, 'R'] = myBowler.loc[bowlerName, 'R'] + 3
            myBowler.loc[bowlerName, 'WD'] = myBowler.loc[bowlerName, 'WD'] + 3

        elif line[i][1] == ' 2 wides':
            wide = wide+2
            extra = extra+2
            score = score+2
            myBowler.loc[bowlerName, 'R'] = myBowler.loc[bowlerName, 'R'] + 2
            myBowler.loc[bowlerName, 'WD'] = myBowler.loc[bowlerName, 'WD'] + 2

        elif line[i][1] == ' no ball':
            noBall = noBall+1
            extra = extra+1
            score = score+1
            myBowler.loc[bowlerName, 'R'] = myBowler.loc[bowlerName, 'R'] + 1
            myBowler.loc[bowlerName, 'NB'] = myBowler.loc[bowlerName, 'NB'] + 1
			
        elif line[i][1] == ' four' or line[i][1] == ' 4' or line[i][1] == ' 4 runs':
            score = score+4
            myBatsman.loc[batsmanName,
                          'R'] = myBatsman.loc[batsmanName, 'R'] + 4
            myBatsman.loc[batsmanName,
                          '4s'] = myBatsman.loc[batsmanName, '4s'] + 1
            myBatsman.loc[batsmanName,
                          'B'] = myBatsman.loc[batsmanName, 'B'] + 1

            myBowler.loc[bowlerName, 'B'] = myBowler.loc[bowlerName, 'B'] + 1
            myBowler.loc[bowlerName, 'R'] = myBowler.loc[bowlerName, 'R'] + 4

        elif line[i][1] == ' six' or line[i][1] == ' 6' or line[i][1] == ' 6 runs':
            score = score+6
            myBatsman.loc[batsmanName,
                          'R'] = myBatsman.loc[batsmanName, 'R'] + 6
            myBatsman.loc[batsmanName,
                          '6s'] = myBatsman.loc[batsmanName, '6s'] + 1
            myBatsman.loc[batsmanName,
                          'B'] = myBatsman.loc[batsmanName, 'B'] + 1

            myBowler.loc[bowlerName, 'B'] = myBowler.loc[bowlerName, 'B'] + 1
            myBowler.loc[bowlerName, 'R'] = myBowler.loc[bowlerName, 'R'] + 6

        elif line[i][1] == ' 1' or line[i][1] == ' 1 run':
            score = score+1
            myBatsman.loc[batsmanName,
                          'R'] = myBatsman.loc[batsmanName, 'R'] + 1
            myBatsman.loc[batsmanName,
                          'B'] = myBatsman.loc[batsmanName, 'B'] + 1

            myBowler.loc[bowlerName, 'B'] = myBowler.loc[bowlerName, 'B'] + 1
            myBowler.loc[bowlerName, 'R'] = myBowler.loc[bowlerName, 'R'] + 1

        elif line[i][1] == ' 2' or line[i][1] == ' 2 runs' or line[i][1] == ' 2 run':
            score = score+2
            myBatsman.loc[batsmanName,
                          'R'] = myBatsman.loc[batsmanName, 'R'] + 2
            myBatsman.loc[batsmanName,
                          'B'] = myBatsman.loc[batsmanName, 'B'] + 1

            myBowler.loc[bowlerName, 'B'] = myBowler.loc[bowlerName, 'B'] + 1
            myBowler.loc[bowlerName, 'R'] = myBowler.loc[bowlerName, 'R'] + 2

        elif line[i][1] == ' 3' or line[i][1] == ' 3 runs' or line[i][1] == ' 3 run':
            score = score+3
            myBatsman.loc[batsmanName,
                          'R'] = myBatsman.loc[batsmanName, 'R'] + 3
            myBatsman.loc[batsmanName,
                          'B'] = myBatsman.loc[batsmanName, 'B'] + 1

            myBowler.loc[bowlerName, 'B'] = myBowler.loc[bowlerName, 'B'] + 1
            myBowler.loc[bowlerName, 'R'] = myBowler.loc[bowlerName, 'R'] + 3

        elif line[i][1] == ' 5' or line[i][1] == ' 5 runs' or line[i][1] == ' 5 run':
            score = score+5
            myBatsman.loc[batsmanName,
                          'R'] = myBatsman.loc[batsmanName, 'R'] + 5
            myBatsman.loc[batsmanName,
                          'B'] = myBatsman.loc[batsmanName, 'B'] + 1

            myBowler.loc[bowlerName, 'B'] = myBowler.loc[bowlerName, 'B'] + 1
            myBowler.loc[bowlerName, 'R'] = myBowler.loc[bowlerName, 'R'] + 5

        elif line[i][1] == ' no run' or line[i][1] == ' no':
            myBatsman.loc[batsmanName,
                          'B'] = myBatsman.loc[batsmanName, 'B'] + 1

            myBowler.loc[bowlerName, 'B'] = myBowler.loc[bowlerName, 'B'] + 1

   			 #  here  when there is leg byes we  update the scores and player's stats
        elif line[i][1] == ' leg byes' or line[i][1] == ' leg bye' or line[i][1] == ' lb':
            myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName, 'B'] + 1
            myBowler.loc[bowlerName, 'B'] = myBowler.loc[bowlerName, 'B'] + 1

            if line[i][2] == ' four' or line[i][2] == ' 4' or line[i][2] == ' 4 runs' or line[i][2] == ' FOUR':
                lb = lb+4
                extra = extra+4
                score = score+4

            if line[i][2] == ' six' or line[i][2] == ' 6' or line[i][2] == ' 6 runs':
                lb = lb+6
                extra = extra+6
                score = score+6

            if line[i][2] == ' 1' or line[i][2] == ' 1 run':
                lb = lb+1
                extra = extra+1
                score = score+1

            if line[i][2] == ' 2' or line[i][2] == ' 2 run' or line[i][2] == ' 2 runs':
                lb = lb+2
                extra = extra+2
                score = score+2

            if line[i][2] == ' 3' or line[i][2] == ' 3 run' or line[i][2] == ' 3 runs':
                lb = lb+3
                extra = extra+3
                score = score+3

            if line[i][2] == ' 5' or line[i][2] == ' 5 run' or line[i][2] == ' 5 runs':
                lb = lb+5
                extra = extra+5
                score = score+5

       		 #    when there is byes we update the scores and player's stats
        elif line[i][1] == ' byes' or line[i][1] == ' bye':
            myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName, 'B'] + 1
            myBowler.loc[bowlerName, 'B'] = myBowler.loc[bowlerName, 'B'] + 1

            if line[i][2] == ' four' or line[i][2] == ' 4' or line[i][2] == ' 4 runs':
                b = b+4
                extra = extra+4
                score = score+4

            if line[i][2] == ' six' or line[i][2] == ' 6' or line[i][2] == ' 6 runs':
                b = b+6
                score = score+6
                extra = extra+6

            if line[i][2] == ' 1' or line[i][2] == ' 1 run':
                b = b+1
                score = score+1
                extra = extra+1

            if line[i][2] == ' 2' or line[i][2] == ' 2 run' or line[i][2] == ' 2 runs':
                b = b+2
                extra = extra+2
                score = score+2

            if line[i][2] == ' 3' or line[i][2] == ' 3 run' or line[i][2] == ' 3 runs':
                b = b+3
                extra = extra+3
                score = score+3

            if line[i][2] == ' 5' or line[i][2] == ' 5 run' or line[i][2] == ' 5 runs':
                b = b+5
                extra = extra+5
                score = score+5

       		 # we find different ways the batsman gets out and update the scorecard
        else:
            myBatsman.loc[batsmanName,'B'] = myBatsman.loc[batsmanName, 'B'] + 1
            myBowler.loc[bowlerName, 'B'] = myBowler.loc[bowlerName, 'B'] + 1

            content = line[i][1].split('!')

            if content[0] == ' out bowled':
                myBatsman.loc[batsmanName, 'status'] = 'b' + bowlerName
                myBowler.loc[bowlerName, 'W'] = myBowler.loc[bowlerName, 'W'] + 1
                wickets = wickets+1

            elif content[0] == ' run out':
                myBatsman.loc[batsmanName, 'status'] = 'run out'
                wickets = wickets+1

            elif content[0] == ' out lbw':
                myBatsman.loc[batsmanName, 'status'] = 'lbw ' + 'b' + bowlerName
                myBowler.loc[bowlerName,'W'] = myBowler.loc[bowlerName, 'W'] + 1
                wickets = wickets+1

            else:
                myBatsman.loc[batsmanName, 'status'] = 'c' + content[0][14:] + ' b' + bowlerName
                myBowler.loc[bowlerName,'W'] = myBowler.loc[bowlerName, 'W'] + 1
                wickets = wickets+1

            # here we add the  wickets down
            add = str(score) + '-' + str(wickets) + '(' + batsmanName + ',' + ball_no + ')'
            fall.append(add)

       		 # here we calculate strike rate and bowler economy
        myBatsman.loc[batsmanName, 'SR'] = round((myBatsman.loc[batsmanName, 'R'] / myBatsman.loc[batsmanName, 'B']) * 100, 2)

        myBowler.loc[bowlerName,'B'] = myBowler.loc[bowlerName, 'B'].astype('float')
        myBowler.loc[bowlerName,'O'] = myBowler.loc[bowlerName, 'O'].astype('float')
        myBowler.loc[bowlerName, 'O'] = float(str(myBowler.loc[bowlerName, 'B'] // 6) + '.' + str(myBowler.loc[bowlerName, 'B'] % 6))
        myBowler.loc[bowlerName, 'EC'] = round(myBowler.loc[bowlerName,'R'] / myBowler.loc[bowlerName, 'O'], 2)

    print(myBatsman)
    		# here we print the  extras run and total run rows

    print('\nExtras\t\t' + str(extra) + '(b ' + str(b) + ', lb ' + str(lb) + ', w ' + str(wide) + ', nb ' + str(noBall) + ', p ' + str(penalty) + ')')
    print('\nTotal\t\t' + str(score) + ' (' + str(wickets) + ' wkts, ' + str(myBowler['O'].sum()) + ' Ov)\n')
    print('Fall of Wickets')
    print(*fall, sep=' ')
    print('\n')
    print(myBowler.iloc[:, :-1])
    print('\nPowerplays\t\t' + 'Overs\t\t' + 'Runs')


text = open("pak_inns1.txt", "r").read()
commentary = []

for i in text.split('\n'):
    commentary.append(i)

tenth_over = 61

print('India won by 5 wkts')
print('Pakistan Innings\t\t\t\t\t' + '147-10 (19.5 Ov)')

		#  printing the scorecard of Pakistan Innings by calling the funtion
scorecard(commentary, tenth_over)

print('Mandatory\t\t' + '0.1-6\t\t' + '43')

text = open("india_inns2.txt", "r").read()
commentary2 = []
for i in text.split('\n'):
    commentary2.append(i)

tenth_over2 = 60

print('\n')
print('India Innings\t\t\t\t\t\t\t' + '148-5 (19.4 Ov)')

		# printing the scorecard of India Innings by calling the funtion
scorecard(commentary2, tenth_over2)

print('Mandatory\t\t' + '0.1-6\t\t' + '38')


# This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))

f.close()