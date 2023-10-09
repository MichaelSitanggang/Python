import heapq
from datetime import datetime, timedelta
import random
import string
import os

costperhours = 15
import sys
duration=0
# start membuat djikra
class Graph(object):
    def __init__(self,nodes,init_graph):
        self.nodes=nodes
        self.graph=self.construct_graph(nodes,init_graph)
    
    def construct_graph(self,nodes,init_graph):
        graph={}
        for node in nodes:
            graph[node]={}
        graph.update(init_graph)
        for node,edges in graph.items():
            for adjacent_node,value in edges.items():
                if graph[adjacent_node].get(node,False)==False:
                    graph[adjacent_node][node]=value
        return graph
    
    def get_nodes(self):
        return self.nodes
    def get_outgoing_edges(self,node):
        connections=[]

        for out_node in self.nodes:
            if self.graph[node].get(out_node,False)!=False:
                connections.append(out_node)
        return connections
    
    def value(self,node1,node2):
        return self.graph[node1][node2]
    
def print_result(previous_nodes,shortest_path,start_node,target_node):
    global duration
    path=[]
    node=target_node

    while node !=start_node:
        path.append(node)
        node=previous_nodes[node]
    path.append(start_node)
    print("->".join(reversed(path)))
    print("Duration {} hours. ".format(shortest_path[target_node]))
    duration=shortest_path[target_node]

def dijkstra_algorithm(graph,start_node):
    unvisited_nodes=list(graph.get_nodes())
    shortest_path={}
    previous_nodes={}
    max_value=sys.maxsize

    for node in unvisited_nodes:
        shortest_path[node]=max_value
    
    shortest_path[start_node]=0
    while unvisited_nodes:
        current_min_node=None
        for node in unvisited_nodes:
            if current_min_node==None:
                current_min_node=node
            elif shortest_path[node]<shortest_path[current_min_node]:
                current_min_node=node
        neighbors=graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value=shortest_path[current_min_node] +graph.value(current_min_node,neighbor)
            if tentative_value<shortest_path[neighbor]:
                shortest_path[neighbor]=tentative_value
                previous_nodes[neighbor]=current_min_node
        unvisited_nodes.remove(current_min_node)
    return previous_nodes,shortest_path

nodes=["Minstowe","Cowstone","Oldcastle","Freeham","New North","Bingborough","Donningpool","Highbrook","Wington","Freeham","Old Mere"]

init_graph={}
for node in nodes:
    init_graph[node]={}

init_graph["Minstowe"]["Cowstone"]=3
init_graph["Oldcastle"]["New North"]=5
init_graph["Oldcastle"]["Freeham"]=2
init_graph["Cowstone"]["New North"]=4
init_graph["Cowstone"]["Bingborough"]=6
init_graph["Cowstone"]["Donningpool"]=7
init_graph["Cowstone"]["Highbrook"]=5
init_graph["New North"]["Bingborough"]=3
init_graph["New North"]["Donningpool"]=6
init_graph["New North"]["Wington"]=4
init_graph["New North"]["Highbrook"]=2
init_graph["Freeham"]["Cowstone"]=2
init_graph["Freeham"]["Donningpool"]=3
init_graph["Freeham"]["Wington"]=5
init_graph["Bingborough"]["Donningpool"]=2
init_graph["Bingborough"]["Highbrook"]=1
init_graph["Donningpool"]["Wington"]=4
init_graph["Donningpool"]["Highbrook"]=5
init_graph["Donningpool"]["Old Mere"]=2

graph=Graph(nodes,init_graph)
# end membuat djiktra

class_capacity = {
    'Economy': 25,
    'Business': 30,
    'Exclusive': 35
}

class_cost = {
    'Economy': 20,
    'Business': 30,
    'Exclusive': 40
}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan konsol2


def view_routes():
    print(f"+{'-'*30}+{'-'*10}+")
    print(f"|\tRoutes (2-ways)\t       | Duration |")
    print(f"|\t\t\t       | (hours)  |")
    print(f"+{'-'*30}+{'-'*10}+")
    print(f"| Minstowe -- Cowstone \t       |    3     |")
    print(f"| Oldcastle -- New North       |    5     |")
    print(f"| Oldcastle -- Freeham\t       |    2     |")
    print(f"| Cowstone -- New North\t       |    4     |")
    print(f"| Cowstone--Bingborough\t       |    6     | ")
    print(f"| Cowstone--Donningpool\t       |    7     | ")
    print(f"| Cowstone--Highbrook\t       |    5     | ")
    print(f"| New North--Bingborough       |    3     | ")
    print(f"| New North--Doningngpool      |    6     | ")
    print(f"| New North--Wington           |    4     | ")
    print(f"| New North--Highbrook         |    2     | ")
    print(f"| Freeham--Cowstone            |    2     | ")
    print(f"| Freeham--Doningngpool        |    3     | ")
    print(f"| Freeham--Wington             |    5     | ")
    print(f"| Bingborough--Doningpool      |    2     | ")
    print(f"| Bingborough--Highbrook       |    1     | ")
    print(f"| Doningpool--Wington          |    4     | ")
    print(f"| Doningpool--Higbrook         |    5     | ")
    print(f"| Doningpool--Old Mere         |    2     | ")
    print(f"+{'-'*30}+{'-'*10}+")
def generate_train_number():
    train_number = str(random.randint(100, 999)) + "-" + random.choice(string.ascii_uppercase)
    return train_number

def generate_platform_number():
    platform_number = str(random.randint(1, 10)).zfill(2)
    return platform_number

def generate_seat_number():
    seat_number = str(random.randint(1, 50)).zfill(2)
    return seat_number

def order_ticket():
    global duration
    print("Make sure you already check your route before you order ticket")
    print("Where do you want to go?")
    start = input("From:")
    end = input("To  :")
    previous_nodes,shortest_path=dijkstra_algorithm(graph=graph,start_node=start)
    if start in nodes or end in nodes:
        print(f"Here is the shortest route from {start} to {end}: ")
        print_result(previous_nodes,shortest_path,start_node=start,target_node=end)
    else:
        print("No route found.")
        order_ticket()
    print(duration)
    print("Make sure you already check your belongings before the class")
    while True:
        class_choice = input("Choose class (Economy/Business/Exclusive): ")
        if class_choice in class_capacity:
            break
        else:
            print(f"There are no {class_choice} class")
            print()
    
    print("\nPlease insert your data:")
    name = input("Name: ")
    departure_date = input("Departure date (DD/MM/YYYY): ")
    departure_time = input("Departure time (HH:MM): ")
    confirm_data = input("Are you sure about all the data above? (Yes/No): ")
    if confirm_data.lower() != "yes":
        print("Order canceled.")
        return
    
    # Generate ticket information
    train_number = generate_train_number()
    platform_number = generate_platform_number()
    seat_number = generate_seat_number()
    departure_time_obj = datetime.strptime(departure_time, "%H:%M")
    arrival_time_obj = departure_time_obj + timedelta(hours=duration)
    arrival_date = (datetime.strptime(departure_date, "%d/%m/%Y") + timedelta(hours=duration // 24)).strftime("%d/%m/%Y")
    
    print("\n----------------------------------------------------")
    print("| TRAIN TICKET                                      |")
    print("----------------------------------------------------")
    print(f"| ORIGIN      | {start.upper():<36}|")
    print("----------------------------------------------------")
    print(f"| DATE        : {departure_date:<16}TIME: {departure_time:<14}|")
    print(f"| TRAIN#      : {train_number:<15} CLASS: {class_choice:<13}|")
    print(f"| PLATFORM    : {platform_number:<15} SEAT: {seat_number:<14}|")
    print("----------------------------------------------------")
    print(f"| DESTINATION | {end.upper():<36}|")
    print("----------------------------------------------------")
    print(f"| DATE        : {arrival_date:<15}TIME: {arrival_time_obj.strftime('%H:%M'):<15}|")
    print("----------------------------------------------------")
    print(f"| PASSENGER NAME   : {name.upper():<31}|")
    print("----------------------------------------------------")

    total_cost = duration * costperhours + class_cost[class_choice]
    print(f"\nTotal cost: ${total_cost}")
    
    print("\nOrder another ticket?")
    choice = input("Yes/No: ")
    if choice.lower() == "yes":
        station_program()
#- ---- ------ --  ---- 

def recommend_items():
    print("We can help you choose what to bring. Would you like to try?")
    choice = input("Yes/No: ")
    if choice.lower() == "yes":
        class_choice = input("Choose class: ")
        if class_choice in class_capacity:
            max_capacity = class_capacity[class_choice]
            print("Give your item priority scale from 1 (very important) to 5 (not important).")
            num_items = int(input("How many items do you want to bring? "))
            items = []
            for i in range(1, num_items+1):
                item = input(f"\nItem-{i}: ")
                weight = float(input("Weight(Kg): "))
                priority = int(input("Priority(1-5): "))
                items.append((item, weight, priority))

            can_divide_parts = input("\nCan your item be divided into parts? (Yes/No): ")
            if can_divide_parts.lower() == "yes":
                sorted_items = sorted(items, key=lambda x: x[2])  # Sorting items based on priority

                total_weight = 0
                recommended_items = []
                item_parts = {}

                for item, weight, priority in sorted_items:
                    if total_weight + weight <= max_capacity:
                        total_weight += weight
                        recommended_items.append(f"{item}(whole)")
                    else:
                        remaining_capacity = max_capacity - total_weight
                        if remaining_capacity > 0:
                            num_parts = int(weight // remaining_capacity) + 1
                            item_parts[item] = f"{num_parts}/4 parts"
                            total_weight += remaining_capacity
                            break

                print("\nWe recommend you to bring:")
                for item in recommended_items:
                    print(f"- {item}")

                if item_parts:
                    for item, parts in item_parts.items():
                        print(f"- {item} ({parts})")

                print("You can use our recommendation or choose another class to carry more.")
            else:
                sorted_items = sorted(items, key=lambda x: x[2])  # Sorting items based on priority

                total_weight = 0
                recommended_items = []

                for item, weight, priority in sorted_items:
                    if total_weight + weight <= max_capacity:
                        total_weight += weight
                        recommended_items.append(f"- {item}")

                print("\n We recommended you bring:")
                for item in recommended_items:
                    print(f"{item}")

                print(f"\nWith total weight: {total_weight} Kg")
                print("You can use our recommendation or choose another class to carry more.")
                try_another_class = input("Try another class (Yes/No): ")
                if try_another_class.lower() == "yes":
                    menu3()
        else:
            print("Invalid class choice.")
    else:
        print("Thank you for using the program!")

def menu1():
    clear_console()
    order_ticket()

def menu2():
    clear_console()
    view_routes()
    print("Take your route")
    print("===============")
    start = input("From:")
    end = input("To:")
    if start in nodes and end in nodes:
        previous_nodes,shortest_path=dijkstra_algorithm(graph=graph,start_node=start)
        print(f"Here is the shortest route from {start} to {end}: ")
        print_result(previous_nodes,shortest_path,start_node=start,target_node=end)
    else:
        print("No route found.")
    print("")    
    print("See another route?")
    choice_menu_2 = input("Yes/No: ") 
    if choice_menu_2.lower() == "yes":
        menu2()
    else:
        station_program() 

def menu3():
    clear_console()
    print("------------------------------------------------------------")
    print("| class           |  Max Capacity(Kg)   | Cost ($)            |")
    print("------------------------------------------------------------")
    for class_name, capacity in class_capacity.items():
        cost = class_cost.get(class_name)
        print(f"| {class_name.ljust(16)}| {str(capacity).ljust(20)}| {str(cost).ljust(20)}|")
    print("------------------------------------------------------------")
    print()
    recommend_items() 
    choice3 = input("Try another class(Yes/No): ")
    if choice3.lower() == "yes" :
        menu3()
    else :
        station_program()               

def station_program():
    while True:
        clear_console()
        print("Welcome to Rizki Express!")
        print("========================")
        print("1. Order ticket")
        print("2. View routes")
        print("3. View train")
        print("4. Exit")
        print("========================")
        
        choice = input("Choose(1-4): ")
        
        if choice == "1":
            menu1()
        elif choice == "2":
            menu2()
        elif choice == "3":
            menu3()
        elif choice == "4":
            print("Thank you for using Rizki Express!")
            break
        else:
            print("Invalid choice. Please try again.")

station_program()
