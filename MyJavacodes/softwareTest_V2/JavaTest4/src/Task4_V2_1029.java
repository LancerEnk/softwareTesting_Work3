import java.util.Scanner;

public class Task4_V2_1029 {

    public void newScreen(){
        // 打开输入流
        Scanner in = new Scanner(System.in);
        int ans=0;
        int m=in.nextInt();
        int n=in.nextInt();
        if(n*m%2==0){
            ans=n*m/2;
        }
        else ans=(n*m-1)/2;
        System.out.println(ans);
    }


    public static void main(String[] args) {
        Task4_V2_1029 task4 = new Task4_V2_1029();
        task4.newScreen();
    }
}
