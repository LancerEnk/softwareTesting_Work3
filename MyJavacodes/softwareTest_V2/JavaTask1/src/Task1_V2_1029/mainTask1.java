package Task1_V2_1029;
import javax.swing.text.DefaultEditorKit;
import java.util.*;
/**
 * 任务编码 1：
 * 一个炎热的夏天，有一个人和他的一个朋友前来买瓜。他们选择了大棚的瓜。
 * 称重西瓜（没有吸铁石）秤显示有w公斤. 他们冲回家分瓜，然而他们面临一个难题。
 * 他们是偶数的超级粉丝，所以他们想把西瓜分成两部分，两个部分的重量都是偶数公斤，同时两个部分不一定相等。
 * 他们非常累，想尽快开始吃饭，所以你应该帮助他们，看看他们是否能按照他们想要的方式分西瓜。
 * 当然，他们每个人都应该得到一部分。
 *
 * Input：第一行(也是唯一一行)输入的是整数w(1≤w≤100)——买的西瓜的重量。
 */

public class mainTask1 {
    public String CutWatermellon(){
        //打开输入流
        Scanner in = new Scanner(System.in);
        int w = in.nextInt();
        String yes = "YES";
        String no = "NO";
        if(w==2) return no;
        else{
            if(w%2==0) return yes;
            else return no;
        }
    }

    public static void main(String[] args) {
        mainTask1 mT1=new mainTask1();
        //mT1.CutWatermellon();
        System.out.println(mT1.CutWatermellon());
    }
}
