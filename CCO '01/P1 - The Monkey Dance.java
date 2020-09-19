
/****************************************************/
// Problem: CCO '01 P1 - The Monkey Dance
// Description: https://dmoj.ca/problem/cco01p1
// Language: Java
// Created by: Willie Pai
// Date: 19/09/2020
/****************************************************/

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        // Hashtable (key, value) memory for arrow directions
        Hashtable<Integer, Integer> directions = new Hashtable<Integer, Integer>();
        // Temporary storage of start and end position of arrows for .split()
        String[] stringInput = new String[2];
        // Tracks number of steps in the dance, for final output
        // Storage for starting position of Monkeys, and their current position
        int[][] startCurrentPos = new int[100][2];
        // Tracking whether all arrows point to self
        boolean isSelf;
        // Tracks current step number
        int stepCount;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        do {
            isSelf = true;
            for (int i = 0; i < N; i++) {
                stringInput = br.readLine().split(" ");
                directions.put(Integer.parseInt(stringInput[0]), Integer.parseInt(stringInput[1]));
                startCurrentPos[i][0] = startCurrentPos[i][1] = Integer.parseInt(stringInput[0]);
                if (!stringInput[0].equals(stringInput[1]))
                    isSelf = false;
            }

            stepCount = 0;

            // If all arrows point to itself (e.g. circle 1 to circle 1), then print 0 & skip
            if (isSelf) {
                System.out.println(0);
                continue;
            }

            do {

                // Move all monkeys to next position
                for (int i = 0; i < N; i++) {
                    startCurrentPos[i][1] = directions.get(startCurrentPos[i][1]);
                }

                stepCount++;

            } while (!hasReturn(startCurrentPos, N));

            System.out.println(stepCount);

            // -------------------------------------------------------------------------
            // Clearing the starting and current position of the monkey's is not needed,
            // since it will overwrite itself for every case
            // -------------------------------------------------------------------------
            // for (int i = 0; i < N; i++)
            // startCurrentPos[i][0] = startCurrentPos[i][1] = 0;

            directions.clear();

            N = Integer.parseInt(br.readLine());

        } while (N != 0);

    }

    public static boolean hasReturn(int[][] startCurrentPos, int N) {
        for (int i = 0; i < N; i++)
            if (startCurrentPos[i][0] != startCurrentPos[i][1])
                return false;
        return true;
    };

}