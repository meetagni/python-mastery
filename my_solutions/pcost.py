def portfolio_cost(filename):
    sum= 0
    with open(filename, 'r') as f:
        try:
            for line in f:
                data= line.split()
                sum= sum+ int(data[1])*float(data[2])
        except ValueError:
            print("Couldn't parse:",line)
    
    return sum

#print(portfolio_cost('../Data/portfolio3.dat'))