import java.util.Scanner;

public class mainTask7 {
    public void matrix(){
        // 打开输入流
        Scanner in = new Scanner(System.in);
        int [][] num = new int[5][5];
        int x=0,y=0;
        int ans;
        for(int i=0;i<5;++i){
            for(int j=0;j<5;++j) {
                num[i][j] = in.nextInt();
                //如果遇到非0，记录位置
                if(num[i][j]!=0){
                    x=i;
                    y=j;
                }
            }
        }
        ans=Math.abs(x-2)+Math.abs(y-2);
        System.out.println(ans);
    }

    public static void main(String[] args) {
        mainTask7 mT7 = new mainTask7();
        mT7.matrix();
    }

}

/**
 *
 * 任务编码 7：
 * 卢本伟方阵
 *
 */