import heapq
import math

def dijkstra(graph, start):
    shortest_paths = {node: math.inf for node in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        for neighbor, travel_time in graph[current_node]['routes'].items():
            distance = current_dist + travel_time
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

def optimalTouristPath(graph, start_island, max_time):
    # Run Dijkstra's algorithm at the first node
    shortest_paths = dijkstra(graph, start_island)
    experience_queue = []
    current_island = start_island
    total_time = 0
    visited_experiences = set()
    tourist_path = []

    # Create the initial experience queue
    for island, data in graph.items():
        for experience, experience_time in data.get('experiences', {}).items():
            if island in shortest_paths:
                combined_time = shortest_paths[island] + experience_time
                heapq.heappush(experience_queue, (combined_time, island, experience, experience_time))

    # Loop to process the experiences based on shortest path and experience time
    while experience_queue and total_time <= max_time:
        combined_time, island, experience, experience_time = heapq.heappop(experience_queue)

        # Skip if visited already
        if experience in visited_experiences:
            continue

        # See if experience is on same island
        if island != current_island:
            # Move to a new island, add travel time, and update shortest paths
            total_time += shortest_paths[island]
            if total_time > max_time:
                break  # Stop if exceeded max time
            current_island = island
            tourist_path.append(f"Travel to {current_island} (time: {shortest_paths[island]})")
            shortest_paths = dijkstra(graph, current_island)  # Rerun Dijkstra's from new island

        # Complete the experience
        visited_experiences.add(experience)
        total_time += experience_time
        if total_time > max_time:
            break  # Stop if exceeded max time
        tourist_path.append(f"Experience {experience} on {current_island} (time: {experience_time})")

        # Repopulate the experience queue with new paths
        for other_island, data in graph.items():
            for new_exp, new_exp_time in data.get('experiences', {}).items():
                if new_exp not in visited_experiences and other_island in shortest_paths:
                    combined_time = shortest_paths[other_island] + new_exp_time
                    heapq.heappush(experience_queue, (combined_time, other_island, new_exp, new_exp_time))

    return tourist_path