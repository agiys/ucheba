using System.Text;
class Biba
{

        static void Main()
        {
        Console.Write("Введите путь к файлу: ");
        string path = Console.ReadLine();
        String text = File.ReadAllText(path, Encoding.Default);
            int min = text.Length;
            String min_word = "";
            text = text.Trim(new char[] { '.', ',', '!', '?', '"' });

            String[] words = text.Split(new char[] { ' ' });
            foreach (String w in words)
            {
                if (w.Length < min)
                {
                    min = w.Length;
                    min_word = w;
                }
            }
            int count = 0;
            foreach (string x in words)
            {
                if (x == min_word) ++count;
            }


            Console.WriteLine("'{0}' - наиболее короткое слово, встречается {1} раз", min_word, count);
        }
    
}