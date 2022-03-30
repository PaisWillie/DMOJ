import java.io.*;

public class J1_Dog_Treats {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int S = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int L = Integer.parseInt(br.readLine());

        if (S + 2*M + 3*L >= 10) System.out.println("happy");
        else System.out.println("sad");
    }
}
