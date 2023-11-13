using Autofac;
using RegistrationBook.ViewModels;
using System;
using System.Collections.Generic;
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
            builder.RegisterType<AppService>().As<IService>();
            //builder.RegisterType<EnterWindow>().AsSelf();
            builder.RegisterType<MainWindow>().AsSelf();
            //builder.RegisterType<EnterWindowViewModel>().AsSelf();
            builder.RegisterType<MainWindowViewModel>().AsSelf();
            // Другие регистрации...

            // Конфигурирование контейнера
            return builder.Build();
        }

    }
}
