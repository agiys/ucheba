using Autofac;
using Newtonsoft.Json;
using RegistrationBook.Data;
using RegistrationBook.Models;
using PropertyChanged;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Collections.Specialized;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Windows.Data;
using System.Windows;
using System.Configuration;
using System.Reflection;
using System.Xml;
using RegistrationBook.Repository;
using RegistrationBook.View;

namespace RegistrationBook.ViewModels
{
    [AddINotifyPropertyChangedInterface]
    public class MainWindowViewModel : IErrorNotifier
    {
        public event EventHandler<string> ErrorOccurred;
        private readonly IService service;
        private readonly RecordViewModel recordViewModel;
        private readonly RecordWindow recordWindow;

        private BindingList<Client> _clients;
        //private readonly string path = $"{Environment.CurrentDirectory}\\clients.json";
        
        public MainWindowViewModel(IService service, RecordViewModel recordViewModel, RecordWindow recordWindow)
        {
            this.service = service;
            this.recordViewModel = recordViewModel;
            this.recordWindow = recordWindow;
            RefreshCommand = new RelayCommand(Refresh);
            Clients = new BindingList<Client>();
            Clients.ListChanged += Clients_ListChanged;
            DeleteCommand = new RelayCommand(DeleteSelectedClient);
            OpenRecord = new RelayCommand(OnOpenRecord);

        }

        private void OnOpenRecord()
        {
            recordWindow.DataContext = recordViewModel;
            recordWindow.ShowDialog();
        }

        public ICommand DeleteCommand { get; set; }
        public ICommand RefreshCommand { get; }
        public ICommand OpenCommand { get; }
        public ICommand OpenRecord { get; }

        public BindingList<Client> Clients
        {
            get { return _clients; }
            set { _clients = value; }
        }
        private void OnErrorOccurred(string errorMessage)
        {
            ErrorOccurred?.Invoke(this, errorMessage);
        }

        private void Clients_ListChanged(object sender, ListChangedEventArgs e)
        {
            //// Создаем и конфигурируем контейнер в методе ConfigureIoC
            //var startup = new Startup();
            //var container = startup.ConfigureIoC();
            //var service1 = container.Resolve<IService>(); // любое другое окно
            //service1.SaveClients();
            //var window = container.Resolve<MainWindow>();
            //var windowviewmodel = container.Resolve<MainWindowViewModel>();
            //window.DataContext = windowviewmodel;
            if (e.ListChangedType == ListChangedType.ItemAdded || e.ListChangedType == ListChangedType.ItemChanged || e.ListChangedType == ListChangedType.ItemDeleted)
            {
                if (e.ListChangedType == ListChangedType.ItemAdded)
                {
                    var newClient = Clients[e.NewIndex];

                    // Проверяем, что обязательное поле "Имя хозяина" не пустое и не состоит только из пробелов
                    if (string.IsNullOrWhiteSpace(newClient.Name))
                    {
                        // Если "Имя хозяина" пустое или содержит только пробелы, просто не сохраняем запись
                        return;
                    }
                }

                try
                {
                    service.SaveClients(sender);
                    
                }
                catch (Exception ex)
                {
                    OnErrorOccurred(ex.Message);
                }
            }
        }

        public void Refresh()
        {
            Clients.Clear();
            try
            {
                var loadedClients = service.GetClients();
                foreach (var client in loadedClients)
                {
                    Clients.Add(client);
                }
            }
            catch (Exception ex)
            {
                OnErrorOccurred(ex.Message);
            }
        }
        private Client _selectedClient;

        public Client SelectedClient { get; set; }

        private void DeleteSelectedClient()
        {
            if (SelectedClient != null)
            {
                Clients.Remove(SelectedClient);
                SelectedClient = null;
            }
        }

    }
}
