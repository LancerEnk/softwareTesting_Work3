import java.util.Scanner;

public class mainTask9 {
    public void passWord(){
        // 打开输入流
        Scanner in = new Scanner(System.in);
        String str1 = in.nextLine();
        //if(str1.charAt(0)<='z'&&str1.charAt(0)>='a') str1.charAt([0])-=32;
        char ch[]=str1.toCharArray();
        if(ch[0]<='z'&&ch[0]>='a') ch[0]-=32;
        System.out.println(new String(ch));
    }

    public static void main(String[] args) {
        mainTask9 mT9 = new mainTask9();
        mT9.passWord();
    }
}
/**
 * 任务编号 9：
 * 一款高端的钛金加密手机问世，专属一对一保密钥匙，忘带会提醒，人机分离十米自动爆炸。
 * 该手机的加密原理为：机主每次输入密码（字符串）时，实际接受的密码为特殊处理后的字符串，即首字母自动变成大写。
 * 请实现特殊处理的步骤：
 * 【输入】第一行表示输入字符串。此字符串仅由大写和小写拉丁字母组成，长度为1到1000。
 * 【输出】打印处理后的字符串。可以保证此字符串不是空的。
 */