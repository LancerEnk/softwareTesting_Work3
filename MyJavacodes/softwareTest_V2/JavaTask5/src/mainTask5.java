import java.util.Scanner;

public class mainTask5 {

    public void password(){
        // 打开输入流
        Scanner in = new Scanner(System.in);

        String inStr = in.nextLine();
        String ans="";  //定义一个空的ans字符串，有操作向里面添加内容即可
        for(int i=0;i<inStr.length();++i){
            //对inStr数组进行遍历
            char index_i = inStr.charAt(i);
            if(index_i=='a'||index_i=='o'||index_i=='y'||index_i=='e'||index_i=='u' ||index_i=='i'
                    ||index_i=='A'||index_i=='O'||index_i=='Y'||index_i=='E'||index_i=='U'
                    ||index_i=='I'){
                //如果是元音，不添加，不管它
            }
            else{
                //否则说明是辅音
                if(index_i>='A'&&index_i<='Z'){
                    //如果是大写，则改成小写
                    index_i+=32;
                }
                ans = ans+"."+index_i;
            }
        }
        System.out.println(ans);
    }

    public static void main(String[] args) {
        mainTask5 task5 = new mainTask5();
        task5.password();
    }


}
/**
 * 任务编号 5：
 * 该手机的加密原理为：机主每次输入密码（字符串）时，实际接受的密码为特殊处理后的字符串。
 * 请实现特殊处理的步骤：
 * （1）删除所有元音，
 * （2）在每个辅音前插入一个字符“.”
 * （3）将所有大写辅音替换为相应的小写辅音。
 * 元音是字母 “A”、“O”、“Y”、“E”、“U”、“I”，其余是辅音。
 * 程序的输入正好是一个字符串，它应该以单个字符串的形式返回输出。
 *
 * Input:第一行表示输入字符串。此字符串仅由大写和小写拉丁字母组成，长度为1到100。
 * Output:打印处理后的字符串。可以保证此字符串不是空的。
 */