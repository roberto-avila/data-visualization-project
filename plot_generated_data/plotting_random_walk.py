import matplotlib.pyplot as plt
from random_walk import RandomWalk

def repeat_prompt():
    """Asks the user if they would like to continue."""
    
    while True:
        prompt = input("\nWould you like to make another plot? (y/n): ")
        if prompt == 'y':
            return True
        elif prompt == 'n':
            return False
        else:
            print("Please enter 'y' or 'n' to continue.")
            continue


print("\nLet's create a plot of random scatter points!")
try:
    while True:
        #Make random walk.
        try:
            pt_number = int(input("\nHow many points would"
            " you like to plot? "))
            rw = RandomWalk(pt_number)
            rw.fill_walk()
        except ValueError:
            print("Please enter a whole integer.")
            continue
        
        #Plot and style points in the walk.
        fig, ax = plt.subplots(figsize=(14,7))
        pt_count = range(pt_number)
        ax.scatter(rw.x_values, rw.y_values, s=5, c=pt_count,
        cmap=plt.cm.Blues, edgecolors='none')
        ax.scatter(0, 0, c='green', edgecolors='none', s=25)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
        edgecolors='none', s=25)
        plt.style.use('classic')
        ax.set_title(f"Random Walk of {pt_number} Points.")
        plt.show()

        if not repeat_prompt():
            print("\nHave a nice day!")
            break

except KeyboardInterrupt:
    print("Quitting program...")
