from optimalResourcePath import optimalResourcePath, useOptimalResourcePath
from optimalLeaderPath import optimalLeaderPath, useOptimalLeaderPath
from optimalTouristPath import optimalTouristPath

ISLAND_GRAPH = {
    'Hawaii': {
        'routes': {'Tahiti': 5, 'Fiji': 10, 'South America': 15},
        'population': 50000,
        'resources': {
            'kahelelani_shells': 20,
            'sweet_potatoes': 50,
            'coconuts': 200,
            'fish': 1000,
        },
        'experiences': {
            'volcano_tour': 3,
            'surfing': 2
        },
        'last_visit_by_leader': 0
    },
    'Tahiti': {
        'routes': {'Hawaii': 5, 'Fiji': 4, 'Samoa': 3, 'South America': 18, 'South Eastern Asia': 221},
        'population': 70000,
        'resources': {
            'kahelelani_shells': 5,
            'sweet_potatoes': 100,
            'coconuts': 300,
            'fish': 800,
            'pearl_shells': 50
        },
        'experiences': {
            'pearl_diving': 4,
            'traditional_dance': 2
        },
        'last_visit_by_leader': 0
    },
    'Fiji': {
        'routes': {'Hawaii': 10, 'Samoa': 2, 'Tahiti': 4, 'South Eastern Asia': 20},
        'population': 60000,
        'resources': {
            'kahelelani_shells': 2,
            'sweet_potatoes': 120,
            'coconuts': 500,
            'fish': 950
        },
        'experiences': {
            'coral_reef_tour': 3,
            'fire_dancing': 2
        },
        'last_visit_by_leader': 0
    },
    'Samoa': {
        'routes': {'Tahiti': 3, 'Fiji': 2, 'Cook Islands': 6},
        'population': 40000,
        'resources': {
            'kahelelani_shells': 1,
            'sweet_potatoes': 30,
            'coconuts': 150,
            'fish': 600,
            'taro': 300
        },
        'experiences': {
            'canoe_race': 3,
            'tapa_making': 2
        },
        'last_visit_by_leader': 0
    },
    'Cook Islands': {
        'routes': {'Samoa': 6, 'Tahiti': 7},
        'population': 20000,
        'resources': {
            'kahelelani_shells': 3,
            'sweet_potatoes': 10,
            'coconuts': 80,
            'fish': 400,
            'pearl_shells': 20
        },
        'experiences': {
            'shell_collecting': 2,
            'traditional_feast': 3
        },
        'last_visit_by_leader': 0
    },
    'Niʻihau': {
        'routes': {'Hawaii': 4},
        'population': 200,
        'resources': {
            'kahelelani_shells': 500
        },
        'experiences': {
            'lei_making': 2
        },
        'last_visit_by_leader': 0
    },
    'South America': {
        'routes': {'Hawaii': 15, 'Tahiti': 18},
        'population': 100000,
        'resources': {
            'sweet_potatoes': 1000
        },
        'last_visit_by_leader': 0
    },
    'South Eastern Asia': {
        'routes': {'Fiji': 20, 'Tahiti': 22},
        'population': 150000,
        'resources': {
            'kalo': 2000
        },
        'last_visit_by_leader': 0
    }
}

def display_menu():
    print("\nIsland Navigation Testing Interface")
    print("1. Distribute Resource (optimalResourcePath + useOptimalResourcePath)")
    print("2. Knowledge Sharing by Leaders (optimalLeaderPath + useOptimalLeaderPath)")
    print("3. Tourist Experience Path (optimalTouristPath)")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    return choice

def run_optimal_resource_path():
    resource = input("Enter the resource to distribute (e.g., kahelelani_shells): ")
    canoe_capacity = int(input("Enter the canoe capacity for resource distribution (e.g., 50): "))
    print("\nRunning optimalResourcePath with resource:", resource, "and canoe capacity:", canoe_capacity)
    
    path = optimalResourcePath(ISLAND_GRAPH, resource, canoe_capacity)
    print("Distribution path:", path)
    
    print("\nUsing the path to update the graph with useOptimalResourcePath...")
    updated_graph = useOptimalResourcePath(ISLAND_GRAPH, path, resource)
    print("Updated Graph:", updated_graph)

def run_optimal_leader_path():
    start_island = input("Enter the starting island for the leader's journey (e.g., Hawaii): ")
    print("\nRunning optimalLeaderPath from island:", start_island)
    path = optimalLeaderPath(ISLAND_GRAPH, start_island)
    print("Leader's path:", path)
    
    print("\nUsing the path to update the graph with useOptimalLeaderPath...")
    updated_graph = useOptimalLeaderPath(ISLAND_GRAPH, path)
    print("Updated Graph:", updated_graph)

def run_optimal_tourist_path():
    start_island = input("Enter the starting island for the tourist (e.g., Hawaii): ")
    max_time = int(input("Enter the maximum travel time in hours (e.g., 15): "))
    print("\nRunning optimalTouristPath from island:", start_island, "with max time:", max_time)
    path = optimalTouristPath(ISLAND_GRAPH, start_island, max_time)
    print("Tourist's path:", path)

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            run_optimal_resource_path()
        elif choice == '2':
            run_optimal_leader_path()
        elif choice == '3':
            run_optimal_tourist_path()
        elif choice == '4':
            print("Exiting the interface. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()