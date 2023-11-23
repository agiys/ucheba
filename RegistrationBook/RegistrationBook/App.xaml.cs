using Autofac;
using IoC;
using RegistrationBook.Data;
using RegistrationBook.ViewModels;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;

namespace RegistrationBook
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        private Autofac.IContainer container;

        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);

            // Создаем и конфигурируем контейнер в методе ConfigureIoC
            var startup = new Startup();
            var container = startup.ConfigureIoC();

            // Создаем экземпляр MainWindowViewModel из контейнера
            var mainWindowViewModel = container.Resolve<MainWindowViewModel>(
                new TypedParameter(typeof(Autofac.IContainer), container));

            // Создаем экземпляр MainWindow, устанавливая DataContext в MainWindowViewModel
            var mainWindow = new MainWindow { DataContext = mainWindowViewModel };

            // Подписываемся на событие ErrorOccurred
            mainWindowViewModel.ErrorOccurred += (sender, errorMessage) =>
            {
                MessageBox.Show(errorMessage);
                // Здесь можно выполнить закрытие окна, например:
                if (mainWindow != null)
                {
                    mainWindow.Close();
                }
            };
            // Отображаем MainWindow
            mainWindow.Show();
            //mainWindow.myDataGrid.RowStyle = (Style)FindResource("DataGridRowStyle");

        }
    }
}
