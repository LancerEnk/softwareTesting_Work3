package allTasks;
import java.lang.reflect.Array;
import java.util.*;

public class Task8 {
    public void aADDb(){

        // 打开输入流
        Scanner in = new Scanner(System.in);
        String str1 = in.nextLine();
        int num = str1.length();
        int [] a = new int[(num+1)/2];
        int count = -1;
        String ans="";
        for(int i=0;i<num;++i){
            if(str1.charAt(i)!='+'){
                //给数组里面存数字
                count++;
                a[count]=str1.charAt(i);
            }
        }

        //数组排序
        Arrays.sort(a);
        ans+=a[0]-48;
        //ans+=a[0];
        for(int i=1;i<=count;i++){
            ans = ans + "+" + String.valueOf(a[i]-48);
        }

        System.out.println(ans);
    }

}

/**
 * 任务编码 8：
 * 卢本伟为了节省欢乐豆，参加了不允许加倍、炸弹不算加倍的斗地主游戏。
 * 由于他不敢叫地主，所以每次游戏胜利的奖分只能是1分、2分、3分。
 * 给定一个加法算式表示卢本伟一天里所有胜场的奖分，为了计算简便，请帮助卢本伟将加数按照“非减顺序”排列。
 *
 * Input:输入一个非空字符串，表示加法算式，只包含数字 1、2、3以及符号 “+”
 * Output:处理后的算式
 */