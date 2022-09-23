import java.util.Arrays;

public class RunningSumof1dArray {
    public static int[] running_Sumof_1d_Array(int [] array)
    {
        int [] results = new int[array.length];
        results[0] = array[0];
        int i = 1;
        while(i<array.length)
        {
            results[i] = array[i] + array[i-1];
            i++;

        }
        return results;

    }

    public static void main(String[] args)
    {
        int [] arr = {1,2,3};
        System.out.println(Arrays.toString(running_Sumof_1d_Array(arr)));

    }
}
