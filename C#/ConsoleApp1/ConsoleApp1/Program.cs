using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //string first = "1 — remove";
            //string second = "2 — delete";
            //string third = "3 — pasha";
            Console.WriteLine
                (
                "Выберите:"  + 
                "\n 1 — remove" +
                "\n 2 — delete" +
                "\n 3 — pasha" 
                );
            //Console.WriteLine($"Выберите: \n {first} \n {second}  \n ") ;

            int a = Convert.ToInt32(Console.ReadLine());
           
  
            switch (a) 
            {
                case 1:
                    Console.WriteLine("remove");
                    break;

                case 2:
                    Console.WriteLine("delete");
                    break;

                default:
                    Console.WriteLine("pasha dogdik");
                    break;
            }          



        }
    }
}

