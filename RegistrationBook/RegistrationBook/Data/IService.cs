using RegistrationBook.Models;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RegistrationBook.Data
{
    public interface IService
    {
        //Client SaveClient(Client client);
        BindingList<Client> GetClients();
        void SaveClients(object clientList);
    }
}
