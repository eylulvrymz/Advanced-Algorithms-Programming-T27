import java.util.*;

public class Exercise3 {
    private Map<String, Set<String>> adjacencyList = new HashMap<>();

    public void addUser(String user) {
        adjacencyList.putIfAbsent(user, new HashSet<>());
    }

    public void addFriendship(String u, String v) {
        adjacencyList.computeIfAbsent(u, k -> new HashSet<>()).add(v);
        adjacencyList.computeIfAbsent(v, k -> new HashSet<>()).add(u);
    }

    public List<String> bfs(String start) {
        List<String> result = new ArrayList<>();
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new LinkedList<>();
        queue.add(start);
        visited.add(start);
        while (!queue.isEmpty()) {
            String user = queue.poll();
            result.add(user);
            for (String neighbor : adjacencyList.getOrDefault(user, new HashSet<>())) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }
        return result;
    }

    public Map<String, Integer> bfsWithDistances(String start) {
        Map<String, Integer> distances = new HashMap<>();
        Queue<String> queue = new LinkedList<>();
        distances.put(start, 0);
        queue.add(start);
        while (!queue.isEmpty()) {
            String user = queue.poll();
            for (String neighbor : adjacencyList.getOrDefault(user, new HashSet<>())) {
                if (!distances.containsKey(neighbor)) {
                    distances.put(neighbor, distances.get(user) + 1);
                    queue.add(neighbor);
                }
            }
        }
        return distances;
    }

    public List<String> shortestPath(String start, String target) {
        if (start.equals(target)) return Collections.singletonList(start);
        Set<String> visited = new HashSet<>();
        Queue<List<String>> queue = new LinkedList<>();
        queue.add(new ArrayList<>(Collections.singletonList(start)));
        visited.add(start);
        while (!queue.isEmpty()) {
            List<String> path = queue.poll();
            String user = path.get(path.size() - 1);
            for (String neighbor : adjacencyList.getOrDefault(user, new HashSet<>())) {
                if (!visited.contains(neighbor)) {
                    List<String> newPath = new ArrayList<>(path);
                    newPath.add(neighbor);
                    if (neighbor.equals(target)) return newPath;
                    visited.add(neighbor);
                    queue.add(newPath);
                }
            }
        }
        return Collections.emptyList();
    }

    public int degreesOfSeparation(String start, String target) {
        List<String> path = shortestPath(start, target);
        return path.isEmpty() ? -1 : path.size() - 1;
    }

    public Set<String> friendsWithinKHops(String start, int k) {
        Map<String, Integer> distances = bfsWithDistances(start);
        Set<String> result = new HashSet<>();
        for (Map.Entry<String, Integer> e : distances.entrySet()) {
            if (!e.getKey().equals(start) && e.getValue() <= k)
                result.add(e.getKey());
        }
        return result;
    }

    public double computeAverageDegreesOfSeparation() {
        long total = 0, count = 0;
        for (String user : adjacencyList.keySet()) {
            Map<String, Integer> distances = bfsWithDistances(user);
            for (Map.Entry<String, Integer> e : distances.entrySet()) {
                if (!e.getKey().equals(user)) {
                    total += e.getValue();
                    count++;
                }
            }
        }
        return count == 0 ? 0 : (double) total / count;
    }

    public Map<Integer, Integer> getDistanceDistribution(String start) {
        Map<String, Integer> distances = bfsWithDistances(start);
        Map<Integer, Integer> distribution = new TreeMap<>();
        for (Map.Entry<String, Integer> e : distances.entrySet()) {
            if (!e.getKey().equals(start))
                distribution.merge(e.getValue(), 1, Integer::sum);
        }
        return distribution;
    }

    public List<String> recommendFriends(String start, int maxRec) {
        Set<String> directFriends = adjacencyList.getOrDefault(start, new HashSet<>());
        Map<String, Integer> candidates = new HashMap<>();
        for (String friend : directFriends) {
            for (String fof : adjacencyList.getOrDefault(friend, new HashSet<>())) {
                if (!fof.equals(start) && !directFriends.contains(fof))
                    candidates.merge(fof, 1, Integer::sum);
            }
        }
        return candidates.entrySet().stream()
                .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
                .limit(maxRec)
                .map(Map.Entry::getKey)
                .collect(java.util.stream.Collectors.toList());
    }
}