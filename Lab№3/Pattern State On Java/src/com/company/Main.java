package com.company;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Random;

public class Main{
    public static void main(String[] args)
    {
        Admission.makeScores();
        for (int i = 0; i < 100; i++) {
            Admission.studentAdmission(i);
        }
        System.out.println("Поступило " + Admission.success + " абитурентов");
    }
}

interface State {
    String getName(StateContext context);
    void doSomething(StateContext context);
}

class StateContext {
    private State state = new Begin();
    void doSomething()
    {
        state.doSomething(this);
    }
    void setState(State state)
    {
        this.state = state;
    }
    public State getState()
    {
        return state;
    }
}

class Begin implements State{
    private static final String NAME = "begin";

    @Override
    public String getName(StateContext context) {
        return NAME;
    }

    @Override
    public void doSomething(StateContext context)
    {
        System.out.println("Приём в ВУЗ открыт.");
        System.out.println("Документы поданы.");
        System.out.println("Проходной балл для 1 волны: " + Admission.n1 + ", для волны 2: " + Admission.n2);
    }
}

class AnalyzeFirstWave implements State{
    private static final String NAME = "analyze_first_wave";

    @Override
    public String getName(StateContext context) {
        return NAME;
    }

    @Override
    public void doSomething(StateContext context)
    {
        System.out.println("Результат вступительных испытаний: " + Admission.mark + ".");
        System.out.println("Конкурс 1 волна.");
        if (Admission.mark > Admission.n1) System.out.println("Попадание в 1 волну.");
    }
}

class AnalyzeSecondWave implements State{
    private static final String NAME = "analyze_first_wave";

    @Override
    public String getName(StateContext context) {
        return NAME;
    }

    @Override
    public void doSomething(StateContext context)
    {
        System.out.println("Конкурс 2 волна.");
        if (Admission.mark >= Admission.n2)
            System.out.println("Попадание во 2 волну");
        else
            System.out.println("Конкурс не пройден");
    }
}

class Treatment implements State{
    private static final String NAME = "treatment";

    @Override
    public String getName(StateContext context) {
        return NAME;
    }

    @Override
    public void doSomething(StateContext context)
    {
        System.out.println("Приказ о зачислении.");
    }
}

class End implements State{
    private static final String NAME = "end";

    @Override
    public String getName(StateContext context) {
        return NAME;
    }

    @Override
    public void doSomething(StateContext context)
    {
        System.out.println("Приём в ВУЗ закрыт.");
    }
}

class Admission{
    static int success;
    static int n1, n2;
    static void makeScores()
    {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try {
            System.out.println("Введите проходной балл для первой волны: ");
            n1 = Integer.parseInt(reader.readLine());
            System.out.println("Введите проходной балл для второй волны: ");
            n2 = Integer.parseInt(reader.readLine());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    static int mark;
    private void makeMark()
    {
        Random random = new Random();
        mark = 65 + random.nextInt(100 - 65);
    }
    static void studentAdmission(int x)
    {
        Admission student = new Admission();
        student.makeMark();
        System.out.println("Student № " +  x);
        StateContext context = new StateContext();
        context.doSomething();
        context.setState(new AnalyzeFirstWave());
        context.doSomething();
        if (mark >= Admission.n1){
            context.setState(new Treatment());
            context.doSomething();
            success += 1;
        }
        else{
            context.setState(new AnalyzeSecondWave());
            context.doSomething();
            if (mark >= Admission.n2){
                context.setState(new Treatment());
                context.doSomething();
                success += 1;
            }
        }
        context.setState(new End());
        context.doSomething();
        System.out.println();
    }
}