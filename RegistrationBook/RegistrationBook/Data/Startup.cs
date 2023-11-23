using Autofac;
using RegistrationBook.Repository;
using RegistrationBook.View;
using RegistrationBook.ViewModels;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Runtime.Serialization;
using System.Text;
using System.Threading.Tasks;

namespace RegistrationBook.Data
{
    public class Startup
    {
        public IContainer ConfigureIoC()
        {
            var builder = new ContainerBuilder();

            // Регистрация зависимостей
            builder.RegisterType<AppService>().As<IService>().SingleInstance();
            builder.RegisterType<WindowService>().As<IWindowService>(); // Регистрируем WindowService как IWindowService
            builder.RegisterType<MainWindow>().AsSelf();
            //builder.RegisterType<RecordViewModelFactory>().As<IRecordFactory>();
            builder.RegisterType<MainWindowViewModel>().AsSelf().SingleInstance();
            builder.RegisterType<RecordViewModel>().AsSelf().SingleInstance();
            builder.RegisterType< RecordWindow>().AsSelf();
            // Другие регистрации...

            // Конфигурирование контейнера
            return builder.Build();
        }

    }
}
