package Task3_V2_1029;

import java.util.Scanner;

public class mainTask3 {
    public int Fighting_landlords(){
        //打开输入流
        Scanner in = new Scanner(System.in);

        int n=in.nextInt();
        int k=in.nextInt();
        int [] score = new int[n];
        boolean isZero=false;

        //for循环向数组输入数据
        for(int i=0;i<n;++i){
            score[i]=in.nextInt();
            //防止0出现 ---bug修改更新内容
            if(score[i]==0 && k>i) {
                //如果当前位置==0且原定胜出人数更多的话，后面的都录不了，k只能直接停止
                isZero=true;
                if(i==0) k=0;
                else {
                    k = i;
                    break;
                }
            }
        }

        int ans=k;

        //计算ans是否要后延
        if( !isZero && k!=0 ) {
            int passNum = score[k - 1];
            for (int t = k; t < n; ++t) {
                if (score[t] == passNum) ans++;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        mainTask3 mT3 = new mainTask3();
        System.out.println(mT3.Fighting_landlords());
    }
}

/**
 * 任务编号 3：
 * 慈善家卢本伟参加了斗地主比赛，欢乐豆（分数）等于或大于 “第 k名选手得分 ”的选手将进入下一轮，但要求该选手得分为正。
 * 假设共有n名参与者参加了比赛（n ≥ k） ，你已经知道他们的分数了。计算有多少参与者将进入下一轮。
 *
 * Input:输入的第一行包含两个整数n和k（1≤k≤n≤50）由单个空格分隔。
 * 第二行包含n个空格分隔的整数a1，a2，...,an（0≤ai≤100），其中ai是获得第i名的参与者获得的分数。给定的序列符合“ai≥ai+1”.
 *
 * Output:输出进入下一轮的参与者人数。
 */