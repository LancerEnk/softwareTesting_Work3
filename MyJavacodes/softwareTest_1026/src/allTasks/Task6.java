package allTasks;
import java.util.*;

public class Task6 {
    public void worldGame(){
        // 打开输入流
        Scanner in = new Scanner(System.in);

        // 大写转小写操作 --> successful
        String str1 = in.nextLine().toLowerCase();
        String str2 = in.nextLine().toLowerCase();

        // 若Str1等于参数字符串Str2字符串，则返回0；
        // 若该Str1按字典顺序小于参数字符串Str2，则返回值小于0；
        // 若Str1按字典顺序大于参数字符串Str2，则返回值大于0。
        int ans=str1.compareTo(str2);
        if(ans==0) System.out.println("0");
        else if(ans<0) System.out.println("-1");
        else System.out.println("1");

    }


}

/**
 * 任务编号 6：
 * TX公司举办了《弱者农药》世界赛，
 * 为了避免小组赛分组抽签过程作弊，新体制的分组机制决定将16支队伍按照队名的顺序进行排列。请实现字符串比较的功能。
 *
 * Input：前两行中的每一行都包含一个购买的字符串。字符串的长度范围从1到100(包括1和100)。
 * 保证字符串长度相同，并且由大写和小写拉丁字母组成。
 * Output：如果第一个字符串小于第二个字符串，则打印“-1”。
 * 如果第二个字符串小于第一个字符串，则打印“1”。
 * 如果字符串相等，则打印“0”。
 * 请注意，在比较字符串时，不考虑字母的大小写。
 */