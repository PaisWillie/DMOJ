
/*********************************************************/
// Problem: Another Contest 5 Problem 2 - Great Graffiti
// Description: https://dmoj.ca/problem/acc5p2
// Language: Java
// Created by: Willie Pai
// Date: 07/08/2019
/*********************************************************/

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String graffiti = br.readLine();
		
		if (graffiti.contains("DMOJ"))
			System.out.println("0");
		else if (graffiti.contains("DMO") || graffiti.contains("MOJ"))
			System.out.println("1");
		else if (graffiti.contains("DM") || graffiti.contains("MO") || graffiti.contains("OJ"))
			System.out.println("2");
		else if (graffiti.contains("D") || graffiti.contains ("M") || graffiti.contains("O") || graffiti.contains ("J"))
			System.out.println("3");
		else
			System.out.println("4");
		
	}

}