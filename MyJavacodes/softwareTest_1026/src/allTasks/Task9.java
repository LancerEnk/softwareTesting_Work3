package allTasks;
import java.util.*;


public class Task9 {
    public void passWord(){
        // 打开输入流
        Scanner in = new Scanner(System.in);
        String str1 = in.nextLine();
        //if(str1.charAt(0)<='z'&&str1.charAt(0)>='a') str1.charAt([0])-=32;
        char ch[]=str1.toCharArray();
        if(ch[0]<='z'&&ch[0]>='a') ch[0]-=32;
        System.out.println(new String(ch));
    }
}
