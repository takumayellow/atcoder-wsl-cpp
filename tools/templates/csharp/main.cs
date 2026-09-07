using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

class Program
{
    static void Main()
    {
        // 出力バッファリング。例外で落ちてもここまでの出力は吐く
        var sw = new StreamWriter(Console.OpenStandardOutput()) { AutoFlush = false };
        Console.SetOut(sw);
        try { Solve(); }
        finally { Console.Out.Flush(); }
    }

    static void Solve()
    {



    }

    // 入力ヘルパ
    // Split(' ') だと連続スペースや行末スペースで空文字が混ざり Parse が落ちるので、
    // 空白全般で切って空要素を捨てる
    static string[] Tokens() => Console.ReadLine().Split((char[])null, StringSplitOptions.RemoveEmptyEntries);
    static string Line() => Console.ReadLine();
    static int Int() => int.Parse(Console.ReadLine());
    static long Long() => long.Parse(Console.ReadLine());
    static int[] Ints() => Tokens().Select(int.Parse).ToArray();
    static long[] Longs() => Tokens().Select(long.Parse).ToArray();
}
