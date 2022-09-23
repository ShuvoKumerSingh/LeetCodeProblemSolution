import java.util.Arrays;

public class RichestCustomerWealth {
    public int[] getmaximumwealth(int [][] accounts)
    {

        int maxwealt = 0;
        for(int [] element: accounts)
        {
            int currentCustomerWealth = 0;
            for(int bank: element)
            {
                currentCustomerWealth+=bank;
            }
            maxwealt = Math.max(maxwealt,currentCustomerWealth);

        }
        return new int[]{maxwealt};
    }

    public static void main(String[] args)
    {
        int [] []arr = {{1,2,3},{1,5,1}};
        RichestCustomerWealth richestCustomerWealth = new RichestCustomerWealth();
        System.out.println(Arrays.toString(richestCustomerWealth.getmaximumwealth(arr)));

    }

}
