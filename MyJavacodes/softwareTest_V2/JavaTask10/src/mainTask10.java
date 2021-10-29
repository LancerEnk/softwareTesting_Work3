import java.util.Scanner;

public class mainTask10 {

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

    public static void main(String[] args) {
        mainTask10 mainTask10 = new mainTask10();
        mainTask10.stone();
    }
}
/**
 * 任务编号 10：
 * 张三捡到了一串彩色石头链子（不是环形），由三种不同颜色的石头组成。
 * 他打算将链子中的部分石头拿下来自己留着，使得链子上剩余的石头中，任意相邻的石头颜色不同。
 * 【输入】
 * 输入的第一行是一个整数表示链子的长度
 * 输入的第二行是一个非空字符串，其中R、G、B分别表示三种颜色的石头。
 * 【输出】
 * 输出张三至少会拿下来多少石头
 */