import heapq
import math

def optimalResourcePath(graph, resource, capacity):
    # Pick the starting island with the most amount of the resource
    start_island = max(graph, key=lambda island: graph[island]['resources'].get(resource, 0))
    
    # Calculate how many resources each population should get, based on proportion of population
    total_population = sum(graph[island]['population'] for island in graph if resource in graph[island]['resources'])
    total_resource = graph[start_island]['resources'][resource]
    
    # Avoid fractions
    required_resources = {
        island: math.floor((graph[island]['population'] / total_population) * total_resource)
        for island in graph if resource in graph[island]['resources']
    }
    
    # Distribute any leftover resources to ensure the total is accurate
    distributed_sum = sum(required_resources.values())
    leftover_resources = total_resource - distributed_sum
    if leftover_resources > 0:
        for island in sorted(required_resources, key=lambda x: graph[x]['population'], reverse=True):
            if leftover_resources > 0:
                required_resources[island] += 1
                leftover_resources -= 1
    
    # Initialize a priority queue and tracking variables
    priority_queue = [(0, start_island)]
    visited = set()
    distribution_path = []
    distributed_resources = {island: 0 for island in required_resources}
    canoe_stock = capacity 

    while priority_queue:
        current_distance, current_island = heapq.heappop(priority_queue)
        
        # Skip islands that don't need this resource
        if current_island not in required_resources:
            continue
        
        # Calculate the remaining amount required for the current island
        required_amount = required_resources[current_island] - distributed_resources[current_island]
        
        # If we need to restock, return to the start island
        if canoe_stock < required_amount and canoe_stock < capacity:
            # Add a restock trip
            distribution_path.append((start_island, 0))
            canoe_stock = capacity  # Refill the canoe
            # Re-queue the current island to try again
            heapq.heappush(priority_queue, (current_distance, current_island))
            continue
        
        # Determine how much we can distribute to the current island
        to_distribute = min(canoe_stock, required_amount)
        
        if to_distribute > 0:
            # Distribute resources and update the canoe stock
            distributed_resources[current_island] += to_distribute
            canoe_stock -= to_distribute
            distribution_path.append((current_island, to_distribute))
        
        # Explore neighboring islands
        for neighbor, distance in graph[current_island]['routes'].items():
            if neighbor not in visited and neighbor in required_resources:
                new_distance = current_distance + distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
        
        # Mark current island as visited once it's fully served
        if distributed_resources[current_island] >= required_resources[current_island]:
            visited.add(current_island)
        
        # Check if we have fully distributed resources
        if all(distributed_resources[island] >= required_resources[island] for island in required_resources):
            break
    
    return distribution_path

# Function to update the graph based on the distribution path
def useOptimalResourcePath(graph, path, resource):
    for island, amount in path:
        if amount > 0 and resource in graph[island]['resources']:
            graph[island]['resources'][resource] += amount
    return graph
