package allTasks;
import java.util.*;

public class Task2 {
    public int rectangle(){
        //打开输入流
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int m = in.nextInt();
        int a = in.nextInt();
        //答案ans初始化为0
        int ans=0;
        //如果一个大正方形能够覆盖广场，则只用一个牌
        if( a>=m && a>=n) ans=1;
        //否则一个牌盖在广场上会有裸露，应该用更多的牌。
        else{
            int x,y;
            if(n%a==0)x=n/a;
            else x=n/a+1;
            if(m%a==0) y=m/a;
            else y=m/a+1;
            ans=x*y;
        }
        //System.out.println(ans);
        return ans;
    }
}

/**
 * 任务编号 2：
 * “卢本伟广场”呈长方形，大小为n × m米。在卡布奇诺纪念日，决定用方形扑克牌铺广场。
 * 每块牌的尺寸都是a × a米。
 * 铺设广场最少需要多少牌？牌可以覆盖超出广场的范围。
 * 但是广场的范围必须被覆盖。不允许切割扑克牌。
 *
 * Input：输入在第一行包含三个正整数:n，m和a (1 ≤ n，m，a ≤ 10^9)。
 * Output：写出所需的牌的数量。
 *
 */
