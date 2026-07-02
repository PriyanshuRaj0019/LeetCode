class Solution {

    int[][] dir = {{1,0},{-1,0},{0,1},{0,-1}};

    public boolean findSafeWalk(List<List<Integer>> grid, int health) {

        int m = grid.size();
        int n = grid.get(0).size();

        int[][] dist = new int[m][n];

        for (int[] row : dist)
            Arrays.fill(row, Integer.MAX_VALUE);

        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> a[0] - b[0]
        );

        dist[0][0] = grid.get(0).get(0);

        pq.offer(new int[]{dist[0][0], 0, 0});

        while (!pq.isEmpty()) {

            int[] cur = pq.poll();

            int damage = cur[0];
            int r = cur[1];
            int c = cur[2];

            if (damage > dist[r][c])
                continue;

            if (r == m - 1 && c == n - 1)
                return damage < health;

            for (int[] d : dir) {

                int nr = r + d[0];
                int nc = c + d[1];

                if (nr < 0 || nr >= m || nc < 0 || nc >= n)
                    continue;

                int newDamage = damage + grid.get(nr).get(nc);

                if (newDamage < dist[nr][nc]) {

                    dist[nr][nc] = newDamage;
                    pq.offer(new int[]{newDamage, nr, nc});
                }
            }
        }

        return false;
    }
}