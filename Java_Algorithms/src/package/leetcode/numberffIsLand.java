// 200. Number of Islands
// Medium
// 18.3K
// 408
// Companies

// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
// return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
// You may assume all four edges of the grid are all surrounded by water.

//  

// Example 1:

// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1

// Example 2:

// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3

public class numberffIsLand {
    public static int numIsLands(char[][] grid) {
        
 
        int res = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == '1'){
                    res+=1;
                    depthfirstSeacrch(grid, i, j);
                }          
            }
        }

        return res;
        
    }
    static void depthfirstSeacrch(char[][] grid, int r , int c) {
        if(r < 0 || r >= grid.length || c <0 || c >= grid[0].length || grid[r][c] == '0'){return ;}
        grid[r][c] = '0';
        depthfirstSeacrch(grid, r+1, c);
        depthfirstSeacrch(grid, r-1, c);
        depthfirstSeacrch(grid, r, c+1);
        depthfirstSeacrch(grid, r, c-1);
    }

    public static void main(String[] args) {
     char[][] grid = {
                {'1','1','0','0','0'},
                {'1','1','0','0','0'},
                {'0','0','1','0','0'},
                {'0','0','0','1','1'}};

    System.out.println(numIsLands(grid));
    }
}
