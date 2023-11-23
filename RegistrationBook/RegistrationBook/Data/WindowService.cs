using RegistrationBook.View;
using RegistrationBook.ViewModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RegistrationBook.Data
{
    public class WindowService : IWindowService
    {
        public void ShowWindow(object viewModel)
        {
            if (viewModel is RecordViewModel recordViewModel)
            {
                var recordView = new RecordWindow(); // Создание представления
                recordView.DataContext = recordViewModel; // Привязка ViewModel к представлению
                recordView.Show(); // Отображение окна
            }
        }
    }
}
