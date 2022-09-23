public class ReduceNumberToZero {
    public static int getReduceNumber(int num) {
        int count = 0;

        while (num != 0) {
            if (num % 2 == 0) {
                count += 1;
                num = num / 2;
            } else {
                count += 1;
                num = num - 1;
            }
        }
        return count;
    }

}
