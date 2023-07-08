using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    public static int NOD(int a, int b)
    {
        if (a == b)
            return a;
        else
            if (a > b)
            return NOD(a - b, b);
        else
            return NOD(b - a, a);
    }
    static void Main(string[] args)
    {
        int a = 17;
        int b = 35;
        int c = 28;
        
        if (NOD(NOD(a, b), c) == 1)
            Console.WriteLine("Числа {0}, {1}, {2} взаимно простые", a, b, c);
        else
            Console.WriteLine("Числа {0}, {1}, {2} не взаимно простые", a, b, c);
        Console.ReadKey(true);
    }
}