// updateScore
EngagementPriorityQueue updatePQ = new EngagementPriorityQueue();
updatePQ.enqueue(new Post(40, 1, "Top post", 100L, 50, 10, 5));
        updatePQ.enqueue(new Post(41, 2, "Mid post", 200L, 10, 2, 1));
        updatePQ.enqueue(new Post(42, 3, "Low post", 300L, 2, 0, 0));
        System.out.println("Before update:");
updatePQ.display();
updatePQ.updateScore(42, 100, 50, 30);
System.out.println("Low post becomes new max:");
updatePQ.display();

// updateScore
updatePQ.updateScore(40, 0, 0, 0);
System.out.println("Top post becomes new min:");
updatePQ.display();