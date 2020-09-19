/*********************************************************/
// Problem: CCC '17 S1 - Sum Game
// Description: https://dmoj.ca/problem/ccc17s1
// Language: Java
// Created by: Willie Pai
// Date: 08/12/2019
/*********************************************************/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class S1_Sum_Game {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] a = new int[N];
		int[] b = new int[N];
		
		String[] line = br.readLine().split(" ");
		for (int i = 0; i < N; i++)
			a[i] = Integer.parseInt(line[i]);
		
		line = br.readLine().split(" ");
		for (int i = 0; i < N; i++)
			b[i] = Integer.parseInt(line[i]);
		
		int score_a = 0, score_b = 0;
		
		int highestDay = 0;
		
		for (int i = 0; i < N; i++) {
			score_a += a[i];
			score_b += b[i];
			if (score_a == score_b) {
				highestDay = i + 1;
			}
		}
		
		System.out.println(highestDay);
		
	}
	
}
