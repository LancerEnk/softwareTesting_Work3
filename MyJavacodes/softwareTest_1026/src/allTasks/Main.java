package allTasks;
import java.util.*;

public class Main {
    public static void main(String[] args) {

        //调用输入流
        Scanner in = new Scanner(System.in);
        System.out.println("请输入要进行测试的任务编码：\r");
        int id = in.nextInt();

        //对任务编号进行判断并进入对应的分支：
        switch(id){
            case 1:
                //【任务1】代码试运行
                //测试用例：1√2√3√4√5√6√7√8√
                System.out.println("当前正在运行任务编码1的代码,请进行测试！\r");
                Task1 task1 = new Task1();
                System.out.println(task1.CutWatermellon());
                break;

            case 2:
                //【任务2】代码试运行
                //测试用例：1√2√3√4√5√6√7√8√
                System.out.println("当前正在运行任务编码2的代码,请进行测试！\r");
                Task2 task2 = new Task2();
                System.out.println(task2.rectangle());
                break;

            case 3:
                //【任务3】代码试运行
                //测试用例：1√2√3√4√5√6√7√8√
                System.out.println("当前正在运行任务编码3的代码,请进行测试！\r");
                Task3 task3 = new Task3();
                System.out.println(task3.Fighting_landlords());
                break;
                //default -> System.out.println("请输入正确的任务编号，范围为1~10！");

            case 4:
                //【任务4】代码试运行
                //测试用例1√2√3√4√5√6√7√8√
                System.out.println("当前正在运行任务编码4的代码,请进行测试！\r");
                Task4 task4 = new Task4();
                for(int i=0;i<8;++i){
                    task4.newScreen();
                }
                break;

            case 5:
                //【任务5】代码试运行
                //测试用例1√2√3√4√5√6√7√8√
                System.out.println("当前正在运行任务编码5的代码,请进行测试！\r");
                Task5 task5 = new Task5();
                for(int i=0;i<8;++i){
                    task5.password();
                }
                break;

            case 6:
                //【任务6】代码试运行
                //测试用例1√2√3√4√5√6√7√8√
                System.out.println("当前正在运行任务编码6的代码,请进行测试！\r");
                Task6 task6 = new Task6();
                for(int i=0;i<8;++i){
                    task6.worldGame();
                }
                break;

            case 7:
                //【任务7】代码试运行
                //测试用例1√2√3√4√5√6√7√8√
                System.out.println("当前正在运行任务编码7的代码,请进行测试！\r");
                Task7 task7 = new Task7();
                for(int i=0;i<8;++i){
                    task7.matrix();
                }
                break;

            case 8:
                //【任务8】代码试运行
                //测试用例1√2√3√4√5√6√7√8√
                System.out.println("当前正在运行任务编码8的代码,请进行测试！\r");
                Task8 task8 = new Task8();
                for(int i=0;i<8;++i){
                    task8.aADDb();
                }
                break;

            case 9:
                //【任务9】代码试运行
                //测试用例1√2√3√4√5√
                System.out.println("当前正在运行任务编码9的代码,请进行测试！\r");
                Task9 task9 = new Task9();
                for(int i=0;i<5;++i){
                    task9.passWord();
                }
                break;

            case 10:
                //【任务10】代码试运行
                //测试用例1√2√3√4√5√6√7√8√9√10√
                System.out.println("当前正在运行任务编码10的代码,请进行测试！\r");
                Task10 task10 = new Task10();
                for(int i=0;i<10;++i){
                    task10.stone();
                }
                break;

            default:
                System.out.println("请输入正确的任务编号，范围为1~10！");
        }

        System.out.println("测试结束！");

    }
}
