using Autofac.Core;
using Newtonsoft.Json;
using RegistrationBook.Data;
using RegistrationBook.Models;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace RegistrationBook.ViewModels
{
    public class EnterWindowViewModel
    {
        private IService _service;

        public EnterWindowViewModel(IService service)
        {
            _service = service;
            SaveCommand = new RelayCommand(OnSaveCommand);
        }

        public int Id { get; set; }
        public string Name { get; set; }
        public string PetName { get; set; }
        public string Type { get; set; }
        public string Description { get; set; }
        public string Phone { get; set; }

        public Client Model
        {
            get; set;
        }

        
        public ICommand SaveCommand { get;}

        public void OnSaveCommand()
        {
            var client = new Client()
            {
                Name = Name,
                PetName = PetName,
                Type = Type,
                Description = Description,
                Phone = Phone
            };
            client = _service.SaveClient(client);

            Name = client.Name;
            PetName= client.PetName;
            Type = client.Type;
            Description = client.Description;
            Phone = client.Phone;
        }
        
    }
}
