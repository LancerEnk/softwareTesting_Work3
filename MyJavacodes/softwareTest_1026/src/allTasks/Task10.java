package allTasks;
import java.util.*;

public class Task10 {
    public void stone(){
        // 打开输入流
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        String str1 = in.next();
        char [] ch = str1.toCharArray();
        int count=0;
        //保证链长==石头数
        if(num!=ch.length) {
            System.out.println("输入的链长和石头数不符，请重新输入！");
        }
        for(int i=0;i<num-1;++i){
            if(ch[i]==ch[i+1]) {
                //如果连着两个相等，就取下一个，默认取ch[i]，因为ch[i+1]可以在下一轮次继续和ch[i+2]判断
                count++;
            }
        }
        System.out.println(count);
    }

}
