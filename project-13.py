# Create a multiplication table application where 
# user will enter a sentinel value n 
# and the application will display the mathematical 
# multiplication tables till given sentinel value n.
# CODE :-
print("""L O V E L Y   P R O F E S S I O N A L   U  N I V E R S I T Y\n____________________________________________________________\n\nS E C T I O N :- K O C 3 2\nName of Student      Registration Number      Roll Number\nDiksha Lanjewar            12220548            RKOC32B38\nVedant Lahane              12217478            RKOC32B39\nRishabh Singh              12217744            RKOC32B40""")
print("************************************************************\nPROJECT:-\n------------------------------------------------------------")
print("\n# M U L T I P L I C A T I O N  T A B L E :-")
print("\n------------------------------------------------------------")
n=int(input("Enter the Number: "))
for c in range(1,n+1):
    for i in range(1,11):
        print(c,"X",i,"=",c*i)
print("***********************  E  N  D  **************************")