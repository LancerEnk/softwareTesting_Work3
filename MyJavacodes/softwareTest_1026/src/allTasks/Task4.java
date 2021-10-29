package allTasks;
import java.util.*;

public class Task4 {
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

}


/**
 * 任务编号 4：
 * 卢本伟在一次斗地主游戏后失去了电脑屏幕，现在需要一个大小为 M × N的新的电脑屏幕。
 * 此外，他有无限数量的大小为2 × 1的长方形小屏幕块。允许旋转小屏幕，使得恰好可以用若干小屏幕块组成新屏幕。
 * 并且小屏幕块不可以切割，不可以有重叠。
 * 找出小屏幕块的最大数量。
 *
 * Input：在一行中，给你两个整数M和N(1 ≤ M ≤ N ≤ 16)。
 * Output：输出一个数字：小屏幕块的最大数量。
 *
 */