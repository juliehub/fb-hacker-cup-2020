class Airline():
    """
    Definition for class Airline
    
    id: a integer indicates the name of airline
    N: an integer indicates the number of countries the airline services
    I: a list of inbound restrictions (length N)
    O: a list of outbound restrictions (length N)
    P: a matrix of size N*N indicates all possible trips between 2 countries
    """
    def __init__(self, id=0, N=2, I=[], O=[]):
        self.id=id
        self.N=N
        self.I=I
        self.O=O
        self.P = ['N'] * self.N
        for x in range (self.N):
            self.P[x] = ['N'] * self.N

        # P[i][i] is always "Y"
        for i in range(self.N):
            self.P[i][i]='Y'

    def __str__(self):
        return "Airline:"%(self.id)
    
    def display(self):   
        print("Airline:",self.id)
        print("The number of countries the airline services is:",self.N,"\n")
        print("Inbound restriction:",self.I,"\n")
        print("Outbound restriction:",self.O,"\n")
        print(self.P)
        print("======================================")
        
    def print_trips_available(self):
        print("Case #{}: ".format(self.id+1))
        #convert list to string and print out
        for i in range(self.N):
            print("".join(self.P[i]))
            
    def find_trips_available_same_airlines(self):
        # same airline, check direction from country i to j
        # flights are available from country i to country j if and only if |i - j|=1.
        for i in range(self.N):
            j=i+1
            if (j<=self.N-1) and self.O[i]=='Y'and self.I[j]=='Y':
                self.P[i][j]='Y'
            
            j=i-1
            if (j>=0) and self.O[i]=='Y'and self.I[j]=='Y':
                self.P[i][j]='Y'
        
        # P[i][j]="Y" if it's possible to travel from country i to country j
        # via a sequence of 0 or more flights (which may pass through other countries along the way)
        # forward from i --> j (i<j)
        for gap in range(2, self.N):
            for i in range(self.N-1):
                j = i+gap # going forward from i to j, separated by 'gap'
                if j <= self.N-1 and self.P[i][j-1] == 'Y' and self.P[j-1][j] == 'Y':
                    self.P[i][j] = 'Y'
                    
        # backward from j <-- i ( i>j)
        for gap in range(2, self.N):
            for i in range(self.N-1,1,-1):
                j = i-gap # going backward from i to j, separated by 'gap'
                if j>=0 and self.P[i][i-1] == 'Y' and self.P[i-1][j] == 'Y':
                    self.P[i][j] = 'Y'
        
def findTrips(filename):
    """
    This function print out the input from a text file and return an output file 
    
    Args: a file
    Input begins with an integer T, the number of airlines. 
    For each airline, there are three lines. 
    The first line contains the integer N. 
    The second line contains the length-N string I_{1..N}.
    The third line contains the length-N string O_{1..N}.
    
    Constraints:
    1≤T≤100
    2≤N≤50
    
    Returns: a file containing information of trips available between the various countries.
    For the ith airline, output a line containing "Case #i:" followed by N more lines,
    the ith of which contains the length-NN string P_{i,1..N} (N∗N matrix of characters).
    """
    my_file = open(filename, "r")
    #read number of airlines
    T=int(my_file.readline())
    if T<1 or T>100:
        return "T is out of range!"
    #print("The number of airlines:",T)
    #print("======================================")
    
    # iterate through each airline
    for a in range(T):
        #number of countries the airline services
        N=int(my_file.readline())
        if N<2 or N>50:
            return "N is out of range!"
        
        #Inbound and Outbound restrictions
        Inbound=list(my_file.readline().strip("\n"))
        Outbound=list(my_file.readline().strip("\n"))
        
        air=Airline(a,N,Inbound,Outbound)
        #Print information for airline
        #air.display()
        
        air.find_trips_available_same_airlines()
        
        #print output N*N matrix for that airline
        air.print_trips_available()
    
findTrips("travel_restrictions_sample_input.txt")
#findTrips("travel_restrictions_validation_input.txt")