public class KthElementOfArray {
    public static void main(String[] args) {
        int[] a = { 5, 8, 12, 2, 4, 1 };
        int k = 3;

        for (int i = 0; i < a.length - 1; i++) {
            for (int j = i + 1; j < a.length; j++) {
                if (a[i] > a[j]) {
                    int temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                }
            }
            if (i == k - 1) {
                System.out.println(k + "th smallest element is " + a[i]);
            }
        }
    }

}
