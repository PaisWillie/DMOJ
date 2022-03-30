import java.io.*;

public class S1_Good_Fours_Good_Fives {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int target = Integer.parseInt(br.readLine());

        int count = 0;
        int sum = 0;

        while(sum <= target) {

            if ((target - sum) % 5 == 0) {
                count++;
            }

            sum += 4;
        }

        System.out.println(count);
    }
}
